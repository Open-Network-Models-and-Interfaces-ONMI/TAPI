import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_VnwserviceUuid_VnwconstraintCostcharacteristicCostalgorithmImpl:

    @classmethod
    def put(cls, uuid, costAlgorithm, costcharacteristic):
        print str(costcharacteristic)
        print 'handling put'
        if uuid in Context._vnwService:
            Context._vnwService[uuid]._vnwConstraint.costCharacteristic[costAlgorithm] = costcharacteristic
        else:
            raise KeyError('costAlgorithm')

    @classmethod
    def post(cls, uuid, costAlgorithm, costcharacteristic):
        print str(costcharacteristic)
        print 'handling post'
        if uuid in Context._vnwService:
            Context._vnwService[uuid]._vnwConstraint.costCharacteristic[costAlgorithm] = costcharacteristic
        else:
            raise KeyError('costAlgorithm')

    @classmethod
    def delete(cls, uuid, costAlgorithm):
        print 'handling delete'
        if uuid in Context._vnwService:
            if costAlgorithm in Context._vnwService[uuid]._vnwConstraint.costCharacteristic:
                del Context._vnwService[uuid]._vnwConstraint.costCharacteristic[costAlgorithm]
            else:
                raise KeyError('costAlgorithm')
        else:
            raise KeyError('uuid')

    @classmethod
    def get(cls, uuid, costAlgorithm):
        print 'handling get'
        if uuid in Context._vnwService:
            if costAlgorithm in Context._vnwService[uuid]._vnwConstraint.costCharacteristic:
                return Context._vnwService[uuid]._vnwConstraint.costCharacteristic[costAlgorithm]
            else:
                raise KeyError('costAlgorithm')
        else:
            raise KeyError('uuid')
