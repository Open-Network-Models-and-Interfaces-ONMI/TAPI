from virtualNetworkServicePort import VirtualNetworkServicePort
from nameAndValue import NameAndValue
from virtualNetworkConstraint import VirtualNetworkConstraint
from adminStatePac import AdminStatePac
from extensionsSpec import ExtensionsSpec
from timeRange import TimeRange
from serviceSpec import ServiceSpec
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType

class _vnwServiceSchema(ServiceSpec):

    def __init__(self, json_struct=None):
        self._servicePort=KeyedArrayType(VirtualNetworkServicePort, 'localId')
        self.layerProtocolName=ArrayType.factory(str)
        self.uuid=""
        self.name=KeyedArrayType(NameAndValue, 'valueName')
        self._vnwConstraint=KeyedArrayType(VirtualNetworkConstraint, 'localId')
        self._state=AdminStatePac() #import
        self._topology=""
        self.label=KeyedArrayType(NameAndValue, 'valueName')
        self._extensions=KeyedArrayType(ExtensionsSpec, 'extensionsSpecification')
        self._schedule=TimeRange() #import
        super(_vnwServiceSchema, self).__init__(json_struct)

