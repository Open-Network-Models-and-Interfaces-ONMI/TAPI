import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))


class Deletep2PpathImpl:

    @classmethod
    def post(cls, deletep2ppathrpcinputschema):
        print str(deletep2ppathrpcinputschema)
        print 'handling RPC operation'
