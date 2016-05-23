from objects_common.jsonObject import JsonObject
from connection import Connection

class GetConnectionDetailsRPCOutputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.connection=Connection() #import
        super(GetConnectionDetailsRPCOutputSchema, self).__init__(json_struct)

