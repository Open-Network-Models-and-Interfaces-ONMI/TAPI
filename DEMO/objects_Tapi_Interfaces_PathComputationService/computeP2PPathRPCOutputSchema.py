from objects_common.jsonObject import JsonObject
from pathComputationService import PathComputationService

class ComputeP2PPathRPCOutputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.pathCompService=PathComputationService() #import
        super(ComputeP2PPathRPCOutputSchema, self).__init__(json_struct)

