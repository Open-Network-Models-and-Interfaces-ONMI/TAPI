from adminStatePac import AdminStatePac
from transferTimingPac import TransferTimingPac
from nodeEdgePoint import NodeEdgePoint
from transferCapacityPac import TransferCapacityPac
from transferCostPac import TransferCostPac
from transferIntegrityPac import TransferIntegrityPac
from resourceSpec import ResourceSpec
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType

class Node(ResourceSpec):

    def __init__(self, json_struct=None):
        self.layerProtocolName=ArrayType.factory(str)
        self._state=AdminStatePac() #import
        self._transferTiming=TransferTimingPac() #import
        self._ownedNodeEdgePoint=KeyedArrayType(NodeEdgePoint, 'uuid')
        self._encapTopology=""
        self._transferCapacity=TransferCapacityPac() #import
        self._transferCost=TransferCostPac() #import
        self._aggregatedNodeEdgePoint=ArrayType.factory(str)
        self._transferIntegrity=TransferIntegrityPac() #import
        super(Node, self).__init__(json_struct)

