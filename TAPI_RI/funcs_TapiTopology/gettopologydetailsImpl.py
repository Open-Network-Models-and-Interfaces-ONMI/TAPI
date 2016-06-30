import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))


class GettopologydetailsImpl:

    @classmethod
    def post(cls, gettopologydetailsrpcinputschema):
        print str(gettopologydetailsrpcinputschema)
        print 'handling RPC operation'
