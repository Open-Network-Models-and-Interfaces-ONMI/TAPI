from lpSpec import LpSpec
from localClass import LocalClass

class LayerProtocol(LocalClass):

    def __init__(self, json_struct=None):
        self.terminationState=""
        self.layerProtocolName=""
        self._lpSpecData=LpSpec() #import
        self.terminationDirection=""
        super(LayerProtocol, self).__init__(json_struct)

