from routingConstraint import RoutingConstraint
from teLink import TeLink
from resourceSpec import ResourceSpec
from objects_common.keyedArrayType import KeyedArrayType

class Path(ResourceSpec):

    def __init__(self, json_struct=None):
        self._routingConstraint=RoutingConstraint() #import
        self._telink=KeyedArrayType(TeLink, 'localId')
        super(Path, self).__init__(json_struct)

