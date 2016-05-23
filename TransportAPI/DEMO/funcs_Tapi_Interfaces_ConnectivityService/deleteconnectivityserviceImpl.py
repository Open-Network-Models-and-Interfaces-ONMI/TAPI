import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))


class DeleteconnectivityserviceImpl:

    @classmethod
    def post(cls, deleteconnectivityservicerpcinputschema):
        print str(deleteconnectivityservicerpcinputschema)
        print 'handling RPC operation'
