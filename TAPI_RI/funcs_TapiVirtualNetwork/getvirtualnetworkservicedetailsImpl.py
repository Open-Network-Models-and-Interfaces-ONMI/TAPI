import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))


class GetvirtualnetworkservicedetailsImpl:

    @classmethod
    def post(cls, getvirtualnetworkservicedetailsrpcinputschema):
        print str(getvirtualnetworkservicedetailsrpcinputschema)
        print 'handling RPC operation'
