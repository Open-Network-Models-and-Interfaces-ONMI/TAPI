from resource import Resource
from service import Service
from globalClass import GlobalClass
from objects_common.keyedArrayType import KeyedArrayType
from objects_TapiTopology._topologySchema import _topologySchema
from objects_TapiConnectivity._connectivityServiceSchema import _connectivityServiceSchema
from objects_TapiConnectivity._connectionSchema import _connectionSchema
from objects_TapiConnectivity._serviceEndPointSchema import _serviceEndPointSchema
from objects_TapiNotification.notification import Notification
from objects_TapiNotification.notificationSubscriptionService import NotificationSubscriptionService
from objects_TapiVirtualNetwork.virtualNetworkService import VirtualNetworkService
from objects_TapiPathComputation._pathCompServiceSchema import _pathCompServiceSchema
from objects_TapiPathComputation._pathSchema import _pathSchema

class ContextSchema(GlobalClass):

    def __init__(self, json_struct=None):
        self._connection=KeyedArrayType(_connectionSchema, 'uuid')
        self._notification=KeyedArrayType(Notification, 'uuid')
        self._vnwService=KeyedArrayType(VirtualNetworkService, 'uuid')
        self._topology=KeyedArrayType(_topologySchema, 'uuid')
        self._notifSubscription=KeyedArrayType(NotificationSubscriptionService, 'uuid')
        self._serviceEndPoint=KeyedArrayType(_serviceEndPointSchema, 'uuid')
        self._pathCompService=KeyedArrayType(_pathCompServiceSchema, 'uuid')
        self._connectivityService=KeyedArrayType(_connectivityServiceSchema, 'uuid')
        self._path=KeyedArrayType(_pathSchema, 'uuid')
        super(ContextSchema, self).__init__(json_struct)

