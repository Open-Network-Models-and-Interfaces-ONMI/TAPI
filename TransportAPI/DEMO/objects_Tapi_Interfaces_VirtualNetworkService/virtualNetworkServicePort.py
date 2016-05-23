from localClass import LocalClass

class VirtualNetworkServicePort(LocalClass):

    def __init__(self, json_struct=None):
        self.serviceLayer=""
        self.direction=""
        self.role=""
        self._serviceEndPoint=""
        super(VirtualNetworkServicePort, self).__init__(json_struct)

