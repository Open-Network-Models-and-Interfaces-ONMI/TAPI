from localClass import LocalClass

class PathCompServicePort(LocalClass):

    def __init__(self, json_struct=None):
        self.serviceLayer=""
        self.direction=""
        self.role=""
        self._serviceEndPoint=""
        super(PathCompServicePort, self).__init__(json_struct)

