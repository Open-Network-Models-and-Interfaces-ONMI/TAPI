import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class ContextLabelValuenameImpl:

    @classmethod
    def put(cls, valueName, nameandvalue):
        print str(nameandvalue)
        print 'handling put'
        Context.label[valueName] = nameandvalue

    @classmethod
    def post(cls, valueName, nameandvalue):
        print str(nameandvalue)
        print 'handling post'
        Context.label[valueName] = nameandvalue

    @classmethod
    def delete(cls, valueName):
        print 'handling delete'
        if valueName in Context.label:
            del Context.label[valueName]
        else:
            raise KeyError('valueName')

    @classmethod
    def get(cls, valueName):
        print 'handling get'
        if valueName in Context.label:
            return Context.label[valueName]
        else:
            raise KeyError('valueName')
