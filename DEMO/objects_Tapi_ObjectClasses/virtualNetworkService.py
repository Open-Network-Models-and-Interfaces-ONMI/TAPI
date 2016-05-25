from virtualNetworkServicePort import VirtualNetworkServicePort
from scheduleInfo import ScheduleInfo
from virtualNetworkConstraint import VirtualNetworkConstraint
from adminStatePac import AdminStatePac
from globalClass import GlobalClass
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType

class VirtualNetworkService(GlobalClass):

    def __init__(self, json_struct=None):
        self._servicePort=KeyedArrayType(VirtualNetworkServicePort, 'localId')
        self.layerProtocolName=ArrayType.factory(str)
        self._schedule=ScheduleInfo() #import
        self._vnwConstraint=VirtualNetworkConstraint() #import
        self._state=AdminStatePac() #import
        self._topology=""
        super(VirtualNetworkService, self).__init__(json_struct)

