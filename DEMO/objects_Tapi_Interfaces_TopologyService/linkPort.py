from localClass import LocalClass

class LinkPort(LocalClass):

    def __init__(self, json_struct=None):
        self._nodeEdgePoint=""
        self.direction=""
        self.role=""
        super(LinkPort, self).__init__(json_struct)

