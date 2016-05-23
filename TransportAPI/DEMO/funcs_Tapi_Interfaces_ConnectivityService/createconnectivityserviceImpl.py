import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))


class CreateconnectivityserviceImpl:

    @classmethod
    def post(cls, createconnectivityservicerpcinputschema):
        print str(createconnectivityservicerpcinputschema)
        print 'handling RPC operation'
