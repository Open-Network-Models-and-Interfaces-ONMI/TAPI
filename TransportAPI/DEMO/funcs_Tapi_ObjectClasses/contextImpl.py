import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class ContextImpl:

    @classmethod
    def put(cls, contextschema):
        print str(contextschema)
        print 'handling put'
        Context = contextschema

    @classmethod
    def post(cls, contextschema):
        print str(contextschema)
        print 'handling post'
        Context = contextschema

    @classmethod
    def delete(cls, ):
        print 'handling delete'
        if Context:
            del Context
        else:
            raise KeyError('')

    @classmethod
    def get(cls, ):
        print 'handling get'
        if Context:
            return Context
        else:
            raise KeyError('')
