from objects_common.jsonObject import JsonObject
from pathComputationService import PathComputationService

class DeleteP2PPathRPCOutputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.pathCompService=PathComputationService() #import
        super(DeleteP2PPathRPCOutputSchema, self).__init__(json_struct)

