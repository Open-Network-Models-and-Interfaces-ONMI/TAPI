import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_NwtopologyserviceLabelValuenameImpl:

    @classmethod
    def get(cls, valueName):
        print 'handling get'
        if valueName in be.Context._nwTopologyService.label:
            return be.Context._nwTopologyService.label[valueName]
        else:
            raise KeyError('valueName')
