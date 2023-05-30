import grpc
import logging
import time

from cachetools import cached,TTLCache

from chirpstack_api.as_pb import as_pb_pb2_grpc 
from chirpstack_api.as_pb import as_pb_pb2

app_server = 'localhost:8001'

_logger = logging.getLogger(__name__)


def check():
    while True:
        try:
            get_organizations()
            break
        except Exception as e:
            _logger.error("Unable to connect to AS. check your grpc connection to application's server: %s", app_server)
            _logger.debug(e)
            time.sleep(5)


# 640K should be enough for anyone...
@cached(cache=TTLCache(ttl=300,maxsize=640*1024), info=True)
def get_organizations():
    with grpc.insecure_channel(app_server) as channel:
        stub = as_pb_pb2_grpc.ApplicationServerServiceStub(channel)
        response = stub.ListOrganisation(as_pb_pb2.ListOrganizationRequest(limit=9999))
        _logger.info("as:get_organizations: got list with %d organization(s) from application's server", response.total_count)

        result = {}
        for org in response.result:
            result[org.id] = org

        return result