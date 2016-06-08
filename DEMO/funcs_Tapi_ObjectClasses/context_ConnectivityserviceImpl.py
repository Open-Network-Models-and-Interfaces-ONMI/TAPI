import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context
import json
from objects_common.StringArray import StringArray

class Context_ConnectivityserviceImpl:

    @classmethod
    def get(cls, ):
        print 'handling get'
        if Context:
            array_cs=[]
            for cs in Context._connectivityService:
                uri="http://127.0.0.1:8080/config/Context/_connectivityService/"+Context._connectivityService[cs].uuid+"/"
                print uri
                array_cs.append(uri)
            return array_cs
        else:
            raise KeyError('')
