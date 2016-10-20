from objects_common.jsonObject import JsonObject
from connection import Connection
from objects_common.arrayType import ArrayType

class GetConnectionListRPCOutputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.conn=ArrayType.factory(Connection)
        super(GetConnectionListRPCOutputSchema, self).__init__(json_struct)

