import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class ContextExtensionValuenameImpl:

    @classmethod
    def get(cls, valueName):
        print 'handling get'
        if valueName in Context.extension:
            return Context.extension[valueName]
        else:
            raise KeyError('valueName')
