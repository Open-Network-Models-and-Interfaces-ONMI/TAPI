import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))


class UpdatenotificationsubscriptionserviceImpl:

    @classmethod
    def post(cls, updatenotificationsubscriptionservicerpcinputschema):
        print str(updatenotificationsubscriptionservicerpcinputschema)
        print 'handling RPC operation'
