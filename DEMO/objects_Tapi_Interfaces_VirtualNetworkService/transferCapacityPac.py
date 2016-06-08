from objects_common.jsonObject import JsonObject
from capacity import Capacity
from objects_common.arrayType import ArrayType

class TransferCapacityPac(JsonObject):

    def __init__(self, json_struct=None):
        self.capacityAssignedToUserView=ArrayType.factory(Capacity)
        self.availableCapacity=Capacity() #import
        self.totalPotentialCapacity=Capacity() #import
        self.capacityInteractionAlgorithm=""
        super(TransferCapacityPac, self).__init__(json_struct)

