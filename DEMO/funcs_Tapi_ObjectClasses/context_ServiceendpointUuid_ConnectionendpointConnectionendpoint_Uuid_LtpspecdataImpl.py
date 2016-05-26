import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_LtpspecdataImpl:

    @classmethod
    def get(cls, uuid, connectionEndPoint_uuid):
        print 'handling get'
        if uuid in Context._serviceEndPoint:
            if connectionEndPoint_uuid in Context._serviceEndPoint[uuid]._connectionEndPoint:
                return Context._serviceEndPoint[uuid]._connectionEndPoint[connectionEndPoint_uuid]._ltpSpecData
            else:
                raise KeyError('connectionEndPoint_uuid')
        else:
            raise KeyError('uuid')
