from objects_common.jsonObject import JsonObject
from link import Link

class GetLinkDetailsRPCOutputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.link=Link() #import
        super(GetLinkDetailsRPCOutputSchema, self).__init__(json_struct)

