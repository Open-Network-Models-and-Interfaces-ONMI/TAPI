import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_ConnectivityserviceImpl:

    @classmethod
    def get(cls, ):
        print 'handling get'
        if be.Context:
            array_cs=[]
            for cs in be.Context._connectivityService:
                uri="http://127.0.0.1:8080/restconf/config/Context/_connectivityService/"+be.Context._connectivityService[cs].uuid+"/"
                print uri
                array_cs.append(uri)
            json = { 'itemlist' : array_cs }
            return json
        else:
            raise KeyError('')
