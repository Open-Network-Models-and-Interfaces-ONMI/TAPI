from localClass import LocalClass

class ConnectivityServicePort(LocalClass):

    def __init__(self, json_struct=None):
        self.serviceLayer=""
        self.direction=""
        self.role=""
        self._serviceEndPoint=""
        super(ConnectivityServicePort, self).__init__(json_struct)

