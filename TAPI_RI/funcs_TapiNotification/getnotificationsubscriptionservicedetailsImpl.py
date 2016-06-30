import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))


class GetnotificationsubscriptionservicedetailsImpl:

    @classmethod
    def post(cls, getnotificationsubscriptionservicedetailsrpcinputschema):
        print str(getnotificationsubscriptionservicedetailsrpcinputschema)
        print 'handling RPC operation'
