import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_TopologyImpl:

    @classmethod
    def get(cls, ):
        print 'handling get'
        if Context:
            array_cs=[]
            for cs in Context._topology:
                uri="http://127.0.0.1:8080/restconf/config/Context/_topology/"+Context._topology[cs].uuid+"/"
                print uri
                array_cs.append(uri)
            return array_cs
        else:
            raise KeyError('')
