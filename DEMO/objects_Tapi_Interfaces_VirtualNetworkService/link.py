from validationPac import ValidationPac
from layerProtocolTransitionPac import LayerProtocolTransitionPac
from adminStatePac import AdminStatePac
from transferTimingPac import TransferTimingPac
from transferCapacityPac import TransferCapacityPac
from transferCostPac import TransferCostPac
from riskParameterPac import RiskParameterPac
from linkPort import LinkPort
from transferIntegrityPac import TransferIntegrityPac
from globalClass import GlobalClass
from objects_common.arrayType import ArrayType

class Link(GlobalClass):

    def __init__(self, json_struct=None):
        self.direction=""
        self.layerProtocolName=ArrayType.factory(str)
        self._validation=ValidationPac() #import
        self._lpTransition=LayerProtocolTransitionPac() #import
        self._state=AdminStatePac() #import
        self._transferTiming=TransferTimingPac() #import
        self._node=ArrayType.factory(str)
        self._transferCapacity=TransferCapacityPac() #import
        self._transferCost=TransferCostPac() #import
        self._riskParameter=RiskParameterPac() #import
        self._linkPort=ArrayType.factory(LinkPort)
        self._transferIntegrity=TransferIntegrityPac() #import
        super(Link, self).__init__(json_struct)

