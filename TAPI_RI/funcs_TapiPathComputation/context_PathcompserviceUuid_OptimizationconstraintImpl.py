import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_PathcompserviceUuid_OptimizationconstraintImpl:

    @classmethod
    def put(cls, uuid, pathoptimizationconstraint):
        print str(pathoptimizationconstraint)
        print 'handling put'
        be.Context._pathCompService[uuid] = pathoptimizationconstraint

    @classmethod
    def post(cls, uuid, pathoptimizationconstraint):
        print str(pathoptimizationconstraint)
        print 'handling post'
        be.Context._pathCompService[uuid] = pathoptimizationconstraint

    @classmethod
    def delete(cls, uuid):
        print 'handling delete'
        if uuid in be.Context._pathCompService:
            del be.Context._pathCompService[uuid]._optimizationConstraint
        else:
            raise KeyError('uuid')

    @classmethod
    def get(cls, uuid):
        print 'handling get'
        if uuid in be.Context._pathCompService:
            return be.Context._pathCompService[uuid]._optimizationConstraint
        else:
            raise KeyError('uuid')
