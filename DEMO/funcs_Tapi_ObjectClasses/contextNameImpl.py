import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class ContextNameImpl:

    @classmethod
    def get(cls, ):
        print 'handling get'
        if Context:
            return Context
        else:
            raise KeyError('')
