import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))


class GetnodeedgepointdetailsImpl:

    @classmethod
    def post(cls, getnodeedgepointdetailsrpcinputschema):
        print str(getnodeedgepointdetailsrpcinputschema)
        print 'handling RPC operation'
