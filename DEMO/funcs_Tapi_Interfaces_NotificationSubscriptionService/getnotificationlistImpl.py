import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))


class GetnotificationlistImpl:

    @classmethod
    def post(cls, getnotificationlistrpcinputschema):
        print str(getnotificationlistrpcinputschema)
        print 'handling RPC operation'
