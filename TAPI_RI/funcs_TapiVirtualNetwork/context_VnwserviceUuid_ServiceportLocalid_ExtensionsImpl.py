import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_VnwserviceUuid_ServiceportLocalid_ExtensionsImpl:

    @classmethod
    def get(cls, uuid, localId):
        print 'handling get'
        if uuid in be.Context._vnwService:
            if localId in be.Context._vnwService[uuid]._servicePort:
                return be.Context._vnwService[uuid]._servicePort[localId]._extensions
            else:
                raise KeyError('localId')
        else:
            raise KeyError('uuid')
