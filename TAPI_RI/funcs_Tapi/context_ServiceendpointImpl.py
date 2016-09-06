import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_ServiceendpointImpl:

    @classmethod
    def get(cls, ):
        print 'handling get'
        array_cs=[]
        for uuid in be.Context._serviceEndPoint:
            uri="http://127.0.0.1:8080/restconf/config/Context/_serviceEndPoint/"+uuid
            print uri
            array_cs.append(uri)
        json = { 'itemlist' : array_cs }
        return json
