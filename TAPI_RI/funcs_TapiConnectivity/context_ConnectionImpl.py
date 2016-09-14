import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_ConnectionImpl:

    @classmethod
    def get(cls, ):
        print 'handling get'
        if be.Context:
            array_cs=[]
            for cs in be.Context._connection:
                uri="http://127.0.0.1:8080/restconf/config/Context/_connection/"+be.Context._connection[cs].uuid+"/"
                print uri
                array_cs.append(uri)
            json = { 'itemlist' : array_cs }
            return json
        else:
            raise KeyError('')
