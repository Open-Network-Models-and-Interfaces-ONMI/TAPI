import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))


class GetserviceendpointdetailsImpl:

    @classmethod
    def post(cls, getserviceendpointdetailsrpcinputschema):
        print str(getserviceendpointdetailsrpcinputschema)
        print 'handling RPC operation'
