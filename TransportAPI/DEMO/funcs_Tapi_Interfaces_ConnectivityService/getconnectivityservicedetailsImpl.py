import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))


class GetconnectivityservicedetailsImpl:

    @classmethod
    def post(cls, getconnectivityservicedetailsrpcinputschema):
        print str(getconnectivityservicedetailsrpcinputschema)
        print 'handling RPC operation'
