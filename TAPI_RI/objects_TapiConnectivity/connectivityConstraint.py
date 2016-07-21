from teLink import TeLink
from capacity import Capacity
from costCharacteristic import CostCharacteristic
from latencyCharacteristic import LatencyCharacteristic
from localClass import LocalClass
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType
from objects_common.enumType import EnumType

class ConnectivityConstraint(LocalClass):

    def __init__(self, json_struct=None):
        self.serviceType=Servicetype(0)
        self._includePath=KeyedArrayType(TeLink, 'localId')
        self.requestedCapacity=Capacity() #import
        self.costCharacteristic=KeyedArrayType(CostCharacteristic, 'costName')
        self._avoidTopology=ArrayType.factory(str)
        self.serviceLayer=ArrayType.factory(str)
        self.serviceLevel=""
        self.latencyCharacteristic=KeyedArrayType(LatencyCharacteristic, 'trafficPropertyName')
        self._diversityExclusion=ArrayType.factory(str)
        self._includeTopology=ArrayType.factory(str)
        self._excludePath=KeyedArrayType(TeLink, 'localId')
        super(ConnectivityConstraint, self).__init__(json_struct)

class Servicetype(EnumType):
    possible_values = ['POINT_TO_POINT_CONNECTIVITY', 'POINT_TO_MULTIPOINT_CONNECTIVTY', 'MULTIPOINT_CONNECTIVITY']
    range_end = 3

    def __init__(self, initial_value):
        super(Servicetype, self).__init__(initial_value)
