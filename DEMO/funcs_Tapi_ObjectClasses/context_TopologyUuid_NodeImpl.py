import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_TopologyUuid_NodeImpl:

    @classmethod
    def get(cls, uuid):
        print 'handling get node list'
        if uuid in Context._topology:
            array_cs=[]
            for cs in Context._topology[uuid]._node:
                uri="http://127.0.0.1:8080/restconf/config/Context/_topology/"+uuid+"/_node/"+Context._topology[uuid]._node[cs].uuid+"/"
                print uri
                array_cs.append(uri)
            return array_cs
        else:
            raise KeyError('uuid')
