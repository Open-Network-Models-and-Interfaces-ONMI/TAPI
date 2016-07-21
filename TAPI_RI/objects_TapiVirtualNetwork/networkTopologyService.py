from serviceSpec import ServiceSpec
from objects_common.arrayType import ArrayType

class NetworkTopologyService(ServiceSpec):

    def __init__(self, json_struct=None):
        self._topology=ArrayType.factory(str)
        super(NetworkTopologyService, self).__init__(json_struct)

