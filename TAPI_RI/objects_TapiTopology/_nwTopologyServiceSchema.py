from extensionsSpec import ExtensionsSpec
from nameAndValue import NameAndValue
from serviceSpec import ServiceSpec
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType

class _nwTopologyServiceSchema(ServiceSpec):

    def __init__(self, json_struct=None):
        self.uuid=""
        self._extensions=KeyedArrayType(ExtensionsSpec, 'extensionsSpecification')
        self._topology=ArrayType.factory(str)
        self.name=KeyedArrayType(NameAndValue, 'valueName')
        self.label=KeyedArrayType(NameAndValue, 'valueName')
        super(_nwTopologyServiceSchema, self).__init__(json_struct)

