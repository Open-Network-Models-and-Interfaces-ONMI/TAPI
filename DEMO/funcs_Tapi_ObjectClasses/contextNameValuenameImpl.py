import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class ContextNameValuenameImpl:

    @classmethod
    def put(cls, valueName, nameandvalue):
        print str(nameandvalue)
        print 'handling put'
        Context.name[valueName] = nameandvalue

    @classmethod
    def post(cls, valueName, nameandvalue):
        print str(nameandvalue)
        print 'handling post'
        Context.name[valueName] = nameandvalue

    @classmethod
    def delete(cls, valueName):
        print 'handling delete'
        if valueName in Context.name:
            del Context.name[valueName]
        else:
            raise KeyError('valueName')

    @classmethod
    def get(cls, valueName):
        print 'handling get'
        if valueName in Context.name:
            return Context.name[valueName]
        else:
            raise KeyError('valueName')
