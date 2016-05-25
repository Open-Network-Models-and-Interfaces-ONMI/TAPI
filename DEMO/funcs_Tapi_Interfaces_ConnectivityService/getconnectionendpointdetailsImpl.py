import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))


class GetconnectionendpointdetailsImpl:

    @classmethod
    def post(cls, getconnectionendpointdetailsrpcinputschema):
        print str(getconnectionendpointdetailsrpcinputschema)
        print 'handling RPC operation'
