from objects_common.jsonObject import JsonObject

class Capacity(JsonObject):

    def __init__(self, json_struct=None):
        self.committedInformationRate=""
        self.packetBwProfileType=""
        self.totalSize=""
        self.committedBurstSize=""
        self.peakBurstSize=""
        self.peakInformationRate=""
        self.couplingFlag=False
        self.colorAware=False
        super(Capacity, self).__init__(json_struct)

