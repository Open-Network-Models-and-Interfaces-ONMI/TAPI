from transferCapacityPac import TransferCapacityPac
from adminStatePac import AdminStatePac
from linkPort import LinkPort
from transferIntegrityPac import TransferIntegrityPac
from layerProtocolTransitionPac import LayerProtocolTransitionPac
from transferCostPac import TransferCostPac
from riskParameterPac import RiskParameterPac
from transferTimingPac import TransferTimingPac
from validationPac import ValidationPac
from resourceSpec import ResourceSpec
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType

class Link(ResourceSpec):

    def __init__(self, json_struct=None):
        self.direction=""
        self.layerProtocolName=ArrayType.factory(str)
        self._transferCapacity=TransferCapacityPac() #import
        self._state=AdminStatePac() #import
        self._linkPort=KeyedArrayType(LinkPort, 'localId')
        self._node=ArrayType.factory(str)
        self._transferIntegrity=TransferIntegrityPac() #import
        self._lpTransition=LayerProtocolTransitionPac() #import
        self._transferCost=TransferCostPac() #import
        self._riskParameter=RiskParameterPac() #import
        self._transferTiming=TransferTimingPac() #import
        self._validation=ValidationPac() #import
        super(Link, self).__init__(json_struct)

