from objects_common.jsonObject import JsonObject
from objects_common.enumType import EnumType

class Capacity(JsonObject):

    def __init__(self, json_struct=None):
        self.committedInformationRate=""
        self.packetBwProfileType=Packetbwprofiletype(0)
        self.totalSize=Totalsize(0)
        self.committedBurstSize=""
        self.peakBurstSize=""
        self.peakInformationRate=""
        self.couplingFlag=False
        self.colorAware=False
        super(Capacity, self).__init__(json_struct)

class Packetbwprofiletype(EnumType):
    possible_values = ['NOT_APPLICABLE', 'MEF_10_x', 'RFC_2697', 'RFC_2698', 'RFC_4115']
    range_end = 5

    def __init__(self, initial_value):
        super(Packetbwprofiletype, self).__init__(initial_value)
class Totalsize(EnumType):
    possible_values = ['NOT_APPLICABLE', '10MBPS', '100MBPS', '1GBPS', '2_4GBPS', '10GBPS', '40GBPS', '100GBPS', '200GBPS', '400GBPS']
    range_end = 10

    def __init__(self, initial_value):
        super(Totalsize, self).__init__(initial_value)
