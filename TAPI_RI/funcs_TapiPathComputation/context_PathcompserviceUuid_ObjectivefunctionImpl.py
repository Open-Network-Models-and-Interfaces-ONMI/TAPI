import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_PathcompserviceUuid_ObjectivefunctionImpl:

    @classmethod
    def put(cls, uuid, pathobjectivefunction):
        print str(pathobjectivefunction)
        print 'handling put'
        be.Context._pathCompService[uuid] = pathobjectivefunction

    @classmethod
    def post(cls, uuid, pathobjectivefunction):
        print str(pathobjectivefunction)
        print 'handling post'
        be.Context._pathCompService[uuid] = pathobjectivefunction

    @classmethod
    def delete(cls, uuid):
        print 'handling delete'
        if uuid in be.Context._pathCompService:
            del be.Context._pathCompService[uuid]._objectiveFunction
        else:
            raise KeyError('uuid')

    @classmethod
    def get(cls, uuid):
        print 'handling get'
        if uuid in be.Context._pathCompService:
            return be.Context._pathCompService[uuid]._objectiveFunction
        else:
            raise KeyError('uuid')
