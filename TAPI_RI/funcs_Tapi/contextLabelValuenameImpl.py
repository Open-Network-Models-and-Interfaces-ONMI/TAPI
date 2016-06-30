import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class ContextLabelValuenameImpl:

    @classmethod
    def put(cls, valueName, nameandvalue):
        print str(nameandvalue)
        print 'handling put'
        be.Context.label[valueName] = nameandvalue

    @classmethod
    def post(cls, valueName, nameandvalue):
        print str(nameandvalue)
        print 'handling post'
        be.Context.label[valueName] = nameandvalue

    @classmethod
    def delete(cls, valueName):
        print 'handling delete'
        if valueName in be.Context.label:
            del be.Context.label[valueName]
        else:
            raise KeyError('valueName')

    @classmethod
    def get(cls, valueName):
        print 'handling get'
        if valueName in be.Context.label:
            return be.Context.label[valueName]
        else:
            raise KeyError('valueName')
