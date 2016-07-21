from link import Link
from nameAndValue import NameAndValue
from node import Node
from extensionsSpec import ExtensionsSpec
from resourceSpec import ResourceSpec
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType

class _topologySchema(ResourceSpec):

    def __init__(self, json_struct=None):
        self.layerProtocolName=ArrayType.factory(str)
        self.uuid=""
        self._link=KeyedArrayType(Link, 'uuid')
        self.label=KeyedArrayType(NameAndValue, 'valueName')
        self._node=KeyedArrayType(Node, 'uuid')
        self._extensions=KeyedArrayType(ExtensionsSpec, 'extensionsSpecification')
        self.name=KeyedArrayType(NameAndValue, 'valueName')
        super(_topologySchema, self).__init__(json_struct)

