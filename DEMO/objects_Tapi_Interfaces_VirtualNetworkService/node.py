from adminStatePac import AdminStatePac
from transferTimingPac import TransferTimingPac
from nodeEdgePoint import NodeEdgePoint
from transferCapacityPac import TransferCapacityPac
from transferCostPac import TransferCostPac
from transferIntegrityPac import TransferIntegrityPac
from globalClass import GlobalClass
from objects_common.arrayType import ArrayType

class Node(GlobalClass):

    def __init__(self, json_struct=None):
        self._encapTopology=""
        self._state=AdminStatePac() #import
        self._transferTiming=TransferTimingPac() #import
        self._ownedNodeEdgePoint=ArrayType.factory(NodeEdgePoint)
        self.layerProtocolName=ArrayType.factory(str)
        self._transferCapacity=TransferCapacityPac() #import
        self._transferCost=TransferCostPac() #import
        self._aggregatedNodeEdgePoint=ArrayType.factory(str)
        self._transferIntegrity=TransferIntegrityPac() #import
        super(Node, self).__init__(json_struct)

