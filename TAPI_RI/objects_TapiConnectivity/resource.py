from globalClass import GlobalClass

class Resource(GlobalClass):

    def __init__(self, json_struct=None):
        self.resourceSpecification=""
        super(Resource, self).__init__(json_struct)

