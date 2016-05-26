import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class ContextLabelValuenameImpl:

    @classmethod
    def get(cls, valueName):
        print 'handling get'
        if valueName in Context.label:
            return Context.label[valueName]
        else:
            raise KeyError('valueName')
