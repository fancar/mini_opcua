import asyncio
import logging
import json
import sys

from asyncua import Server, ua

from aiohttp import web

import as_grpc

uri = "ERNET OPCUA"
web_host = '0.0.0.0'
web_port = 8072
server = Server()

_logger = logging.getLogger(__name__)


async def uplink(request):
    data = await request.json()

    if 'deviceName' not in data:
        return web.Response(status=400, text='deviceName is missing')

    if 'orgID' not in data:
        return web.Response(status=400, text='orgID is missing')

    if 'objectJSON' not in data:
        return web.Response(status=400, text='objectJSON is missing')

    items = json.loads(data['objectJSON'])

    orgID = data['orgID']
    try:
        orgs = as_grpc.get_organizations()
    except Exception as e:
        _logger.debug(f"uplink: unable to get a name for the orgID:{orgID}: {e}")
        return web.Response(status=500, text=f'unable to get a name for the orgID:{orgID}')
      
    if orgID not in orgs:
            return web.Response(status=400, text='orgID is unknown. The message is skipped')


    node = orgs[orgID].name
    device = str(data['deviceName'])

    for key,value in items.items():
        _logger.info(f"uplink: node={node} device={device} seting key={key} with value={value}...")
        await set_node_variable(node,device,key,value)

    return web.Response(text=f"node:{node}->device:{device}: recieved items: {items}")

async def init_webapp():
    app = web.Application()
    app.add_routes([web.post('/', uplink)])
    return app

async def http_server(queue):
    app = await init_webapp()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, web_host, web_port)
    await site.start()


async def set_node_variable(node_name: str, device_name: str, var_name: str, var_value):
    """ обновление значений переменных """

    root = server.nodes.objects

    # idx = await server.register_namespace(uri)
    idx = 2

    # Проверяем, существует ли узел с таким именем
    try:
        # node = await root.get_child(node_name)
        node = await root.get_child(f"{idx}:{node_name}")
        _logger.debug(f"set_node_variable: got node={idx}:{node_name}")
    except ua.uaerrors.BadNoMatch:
        # Если узла нет, то создаем его
        _logger.debug(f"set_node_variable: creating node object{idx}:{node_name} ...")
        # node = await root.add_object(ua.NodeId(node_name, 2), node_name)
        node = await root.add_object(idx, node_name)

    _logger.debug(f"set_node_variable: processing node {idx}:{node_name}: {node} ...")


    # Проверяем, существует ли объект в узеле с таким именем
    try:
        # node = await root.get_child(node_name)
        device = await node.get_child(f"{idx}:{device_name}")
        _logger.debug(f"set_node_variable: node {node} got device={idx}:{device_name}")
    except ua.uaerrors.BadNoMatch:
        # Если узла нет, то создаем его
        _logger.debug(f"set_node_variable: creating node device object with name {device_name} ...")
        # node = await root.add_object(ua.NodeId(node_name, 2), node_name)
        device = await node.add_object(idx, device_name)

    _logger.debug(f"set_node_variable: node {node_name}: {node}")

    var_node = None
    try:
        var_node = await root.get_child([f"{idx}:{node_name}", f"{idx}:{device_name}", f"{idx}:{var_name}"])
        _logger.debug(f"set_node_variable: {idx}:{node_name}->{idx}:{device_name}->{idx}:{var_name} found value={var_node.get_value()}")
        
        # _logger.debug(f"set_node_variable: setting {var_node} new value ...")
        _logger.debug("set_node_variable: Set value of %s to %.1f ...", var_node, var_value)
        # Если переменная уже существует, то устанавливаем ей новое значение
        await var_node.write_value(var_value)

    except ua.uaerrors.BadNoMatch:
        _logger.debug(f"set_node_variable: {idx}:{node_name}->{idx}:{device_name}->{idx}:{var_name}  adding the variable ...")

        var_node = await device.add_variable(idx, var_name, var_value)
        await var_node.set_writable(True)

    return var_node


async def opc_server(queue):
    """ opcua server implementation """
    # setup our server
    
    await server.init()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    async with server:
        while True:
            await asyncio.sleep(1)


async def main():
    as_grpc.check()

    queue = asyncio.Queue()
    await asyncio.gather(http_server(queue), opc_server(queue))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main(), debug=True)