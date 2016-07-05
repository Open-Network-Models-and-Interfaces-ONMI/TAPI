import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_VnwserviceUuid_VnwconstraintLocalidRequestedcapacityImpl:

    @classmethod
    def put(cls, uuid, localId, capacity):
        print str(capacity)
        print 'handling put'
        if uuid in Context._vnwService:
            be.Context._vnwService[uuid]._vnwConstraint[localId] = capacity
        else:
            raise KeyError('localId')

    @classmethod
    def post(cls, uuid, localId, capacity):
        print str(capacity)
        print 'handling post'
        if uuid in Context._vnwService:
            be.Context._vnwService[uuid]._vnwConstraint[localId] = capacity
        else:
            raise KeyError('localId')

    @classmethod
    def delete(cls, uuid, localId):
        print 'handling delete'
        if uuid in be.Context._vnwService:
            if localId in be.Context._vnwService[uuid]._vnwConstraint:
                del be.Context._vnwService[uuid]._vnwConstraint[localId].requestedCapacity
            else:
                raise KeyError('localId')
        else:
            raise KeyError('uuid')

    @classmethod
    def get(cls, uuid, localId):
        print 'handling get'
        if uuid in be.Context._vnwService:
            if localId in be.Context._vnwService[uuid]._vnwConstraint:
                return be.Context._vnwService[uuid]._vnwConstraint[localId].requestedCapacity
            else:
                raise KeyError('localId')
        else:
            raise KeyError('uuid')
