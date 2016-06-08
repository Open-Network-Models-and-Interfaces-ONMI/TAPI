import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))


class CreatenotificationsubscriptionserviceImpl:

    @classmethod
    def post(cls, createnotificationsubscriptionservicerpcinputschema):
        print str(createnotificationsubscriptionservicerpcinputschema)
        print 'handling RPC operation'
