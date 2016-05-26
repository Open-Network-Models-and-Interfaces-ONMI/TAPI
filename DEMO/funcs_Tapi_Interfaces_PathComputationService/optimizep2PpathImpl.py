import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))


class Optimizep2PpathImpl:

    @classmethod
    def post(cls, optimizep2ppathrpcinputschema):
        print str(optimizep2ppathrpcinputschema)
        print 'handling RPC operation'
