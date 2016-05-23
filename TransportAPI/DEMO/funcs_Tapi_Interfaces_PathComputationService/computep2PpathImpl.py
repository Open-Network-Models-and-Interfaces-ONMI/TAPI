import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))


class Computep2PpathImpl:

    @classmethod
    def post(cls, computep2ppathrpcinputschema):
        print str(computep2ppathrpcinputschema)
        print 'handling RPC operation'
