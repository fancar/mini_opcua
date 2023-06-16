import asyncio
import logging
import json
import sys
import os
import signal
import functools

from asyncua import Server, ua

from aiohttp import web
from setup import setup
from time import perf_counter

import as_grpc

idx = 0 # index of an opc object we are collecting all the data in
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

async def http_server(queue,cfg):
    app = await init_webapp()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, cfg.Web.host, cfg.Web.port)
    await site.start()


async def set_node_variable(node_name: str, device_name: str, var_name: str, var_value):
    """ обновление значений переменных """
    _logger.info(f"set_node_variable: node={node_name} device:{device_name} setting {var_name}={var_value} ...")

    root = server.get_objects_node()

    # first create node if it does not exist
    try:
        node = await root.get_child(f"{idx}:{node_name}")
    except ua.uaerrors.BadNoMatch:
        node = await root.add_object(idx, node_name)


    # then create a device object in the node or get it
    try:
        device = await node.get_child(f"{idx}:{device_name}")
    except ua.uaerrors.BadNoMatch:
        device = await node.add_object(idx, device_name)

    # and finnaly save the variable
    var_node = None
    try:
        var_node = await root.get_child([f"{idx}:{node_name}", f"{idx}:{device_name}", f"{idx}:{var_name}"])
        await var_node.write_value(var_value)

    except ua.uaerrors.BadNoMatch:
        var_node = await device.add_variable(idx, var_name, var_value)
        await var_node.set_writable(True)

    return var_node

async def set_example_node():
    """ the node is just to show off.
     When no data transfered yet we have to show at least something """
    await set_node_variable(
        node_name="example",
        device_name="example_device",
        var_name="voltage",
        var_value="3.7"
        )
    
    await set_node_variable(
        node_name="example",
        device_name="example_device",
        var_name="current",
        var_value="2.1"
        )


async def dump_to_file(fname):
    """ saves the whole opc tree to the xml file """
    t = perf_counter()
    # nodes_to_skip = ["Server","Aliases"]
    data = []

    root = server.get_objects_node()
    orgs = await root.get_children()

    data = orgs

    for org in orgs:
        # org_name = await org.read_display_name()
        # if nodes_to_skip in nodes_to_skip:
        #     continue
        # print("org_name: ",org_name)

        devices = await org.get_children()
        data = [*data,*devices]

        for device in devices:
            # deviceName = await org.read_display_name()
            
            metrics = await device.get_variables()
            data = [*data,*metrics]

    await server.export_xml(data, fname, export_values=True)
    _logger.info("opcua data has been dumped to %s. Took %.3f s",fname, perf_counter() - t)


async def restore_from_file(fname):
    if not os.path.isfile(fname):
        _logger.info("there is no dump file: %s. Starting from scratch ...", fname)
        return
    _logger.info("restoring data from %s ...", fname)
    await server.import_xml(fname, strict_mode=False)


async def opc_server(queue,cfg):
    """ opcua server implementation """
    await server.init()
    server.set_endpoint(cfg.Opcua.endpoint)

    await restore_from_file(cfg.Opcua.dumpfile)
    await set_example_node()

    # await dump_to_file(dump_file)


    async with server:
        while True:
            await asyncio.sleep(1)


async def dumper(cfg):
    while True:
        await asyncio.sleep(cfg.Opcua.DumpPeriod)
        await dump_to_file(cfg.Opcua.dumpfile)


async def shutdown(cfg):
    _logger.info('Exit signal has been recieved. Shutting down  ...')
    await dump_to_file(cfg.Opcua.dumpfile)

    _logger.info('bye')


async def main(cfg):
    idx = cfg.Opcua.idx

    as_grpc.check(cfg)

    queue = asyncio.Queue()

    await asyncio.gather(
        http_server(queue, cfg),
        opc_server(queue, cfg),
        dumper(cfg),
        )




if __name__ == "__main__":
    cfg = setup()

    logging.basicConfig(level=logging.INFO)

    try:
        asyncio.run(main(cfg), debug=False)
    except (SystemExit, KeyboardInterrupt):
        asyncio.run(shutdown(cfg))
    except Exception as e:
        print("recieved exception ",e)
        raise

