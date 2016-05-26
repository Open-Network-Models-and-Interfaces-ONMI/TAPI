import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_VnwserviceUuid_VnwconstraintRiskcharacteristicRiskcharacteristicnameImpl:

    @classmethod
    def put(cls, uuid, riskCharacteristicName, riskcharacteristic):
        print str(riskcharacteristic)
        print 'handling put'
        if uuid in Context._vnwService:
            Context._vnwService[uuid]._vnwConstraint.riskCharacteristic[riskCharacteristicName] = riskcharacteristic
        else:
            raise KeyError('riskCharacteristicName')

    @classmethod
    def post(cls, uuid, riskCharacteristicName, riskcharacteristic):
        print str(riskcharacteristic)
        print 'handling post'
        if uuid in Context._vnwService:
            Context._vnwService[uuid]._vnwConstraint.riskCharacteristic[riskCharacteristicName] = riskcharacteristic
        else:
            raise KeyError('riskCharacteristicName')

    @classmethod
    def delete(cls, uuid, riskCharacteristicName):
        print 'handling delete'
        if uuid in Context._vnwService:
            if riskCharacteristicName in Context._vnwService[uuid]._vnwConstraint.riskCharacteristic:
                del Context._vnwService[uuid]._vnwConstraint.riskCharacteristic[riskCharacteristicName]
            else:
                raise KeyError('riskCharacteristicName')
        else:
            raise KeyError('uuid')

    @classmethod
    def get(cls, uuid, riskCharacteristicName):
        print 'handling get'
        if uuid in Context._vnwService:
            if riskCharacteristicName in Context._vnwService[uuid]._vnwConstraint.riskCharacteristic:
                return Context._vnwService[uuid]._vnwConstraint.riskCharacteristic[riskCharacteristicName]
            else:
                raise KeyError('riskCharacteristicName')
        else:
            raise KeyError('uuid')
