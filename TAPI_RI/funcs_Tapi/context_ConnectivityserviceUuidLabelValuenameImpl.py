import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_ConnectivityserviceUuidLabelValuenameImpl:

    @classmethod
    def put(cls, uuid, valueName, nameandvalue):
        print str(nameandvalue)
        print 'handling put'
        if uuid in Context._connectivityService:
            be.Context._connectivityService[uuid].label[valueName] = nameandvalue
        else:
            raise KeyError('valueName')

    @classmethod
    def post(cls, uuid, valueName, nameandvalue):
        print str(nameandvalue)
        print 'handling post'
        if uuid in Context._connectivityService:
            be.Context._connectivityService[uuid].label[valueName] = nameandvalue
        else:
            raise KeyError('valueName')

    @classmethod
    def delete(cls, uuid, valueName):
        print 'handling delete'
        if uuid in be.Context._connectivityService:
            if valueName in be.Context._connectivityService[uuid].label:
                del be.Context._connectivityService[uuid].label[valueName]
            else:
                raise KeyError('valueName')
        else:
            raise KeyError('uuid')

    @classmethod
    def get(cls, uuid, valueName):
        print 'handling get'
        if uuid in be.Context._connectivityService:
            if valueName in be.Context._connectivityService[uuid].label:
                return be.Context._connectivityService[uuid].label[valueName]
            else:
                raise KeyError('valueName')
        else:
            raise KeyError('uuid')
