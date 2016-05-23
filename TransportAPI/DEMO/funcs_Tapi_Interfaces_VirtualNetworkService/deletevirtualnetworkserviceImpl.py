import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))


class DeletevirtualnetworkserviceImpl:

    @classmethod
    def post(cls, deletevirtualnetworkservicerpcinputschema):
        print str(deletevirtualnetworkservicerpcinputschema)
        print 'handling RPC operation'
