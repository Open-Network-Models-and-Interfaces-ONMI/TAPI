import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))


class UpdateconnectivityserviceImpl:

    @classmethod
    def post(cls, updateconnectivityservicerpcinputschema):
        print str(updateconnectivityservicerpcinputschema)
        print 'handling RPC operation'
