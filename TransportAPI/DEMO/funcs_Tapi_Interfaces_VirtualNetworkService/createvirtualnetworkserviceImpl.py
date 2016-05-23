import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))


class CreatevirtualnetworkserviceImpl:

    @classmethod
    def post(cls, createvirtualnetworkservicerpcinputschema):
        print str(createvirtualnetworkservicerpcinputschema)
        print 'handling RPC operation'
