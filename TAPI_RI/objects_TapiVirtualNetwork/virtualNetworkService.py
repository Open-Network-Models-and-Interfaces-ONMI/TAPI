from virtualNetworkServicePort import VirtualNetworkServicePort
from timeRange import TimeRange
from virtualNetworkConstraint import VirtualNetworkConstraint
from adminStatePac import AdminStatePac
from serviceSpec import ServiceSpec
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType

class VirtualNetworkService(ServiceSpec):

    def __init__(self, json_struct=None):
        self._servicePort=KeyedArrayType(VirtualNetworkServicePort, 'localId')
        self.layerProtocolName=ArrayType.factory(str)
        self._schedule=TimeRange() #import
        self._vnwConstraint=KeyedArrayType(VirtualNetworkConstraint, 'localId')
        self._state=AdminStatePac() #import
        self._topology=""
        super(VirtualNetworkService, self).__init__(json_struct)

