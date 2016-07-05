import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_VnwserviceUuid_VnwconstraintLocalidRiskcharacteristicRiskcharacteristicnameImpl:

    @classmethod
    def put(cls, uuid, localId, riskCharacteristicName, riskcharacteristic):
        print str(riskcharacteristic)
        print 'handling put'
        if uuid in Context._vnwService:
            if localId in Context._vnwService[uuid]._vnwConstraint:
                be.Context._vnwService[uuid]._vnwConstraint[localId].riskCharacteristic[riskCharacteristicName] = riskcharacteristic
            else:
                raise KeyError('riskCharacteristicName')
        else:
            raise KeyError('localId')

    @classmethod
    def post(cls, uuid, localId, riskCharacteristicName, riskcharacteristic):
        print str(riskcharacteristic)
        print 'handling post'
        if uuid in Context._vnwService:
            if localId in Context._vnwService[uuid]._vnwConstraint:
                be.Context._vnwService[uuid]._vnwConstraint[localId].riskCharacteristic[riskCharacteristicName] = riskcharacteristic
            else:
                raise KeyError('riskCharacteristicName')
        else:
            raise KeyError('localId')

    @classmethod
    def delete(cls, uuid, localId, riskCharacteristicName):
        print 'handling delete'
        if uuid in be.Context._vnwService:
            if localId in be.Context._vnwService[uuid]._vnwConstraint:
                if riskCharacteristicName in be.Context._vnwService[uuid]._vnwConstraint[localId].riskCharacteristic:
                    del be.Context._vnwService[uuid]._vnwConstraint[localId].riskCharacteristic[riskCharacteristicName]
                else:
                    raise KeyError('riskCharacteristicName')
            else:
                raise KeyError('localId')
        else:
            raise KeyError('uuid')

    @classmethod
    def get(cls, uuid, localId, riskCharacteristicName):
        print 'handling get'
        if uuid in be.Context._vnwService:
            if localId in be.Context._vnwService[uuid]._vnwConstraint:
                if riskCharacteristicName in be.Context._vnwService[uuid]._vnwConstraint[localId].riskCharacteristic:
                    return be.Context._vnwService[uuid]._vnwConstraint[localId].riskCharacteristic[riskCharacteristicName]
                else:
                    raise KeyError('riskCharacteristicName')
            else:
                raise KeyError('localId')
        else:
            raise KeyError('uuid')
