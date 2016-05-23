import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))


class GetnodedetailsImpl:

    @classmethod
    def post(cls, getnodedetailsrpcinputschema):
        print str(getnodedetailsrpcinputschema)
        print 'handling RPC operation'
