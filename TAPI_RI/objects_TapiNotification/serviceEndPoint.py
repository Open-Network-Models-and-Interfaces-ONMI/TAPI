from objects_common.jsonObject import JsonObject
from layerProtocol import LayerProtocol
from lifecycleStatePac import LifecycleStatePac
from objects_common.keyedArrayType import KeyedArrayType

class ServiceEndPoint(JsonObject):

    def __init__(self, json_struct=None):
        self._layerProtocol=KeyedArrayType(LayerProtocol, 'localId')
        self.direction=""
        self._state=LifecycleStatePac() #import
        super(ServiceEndPoint, self).__init__(json_struct)

