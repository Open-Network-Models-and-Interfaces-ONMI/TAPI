from objects_common.jsonObject import JsonObject
from capacity import Capacity
from objects_common.keyedArrayType import KeyedArrayType

class TransferCapacityPac(JsonObject):

    def __init__(self, json_struct=None):
        self.capacityAssignedToUserView=KeyedArrayType(Capacity, 'totalSize')
        self.availableCapacity=Capacity() #import
        self.totalPotentialCapacity=Capacity() #import
        self.capacityInteractionAlgorithm=""
        super(TransferCapacityPac, self).__init__(json_struct)

