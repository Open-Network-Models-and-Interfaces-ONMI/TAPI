from serviceEndPoint import ServiceEndPoint
from connectivityService import ConnectivityService
from virtualNetworkService import VirtualNetworkService
from topology import Topology
from path import Path
from globalClass import GlobalClass
from objects_common.keyedArrayType import KeyedArrayType

class ContextSchema(GlobalClass):

    def __init__(self, json_struct=None):
        self._serviceEndPoint=KeyedArrayType(ServiceEndPoint, 'uuid')
        self._connectivityService=KeyedArrayType(ConnectivityService, 'uuid')
        self._vnwService=KeyedArrayType(VirtualNetworkService, 'uuid')
        self._topology=KeyedArrayType(Topology, 'uuid')
        self._path=KeyedArrayType(Path, 'uuid')
        super(ContextSchema, self).__init__(json_struct)

