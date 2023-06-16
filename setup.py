import os
import configparser
import logging

_logger = logging.getLogger(__name__)

class HttpConfig:
    host: str = '0.0.0.0'
    port: int = 8072

class OpcuaConfig:
    idx: int = 2
    endpoint: str = "opc.tcp://0.0.0.0:4840/ernetopcua/server/"
    dumpfile: str = "dump.xml"

class Config:
    DumpPeriod: int = 300 # dump saving period in seconds
    Web: HttpConfig = HttpConfig()
    Opcua: OpcuaConfig = OpcuaConfig()

def setup():
    fname = "config.cfg"
    result = Config()

    write_defaults(result)

    if not os.path.isfile(fname):
        _logger.info("there is no %s. Going to use defaults ...", fname)
        return result

    config = configparser.ConfigParser()
    config.read(fname)

    if 'MAIN' in config:
        main = config['MAIN']
        result.DumpPeriod = main.get('dumpperiod', result.DumpPeriod)

    if 'server.http' in config:
        httpcfg = config['server.http']
        result.Web.host = httpcfg.get('host', result.Web.host)
        result.Web.port = httpcfg.get('port', result.Web.port)

    if 'server.opcua' in config:
        opccfg = config['server.opcua']
        result.Opcua.idx = opccfg.get('idx', result.Opcua.idx)
        result.Opcua.endpoint = opccfg.get('endpoint', result.Opcua.endpoint)
        result.Opcua.dumpfile = opccfg.get('dumpfile', result.Opcua.dumpfile)

    print("idx is ", result.Opcua.idx)
    print("endpoint is ", result.Opcua.endpoint)
    print("dumpfile is ", result.Opcua.dumpfile)

    return result


def write_defaults(defaults):
    config = configparser.ConfigParser()
    config['MAIN'] = {
        "dumpperiod": defaults.DumpPeriod,
    }

    config['server.http'] = {
        "host": defaults.Web.host,
        "port": defaults.Web.port,
    }

    config['server.opcua'] = {
        "idx": defaults.Opcua.idx,
        "endpoint": defaults.Opcua.endpoint,
        "dumpfile": defaults.Opcua.dumpfile,
    }


    with open('config.cfg.defaults', 'w') as configfile:
        config.write(configfile)
