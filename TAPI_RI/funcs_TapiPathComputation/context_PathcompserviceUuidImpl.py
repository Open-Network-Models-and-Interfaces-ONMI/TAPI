import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_PathcompserviceUuidImpl:

    @classmethod
    def put(cls, uuid, _pathcompserviceschema):
        print str(_pathcompserviceschema)
        print 'handling put'
        be.Context._pathCompService[uuid] = _pathcompserviceschema

    @classmethod
    def post(cls, uuid, _pathcompserviceschema):
        print str(_pathcompserviceschema)
        print 'handling post'
        be.Context._pathCompService[uuid] = _pathcompserviceschema

    @classmethod
    def delete(cls, uuid):
        print 'handling delete'
        if uuid in be.Context._pathCompService:
            del be.Context._pathCompService[uuid]
        else:
            raise KeyError('uuid')

    @classmethod
    def get(cls, uuid):
        print 'handling get'
        if uuid in be.Context._pathCompService:
            return be.Context._pathCompService[uuid]
        else:
            raise KeyError('uuid')
