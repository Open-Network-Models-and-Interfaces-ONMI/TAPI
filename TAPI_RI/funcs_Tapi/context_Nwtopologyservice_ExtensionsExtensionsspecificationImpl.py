import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_Nwtopologyservice_ExtensionsExtensionsspecificationImpl:

    @classmethod
    def get(cls, extensionsSpecification):
        print 'handling get'
        if extensionsSpecification in be.Context._nwTopologyService._extensions:
            return be.Context._nwTopologyService._extensions[extensionsSpecification]
        else:
            raise KeyError('extensionsSpecification')
