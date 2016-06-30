import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_ConnectivityserviceUuid_Connconstraint_ExcludepathLocalid_ExtensionsExtensionsspecificationImpl:

    @classmethod
    def get(cls, uuid, localId, extensionsSpecification):
        print 'handling get'
        if uuid in be.Context._connectivityService:
            if localId in be.Context._connectivityService[uuid]._connConstraint._excludePath:
                if extensionsSpecification in be.Context._connectivityService[uuid]._connConstraint._excludePath[localId]._extensions:
                    return be.Context._connectivityService[uuid]._connConstraint._excludePath[localId]._extensions[extensionsSpecification]
                else:
                    raise KeyError('extensionsSpecification')
            else:
                raise KeyError('localId')
        else:
            raise KeyError('uuid')
