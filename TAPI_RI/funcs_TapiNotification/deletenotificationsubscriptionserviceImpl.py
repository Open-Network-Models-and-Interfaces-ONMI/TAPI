import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))


class DeletenotificationsubscriptionserviceImpl:

    @classmethod
    def post(cls, deletenotificationsubscriptionservicerpcinputschema):
        print str(deletenotificationsubscriptionservicerpcinputschema)
        print 'handling RPC operation'
