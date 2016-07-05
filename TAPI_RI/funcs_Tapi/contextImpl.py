import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class ContextImpl:

    @classmethod
    def put(cls, contextschema):
        print str(contextschema)
        print 'handling put'
        be.Context = contextschema

    @classmethod
    def post(cls, contextschema):
        print str(contextschema)
        print 'handling post'
        be.Context = contextschema

    @classmethod
    def delete(cls, ):
        print 'handling delete'
        if be.Context:
            del be.Context
        else:
            raise KeyError('')

    @classmethod
    def get(cls, ):
        print 'handling get'
        if be.Context:
            return be.Context
        else:
            raise KeyError('')
