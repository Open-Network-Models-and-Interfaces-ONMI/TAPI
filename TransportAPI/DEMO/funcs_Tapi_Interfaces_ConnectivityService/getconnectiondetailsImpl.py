import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))


class GetconnectiondetailsImpl:

    @classmethod
    def post(cls, getconnectiondetailsrpcinputschema):
        print str(getconnectiondetailsrpcinputschema)
        print 'handling RPC operation'
