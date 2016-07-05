import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_VnwserviceUuid_VnwconstraintLocalidCostcharacteristicCostalgorithmImpl:

    @classmethod
    def put(cls, uuid, localId, costAlgorithm, costcharacteristic):
        print str(costcharacteristic)
        print 'handling put'
        if uuid in Context._vnwService:
            if localId in Context._vnwService[uuid]._vnwConstraint:
                be.Context._vnwService[uuid]._vnwConstraint[localId].costCharacteristic[costAlgorithm] = costcharacteristic
            else:
                raise KeyError('costAlgorithm')
        else:
            raise KeyError('localId')

    @classmethod
    def post(cls, uuid, localId, costAlgorithm, costcharacteristic):
        print str(costcharacteristic)
        print 'handling post'
        if uuid in Context._vnwService:
            if localId in Context._vnwService[uuid]._vnwConstraint:
                be.Context._vnwService[uuid]._vnwConstraint[localId].costCharacteristic[costAlgorithm] = costcharacteristic
            else:
                raise KeyError('costAlgorithm')
        else:
            raise KeyError('localId')

    @classmethod
    def delete(cls, uuid, localId, costAlgorithm):
        print 'handling delete'
        if uuid in be.Context._vnwService:
            if localId in be.Context._vnwService[uuid]._vnwConstraint:
                if costAlgorithm in be.Context._vnwService[uuid]._vnwConstraint[localId].costCharacteristic:
                    del be.Context._vnwService[uuid]._vnwConstraint[localId].costCharacteristic[costAlgorithm]
                else:
                    raise KeyError('costAlgorithm')
            else:
                raise KeyError('localId')
        else:
            raise KeyError('uuid')

    @classmethod
    def get(cls, uuid, localId, costAlgorithm):
        print 'handling get'
        if uuid in be.Context._vnwService:
            if localId in be.Context._vnwService[uuid]._vnwConstraint:
                if costAlgorithm in be.Context._vnwService[uuid]._vnwConstraint[localId].costCharacteristic:
                    return be.Context._vnwService[uuid]._vnwConstraint[localId].costCharacteristic[costAlgorithm]
                else:
                    raise KeyError('costAlgorithm')
            else:
                raise KeyError('localId')
        else:
            raise KeyError('uuid')
