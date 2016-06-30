import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class ContextNameImpl:

    @classmethod
    def get(cls, ):
        print 'handling get'
        if be.Context:
            return be.Context
        else:
            raise KeyError('')
