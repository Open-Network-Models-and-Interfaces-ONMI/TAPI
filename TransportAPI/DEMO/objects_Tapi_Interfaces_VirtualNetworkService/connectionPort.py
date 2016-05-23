from localClass import LocalClass

class ConnectionPort(LocalClass):

    def __init__(self, json_struct=None):
        self.direction=""
        self._connectionEndPoint=""
        self.role=""
        super(ConnectionPort, self).__init__(json_struct)

