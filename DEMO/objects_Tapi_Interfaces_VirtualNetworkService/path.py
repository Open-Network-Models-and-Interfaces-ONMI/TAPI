from connectivityConstraint import ConnectivityConstraint
from teLink import TeLink
from globalClass import GlobalClass
from objects_common.keyedArrayType import KeyedArrayType

class Path(GlobalClass):

    def __init__(self, json_struct=None):
        self._routingConstraint=ConnectivityConstraint() #import
        self._telink=KeyedArrayType(TeLink, 'localId')
        super(Path, self).__init__(json_struct)

