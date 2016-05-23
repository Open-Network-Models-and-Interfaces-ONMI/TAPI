import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class ContextNameValuenameImpl:

    @classmethod
    def get(cls, valueName):
        print 'handling get'
        if valueName in Context.name:
            return Context.name[valueName]
        else:
            raise KeyError('valueName')
