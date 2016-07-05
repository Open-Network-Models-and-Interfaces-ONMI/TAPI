from globalClass import GlobalClass

class Service(GlobalClass):

    def __init__(self, json_struct=None):
        self.serviceSpecification=""
        super(Service, self).__init__(json_struct)

