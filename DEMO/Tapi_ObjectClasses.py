from flask import json, Blueprint, request, Response
from flask.views import MethodView
import sys
from objects_common.keyedArrayType import KeyedArrayKeyError

import base64
import re

# BACKEND FUNCTIONS
from funcs_Tapi_ObjectClasses.context_NotificationNotificationidTargetobjectnameValuenameImpl import Context_NotificationNotificationidTargetobjectnameValuenameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_TransfercostCostcharacteristicCostalgorithmImpl import Context_TopologyUuid_NodeNode_Uuid_TransfercostCostcharacteristicCostalgorithmImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_UuidNameValuenameImpl import Context_TopologyUuid_NodeNode_UuidNameValuenameImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuidLabelValuenameImpl import Context_ServiceendpointUuidLabelValuenameImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_StateImpl import Context_ConnectivityserviceUuid_StateImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuidImpl import Context_PathcompserviceUuidImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuidNameValuenameImpl import Context_PathcompserviceUuidNameValuenameImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuid_LayerprotocolImpl import Context_ServiceendpointUuid_LayerprotocolImpl
from funcs_Tapi_ObjectClasses.context_NotifsubscriptionUuidLabelValuenameImpl import Context_NotifsubscriptionUuidLabelValuenameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_TransferintegrityImpl import Context_TopologyUuid_LinkLink_Uuid_TransferintegrityImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_StateImpl import Context_TopologyUuid_LinkLink_Uuid_StateImpl
from funcs_Tapi_ObjectClasses.context_NotifsubscriptionUuid_NotificationNotificationidAdditionalinfoImpl import Context_NotifsubscriptionUuid_NotificationNotificationidAdditionalinfoImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuidLabelImpl import Context_ConnectivityserviceUuidLabelImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuid_StateImpl import Context_ServiceendpointUuid_StateImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuidNameImpl import Context_PathcompserviceUuidNameImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuid_ConnectionendpointImpl import Context_ServiceendpointUuid_ConnectionendpointImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuidLabelImpl import Context_PathcompserviceUuidLabelImpl
from funcs_Tapi_ObjectClasses.context_VnwserviceUuid_ScheduleImpl import Context_VnwserviceUuid_ScheduleImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_TransfertimingImpl import Context_TopologyUuid_LinkLink_Uuid_TransfertimingImpl
from funcs_Tapi_ObjectClasses.context_NotifsubscriptionUuid_NotificationNotificationidTargetobjectnameValuenameImpl import Context_NotifsubscriptionUuid_NotificationNotificationidTargetobjectnameValuenameImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_LayerprotocolImpl import Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_LayerprotocolImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuidNameValuenameImpl import Context_ServiceendpointUuidNameValuenameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_StateImpl import Context_TopologyUuid_NodeNode_Uuid_StateImpl
from funcs_Tapi_ObjectClasses.context_NotifsubscriptionUuid_NotificationNotificationidChangedattributesImpl import Context_NotifsubscriptionUuid_NotificationNotificationidChangedattributesImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnectionConnection_UuidNameValuenameImpl import Context_ConnectivityserviceUuid_ConnectionConnection_UuidNameValuenameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnectionConnection_Uuid_RouteLocalidImpl import Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_RouteLocalidImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_TransfertimingQueuinglatencyLatencyvalueImpl import Context_TopologyUuid_NodeNode_Uuid_TransfertimingQueuinglatencyLatencyvalueImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_RiskparameterRiskcharacteristicImpl import Context_TopologyUuid_LinkLink_Uuid_RiskparameterRiskcharacteristicImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_TransfertimingQueuinglatencyImpl import Context_TopologyUuid_NodeNode_Uuid_TransfertimingQueuinglatencyImpl
from funcs_Tapi_ObjectClasses.context_VnwserviceUuidNameValuenameImpl import Context_VnwserviceUuidNameValuenameImpl
from funcs_Tapi_ObjectClasses.contextImpl import ContextImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeImpl import Context_TopologyUuid_NodeImpl
from funcs_Tapi_ObjectClasses.contextLabelImpl import ContextLabelImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_TransfertimingQueuinglatencyLatencyvalueImpl import Context_TopologyUuid_LinkLink_Uuid_TransfertimingQueuinglatencyLatencyvalueImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_TransfercapacityCapacityassignedtouserviewNumberingrangeImpl import Context_TopologyUuid_NodeNode_Uuid_TransfercapacityCapacityassignedtouserviewNumberingrangeImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceImpl import Context_PathcompserviceImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LtpspecdataImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LtpspecdataImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_UuidImpl import Context_TopologyUuid_NodeNode_UuidImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintRiskcharacteristicImpl import Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintRiskcharacteristicImpl
from funcs_Tapi_ObjectClasses.context_NotifsubscriptionUuidNameValuenameImpl import Context_NotifsubscriptionUuidNameValuenameImpl
from funcs_Tapi_ObjectClasses.context_VnwserviceUuid_VnwconstraintLatencycharacteristicLatencyvalueImpl import Context_VnwserviceUuid_VnwconstraintLatencycharacteristicLatencyvalueImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalid_LpspecdataImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalid_LpspecdataImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuidNameValuenameImpl import Context_TopologyUuidNameValuenameImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuid_RoutingconstraintLatencycharacteristicImpl import Context_PathcompserviceUuid_RoutingconstraintLatencycharacteristicImpl
from funcs_Tapi_ObjectClasses.context_NotificationNotificationidChangedattributesImpl import Context_NotificationNotificationidChangedattributesImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_StateImpl import Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_StateImpl
from funcs_Tapi_ObjectClasses.context_VnwserviceUuid_VnwconstraintImpl import Context_VnwserviceUuid_VnwconstraintImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuid_RoutingconstraintRequestedcapacityImpl import Context_PathcompserviceUuid_RoutingconstraintRequestedcapacityImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuid_PathPath_UuidNameImpl import Context_PathcompserviceUuid_PathPath_UuidNameImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnconstraintsRequestedcapacityImpl import Context_ConnectivityserviceUuid_ConnconstraintsRequestedcapacityImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnconstraintsLatencycharacteristicLatencyvalueImpl import Context_ConnectivityserviceUuid_ConnconstraintsLatencycharacteristicLatencyvalueImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_TransfercostImpl import Context_TopologyUuid_LinkLink_Uuid_TransfercostImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuid_RoutingconstraintLatencycharacteristicLatencyvalueImpl import Context_PathcompserviceUuid_RoutingconstraintLatencycharacteristicLatencyvalueImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidNameImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidNameImpl
from funcs_Tapi_ObjectClasses.context_NotifsubscriptionUuidNameImpl import Context_NotifsubscriptionUuidNameImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ServiceportImpl import Context_ConnectivityserviceUuid_ServiceportImpl
from funcs_Tapi_ObjectClasses.context_NotifsubscriptionUuid_NotificationImpl import Context_NotifsubscriptionUuid_NotificationImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_UuidLabelValuenameImpl import Context_TopologyUuid_LinkLink_UuidLabelValuenameImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuid_RoutingconstraintCostcharacteristicImpl import Context_PathcompserviceUuid_RoutingconstraintCostcharacteristicImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_UuidLabelImpl import Context_TopologyUuid_NodeNode_UuidLabelImpl
from funcs_Tapi_ObjectClasses.context_VnwserviceUuid_ServiceportLocalidImpl import Context_VnwserviceUuid_ServiceportLocalidImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_LptransitionImpl import Context_TopologyUuid_LinkLink_Uuid_LptransitionImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_ValidationValidationmechanismImpl import Context_TopologyUuid_LinkLink_Uuid_ValidationValidationmechanismImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintLatencycharacteristicImpl import Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintLatencycharacteristicImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuidLabelValuenameImpl import Context_PathcompserviceUuidLabelValuenameImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuid_PathImpl import Context_PathcompserviceUuid_PathImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuid_PathPath_UuidLabelImpl import Context_PathcompserviceUuid_PathPath_UuidLabelImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuid_RoutingconstraintImpl import Context_PathcompserviceUuid_RoutingconstraintImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuidNameImpl import Context_TopologyUuidNameImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_LayerprotocolLocalid_LpspecdataImpl import Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_LayerprotocolLocalid_LpspecdataImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuid_RoutingconstraintRiskcharacteristicRiskcharacteristicnameImpl import Context_PathcompserviceUuid_RoutingconstraintRiskcharacteristicRiskcharacteristicnameImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuidNameImpl import Context_ConnectivityserviceUuidNameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_LinkportLocalidImpl import Context_TopologyUuid_LinkLink_Uuid_LinkportLocalidImpl
from funcs_Tapi_ObjectClasses.context_VnwserviceUuidNameImpl import Context_VnwserviceUuidNameImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidNameValuenameImpl import Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidNameValuenameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidNameValuenameImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidNameValuenameImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuid_ServiceportLocalidImpl import Context_PathcompserviceUuid_ServiceportLocalidImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointImpl import Context_ServiceendpointImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuidNameImpl import Context_ServiceendpointUuidNameImpl
from funcs_Tapi_ObjectClasses.contextNameImpl import ContextNameImpl
from funcs_Tapi_ObjectClasses.context_VnwserviceUuid_VnwconstraintCostcharacteristicImpl import Context_VnwserviceUuid_VnwconstraintCostcharacteristicImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuid_ObjectivefunctionImpl import Context_PathcompserviceUuid_ObjectivefunctionImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_RiskparameterRiskcharacteristicRiskcharacteristicnameImpl import Context_TopologyUuid_LinkLink_Uuid_RiskparameterRiskcharacteristicRiskcharacteristicnameImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_LayerprotocolLocalidImpl import Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_LayerprotocolLocalidImpl
from funcs_Tapi_ObjectClasses.context_NotifsubscriptionImpl import Context_NotifsubscriptionImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuid_LayerprotocolLocalidImpl import Context_ServiceendpointUuid_LayerprotocolLocalidImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_TransfercostCostcharacteristicCostalgorithmImpl import Context_TopologyUuid_LinkLink_Uuid_TransfercostCostcharacteristicCostalgorithmImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidLabelValuenameImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidLabelValuenameImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ServiceportLocalidImpl import Context_ConnectivityserviceUuid_ServiceportLocalidImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_TransfertimingQueuinglatencyImpl import Context_TopologyUuid_LinkLink_Uuid_TransfertimingQueuinglatencyImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuidImpl import Context_ConnectivityserviceUuidImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuidImpl import Context_TopologyUuidImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnectionConnection_UuidImpl import Context_ConnectivityserviceUuid_ConnectionConnection_UuidImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceImpl import Context_ConnectivityserviceImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_ValidationImpl import Context_TopologyUuid_LinkLink_Uuid_ValidationImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_TransfercapacityTotalpotentialcapacityImpl import Context_TopologyUuid_LinkLink_Uuid_TransfercapacityTotalpotentialcapacityImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointImpl
from funcs_Tapi_ObjectClasses.context_TopologyImpl import Context_TopologyImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnectionImpl import Context_ConnectivityserviceUuid_ConnectionImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnectionConnection_Uuid_RouteImpl import Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_RouteImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_UuidLabelValuenameImpl import Context_TopologyUuid_NodeNode_UuidLabelValuenameImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnectionConnection_Uuid_StateImpl import Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_StateImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnconstraintsRiskcharacteristicImpl import Context_ConnectivityserviceUuid_ConnconstraintsRiskcharacteristicImpl
from funcs_Tapi_ObjectClasses.context_NotifsubscriptionUuid_NotificationNotificationidAdditionalinfoValuenameImpl import Context_NotifsubscriptionUuid_NotificationNotificationidAdditionalinfoValuenameImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnectionConnection_Uuid_ConnectionportLocalidImpl import Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_ConnectionportLocalidImpl
from funcs_Tapi_ObjectClasses.context_VnwserviceUuidImpl import Context_VnwserviceUuidImpl
from funcs_Tapi_ObjectClasses.context_NotifsubscriptionUuid_SubscriptionfilterImpl import Context_NotifsubscriptionUuid_SubscriptionfilterImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnectionConnection_UuidNameImpl import Context_ConnectivityserviceUuid_ConnectionConnection_UuidNameImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintCostcharacteristicCostalgorithmImpl import Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintCostcharacteristicCostalgorithmImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuid_RoutingconstraintRiskcharacteristicImpl import Context_PathcompserviceUuid_RoutingconstraintRiskcharacteristicImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_RiskparameterImpl import Context_TopologyUuid_LinkLink_Uuid_RiskparameterImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuidLabelImpl import Context_TopologyUuidLabelImpl
from funcs_Tapi_ObjectClasses.context_VnwserviceImpl import Context_VnwserviceImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidImpl import Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuid_LayerprotocolLocalid_LpspecdataImpl import Context_ServiceendpointUuid_LayerprotocolLocalid_LpspecdataImpl
from funcs_Tapi_ObjectClasses.context_NotificationNotificationidAdditionalinfoValuenameImpl import Context_NotificationNotificationidAdditionalinfoValuenameImpl
from funcs_Tapi_ObjectClasses.context_VnwserviceUuidLabelImpl import Context_VnwserviceUuidLabelImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintRiskcharacteristicRiskcharacteristicnameImpl import Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintRiskcharacteristicRiskcharacteristicnameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_TransfercapacityCapacityassignedtouserviewImpl import Context_TopologyUuid_LinkLink_Uuid_TransfercapacityCapacityassignedtouserviewImpl
from funcs_Tapi_ObjectClasses.context_VnwserviceUuid_VnwconstraintLatencycharacteristicImpl import Context_VnwserviceUuid_VnwconstraintLatencycharacteristicImpl
from funcs_Tapi_ObjectClasses.context_VnwserviceUuid_VnwconstraintRequestedcapacityImpl import Context_VnwserviceUuid_VnwconstraintRequestedcapacityImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnconstraintsCostcharacteristicCostalgorithmImpl import Context_ConnectivityserviceUuid_ConnconstraintsCostcharacteristicCostalgorithmImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_TransfercostCostcharacteristicImpl import Context_TopologyUuid_NodeNode_Uuid_TransfercostCostcharacteristicImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuid_PathPath_UuidNameValuenameImpl import Context_PathcompserviceUuid_PathPath_UuidNameValuenameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkImpl import Context_TopologyUuid_LinkImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuidNameValuenameImpl import Context_ConnectivityserviceUuidNameValuenameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_TransfercapacityCapacityassignedtouserviewNumberingrangeImpl import Context_TopologyUuid_LinkLink_Uuid_TransfercapacityCapacityassignedtouserviewNumberingrangeImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuid_OptimizationconstraintImpl import Context_PathcompserviceUuid_OptimizationconstraintImpl
from funcs_Tapi_ObjectClasses.context_NotifsubscriptionUuid_NotificationNotificationidImpl import Context_NotifsubscriptionUuid_NotificationNotificationidImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_LinkportImpl import Context_TopologyUuid_LinkLink_Uuid_LinkportImpl
from funcs_Tapi_ObjectClasses.context_VnwserviceUuid_ServiceportImpl import Context_VnwserviceUuid_ServiceportImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidLabelImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidLabelImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnectionConnection_Uuid_ConnectionportImpl import Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_ConnectionportImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintCostcharacteristicImpl import Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintCostcharacteristicImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnconstraintsRiskcharacteristicRiskcharacteristicnameImpl import Context_ConnectivityserviceUuid_ConnconstraintsRiskcharacteristicRiskcharacteristicnameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_TransfercapacityAvailablecapacityImpl import Context_TopologyUuid_LinkLink_Uuid_TransfercapacityAvailablecapacityImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_ValidationValidationmechanismValidationrobustnessImpl import Context_TopologyUuid_LinkLink_Uuid_ValidationValidationmechanismValidationrobustnessImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnectionConnection_UuidLabelValuenameImpl import Context_ConnectivityserviceUuid_ConnectionConnection_UuidLabelValuenameImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidLabelImpl import Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidLabelImpl
from funcs_Tapi_ObjectClasses.context_NotifsubscriptionUuidLabelImpl import Context_NotifsubscriptionUuidLabelImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuid_RoutingconstraintCostcharacteristicCostalgorithmImpl import Context_PathcompserviceUuid_RoutingconstraintCostcharacteristicCostalgorithmImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidNameImpl import Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidNameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuidLabelValuenameImpl import Context_TopologyUuidLabelValuenameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_TransfercapacityImpl import Context_TopologyUuid_LinkLink_Uuid_TransfercapacityImpl
from funcs_Tapi_ObjectClasses.context_NotifsubscriptionUuid_NotificationNotificationidTargetobjectnameImpl import Context_NotifsubscriptionUuid_NotificationNotificationidTargetobjectnameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_TransfercostCostcharacteristicImpl import Context_TopologyUuid_LinkLink_Uuid_TransfercostCostcharacteristicImpl
from funcs_Tapi_ObjectClasses.context_VnwserviceUuid_VnwconstraintRiskcharacteristicRiskcharacteristicnameImpl import Context_VnwserviceUuid_VnwconstraintRiskcharacteristicRiskcharacteristicnameImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuidLabelImpl import Context_ServiceendpointUuidLabelImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_UuidNameImpl import Context_TopologyUuid_LinkLink_UuidNameImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuid_PathPath_UuidLabelValuenameImpl import Context_PathcompserviceUuid_PathPath_UuidLabelValuenameImpl
from funcs_Tapi_ObjectClasses.context_NotificationNotificationidImpl import Context_NotificationNotificationidImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintRequestedcapacityImpl import Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintRequestedcapacityImpl
from funcs_Tapi_ObjectClasses.context_VnwserviceUuid_StateImpl import Context_VnwserviceUuid_StateImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuid_ServiceportImpl import Context_PathcompserviceUuid_ServiceportImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_StateImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_StateImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuidLabelValuenameImpl import Context_ConnectivityserviceUuidLabelValuenameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_TransferintegrityImpl import Context_TopologyUuid_NodeNode_Uuid_TransferintegrityImpl
from funcs_Tapi_ObjectClasses.context_NotifsubscriptionUuidImpl import Context_NotifsubscriptionUuidImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_UuidLabelImpl import Context_TopologyUuid_LinkLink_UuidLabelImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ScheduleImpl import Context_ConnectivityserviceUuid_ScheduleImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnectionConnection_UuidLabelImpl import Context_ConnectivityserviceUuid_ConnectionConnection_UuidLabelImpl
from funcs_Tapi_ObjectClasses.context_VnwserviceUuid_VnwconstraintCostcharacteristicCostalgorithmImpl import Context_VnwserviceUuid_VnwconstraintCostcharacteristicCostalgorithmImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_TransfercapacityImpl import Context_TopologyUuid_NodeNode_Uuid_TransfercapacityImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnconstraintsCostcharacteristicImpl import Context_ConnectivityserviceUuid_ConnconstraintsCostcharacteristicImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalidImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalidImpl
from funcs_Tapi_ObjectClasses.contextNameValuenameImpl import ContextNameValuenameImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_LtpspecdataImpl import Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_LtpspecdataImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnconstraintsImpl import Context_ConnectivityserviceUuid_ConnconstraintsImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuid_PathPath_Uuid_TelinkLocalidImpl import Context_PathcompserviceUuid_PathPath_Uuid_TelinkLocalidImpl
from funcs_Tapi_ObjectClasses.context_NotificationNotificationidTargetobjectnameImpl import Context_NotificationNotificationidTargetobjectnameImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuid_PathPath_Uuid_TelinkImpl import Context_PathcompserviceUuid_PathPath_Uuid_TelinkImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuid_PathPath_UuidImpl import Context_PathcompserviceUuid_PathPath_UuidImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_TransfertimingImpl import Context_TopologyUuid_NodeNode_Uuid_TransfertimingImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_UuidNameImpl import Context_TopologyUuid_NodeNode_UuidNameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_TransfercapacityAvailablecapacityImpl import Context_TopologyUuid_NodeNode_Uuid_TransfercapacityAvailablecapacityImpl
from funcs_Tapi_ObjectClasses.context_VnwserviceUuidLabelValuenameImpl import Context_VnwserviceUuidLabelValuenameImpl
from funcs_Tapi_ObjectClasses.context_NotificationNotificationidAdditionalinfoImpl import Context_NotificationNotificationidAdditionalinfoImpl
from funcs_Tapi_ObjectClasses.context_NotificationImpl import Context_NotificationImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnconstraintsLatencycharacteristicImpl import Context_ConnectivityserviceUuid_ConnconstraintsLatencycharacteristicImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_TransfercostImpl import Context_TopologyUuid_NodeNode_Uuid_TransfercostImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintImpl import Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintImpl
from funcs_Tapi_ObjectClasses.context_VnwserviceUuid_VnwconstraintRiskcharacteristicImpl import Context_VnwserviceUuid_VnwconstraintRiskcharacteristicImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_TransfercapacityCapacityassignedtouserviewImpl import Context_TopologyUuid_NodeNode_Uuid_TransfercapacityCapacityassignedtouserviewImpl
from funcs_Tapi_ObjectClasses.context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintLatencycharacteristicLatencyvalueImpl import Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintLatencycharacteristicLatencyvalueImpl
from funcs_Tapi_ObjectClasses.contextLabelValuenameImpl import ContextLabelValuenameImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuid_LtpspecdataImpl import Context_ServiceendpointUuid_LtpspecdataImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidLabelValuenameImpl import Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidLabelValuenameImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuidImpl import Context_ServiceendpointUuidImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_UuidImpl import Context_TopologyUuid_LinkLink_UuidImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_TransfercapacityTotalpotentialcapacityImpl import Context_TopologyUuid_NodeNode_Uuid_TransfercapacityTotalpotentialcapacityImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_UuidNameValuenameImpl import Context_TopologyUuid_LinkLink_UuidNameValuenameImpl

# CALLABLE OBJECTS
from objects_Tapi_ObjectClasses.linkPort import LinkPort
from objects_Tapi_ObjectClasses.virtualNetworkServicePort import VirtualNetworkServicePort
from objects_Tapi_ObjectClasses.capacity import Capacity
from objects_Tapi_ObjectClasses.transferCostPac import TransferCostPac
from objects_Tapi_ObjectClasses.notification import Notification
from objects_Tapi_ObjectClasses.timeRange import TimeRange
from objects_Tapi_ObjectClasses.layerProtocolTransitionPac import LayerProtocolTransitionPac
from objects_Tapi_ObjectClasses.transferTimingPac import TransferTimingPac
from objects_Tapi_ObjectClasses.transferIntegrityPac import TransferIntegrityPac
from objects_Tapi_ObjectClasses.nameAndValue import NameAndValue
from objects_Tapi_ObjectClasses.adminStatePac import AdminStatePac
from objects_Tapi_ObjectClasses.serviceEndPoint import ServiceEndPoint
from objects_Tapi_ObjectClasses.validationMechanism import ValidationMechanism
from objects_Tapi_ObjectClasses.node import Node
from objects_Tapi_ObjectClasses.teLink import TeLink
from objects_Tapi_ObjectClasses.costCharacteristic import CostCharacteristic
from objects_Tapi_ObjectClasses.connectionEndPoint import ConnectionEndPoint
from objects_Tapi_ObjectClasses.transferCapacityPac import TransferCapacityPac
from objects_Tapi_ObjectClasses.connectivityService import ConnectivityService
from objects_Tapi_ObjectClasses.connectionPort import ConnectionPort
from objects_Tapi_ObjectClasses.ltpSpec import LtpSpec
from objects_Tapi_ObjectClasses.pathComputationService import PathComputationService
from objects_Tapi_ObjectClasses.link import Link
from objects_Tapi_ObjectClasses.localClass import LocalClass
from objects_Tapi_ObjectClasses.path import Path
from objects_Tapi_ObjectClasses.topology import Topology
from objects_Tapi_ObjectClasses.queuingLatency import QueuingLatency
from objects_Tapi_ObjectClasses.connectivityConstraint import ConnectivityConstraint
from objects_Tapi_ObjectClasses.pathCompServicePort import PathCompServicePort
from objects_Tapi_ObjectClasses.virtualNetworkService import VirtualNetworkService
from objects_Tapi_ObjectClasses.route import Route
from objects_Tapi_ObjectClasses.contextSchema import ContextSchema
from objects_Tapi_ObjectClasses.connection import Connection
from objects_Tapi_ObjectClasses.pathOptimizationConstraint import PathOptimizationConstraint
from objects_Tapi_ObjectClasses.pathObjectiveFunction import PathObjectiveFunction
from objects_Tapi_ObjectClasses.virtualNetworkConstraint import VirtualNetworkConstraint
from objects_Tapi_ObjectClasses.riskCharacteristic import RiskCharacteristic
from objects_Tapi_ObjectClasses.riskParameterPac import RiskParameterPac
from objects_Tapi_ObjectClasses.connectivityServicePort import ConnectivityServicePort
from objects_Tapi_ObjectClasses.nameAndValueChange import NameAndValueChange
from objects_Tapi_ObjectClasses.operationalStatePac import OperationalStatePac
from objects_Tapi_ObjectClasses.globalClass import GlobalClass
from objects_Tapi_ObjectClasses.layerProtocol import LayerProtocol
from objects_Tapi_ObjectClasses.notificationSubscriptionService import NotificationSubscriptionService
from objects_Tapi_ObjectClasses.nodeEdgePoint import NodeEdgePoint
from objects_Tapi_ObjectClasses.lpSpec import LpSpec
from objects_Tapi_ObjectClasses.lifecycleStatePac import LifecycleStatePac
from objects_Tapi_ObjectClasses.validationPac import ValidationPac
from objects_Tapi_ObjectClasses.subscriptionFilter import SubscriptionFilter

users = {"admin": "pswd1", "user": "pswd2"}

setattr(sys.modules[__name__], __name__,  Blueprint(__name__, __name__))



def byteify(input):
    # Convert JSON unicode strings to python byte strings, recursively on a json_struct
    if isinstance(input, dict):
        return {byteify(key):byteify(value) for key,value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

def json_loads(json_string):
    # Try to use json.loads and raise HTTP Error
    try:
        json_struct = json.loads(json_string) #json parser.
    except ValueError:
        raise BadRequestError("Malformed JSON")
    else:
        return byteify(json_struct)

def json_dumps(js):
    # Pretty-print version of json.dumps
    return json.dumps(js, sort_keys=True, indent=4, separators=(',', ': '))

def create_instance(klass, json_struct, id=None):
    # Try to create an object instance and raise HTTP Errors
    try:
        new_object = klass(json_struct) # Creates an object instance of type klass from the json_struct data
    except KeyError as inst:
        return BadRequestError("Unknown entity name in JSON:" + "<br>" + inst.args[0])
    except TypeError as inst:
        key = inst.args[0]
        value = json.dumps(inst.args[1])
        return BadRequestError("Incorrect type in JSON:" + "<br>" +
                              key + " was:" + "<br>" +
                              value + "<br>" +
                              "Allowed type:" + "<br>" +
                              inst.args[2])
    except ValueError as inst:
        if type(inst.args[1]) == str:
            return BadRequestError("Incorrect value in JSON:" + "<br>" +
                                  "Enum " + inst.args[0] + " was:" + "<br>" +
                                  inst.args[1] + "<br>" +
                                  "Allowed values:" + "<br>" +
                                  "[" + ", ".join(inst.args[2]) + "]")
        elif type(inst.args[1]) == int:
            return BadRequestError("Incorrect value in JSON:" + "<br>" +
                                  "Enum " + inst.args[0] + " was:" + "<br>" +
                                  str(inst.args[1]) + "<br>" +
                                  "Allowed range:" + "<br>" +
                                  "1 - " + str(inst.args[2]))
    except KeyedArrayKeyError as inst:
        return BadRequestError("Error in JSON:" + "<br>" +
                              "Missing key in list:" + "<br>" +
                              inst.args[0] + "<br>" +
                              "Received JSON:" + "<br>" +
                              json.dumps(inst.args[1]) + "<br>" +
                              "Key name:" + "<br>" +
                              inst.args[2])
    else:
        # Check if the id given in the URL matches the id given in the body
        if id != None and id[0] != getattr(new_object, id[1]):
            return BadRequestError(id[1] + " in body not matching " + id[1] + " in URL")
        else:
            return new_object

def modify_instance(existing_object, json_struct):
    try:
        existing_object.load_json(json_struct)
    except KeyError as inst:
        return BadRequestError("Unknown entity name in JSON:" + "<br>" + inst.args[0])
    except TypeError as inst:
        key = inst.args[0]
        value = json.dumps(inst.args[1])
        return BadRequestError("Incorrect type in JSON:" + "<br>" +
                              key + " was:" + "<br>" +
                              value + "<br>" +
                              "Allowed type:" + "<br>" +
                              inst.args[2])
    except ValueError as inst:
        if type(inst.args[1]) == str:
            return BadRequestError("Incorrect value in JSON:" + "<br>" +
                                  "Enum " + inst.args[0] + " was:" + "<br>" +
                                  inst.args[1] + "<br>" +
                                  "Allowed values:" + "<br>" +
                                  "[" + ", ".join(inst.args[2]) + "]")
        elif type(inst.args[1]) == int:
            return BadRequestError("Incorrect value in JSON:" + "<br>" +
                                  "Enum " + inst.args[0] + " was:" + "<br>" +
                                  str(inst.args[1]) + "<br>" +
                                  "Allowed range:" + "<br>" +
                                  "1 - " + str(inst.args[2]))
    except KeyedArrayKeyError as inst:
        return BadRequestError("Error in JSON:" + "<br>" +
                              "Missing key in list:" + "<br>" +
                              inst.args[0] + "<br>" +
                              "Received JSON:" + "<br>" +
                              json.dumps(inst.args[1]) + "<br>" +
                              "Key name:" + "<br>" +
                              inst.args[2])
    else:
        return existing_object


class NotFoundError(Response):
    def __init__(self, message):
        super(NotFoundError, self).__init__()
        self.status = '404 '+message
        self.status_code = 404
        self.headers = {'Content-Type': 'text/html'}
        self.data = '<h1>'+message+'</h1>'

class BadRequestError(Response):
    def __init__(self, message):
        super(BadRequestError, self).__init__()
        self.status = '400 '+message
        self.status_code = 400
        self.headers = {'Content-Type': 'text/html'}
        self.data = '<h1>'+message+'</h1>'

class Unauthorized(Response):
    def __init__(self, message):
        super(Unauthorized, self).__init__()
        self.status = '401 '+message
        self.status_code = 401
        self.headers = {'WWW-Authenticate','Basic realm="Auth example"'}
        self.data = '<h1>'+message+'</h1>'

class Successful(Response):
    def __init__(self, message, info=''):
        super(Successful, self).__init__()
        self.status = '200 '+message
        self.status_code = 200
        self.headers = {'Content-Type': 'application/json'}
        self.data = info


#/restconf/config/Context/_notification/(\w+)/targetObjectName/(\w+)/
class Context_NotificationNotificationidTargetobjectnameValuename(MethodView):

    def get(self, notificationId, valueName):
        print "Retrieve operation of resource: targetObjectName"
        try:
            response = Context_NotificationNotificationidTargetobjectnameValuenameImpl.get(notificationId, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_transferCost/costCharacteristic/(\w+)/
class Context_TopologyUuid_NodeNode_Uuid_TransfercostCostcharacteristicCostalgorithm(MethodView):

    def get(self, uuid, node_uuid, costAlgorithm):
        print "Retrieve operation of resource: costCharacteristic"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_TransfercostCostcharacteristicCostalgorithmImpl.get(uuid, node_uuid, costAlgorithm)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/name/(\w+)/
class Context_TopologyUuid_NodeNode_UuidNameValuename(MethodView):

    def get(self, uuid, node_uuid, valueName):
        print "Retrieve operation of resource: name"
        try:
            response = Context_TopologyUuid_NodeNode_UuidNameValuenameImpl.get(uuid, node_uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_serviceEndPoint/(\w+)/label/(\w+)/
class Context_ServiceendpointUuidLabelValuename(MethodView):

    def get(self, uuid, valueName):
        print "Retrieve operation of resource: label"
        try:
            response = Context_ServiceendpointUuidLabelValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_state/
class Context_ConnectivityserviceUuid_State(MethodView):

    def put(self, uuid):
        print "Update operation of resource: _state"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_ConnectivityserviceUuid_StateImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(AdminStatePac, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_ConnectivityserviceUuid_StateImpl.put(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    Context_ConnectivityserviceUuid_StateImpl.put(uuid, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid):
        print "Create operation of resource: _state"
        try:
            response = Context_ConnectivityserviceUuid_StateImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(AdminStatePac, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_ConnectivityserviceUuid_StateImpl.post(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid):
        print "Delete operation of resource: _state"
        try:
            response=Context_ConnectivityserviceUuid_StateImpl.delete(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid):
        print "Retrieve operation of resource: _state"
        try:
            response = Context_ConnectivityserviceUuid_StateImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/
class Context_PathcompserviceUuid(MethodView):

    def put(self, uuid):
        print "Update operation of resource: _pathCompService"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_PathcompserviceUuidImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(PathComputationService, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_PathcompserviceUuidImpl.put(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    Context_PathcompserviceUuidImpl.put(uuid, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid):
        print "Create operation of resource: _pathCompService"
        try:
            response = Context_PathcompserviceUuidImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(PathComputationService, json_struct, (uuid,'uuid'))
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_PathcompserviceUuidImpl.post(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid):
        print "Delete operation of resource: _pathCompService"
        try:
            response=Context_PathcompserviceUuidImpl.delete(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid):
        print "Retrieve operation of resource: _pathCompService"
        try:
            response = Context_PathcompserviceUuidImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/name/(\w+)/
class Context_PathcompserviceUuidNameValuename(MethodView):

    def put(self, uuid, valueName):
        print "Update operation of resource: name"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_PathcompserviceUuidNameValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            if inst.args[0] != 'valueName':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(NameAndValue, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_PathcompserviceUuidNameValuenameImpl.put(uuid, valueName, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    Context_PathcompserviceUuidNameValuenameImpl.put(uuid, valueName, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid, valueName):
        print "Create operation of resource: name"
        try:
            response = Context_PathcompserviceUuidNameValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            if inst.args[0] != 'valueName':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(NameAndValue, json_struct, (valueName,'valueName'))
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_PathcompserviceUuidNameValuenameImpl.post(uuid, valueName, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid, valueName):
        print "Delete operation of resource: name"
        try:
            response=Context_PathcompserviceUuidNameValuenameImpl.delete(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid, valueName):
        print "Retrieve operation of resource: name"
        try:
            response = Context_PathcompserviceUuidNameValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_serviceEndPoint/(\w+)/_layerProtocol/
class Context_ServiceendpointUuid_Layerprotocol(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _layerProtocol"
        try:
            response = Context_ServiceendpointUuid_LayerprotocolImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notifSubscription/(\w+)/label/(\w+)/
class Context_NotifsubscriptionUuidLabelValuename(MethodView):

    def put(self, uuid, valueName):
        print "Update operation of resource: label"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_NotifsubscriptionUuidLabelValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            if inst.args[0] != 'valueName':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(NameAndValue, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_NotifsubscriptionUuidLabelValuenameImpl.put(uuid, valueName, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    Context_NotifsubscriptionUuidLabelValuenameImpl.put(uuid, valueName, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid, valueName):
        print "Create operation of resource: label"
        try:
            response = Context_NotifsubscriptionUuidLabelValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            if inst.args[0] != 'valueName':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(NameAndValue, json_struct, (valueName,'valueName'))
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_NotifsubscriptionUuidLabelValuenameImpl.post(uuid, valueName, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid, valueName):
        print "Delete operation of resource: label"
        try:
            response=Context_NotifsubscriptionUuidLabelValuenameImpl.delete(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid, valueName):
        print "Retrieve operation of resource: label"
        try:
            response = Context_NotifsubscriptionUuidLabelValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_transferIntegrity/
class Context_TopologyUuid_LinkLink_Uuid_Transferintegrity(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: _transferIntegrity"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_TransferintegrityImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_state/
class Context_TopologyUuid_LinkLink_Uuid_State(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: _state"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_StateImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notifSubscription/(\w+)/_notification/(\w+)/additionalInfo/
class Context_NotifsubscriptionUuid_NotificationNotificationidAdditionalinfo(MethodView):

    def get(self, uuid, notificationId):
        print "Retrieve operation of resource: additionalInfo"
        try:
            response = Context_NotifsubscriptionUuid_NotificationNotificationidAdditionalinfoImpl.get(uuid, notificationId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/label/
class Context_ConnectivityserviceUuidLabel(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: label"
        try:
            response = Context_ConnectivityserviceUuidLabelImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_serviceEndPoint/(\w+)/_state/
class Context_ServiceendpointUuid_State(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _state"
        try:
            response = Context_ServiceendpointUuid_StateImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/name/
class Context_PathcompserviceUuidName(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: name"
        try:
            response = Context_PathcompserviceUuidNameImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_serviceEndPoint/(\w+)/_connectionEndPoint/
class Context_ServiceendpointUuid_Connectionendpoint(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _connectionEndPoint"
        try:
            response = Context_ServiceendpointUuid_ConnectionendpointImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/label/
class Context_PathcompserviceUuidLabel(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: label"
        try:
            response = Context_PathcompserviceUuidLabelImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/(\w+)/_schedule/
class Context_VnwserviceUuid_Schedule(MethodView):

    def put(self, uuid):
        print "Update operation of resource: _schedule"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_VnwserviceUuid_ScheduleImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(TimeRange, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_VnwserviceUuid_ScheduleImpl.put(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    Context_VnwserviceUuid_ScheduleImpl.put(uuid, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid):
        print "Create operation of resource: _schedule"
        try:
            response = Context_VnwserviceUuid_ScheduleImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(TimeRange, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_VnwserviceUuid_ScheduleImpl.post(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid):
        print "Delete operation of resource: _schedule"
        try:
            response=Context_VnwserviceUuid_ScheduleImpl.delete(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid):
        print "Retrieve operation of resource: _schedule"
        try:
            response = Context_VnwserviceUuid_ScheduleImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_transferTiming/
class Context_TopologyUuid_LinkLink_Uuid_Transfertiming(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: _transferTiming"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_TransfertimingImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notifSubscription/(\w+)/_notification/(\w+)/targetObjectName/(\w+)/
class Context_NotifsubscriptionUuid_NotificationNotificationidTargetobjectnameValuename(MethodView):

    def get(self, uuid, notificationId, valueName):
        print "Retrieve operation of resource: targetObjectName"
        try:
            response = Context_NotifsubscriptionUuid_NotificationNotificationidTargetobjectnameValuenameImpl.get(uuid, notificationId, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_serviceEndPoint/(\w+)/_connectionEndPoint/(\w+)/_layerProtocol/
class Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_Layerprotocol(MethodView):

    def get(self, uuid, connectionEndPoint_uuid):
        print "Retrieve operation of resource: _layerProtocol"
        try:
            response = Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_LayerprotocolImpl.get(uuid, connectionEndPoint_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_serviceEndPoint/(\w+)/name/(\w+)/
class Context_ServiceendpointUuidNameValuename(MethodView):

    def get(self, uuid, valueName):
        print "Retrieve operation of resource: name"
        try:
            response = Context_ServiceendpointUuidNameValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_state/
class Context_TopologyUuid_NodeNode_Uuid_State(MethodView):

    def get(self, uuid, node_uuid):
        print "Retrieve operation of resource: _state"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_StateImpl.get(uuid, node_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notifSubscription/(\w+)/_notification/(\w+)/changedAttributes/
class Context_NotifsubscriptionUuid_NotificationNotificationidChangedattributes(MethodView):

    def get(self, uuid, notificationId):
        print "Retrieve operation of resource: changedAttributes"
        try:
            response = Context_NotifsubscriptionUuid_NotificationNotificationidChangedattributesImpl.get(uuid, notificationId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connection/(\w+)/name/(\w+)/
class Context_ConnectivityserviceUuid_ConnectionConnection_UuidNameValuename(MethodView):

    def get(self, uuid, connection_uuid, valueName):
        print "Retrieve operation of resource: name"
        try:
            response = Context_ConnectivityserviceUuid_ConnectionConnection_UuidNameValuenameImpl.get(uuid, connection_uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_ownedNodeEdgePoint/(\w+)/_layerProtocol/
class Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_Layerprotocol(MethodView):

    def get(self, uuid, node_uuid, ownedNodeEdgePoint_uuid):
        print "Retrieve operation of resource: _layerProtocol"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolImpl.get(uuid, node_uuid, ownedNodeEdgePoint_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connection/(\w+)/_route/(\w+)/
class Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_RouteLocalid(MethodView):

    def get(self, uuid, connection_uuid, localId):
        print "Retrieve operation of resource: _route"
        try:
            response = Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_RouteLocalidImpl.get(uuid, connection_uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_transferTiming/queuingLatency/(\w+)/
class Context_TopologyUuid_NodeNode_Uuid_TransfertimingQueuinglatencyLatencyvalue(MethodView):

    def get(self, uuid, node_uuid, latencyValue):
        print "Retrieve operation of resource: queuingLatency"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_TransfertimingQueuinglatencyLatencyvalueImpl.get(uuid, node_uuid, latencyValue)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_riskParameter/riskCharacteristic/
class Context_TopologyUuid_LinkLink_Uuid_RiskparameterRiskcharacteristic(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: riskCharacteristic"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_RiskparameterRiskcharacteristicImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_transferTiming/queuingLatency/
class Context_TopologyUuid_NodeNode_Uuid_TransfertimingQueuinglatency(MethodView):

    def get(self, uuid, node_uuid):
        print "Retrieve operation of resource: queuingLatency"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_TransfertimingQueuinglatencyImpl.get(uuid, node_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/(\w+)/name/(\w+)/
class Context_VnwserviceUuidNameValuename(MethodView):

    def put(self, uuid, valueName):
        print "Update operation of resource: name"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_VnwserviceUuidNameValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            if inst.args[0] != 'valueName':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(NameAndValue, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_VnwserviceUuidNameValuenameImpl.put(uuid, valueName, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    Context_VnwserviceUuidNameValuenameImpl.put(uuid, valueName, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid, valueName):
        print "Create operation of resource: name"
        try:
            response = Context_VnwserviceUuidNameValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            if inst.args[0] != 'valueName':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(NameAndValue, json_struct, (valueName,'valueName'))
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_VnwserviceUuidNameValuenameImpl.post(uuid, valueName, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid, valueName):
        print "Delete operation of resource: name"
        try:
            response=Context_VnwserviceUuidNameValuenameImpl.delete(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid, valueName):
        print "Retrieve operation of resource: name"
        try:
            response = Context_VnwserviceUuidNameValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/
class Context(MethodView):

    def put(self, ):
        print "Update operation of resource: Context"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = ContextImpl.get()
        except KeyError as inst:
            if inst.args[0] != '':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(ContextSchema, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    ContextImpl.put(new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    ContextImpl.put(existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, ):
        print "Create operation of resource: Context"
        try:
            response = ContextImpl.get()
        except KeyError as inst:
            if inst.args[0] != '':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(ContextSchema, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    ContextImpl.post(new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, ):
        print "Delete operation of resource: Context"
        try:
            response=ContextImpl.delete()
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, ):
        print "Retrieve operation of resource: Context"
        try:
            response = ContextImpl.get()
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/
class Context_TopologyUuid_Node(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _node"
        try:
            response = Context_TopologyUuid_NodeImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/label/
class ContextLabel(MethodView):

    def get(self, ):
        print "Retrieve operation of resource: label"
        try:
            response = ContextLabelImpl.get()
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_transferTiming/queuingLatency/(\w+)/
class Context_TopologyUuid_LinkLink_Uuid_TransfertimingQueuinglatencyLatencyvalue(MethodView):

    def get(self, uuid, link_uuid, latencyValue):
        print "Retrieve operation of resource: queuingLatency"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_TransfertimingQueuinglatencyLatencyvalueImpl.get(uuid, link_uuid, latencyValue)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_transferCapacity/capacityAssignedToUserView/(\w+)/
class Context_TopologyUuid_NodeNode_Uuid_TransfercapacityCapacityassignedtouserviewNumberingrange(MethodView):

    def get(self, uuid, node_uuid, numberingRange):
        print "Retrieve operation of resource: capacityAssignedToUserView"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_TransfercapacityCapacityassignedtouserviewNumberingrangeImpl.get(uuid, node_uuid, numberingRange)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/
class Context_Pathcompservice(MethodView):

    def get(self, ):
        print "Retrieve operation of resource: _pathCompService"
        try:
            response = Context_PathcompserviceImpl.get()
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_ownedNodeEdgePoint/(\w+)/_ltpSpecData/
class Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_Ltpspecdata(MethodView):

    def get(self, uuid, node_uuid, ownedNodeEdgePoint_uuid):
        print "Retrieve operation of resource: _ltpSpecData"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LtpspecdataImpl.get(uuid, node_uuid, ownedNodeEdgePoint_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/
class Context_TopologyUuid_NodeNode_Uuid(MethodView):

    def get(self, uuid, node_uuid):
        print "Retrieve operation of resource: _node"
        try:
            response = Context_TopologyUuid_NodeNode_UuidImpl.get(uuid, node_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_path/(\w+)/_routingConstraint/riskCharacteristic/
class Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintRiskcharacteristic(MethodView):

    def get(self, uuid, path_uuid):
        print "Retrieve operation of resource: riskCharacteristic"
        try:
            response = Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintRiskcharacteristicImpl.get(uuid, path_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notifSubscription/(\w+)/name/(\w+)/
class Context_NotifsubscriptionUuidNameValuename(MethodView):

    def put(self, uuid, valueName):
        print "Update operation of resource: name"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_NotifsubscriptionUuidNameValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            if inst.args[0] != 'valueName':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(NameAndValue, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_NotifsubscriptionUuidNameValuenameImpl.put(uuid, valueName, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    Context_NotifsubscriptionUuidNameValuenameImpl.put(uuid, valueName, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid, valueName):
        print "Create operation of resource: name"
        try:
            response = Context_NotifsubscriptionUuidNameValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            if inst.args[0] != 'valueName':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(NameAndValue, json_struct, (valueName,'valueName'))
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_NotifsubscriptionUuidNameValuenameImpl.post(uuid, valueName, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid, valueName):
        print "Delete operation of resource: name"
        try:
            response=Context_NotifsubscriptionUuidNameValuenameImpl.delete(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid, valueName):
        print "Retrieve operation of resource: name"
        try:
            response = Context_NotifsubscriptionUuidNameValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/(\w+)/_vnwConstraint/latencyCharacteristic/(\w+)/
class Context_VnwserviceUuid_VnwconstraintLatencycharacteristicLatencyvalue(MethodView):

    def put(self, uuid, latencyValue):
        print "Update operation of resource: latencyCharacteristic"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_VnwserviceUuid_VnwconstraintLatencycharacteristicLatencyvalueImpl.get(uuid, latencyValue)
        except KeyError as inst:
            if inst.args[0] != 'latencyValue':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(QueuingLatency, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_VnwserviceUuid_VnwconstraintLatencycharacteristicLatencyvalueImpl.put(uuid, latencyValue, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    Context_VnwserviceUuid_VnwconstraintLatencycharacteristicLatencyvalueImpl.put(uuid, latencyValue, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid, latencyValue):
        print "Create operation of resource: latencyCharacteristic"
        try:
            response = Context_VnwserviceUuid_VnwconstraintLatencycharacteristicLatencyvalueImpl.get(uuid, latencyValue)
        except KeyError as inst:
            if inst.args[0] != 'latencyValue':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(QueuingLatency, json_struct, (latencyValue,'latencyValue'))
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_VnwserviceUuid_VnwconstraintLatencycharacteristicLatencyvalueImpl.post(uuid, latencyValue, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid, latencyValue):
        print "Delete operation of resource: latencyCharacteristic"
        try:
            response=Context_VnwserviceUuid_VnwconstraintLatencycharacteristicLatencyvalueImpl.delete(uuid, latencyValue)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid, latencyValue):
        print "Retrieve operation of resource: latencyCharacteristic"
        try:
            response = Context_VnwserviceUuid_VnwconstraintLatencycharacteristicLatencyvalueImpl.get(uuid, latencyValue)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_ownedNodeEdgePoint/(\w+)/_layerProtocol/(\w+)/_lpSpecData/
class Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalid_Lpspecdata(MethodView):

    def get(self, uuid, node_uuid, ownedNodeEdgePoint_uuid, localId):
        print "Retrieve operation of resource: _lpSpecData"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalid_LpspecdataImpl.get(uuid, node_uuid, ownedNodeEdgePoint_uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/name/(\w+)/
class Context_TopologyUuidNameValuename(MethodView):

    def get(self, uuid, valueName):
        print "Retrieve operation of resource: name"
        try:
            response = Context_TopologyUuidNameValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_routingConstraint/latencyCharacteristic/
class Context_PathcompserviceUuid_RoutingconstraintLatencycharacteristic(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: latencyCharacteristic"
        try:
            response = Context_PathcompserviceUuid_RoutingconstraintLatencycharacteristicImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notification/(\w+)/changedAttributes/
class Context_NotificationNotificationidChangedattributes(MethodView):

    def get(self, notificationId):
        print "Retrieve operation of resource: changedAttributes"
        try:
            response = Context_NotificationNotificationidChangedattributesImpl.get(notificationId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_serviceEndPoint/(\w+)/_connectionEndPoint/(\w+)/_state/
class Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_State(MethodView):

    def get(self, uuid, connectionEndPoint_uuid):
        print "Retrieve operation of resource: _state"
        try:
            response = Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_StateImpl.get(uuid, connectionEndPoint_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/(\w+)/_vnwConstraint/
class Context_VnwserviceUuid_Vnwconstraint(MethodView):

    def put(self, uuid):
        print "Update operation of resource: _vnwConstraint"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_VnwserviceUuid_VnwconstraintImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(VirtualNetworkConstraint, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_VnwserviceUuid_VnwconstraintImpl.put(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    Context_VnwserviceUuid_VnwconstraintImpl.put(uuid, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid):
        print "Create operation of resource: _vnwConstraint"
        try:
            response = Context_VnwserviceUuid_VnwconstraintImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(VirtualNetworkConstraint, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_VnwserviceUuid_VnwconstraintImpl.post(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid):
        print "Delete operation of resource: _vnwConstraint"
        try:
            response=Context_VnwserviceUuid_VnwconstraintImpl.delete(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid):
        print "Retrieve operation of resource: _vnwConstraint"
        try:
            response = Context_VnwserviceUuid_VnwconstraintImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_routingConstraint/requestedCapacity/
class Context_PathcompserviceUuid_RoutingconstraintRequestedcapacity(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: requestedCapacity"
        try:
            response = Context_PathcompserviceUuid_RoutingconstraintRequestedcapacityImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_path/(\w+)/name/
class Context_PathcompserviceUuid_PathPath_UuidName(MethodView):

    def get(self, uuid, path_uuid):
        print "Retrieve operation of resource: name"
        try:
            response = Context_PathcompserviceUuid_PathPath_UuidNameImpl.get(uuid, path_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connConstraints/requestedCapacity/
class Context_ConnectivityserviceUuid_ConnconstraintsRequestedcapacity(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: requestedCapacity"
        try:
            response = Context_ConnectivityserviceUuid_ConnconstraintsRequestedcapacityImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connConstraints/latencyCharacteristic/(\w+)/
class Context_ConnectivityserviceUuid_ConnconstraintsLatencycharacteristicLatencyvalue(MethodView):

    def get(self, uuid, latencyValue):
        print "Retrieve operation of resource: latencyCharacteristic"
        try:
            response = Context_ConnectivityserviceUuid_ConnconstraintsLatencycharacteristicLatencyvalueImpl.get(uuid, latencyValue)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_transferCost/
class Context_TopologyUuid_LinkLink_Uuid_Transfercost(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: _transferCost"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_TransfercostImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_routingConstraint/latencyCharacteristic/(\w+)/
class Context_PathcompserviceUuid_RoutingconstraintLatencycharacteristicLatencyvalue(MethodView):

    def get(self, uuid, latencyValue):
        print "Retrieve operation of resource: latencyCharacteristic"
        try:
            response = Context_PathcompserviceUuid_RoutingconstraintLatencycharacteristicLatencyvalueImpl.get(uuid, latencyValue)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_ownedNodeEdgePoint/(\w+)/name/
class Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidName(MethodView):

    def get(self, uuid, node_uuid, ownedNodeEdgePoint_uuid):
        print "Retrieve operation of resource: name"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidNameImpl.get(uuid, node_uuid, ownedNodeEdgePoint_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notifSubscription/(\w+)/name/
class Context_NotifsubscriptionUuidName(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: name"
        try:
            response = Context_NotifsubscriptionUuidNameImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_servicePort/
class Context_ConnectivityserviceUuid_Serviceport(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _servicePort"
        try:
            response = Context_ConnectivityserviceUuid_ServiceportImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notifSubscription/(\w+)/_notification/
class Context_NotifsubscriptionUuid_Notification(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _notification"
        try:
            response = Context_NotifsubscriptionUuid_NotificationImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/label/(\w+)/
class Context_TopologyUuid_LinkLink_UuidLabelValuename(MethodView):

    def get(self, uuid, link_uuid, valueName):
        print "Retrieve operation of resource: label"
        try:
            response = Context_TopologyUuid_LinkLink_UuidLabelValuenameImpl.get(uuid, link_uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_routingConstraint/costCharacteristic/
class Context_PathcompserviceUuid_RoutingconstraintCostcharacteristic(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: costCharacteristic"
        try:
            response = Context_PathcompserviceUuid_RoutingconstraintCostcharacteristicImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/label/
class Context_TopologyUuid_NodeNode_UuidLabel(MethodView):

    def get(self, uuid, node_uuid):
        print "Retrieve operation of resource: label"
        try:
            response = Context_TopologyUuid_NodeNode_UuidLabelImpl.get(uuid, node_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/(\w+)/_servicePort/(\w+)/
class Context_VnwserviceUuid_ServiceportLocalid(MethodView):

    def put(self, uuid, localId):
        print "Update operation of resource: _servicePort"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_VnwserviceUuid_ServiceportLocalidImpl.get(uuid, localId)
        except KeyError as inst:
            if inst.args[0] != 'localId':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(VirtualNetworkServicePort, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_VnwserviceUuid_ServiceportLocalidImpl.put(uuid, localId, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    Context_VnwserviceUuid_ServiceportLocalidImpl.put(uuid, localId, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid, localId):
        print "Create operation of resource: _servicePort"
        try:
            response = Context_VnwserviceUuid_ServiceportLocalidImpl.get(uuid, localId)
        except KeyError as inst:
            if inst.args[0] != 'localId':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(VirtualNetworkServicePort, json_struct, (localId,'localId'))
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_VnwserviceUuid_ServiceportLocalidImpl.post(uuid, localId, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid, localId):
        print "Delete operation of resource: _servicePort"
        try:
            response=Context_VnwserviceUuid_ServiceportLocalidImpl.delete(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid, localId):
        print "Retrieve operation of resource: _servicePort"
        try:
            response = Context_VnwserviceUuid_ServiceportLocalidImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_lpTransition/
class Context_TopologyUuid_LinkLink_Uuid_Lptransition(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: _lpTransition"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_LptransitionImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_validation/validationMechanism/
class Context_TopologyUuid_LinkLink_Uuid_ValidationValidationmechanism(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: validationMechanism"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_ValidationValidationmechanismImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_path/(\w+)/_routingConstraint/latencyCharacteristic/
class Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintLatencycharacteristic(MethodView):

    def get(self, uuid, path_uuid):
        print "Retrieve operation of resource: latencyCharacteristic"
        try:
            response = Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintLatencycharacteristicImpl.get(uuid, path_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/label/(\w+)/
class Context_PathcompserviceUuidLabelValuename(MethodView):

    def put(self, uuid, valueName):
        print "Update operation of resource: label"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_PathcompserviceUuidLabelValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            if inst.args[0] != 'valueName':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(NameAndValue, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_PathcompserviceUuidLabelValuenameImpl.put(uuid, valueName, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    Context_PathcompserviceUuidLabelValuenameImpl.put(uuid, valueName, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid, valueName):
        print "Create operation of resource: label"
        try:
            response = Context_PathcompserviceUuidLabelValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            if inst.args[0] != 'valueName':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(NameAndValue, json_struct, (valueName,'valueName'))
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_PathcompserviceUuidLabelValuenameImpl.post(uuid, valueName, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid, valueName):
        print "Delete operation of resource: label"
        try:
            response=Context_PathcompserviceUuidLabelValuenameImpl.delete(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid, valueName):
        print "Retrieve operation of resource: label"
        try:
            response = Context_PathcompserviceUuidLabelValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_path/
class Context_PathcompserviceUuid_Path(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _path"
        try:
            response = Context_PathcompserviceUuid_PathImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_path/(\w+)/label/
class Context_PathcompserviceUuid_PathPath_UuidLabel(MethodView):

    def get(self, uuid, path_uuid):
        print "Retrieve operation of resource: label"
        try:
            response = Context_PathcompserviceUuid_PathPath_UuidLabelImpl.get(uuid, path_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_routingConstraint/
class Context_PathcompserviceUuid_Routingconstraint(MethodView):

    def put(self, uuid):
        print "Update operation of resource: _routingConstraint"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_PathcompserviceUuid_RoutingconstraintImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(ConnectivityConstraint, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_PathcompserviceUuid_RoutingconstraintImpl.put(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    Context_PathcompserviceUuid_RoutingconstraintImpl.put(uuid, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid):
        print "Create operation of resource: _routingConstraint"
        try:
            response = Context_PathcompserviceUuid_RoutingconstraintImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(ConnectivityConstraint, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_PathcompserviceUuid_RoutingconstraintImpl.post(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid):
        print "Delete operation of resource: _routingConstraint"
        try:
            response=Context_PathcompserviceUuid_RoutingconstraintImpl.delete(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid):
        print "Retrieve operation of resource: _routingConstraint"
        try:
            response = Context_PathcompserviceUuid_RoutingconstraintImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/name/
class Context_TopologyUuidName(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: name"
        try:
            response = Context_TopologyUuidNameImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_serviceEndPoint/(\w+)/_connectionEndPoint/(\w+)/_layerProtocol/(\w+)/_lpSpecData/
class Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_LayerprotocolLocalid_Lpspecdata(MethodView):

    def get(self, uuid, connectionEndPoint_uuid, localId):
        print "Retrieve operation of resource: _lpSpecData"
        try:
            response = Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_LayerprotocolLocalid_LpspecdataImpl.get(uuid, connectionEndPoint_uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_routingConstraint/riskCharacteristic/(\w+)/
class Context_PathcompserviceUuid_RoutingconstraintRiskcharacteristicRiskcharacteristicname(MethodView):

    def get(self, uuid, riskCharacteristicName):
        print "Retrieve operation of resource: riskCharacteristic"
        try:
            response = Context_PathcompserviceUuid_RoutingconstraintRiskcharacteristicRiskcharacteristicnameImpl.get(uuid, riskCharacteristicName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/name/
class Context_ConnectivityserviceUuidName(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: name"
        try:
            response = Context_ConnectivityserviceUuidNameImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_linkPort/(\w+)/
class Context_TopologyUuid_LinkLink_Uuid_LinkportLocalid(MethodView):

    def get(self, uuid, link_uuid, localId):
        print "Retrieve operation of resource: _linkPort"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_LinkportLocalidImpl.get(uuid, link_uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/(\w+)/name/
class Context_VnwserviceUuidName(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: name"
        try:
            response = Context_VnwserviceUuidNameImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_serviceEndPoint/(\w+)/_connectionEndPoint/(\w+)/name/(\w+)/
class Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidNameValuename(MethodView):

    def get(self, uuid, connectionEndPoint_uuid, valueName):
        print "Retrieve operation of resource: name"
        try:
            response = Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidNameValuenameImpl.get(uuid, connectionEndPoint_uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_ownedNodeEdgePoint/(\w+)/name/(\w+)/
class Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidNameValuename(MethodView):

    def get(self, uuid, node_uuid, ownedNodeEdgePoint_uuid, valueName):
        print "Retrieve operation of resource: name"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidNameValuenameImpl.get(uuid, node_uuid, ownedNodeEdgePoint_uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_servicePort/(\w+)/
class Context_PathcompserviceUuid_ServiceportLocalid(MethodView):

    def put(self, uuid, localId):
        print "Update operation of resource: _servicePort"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_PathcompserviceUuid_ServiceportLocalidImpl.get(uuid, localId)
        except KeyError as inst:
            if inst.args[0] != 'localId':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(PathCompServicePort, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_PathcompserviceUuid_ServiceportLocalidImpl.put(uuid, localId, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    Context_PathcompserviceUuid_ServiceportLocalidImpl.put(uuid, localId, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid, localId):
        print "Create operation of resource: _servicePort"
        try:
            response = Context_PathcompserviceUuid_ServiceportLocalidImpl.get(uuid, localId)
        except KeyError as inst:
            if inst.args[0] != 'localId':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(PathCompServicePort, json_struct, (localId,'localId'))
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_PathcompserviceUuid_ServiceportLocalidImpl.post(uuid, localId, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid, localId):
        print "Delete operation of resource: _servicePort"
        try:
            response=Context_PathcompserviceUuid_ServiceportLocalidImpl.delete(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid, localId):
        print "Retrieve operation of resource: _servicePort"
        try:
            response = Context_PathcompserviceUuid_ServiceportLocalidImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_serviceEndPoint/
class Context_Serviceendpoint(MethodView):

    def get(self, ):
        print "Retrieve operation of resource: _serviceEndPoint"
        try:
            response = Context_ServiceendpointImpl.get()
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_serviceEndPoint/(\w+)/name/
class Context_ServiceendpointUuidName(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: name"
        try:
            response = Context_ServiceendpointUuidNameImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/name/
class ContextName(MethodView):

    def get(self, ):
        print "Retrieve operation of resource: name"
        try:
            response = ContextNameImpl.get()
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/(\w+)/_vnwConstraint/costCharacteristic/
class Context_VnwserviceUuid_VnwconstraintCostcharacteristic(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: costCharacteristic"
        try:
            response = Context_VnwserviceUuid_VnwconstraintCostcharacteristicImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_objectiveFunction/
class Context_PathcompserviceUuid_Objectivefunction(MethodView):

    def put(self, uuid):
        print "Update operation of resource: _objectiveFunction"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_PathcompserviceUuid_ObjectivefunctionImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(PathObjectiveFunction, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_PathcompserviceUuid_ObjectivefunctionImpl.put(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    Context_PathcompserviceUuid_ObjectivefunctionImpl.put(uuid, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid):
        print "Create operation of resource: _objectiveFunction"
        try:
            response = Context_PathcompserviceUuid_ObjectivefunctionImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(PathObjectiveFunction, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_PathcompserviceUuid_ObjectivefunctionImpl.post(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid):
        print "Delete operation of resource: _objectiveFunction"
        try:
            response=Context_PathcompserviceUuid_ObjectivefunctionImpl.delete(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid):
        print "Retrieve operation of resource: _objectiveFunction"
        try:
            response = Context_PathcompserviceUuid_ObjectivefunctionImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_riskParameter/riskCharacteristic/(\w+)/
class Context_TopologyUuid_LinkLink_Uuid_RiskparameterRiskcharacteristicRiskcharacteristicname(MethodView):

    def get(self, uuid, link_uuid, riskCharacteristicName):
        print "Retrieve operation of resource: riskCharacteristic"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_RiskparameterRiskcharacteristicRiskcharacteristicnameImpl.get(uuid, link_uuid, riskCharacteristicName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_serviceEndPoint/(\w+)/_connectionEndPoint/(\w+)/_layerProtocol/(\w+)/
class Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_LayerprotocolLocalid(MethodView):

    def get(self, uuid, connectionEndPoint_uuid, localId):
        print "Retrieve operation of resource: _layerProtocol"
        try:
            response = Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_LayerprotocolLocalidImpl.get(uuid, connectionEndPoint_uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notifSubscription/
class Context_Notifsubscription(MethodView):

    def get(self, ):
        print "Retrieve operation of resource: _notifSubscription"
        try:
            response = Context_NotifsubscriptionImpl.get()
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_serviceEndPoint/(\w+)/_layerProtocol/(\w+)/
class Context_ServiceendpointUuid_LayerprotocolLocalid(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _layerProtocol"
        try:
            response = Context_ServiceendpointUuid_LayerprotocolLocalidImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_transferCost/costCharacteristic/(\w+)/
class Context_TopologyUuid_LinkLink_Uuid_TransfercostCostcharacteristicCostalgorithm(MethodView):

    def get(self, uuid, link_uuid, costAlgorithm):
        print "Retrieve operation of resource: costCharacteristic"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_TransfercostCostcharacteristicCostalgorithmImpl.get(uuid, link_uuid, costAlgorithm)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_ownedNodeEdgePoint/(\w+)/label/(\w+)/
class Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidLabelValuename(MethodView):

    def get(self, uuid, node_uuid, ownedNodeEdgePoint_uuid, valueName):
        print "Retrieve operation of resource: label"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidLabelValuenameImpl.get(uuid, node_uuid, ownedNodeEdgePoint_uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_servicePort/(\w+)/
class Context_ConnectivityserviceUuid_ServiceportLocalid(MethodView):

    def put(self, uuid, localId):
        print "Update operation of resource: _servicePort"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_ConnectivityserviceUuid_ServiceportLocalidImpl.get(uuid, localId)
        except KeyError as inst:
            if inst.args[0] != 'localId':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(ConnectivityServicePort, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_ConnectivityserviceUuid_ServiceportLocalidImpl.put(uuid, localId, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    Context_ConnectivityserviceUuid_ServiceportLocalidImpl.put(uuid, localId, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid, localId):
        print "Create operation of resource: _servicePort"
        try:
            response = Context_ConnectivityserviceUuid_ServiceportLocalidImpl.get(uuid, localId)
        except KeyError as inst:
            if inst.args[0] != 'localId':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(ConnectivityServicePort, json_struct, (localId,'localId'))
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_ConnectivityserviceUuid_ServiceportLocalidImpl.post(uuid, localId, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid, localId):
        print "Delete operation of resource: _servicePort"
        try:
            response=Context_ConnectivityserviceUuid_ServiceportLocalidImpl.delete(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid, localId):
        print "Retrieve operation of resource: _servicePort"
        try:
            response = Context_ConnectivityserviceUuid_ServiceportLocalidImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_transferTiming/queuingLatency/
class Context_TopologyUuid_LinkLink_Uuid_TransfertimingQueuinglatency(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: queuingLatency"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_TransfertimingQueuinglatencyImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/
class Context_ConnectivityserviceUuid(MethodView):

    def put(self, uuid):
        print "Update operation of resource: _connectivityService"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_ConnectivityserviceUuidImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(ConnectivityService, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_ConnectivityserviceUuidImpl.put(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    Context_ConnectivityserviceUuidImpl.put(uuid, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid):
        print "Create operation of resource: _connectivityService"
        try:
            response = Context_ConnectivityserviceUuidImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(ConnectivityService, json_struct, (uuid,'uuid'))
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_ConnectivityserviceUuidImpl.post(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid):
        print "Delete operation of resource: _connectivityService"
        try:
            response=Context_ConnectivityserviceUuidImpl.delete(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid):
        print "Retrieve operation of resource: _connectivityService"
        try:
            response = Context_ConnectivityserviceUuidImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/
class Context_TopologyUuid(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _topology"
        try:
            response = Context_TopologyUuidImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connection/(\w+)/
class Context_ConnectivityserviceUuid_ConnectionConnection_Uuid(MethodView):

    def get(self, uuid, connection_uuid):
        print "Retrieve operation of resource: _connection"
        try:
            response = Context_ConnectivityserviceUuid_ConnectionConnection_UuidImpl.get(uuid, connection_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/
class Context_Connectivityservice(MethodView):

    def get(self, ):
        print "Retrieve operation of resource: _connectivityService"
        try:
            response = Context_ConnectivityserviceImpl.get()
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_validation/
class Context_TopologyUuid_LinkLink_Uuid_Validation(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: _validation"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_ValidationImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_transferCapacity/totalPotentialCapacity/
class Context_TopologyUuid_LinkLink_Uuid_TransfercapacityTotalpotentialcapacity(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: totalPotentialCapacity"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_TransfercapacityTotalpotentialcapacityImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_ownedNodeEdgePoint/
class Context_TopologyUuid_NodeNode_Uuid_Ownednodeedgepoint(MethodView):

    def get(self, uuid, node_uuid):
        print "Retrieve operation of resource: _ownedNodeEdgePoint"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointImpl.get(uuid, node_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/
class Context_Topology(MethodView):

    def get(self, ):
        print "Retrieve operation of resource: _topology"
        try:
            response = Context_TopologyImpl.get()
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connection/
class Context_ConnectivityserviceUuid_Connection(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _connection"
        try:
            response = Context_ConnectivityserviceUuid_ConnectionImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connection/(\w+)/_route/
class Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_Route(MethodView):

    def get(self, uuid, connection_uuid):
        print "Retrieve operation of resource: _route"
        try:
            response = Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_RouteImpl.get(uuid, connection_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/label/(\w+)/
class Context_TopologyUuid_NodeNode_UuidLabelValuename(MethodView):

    def get(self, uuid, node_uuid, valueName):
        print "Retrieve operation of resource: label"
        try:
            response = Context_TopologyUuid_NodeNode_UuidLabelValuenameImpl.get(uuid, node_uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connection/(\w+)/_state/
class Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_State(MethodView):

    def get(self, uuid, connection_uuid):
        print "Retrieve operation of resource: _state"
        try:
            response = Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_StateImpl.get(uuid, connection_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connConstraints/riskCharacteristic/
class Context_ConnectivityserviceUuid_ConnconstraintsRiskcharacteristic(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: riskCharacteristic"
        try:
            response = Context_ConnectivityserviceUuid_ConnconstraintsRiskcharacteristicImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notifSubscription/(\w+)/_notification/(\w+)/additionalInfo/(\w+)/
class Context_NotifsubscriptionUuid_NotificationNotificationidAdditionalinfoValuename(MethodView):

    def get(self, uuid, notificationId, valueName):
        print "Retrieve operation of resource: additionalInfo"
        try:
            response = Context_NotifsubscriptionUuid_NotificationNotificationidAdditionalinfoValuenameImpl.get(uuid, notificationId, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connection/(\w+)/_connectionPort/(\w+)/
class Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_ConnectionportLocalid(MethodView):

    def get(self, uuid, connection_uuid, localId):
        print "Retrieve operation of resource: _connectionPort"
        try:
            response = Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_ConnectionportLocalidImpl.get(uuid, connection_uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/(\w+)/
class Context_VnwserviceUuid(MethodView):

    def put(self, uuid):
        print "Update operation of resource: _vnwService"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_VnwserviceUuidImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(VirtualNetworkService, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_VnwserviceUuidImpl.put(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    Context_VnwserviceUuidImpl.put(uuid, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid):
        print "Create operation of resource: _vnwService"
        try:
            response = Context_VnwserviceUuidImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(VirtualNetworkService, json_struct, (uuid,'uuid'))
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_VnwserviceUuidImpl.post(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid):
        print "Delete operation of resource: _vnwService"
        try:
            response=Context_VnwserviceUuidImpl.delete(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid):
        print "Retrieve operation of resource: _vnwService"
        try:
            response = Context_VnwserviceUuidImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notifSubscription/(\w+)/_subscriptionFilter/
class Context_NotifsubscriptionUuid_Subscriptionfilter(MethodView):

    def put(self, uuid):
        print "Update operation of resource: _subscriptionFilter"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_NotifsubscriptionUuid_SubscriptionfilterImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(SubscriptionFilter, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_NotifsubscriptionUuid_SubscriptionfilterImpl.put(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    Context_NotifsubscriptionUuid_SubscriptionfilterImpl.put(uuid, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid):
        print "Create operation of resource: _subscriptionFilter"
        try:
            response = Context_NotifsubscriptionUuid_SubscriptionfilterImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(SubscriptionFilter, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_NotifsubscriptionUuid_SubscriptionfilterImpl.post(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid):
        print "Delete operation of resource: _subscriptionFilter"
        try:
            response=Context_NotifsubscriptionUuid_SubscriptionfilterImpl.delete(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid):
        print "Retrieve operation of resource: _subscriptionFilter"
        try:
            response = Context_NotifsubscriptionUuid_SubscriptionfilterImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connection/(\w+)/name/
class Context_ConnectivityserviceUuid_ConnectionConnection_UuidName(MethodView):

    def get(self, uuid, connection_uuid):
        print "Retrieve operation of resource: name"
        try:
            response = Context_ConnectivityserviceUuid_ConnectionConnection_UuidNameImpl.get(uuid, connection_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_path/(\w+)/_routingConstraint/costCharacteristic/(\w+)/
class Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintCostcharacteristicCostalgorithm(MethodView):

    def get(self, uuid, path_uuid, costAlgorithm):
        print "Retrieve operation of resource: costCharacteristic"
        try:
            response = Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintCostcharacteristicCostalgorithmImpl.get(uuid, path_uuid, costAlgorithm)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_routingConstraint/riskCharacteristic/
class Context_PathcompserviceUuid_RoutingconstraintRiskcharacteristic(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: riskCharacteristic"
        try:
            response = Context_PathcompserviceUuid_RoutingconstraintRiskcharacteristicImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_riskParameter/
class Context_TopologyUuid_LinkLink_Uuid_Riskparameter(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: _riskParameter"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_RiskparameterImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/label/
class Context_TopologyUuidLabel(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: label"
        try:
            response = Context_TopologyUuidLabelImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/
class Context_Vnwservice(MethodView):

    def get(self, ):
        print "Retrieve operation of resource: _vnwService"
        try:
            response = Context_VnwserviceImpl.get()
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_serviceEndPoint/(\w+)/_connectionEndPoint/(\w+)/
class Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid(MethodView):

    def get(self, uuid, connectionEndPoint_uuid):
        print "Retrieve operation of resource: _connectionEndPoint"
        try:
            response = Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidImpl.get(uuid, connectionEndPoint_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_serviceEndPoint/(\w+)/_layerProtocol/(\w+)/_lpSpecData/
class Context_ServiceendpointUuid_LayerprotocolLocalid_Lpspecdata(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _lpSpecData"
        try:
            response = Context_ServiceendpointUuid_LayerprotocolLocalid_LpspecdataImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notification/(\w+)/additionalInfo/(\w+)/
class Context_NotificationNotificationidAdditionalinfoValuename(MethodView):

    def get(self, notificationId, valueName):
        print "Retrieve operation of resource: additionalInfo"
        try:
            response = Context_NotificationNotificationidAdditionalinfoValuenameImpl.get(notificationId, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/(\w+)/label/
class Context_VnwserviceUuidLabel(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: label"
        try:
            response = Context_VnwserviceUuidLabelImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_path/(\w+)/_routingConstraint/riskCharacteristic/(\w+)/
class Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintRiskcharacteristicRiskcharacteristicname(MethodView):

    def get(self, uuid, path_uuid, riskCharacteristicName):
        print "Retrieve operation of resource: riskCharacteristic"
        try:
            response = Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintRiskcharacteristicRiskcharacteristicnameImpl.get(uuid, path_uuid, riskCharacteristicName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_transferCapacity/capacityAssignedToUserView/
class Context_TopologyUuid_LinkLink_Uuid_TransfercapacityCapacityassignedtouserview(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: capacityAssignedToUserView"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_TransfercapacityCapacityassignedtouserviewImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/(\w+)/_vnwConstraint/latencyCharacteristic/
class Context_VnwserviceUuid_VnwconstraintLatencycharacteristic(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: latencyCharacteristic"
        try:
            response = Context_VnwserviceUuid_VnwconstraintLatencycharacteristicImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/(\w+)/_vnwConstraint/requestedCapacity/
class Context_VnwserviceUuid_VnwconstraintRequestedcapacity(MethodView):

    def put(self, uuid):
        print "Update operation of resource: requestedCapacity"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_VnwserviceUuid_VnwconstraintRequestedcapacityImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(Capacity, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_VnwserviceUuid_VnwconstraintRequestedcapacityImpl.put(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    Context_VnwserviceUuid_VnwconstraintRequestedcapacityImpl.put(uuid, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid):
        print "Create operation of resource: requestedCapacity"
        try:
            response = Context_VnwserviceUuid_VnwconstraintRequestedcapacityImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(Capacity, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_VnwserviceUuid_VnwconstraintRequestedcapacityImpl.post(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid):
        print "Delete operation of resource: requestedCapacity"
        try:
            response=Context_VnwserviceUuid_VnwconstraintRequestedcapacityImpl.delete(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid):
        print "Retrieve operation of resource: requestedCapacity"
        try:
            response = Context_VnwserviceUuid_VnwconstraintRequestedcapacityImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connConstraints/costCharacteristic/(\w+)/
class Context_ConnectivityserviceUuid_ConnconstraintsCostcharacteristicCostalgorithm(MethodView):

    def get(self, uuid, costAlgorithm):
        print "Retrieve operation of resource: costCharacteristic"
        try:
            response = Context_ConnectivityserviceUuid_ConnconstraintsCostcharacteristicCostalgorithmImpl.get(uuid, costAlgorithm)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_transferCost/costCharacteristic/
class Context_TopologyUuid_NodeNode_Uuid_TransfercostCostcharacteristic(MethodView):

    def get(self, uuid, node_uuid):
        print "Retrieve operation of resource: costCharacteristic"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_TransfercostCostcharacteristicImpl.get(uuid, node_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_ownedNodeEdgePoint/(\w+)/
class Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid(MethodView):

    def get(self, uuid, node_uuid, ownedNodeEdgePoint_uuid):
        print "Retrieve operation of resource: _ownedNodeEdgePoint"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidImpl.get(uuid, node_uuid, ownedNodeEdgePoint_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_path/(\w+)/name/(\w+)/
class Context_PathcompserviceUuid_PathPath_UuidNameValuename(MethodView):

    def get(self, uuid, path_uuid, valueName):
        print "Retrieve operation of resource: name"
        try:
            response = Context_PathcompserviceUuid_PathPath_UuidNameValuenameImpl.get(uuid, path_uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/
class Context_TopologyUuid_Link(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _link"
        try:
            response = Context_TopologyUuid_LinkImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/name/(\w+)/
class Context_ConnectivityserviceUuidNameValuename(MethodView):

    def put(self, uuid, valueName):
        print "Update operation of resource: name"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_ConnectivityserviceUuidNameValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            if inst.args[0] != 'valueName':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(NameAndValue, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_ConnectivityserviceUuidNameValuenameImpl.put(uuid, valueName, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    Context_ConnectivityserviceUuidNameValuenameImpl.put(uuid, valueName, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid, valueName):
        print "Create operation of resource: name"
        try:
            response = Context_ConnectivityserviceUuidNameValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            if inst.args[0] != 'valueName':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(NameAndValue, json_struct, (valueName,'valueName'))
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_ConnectivityserviceUuidNameValuenameImpl.post(uuid, valueName, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid, valueName):
        print "Delete operation of resource: name"
        try:
            response=Context_ConnectivityserviceUuidNameValuenameImpl.delete(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid, valueName):
        print "Retrieve operation of resource: name"
        try:
            response = Context_ConnectivityserviceUuidNameValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_transferCapacity/capacityAssignedToUserView/(\w+)/
class Context_TopologyUuid_LinkLink_Uuid_TransfercapacityCapacityassignedtouserviewNumberingrange(MethodView):

    def get(self, uuid, link_uuid, numberingRange):
        print "Retrieve operation of resource: capacityAssignedToUserView"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_TransfercapacityCapacityassignedtouserviewNumberingrangeImpl.get(uuid, link_uuid, numberingRange)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_optimizationConstraint/
class Context_PathcompserviceUuid_Optimizationconstraint(MethodView):

    def put(self, uuid):
        print "Update operation of resource: _optimizationConstraint"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_PathcompserviceUuid_OptimizationconstraintImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(PathOptimizationConstraint, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_PathcompserviceUuid_OptimizationconstraintImpl.put(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    Context_PathcompserviceUuid_OptimizationconstraintImpl.put(uuid, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid):
        print "Create operation of resource: _optimizationConstraint"
        try:
            response = Context_PathcompserviceUuid_OptimizationconstraintImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(PathOptimizationConstraint, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_PathcompserviceUuid_OptimizationconstraintImpl.post(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid):
        print "Delete operation of resource: _optimizationConstraint"
        try:
            response=Context_PathcompserviceUuid_OptimizationconstraintImpl.delete(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid):
        print "Retrieve operation of resource: _optimizationConstraint"
        try:
            response = Context_PathcompserviceUuid_OptimizationconstraintImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notifSubscription/(\w+)/_notification/(\w+)/
class Context_NotifsubscriptionUuid_NotificationNotificationid(MethodView):

    def get(self, uuid, notificationId):
        print "Retrieve operation of resource: _notification"
        try:
            response = Context_NotifsubscriptionUuid_NotificationNotificationidImpl.get(uuid, notificationId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_linkPort/
class Context_TopologyUuid_LinkLink_Uuid_Linkport(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: _linkPort"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_LinkportImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/(\w+)/_servicePort/
class Context_VnwserviceUuid_Serviceport(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _servicePort"
        try:
            response = Context_VnwserviceUuid_ServiceportImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_ownedNodeEdgePoint/(\w+)/label/
class Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidLabel(MethodView):

    def get(self, uuid, node_uuid, ownedNodeEdgePoint_uuid):
        print "Retrieve operation of resource: label"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidLabelImpl.get(uuid, node_uuid, ownedNodeEdgePoint_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connection/(\w+)/_connectionPort/
class Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_Connectionport(MethodView):

    def get(self, uuid, connection_uuid):
        print "Retrieve operation of resource: _connectionPort"
        try:
            response = Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_ConnectionportImpl.get(uuid, connection_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_path/(\w+)/_routingConstraint/costCharacteristic/
class Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintCostcharacteristic(MethodView):

    def get(self, uuid, path_uuid):
        print "Retrieve operation of resource: costCharacteristic"
        try:
            response = Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintCostcharacteristicImpl.get(uuid, path_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connConstraints/riskCharacteristic/(\w+)/
class Context_ConnectivityserviceUuid_ConnconstraintsRiskcharacteristicRiskcharacteristicname(MethodView):

    def get(self, uuid, riskCharacteristicName):
        print "Retrieve operation of resource: riskCharacteristic"
        try:
            response = Context_ConnectivityserviceUuid_ConnconstraintsRiskcharacteristicRiskcharacteristicnameImpl.get(uuid, riskCharacteristicName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_transferCapacity/availableCapacity/
class Context_TopologyUuid_LinkLink_Uuid_TransfercapacityAvailablecapacity(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: availableCapacity"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_TransfercapacityAvailablecapacityImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_validation/validationMechanism/(\w+)/
class Context_TopologyUuid_LinkLink_Uuid_ValidationValidationmechanismValidationrobustness(MethodView):

    def get(self, uuid, link_uuid, validationRobustness):
        print "Retrieve operation of resource: validationMechanism"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_ValidationValidationmechanismValidationrobustnessImpl.get(uuid, link_uuid, validationRobustness)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connection/(\w+)/label/(\w+)/
class Context_ConnectivityserviceUuid_ConnectionConnection_UuidLabelValuename(MethodView):

    def get(self, uuid, connection_uuid, valueName):
        print "Retrieve operation of resource: label"
        try:
            response = Context_ConnectivityserviceUuid_ConnectionConnection_UuidLabelValuenameImpl.get(uuid, connection_uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_serviceEndPoint/(\w+)/_connectionEndPoint/(\w+)/label/
class Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidLabel(MethodView):

    def get(self, uuid, connectionEndPoint_uuid):
        print "Retrieve operation of resource: label"
        try:
            response = Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidLabelImpl.get(uuid, connectionEndPoint_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notifSubscription/(\w+)/label/
class Context_NotifsubscriptionUuidLabel(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: label"
        try:
            response = Context_NotifsubscriptionUuidLabelImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_routingConstraint/costCharacteristic/(\w+)/
class Context_PathcompserviceUuid_RoutingconstraintCostcharacteristicCostalgorithm(MethodView):

    def get(self, uuid, costAlgorithm):
        print "Retrieve operation of resource: costCharacteristic"
        try:
            response = Context_PathcompserviceUuid_RoutingconstraintCostcharacteristicCostalgorithmImpl.get(uuid, costAlgorithm)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_serviceEndPoint/(\w+)/_connectionEndPoint/(\w+)/name/
class Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidName(MethodView):

    def get(self, uuid, connectionEndPoint_uuid):
        print "Retrieve operation of resource: name"
        try:
            response = Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidNameImpl.get(uuid, connectionEndPoint_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/label/(\w+)/
class Context_TopologyUuidLabelValuename(MethodView):

    def get(self, uuid, valueName):
        print "Retrieve operation of resource: label"
        try:
            response = Context_TopologyUuidLabelValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_transferCapacity/
class Context_TopologyUuid_LinkLink_Uuid_Transfercapacity(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: _transferCapacity"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_TransfercapacityImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notifSubscription/(\w+)/_notification/(\w+)/targetObjectName/
class Context_NotifsubscriptionUuid_NotificationNotificationidTargetobjectname(MethodView):

    def get(self, uuid, notificationId):
        print "Retrieve operation of resource: targetObjectName"
        try:
            response = Context_NotifsubscriptionUuid_NotificationNotificationidTargetobjectnameImpl.get(uuid, notificationId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_transferCost/costCharacteristic/
class Context_TopologyUuid_LinkLink_Uuid_TransfercostCostcharacteristic(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: costCharacteristic"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_TransfercostCostcharacteristicImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/(\w+)/_vnwConstraint/riskCharacteristic/(\w+)/
class Context_VnwserviceUuid_VnwconstraintRiskcharacteristicRiskcharacteristicname(MethodView):

    def put(self, uuid, riskCharacteristicName):
        print "Update operation of resource: riskCharacteristic"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_VnwserviceUuid_VnwconstraintRiskcharacteristicRiskcharacteristicnameImpl.get(uuid, riskCharacteristicName)
        except KeyError as inst:
            if inst.args[0] != 'riskCharacteristicName':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(RiskCharacteristic, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_VnwserviceUuid_VnwconstraintRiskcharacteristicRiskcharacteristicnameImpl.put(uuid, riskCharacteristicName, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    Context_VnwserviceUuid_VnwconstraintRiskcharacteristicRiskcharacteristicnameImpl.put(uuid, riskCharacteristicName, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid, riskCharacteristicName):
        print "Create operation of resource: riskCharacteristic"
        try:
            response = Context_VnwserviceUuid_VnwconstraintRiskcharacteristicRiskcharacteristicnameImpl.get(uuid, riskCharacteristicName)
        except KeyError as inst:
            if inst.args[0] != 'riskCharacteristicName':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(RiskCharacteristic, json_struct, (riskCharacteristicName,'riskCharacteristicName'))
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_VnwserviceUuid_VnwconstraintRiskcharacteristicRiskcharacteristicnameImpl.post(uuid, riskCharacteristicName, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid, riskCharacteristicName):
        print "Delete operation of resource: riskCharacteristic"
        try:
            response=Context_VnwserviceUuid_VnwconstraintRiskcharacteristicRiskcharacteristicnameImpl.delete(uuid, riskCharacteristicName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid, riskCharacteristicName):
        print "Retrieve operation of resource: riskCharacteristic"
        try:
            response = Context_VnwserviceUuid_VnwconstraintRiskcharacteristicRiskcharacteristicnameImpl.get(uuid, riskCharacteristicName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_serviceEndPoint/(\w+)/label/
class Context_ServiceendpointUuidLabel(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: label"
        try:
            response = Context_ServiceendpointUuidLabelImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/name/
class Context_TopologyUuid_LinkLink_UuidName(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: name"
        try:
            response = Context_TopologyUuid_LinkLink_UuidNameImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_path/(\w+)/label/(\w+)/
class Context_PathcompserviceUuid_PathPath_UuidLabelValuename(MethodView):

    def get(self, uuid, path_uuid, valueName):
        print "Retrieve operation of resource: label"
        try:
            response = Context_PathcompserviceUuid_PathPath_UuidLabelValuenameImpl.get(uuid, path_uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notification/(\w+)/
class Context_NotificationNotificationid(MethodView):

    def get(self, notificationId):
        print "Retrieve operation of resource: _notification"
        try:
            response = Context_NotificationNotificationidImpl.get(notificationId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_path/(\w+)/_routingConstraint/requestedCapacity/
class Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintRequestedcapacity(MethodView):

    def get(self, uuid, path_uuid):
        print "Retrieve operation of resource: requestedCapacity"
        try:
            response = Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintRequestedcapacityImpl.get(uuid, path_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/(\w+)/_state/
class Context_VnwserviceUuid_State(MethodView):

    def put(self, uuid):
        print "Update operation of resource: _state"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_VnwserviceUuid_StateImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(AdminStatePac, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_VnwserviceUuid_StateImpl.put(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    Context_VnwserviceUuid_StateImpl.put(uuid, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid):
        print "Create operation of resource: _state"
        try:
            response = Context_VnwserviceUuid_StateImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(AdminStatePac, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_VnwserviceUuid_StateImpl.post(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid):
        print "Delete operation of resource: _state"
        try:
            response=Context_VnwserviceUuid_StateImpl.delete(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid):
        print "Retrieve operation of resource: _state"
        try:
            response = Context_VnwserviceUuid_StateImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_servicePort/
class Context_PathcompserviceUuid_Serviceport(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _servicePort"
        try:
            response = Context_PathcompserviceUuid_ServiceportImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_ownedNodeEdgePoint/(\w+)/_state/
class Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_State(MethodView):

    def get(self, uuid, node_uuid, ownedNodeEdgePoint_uuid):
        print "Retrieve operation of resource: _state"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_StateImpl.get(uuid, node_uuid, ownedNodeEdgePoint_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/label/(\w+)/
class Context_ConnectivityserviceUuidLabelValuename(MethodView):

    def put(self, uuid, valueName):
        print "Update operation of resource: label"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_ConnectivityserviceUuidLabelValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            if inst.args[0] != 'valueName':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(NameAndValue, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_ConnectivityserviceUuidLabelValuenameImpl.put(uuid, valueName, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    Context_ConnectivityserviceUuidLabelValuenameImpl.put(uuid, valueName, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid, valueName):
        print "Create operation of resource: label"
        try:
            response = Context_ConnectivityserviceUuidLabelValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            if inst.args[0] != 'valueName':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(NameAndValue, json_struct, (valueName,'valueName'))
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_ConnectivityserviceUuidLabelValuenameImpl.post(uuid, valueName, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid, valueName):
        print "Delete operation of resource: label"
        try:
            response=Context_ConnectivityserviceUuidLabelValuenameImpl.delete(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid, valueName):
        print "Retrieve operation of resource: label"
        try:
            response = Context_ConnectivityserviceUuidLabelValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_transferIntegrity/
class Context_TopologyUuid_NodeNode_Uuid_Transferintegrity(MethodView):

    def get(self, uuid, node_uuid):
        print "Retrieve operation of resource: _transferIntegrity"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_TransferintegrityImpl.get(uuid, node_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notifSubscription/(\w+)/
class Context_NotifsubscriptionUuid(MethodView):

    def put(self, uuid):
        print "Update operation of resource: _notifSubscription"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_NotifsubscriptionUuidImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(NotificationSubscriptionService, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_NotifsubscriptionUuidImpl.put(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    Context_NotifsubscriptionUuidImpl.put(uuid, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid):
        print "Create operation of resource: _notifSubscription"
        try:
            response = Context_NotifsubscriptionUuidImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(NotificationSubscriptionService, json_struct, (uuid,'uuid'))
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_NotifsubscriptionUuidImpl.post(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid):
        print "Delete operation of resource: _notifSubscription"
        try:
            response=Context_NotifsubscriptionUuidImpl.delete(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid):
        print "Retrieve operation of resource: _notifSubscription"
        try:
            response = Context_NotifsubscriptionUuidImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/label/
class Context_TopologyUuid_LinkLink_UuidLabel(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: label"
        try:
            response = Context_TopologyUuid_LinkLink_UuidLabelImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_schedule/
class Context_ConnectivityserviceUuid_Schedule(MethodView):

    def put(self, uuid):
        print "Update operation of resource: _schedule"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_ConnectivityserviceUuid_ScheduleImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(TimeRange, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_ConnectivityserviceUuid_ScheduleImpl.put(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    Context_ConnectivityserviceUuid_ScheduleImpl.put(uuid, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid):
        print "Create operation of resource: _schedule"
        try:
            response = Context_ConnectivityserviceUuid_ScheduleImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(TimeRange, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_ConnectivityserviceUuid_ScheduleImpl.post(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid):
        print "Delete operation of resource: _schedule"
        try:
            response=Context_ConnectivityserviceUuid_ScheduleImpl.delete(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid):
        print "Retrieve operation of resource: _schedule"
        try:
            response = Context_ConnectivityserviceUuid_ScheduleImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connection/(\w+)/label/
class Context_ConnectivityserviceUuid_ConnectionConnection_UuidLabel(MethodView):

    def get(self, uuid, connection_uuid):
        print "Retrieve operation of resource: label"
        try:
            response = Context_ConnectivityserviceUuid_ConnectionConnection_UuidLabelImpl.get(uuid, connection_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/(\w+)/_vnwConstraint/costCharacteristic/(\w+)/
class Context_VnwserviceUuid_VnwconstraintCostcharacteristicCostalgorithm(MethodView):

    def put(self, uuid, costAlgorithm):
        print "Update operation of resource: costCharacteristic"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_VnwserviceUuid_VnwconstraintCostcharacteristicCostalgorithmImpl.get(uuid, costAlgorithm)
        except KeyError as inst:
            if inst.args[0] != 'costAlgorithm':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(CostCharacteristic, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_VnwserviceUuid_VnwconstraintCostcharacteristicCostalgorithmImpl.put(uuid, costAlgorithm, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    Context_VnwserviceUuid_VnwconstraintCostcharacteristicCostalgorithmImpl.put(uuid, costAlgorithm, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid, costAlgorithm):
        print "Create operation of resource: costCharacteristic"
        try:
            response = Context_VnwserviceUuid_VnwconstraintCostcharacteristicCostalgorithmImpl.get(uuid, costAlgorithm)
        except KeyError as inst:
            if inst.args[0] != 'costAlgorithm':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(CostCharacteristic, json_struct, (costAlgorithm,'costAlgorithm'))
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_VnwserviceUuid_VnwconstraintCostcharacteristicCostalgorithmImpl.post(uuid, costAlgorithm, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid, costAlgorithm):
        print "Delete operation of resource: costCharacteristic"
        try:
            response=Context_VnwserviceUuid_VnwconstraintCostcharacteristicCostalgorithmImpl.delete(uuid, costAlgorithm)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid, costAlgorithm):
        print "Retrieve operation of resource: costCharacteristic"
        try:
            response = Context_VnwserviceUuid_VnwconstraintCostcharacteristicCostalgorithmImpl.get(uuid, costAlgorithm)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_transferCapacity/
class Context_TopologyUuid_NodeNode_Uuid_Transfercapacity(MethodView):

    def get(self, uuid, node_uuid):
        print "Retrieve operation of resource: _transferCapacity"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_TransfercapacityImpl.get(uuid, node_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connConstraints/costCharacteristic/
class Context_ConnectivityserviceUuid_ConnconstraintsCostcharacteristic(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: costCharacteristic"
        try:
            response = Context_ConnectivityserviceUuid_ConnconstraintsCostcharacteristicImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_ownedNodeEdgePoint/(\w+)/_layerProtocol/(\w+)/
class Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalid(MethodView):

    def get(self, uuid, node_uuid, ownedNodeEdgePoint_uuid, localId):
        print "Retrieve operation of resource: _layerProtocol"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalidImpl.get(uuid, node_uuid, ownedNodeEdgePoint_uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/name/(\w+)/
class ContextNameValuename(MethodView):

    def put(self, valueName):
        print "Update operation of resource: name"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = ContextNameValuenameImpl.get(valueName)
        except KeyError as inst:
            if inst.args[0] != 'valueName':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(NameAndValue, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    ContextNameValuenameImpl.put(valueName, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    ContextNameValuenameImpl.put(valueName, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, valueName):
        print "Create operation of resource: name"
        try:
            response = ContextNameValuenameImpl.get(valueName)
        except KeyError as inst:
            if inst.args[0] != 'valueName':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(NameAndValue, json_struct, (valueName,'valueName'))
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    ContextNameValuenameImpl.post(valueName, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, valueName):
        print "Delete operation of resource: name"
        try:
            response=ContextNameValuenameImpl.delete(valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, valueName):
        print "Retrieve operation of resource: name"
        try:
            response = ContextNameValuenameImpl.get(valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_serviceEndPoint/(\w+)/_connectionEndPoint/(\w+)/_ltpSpecData/
class Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_Ltpspecdata(MethodView):

    def get(self, uuid, connectionEndPoint_uuid):
        print "Retrieve operation of resource: _ltpSpecData"
        try:
            response = Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_LtpspecdataImpl.get(uuid, connectionEndPoint_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connConstraints/
class Context_ConnectivityserviceUuid_Connconstraints(MethodView):

    def put(self, uuid):
        print "Update operation of resource: _connConstraints"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_ConnectivityserviceUuid_ConnconstraintsImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(ConnectivityConstraint, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_ConnectivityserviceUuid_ConnconstraintsImpl.put(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    Context_ConnectivityserviceUuid_ConnconstraintsImpl.put(uuid, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid):
        print "Create operation of resource: _connConstraints"
        try:
            response = Context_ConnectivityserviceUuid_ConnconstraintsImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(ConnectivityConstraint, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_ConnectivityserviceUuid_ConnconstraintsImpl.post(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid):
        print "Delete operation of resource: _connConstraints"
        try:
            response=Context_ConnectivityserviceUuid_ConnconstraintsImpl.delete(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid):
        print "Retrieve operation of resource: _connConstraints"
        try:
            response = Context_ConnectivityserviceUuid_ConnconstraintsImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_path/(\w+)/_telink/(\w+)/
class Context_PathcompserviceUuid_PathPath_Uuid_TelinkLocalid(MethodView):

    def get(self, uuid, path_uuid, localId):
        print "Retrieve operation of resource: _telink"
        try:
            response = Context_PathcompserviceUuid_PathPath_Uuid_TelinkLocalidImpl.get(uuid, path_uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notification/(\w+)/targetObjectName/
class Context_NotificationNotificationidTargetobjectname(MethodView):

    def get(self, notificationId):
        print "Retrieve operation of resource: targetObjectName"
        try:
            response = Context_NotificationNotificationidTargetobjectnameImpl.get(notificationId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_path/(\w+)/_telink/
class Context_PathcompserviceUuid_PathPath_Uuid_Telink(MethodView):

    def get(self, uuid, path_uuid):
        print "Retrieve operation of resource: _telink"
        try:
            response = Context_PathcompserviceUuid_PathPath_Uuid_TelinkImpl.get(uuid, path_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_path/(\w+)/
class Context_PathcompserviceUuid_PathPath_Uuid(MethodView):

    def get(self, uuid, path_uuid):
        print "Retrieve operation of resource: _path"
        try:
            response = Context_PathcompserviceUuid_PathPath_UuidImpl.get(uuid, path_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_transferTiming/
class Context_TopologyUuid_NodeNode_Uuid_Transfertiming(MethodView):

    def get(self, uuid, node_uuid):
        print "Retrieve operation of resource: _transferTiming"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_TransfertimingImpl.get(uuid, node_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/name/
class Context_TopologyUuid_NodeNode_UuidName(MethodView):

    def get(self, uuid, node_uuid):
        print "Retrieve operation of resource: name"
        try:
            response = Context_TopologyUuid_NodeNode_UuidNameImpl.get(uuid, node_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_transferCapacity/availableCapacity/
class Context_TopologyUuid_NodeNode_Uuid_TransfercapacityAvailablecapacity(MethodView):

    def get(self, uuid, node_uuid):
        print "Retrieve operation of resource: availableCapacity"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_TransfercapacityAvailablecapacityImpl.get(uuid, node_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/(\w+)/label/(\w+)/
class Context_VnwserviceUuidLabelValuename(MethodView):

    def put(self, uuid, valueName):
        print "Update operation of resource: label"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_VnwserviceUuidLabelValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            if inst.args[0] != 'valueName':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(NameAndValue, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_VnwserviceUuidLabelValuenameImpl.put(uuid, valueName, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    Context_VnwserviceUuidLabelValuenameImpl.put(uuid, valueName, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid, valueName):
        print "Create operation of resource: label"
        try:
            response = Context_VnwserviceUuidLabelValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            if inst.args[0] != 'valueName':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(NameAndValue, json_struct, (valueName,'valueName'))
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_VnwserviceUuidLabelValuenameImpl.post(uuid, valueName, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid, valueName):
        print "Delete operation of resource: label"
        try:
            response=Context_VnwserviceUuidLabelValuenameImpl.delete(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid, valueName):
        print "Retrieve operation of resource: label"
        try:
            response = Context_VnwserviceUuidLabelValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notification/(\w+)/additionalInfo/
class Context_NotificationNotificationidAdditionalinfo(MethodView):

    def get(self, notificationId):
        print "Retrieve operation of resource: additionalInfo"
        try:
            response = Context_NotificationNotificationidAdditionalinfoImpl.get(notificationId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notification/
class Context_Notification(MethodView):

    def get(self, ):
        print "Retrieve operation of resource: _notification"
        try:
            response = Context_NotificationImpl.get()
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connConstraints/latencyCharacteristic/
class Context_ConnectivityserviceUuid_ConnconstraintsLatencycharacteristic(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: latencyCharacteristic"
        try:
            response = Context_ConnectivityserviceUuid_ConnconstraintsLatencycharacteristicImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_transferCost/
class Context_TopologyUuid_NodeNode_Uuid_Transfercost(MethodView):

    def get(self, uuid, node_uuid):
        print "Retrieve operation of resource: _transferCost"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_TransfercostImpl.get(uuid, node_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_path/(\w+)/_routingConstraint/
class Context_PathcompserviceUuid_PathPath_Uuid_Routingconstraint(MethodView):

    def get(self, uuid, path_uuid):
        print "Retrieve operation of resource: _routingConstraint"
        try:
            response = Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintImpl.get(uuid, path_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/(\w+)/_vnwConstraint/riskCharacteristic/
class Context_VnwserviceUuid_VnwconstraintRiskcharacteristic(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: riskCharacteristic"
        try:
            response = Context_VnwserviceUuid_VnwconstraintRiskcharacteristicImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_transferCapacity/capacityAssignedToUserView/
class Context_TopologyUuid_NodeNode_Uuid_TransfercapacityCapacityassignedtouserview(MethodView):

    def get(self, uuid, node_uuid):
        print "Retrieve operation of resource: capacityAssignedToUserView"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_TransfercapacityCapacityassignedtouserviewImpl.get(uuid, node_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_path/(\w+)/_routingConstraint/latencyCharacteristic/(\w+)/
class Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintLatencycharacteristicLatencyvalue(MethodView):

    def get(self, uuid, path_uuid, latencyValue):
        print "Retrieve operation of resource: latencyCharacteristic"
        try:
            response = Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintLatencycharacteristicLatencyvalueImpl.get(uuid, path_uuid, latencyValue)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/label/(\w+)/
class ContextLabelValuename(MethodView):

    def put(self, valueName):
        print "Update operation of resource: label"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = ContextLabelValuenameImpl.get(valueName)
        except KeyError as inst:
            if inst.args[0] != 'valueName':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(NameAndValue, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    ContextLabelValuenameImpl.put(valueName, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            existing_object = modify_instance(existing_object, json_struct)
            if isinstance(existing_object, BadRequestError):
                return existing_object
            elif isinstance(existing_object, NotFoundError):
                return existing_object
            else:
                try:
                    ContextLabelValuenameImpl.put(valueName, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, valueName):
        print "Create operation of resource: label"
        try:
            response = ContextLabelValuenameImpl.get(valueName)
        except KeyError as inst:
            if inst.args[0] != 'valueName':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(NameAndValue, json_struct, (valueName,'valueName'))
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    ContextLabelValuenameImpl.post(valueName, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, valueName):
        print "Delete operation of resource: label"
        try:
            response=ContextLabelValuenameImpl.delete(valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, valueName):
        print "Retrieve operation of resource: label"
        try:
            response = ContextLabelValuenameImpl.get(valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_serviceEndPoint/(\w+)/_ltpSpecData/
class Context_ServiceendpointUuid_Ltpspecdata(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _ltpSpecData"
        try:
            response = Context_ServiceendpointUuid_LtpspecdataImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_serviceEndPoint/(\w+)/_connectionEndPoint/(\w+)/label/(\w+)/
class Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidLabelValuename(MethodView):

    def get(self, uuid, connectionEndPoint_uuid, valueName):
        print "Retrieve operation of resource: label"
        try:
            response = Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidLabelValuenameImpl.get(uuid, connectionEndPoint_uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_serviceEndPoint/(\w+)/
class Context_ServiceendpointUuid(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _serviceEndPoint"
        try:
            response = Context_ServiceendpointUuidImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/
class Context_TopologyUuid_LinkLink_Uuid(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: _link"
        try:
            response = Context_TopologyUuid_LinkLink_UuidImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_transferCapacity/totalPotentialCapacity/
class Context_TopologyUuid_NodeNode_Uuid_TransfercapacityTotalpotentialcapacity(MethodView):

    def get(self, uuid, node_uuid):
        print "Retrieve operation of resource: totalPotentialCapacity"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_TransfercapacityTotalpotentialcapacityImpl.get(uuid, node_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/name/(\w+)/
class Context_TopologyUuid_LinkLink_UuidNameValuename(MethodView):

    def get(self, uuid, link_uuid, valueName):
        print "Retrieve operation of resource: name"
        try:
            response = Context_TopologyUuid_LinkLink_UuidNameValuenameImpl.get(uuid, link_uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))



getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notification/<notificationId>/targetObjectName/<valueName>/", view_func = globals()["Context_NotificationNotificationidTargetobjectnameValuename"].as_view('"Context_NotificationNotificationidTargetobjectnameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferCost/costCharacteristic/<costAlgorithm>/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_TransfercostCostcharacteristicCostalgorithm"].as_view('"Context_TopologyUuid_NodeNode_Uuid_TransfercostCostcharacteristicCostalgorithm"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/name/<valueName>/", view_func = globals()["Context_TopologyUuid_NodeNode_UuidNameValuename"].as_view('"Context_TopologyUuid_NodeNode_UuidNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/label/<valueName>/", view_func = globals()["Context_ServiceendpointUuidLabelValuename"].as_view('"Context_ServiceendpointUuidLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_state/", view_func = globals()["Context_ConnectivityserviceUuid_State"].as_view('"Context_ConnectivityserviceUuid_State"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/", view_func = globals()["Context_PathcompserviceUuid"].as_view('"Context_PathcompserviceUuid"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/name/<valueName>/", view_func = globals()["Context_PathcompserviceUuidNameValuename"].as_view('"Context_PathcompserviceUuidNameValuename"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_layerProtocol/", view_func = globals()["Context_ServiceendpointUuid_Layerprotocol"].as_view('"Context_ServiceendpointUuid_Layerprotocol"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/label/<valueName>/", view_func = globals()["Context_NotifsubscriptionUuidLabelValuename"].as_view('"Context_NotifsubscriptionUuidLabelValuename"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferIntegrity/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_Transferintegrity"].as_view('"Context_TopologyUuid_LinkLink_Uuid_Transferintegrity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_state/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_State"].as_view('"Context_TopologyUuid_LinkLink_Uuid_State"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/_notification/<notificationId>/additionalInfo/", view_func = globals()["Context_NotifsubscriptionUuid_NotificationNotificationidAdditionalinfo"].as_view('"Context_NotifsubscriptionUuid_NotificationNotificationidAdditionalinfo"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/label/", view_func = globals()["Context_ConnectivityserviceUuidLabel"].as_view('"Context_ConnectivityserviceUuidLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_state/", view_func = globals()["Context_ServiceendpointUuid_State"].as_view('"Context_ServiceendpointUuid_State"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/name/", view_func = globals()["Context_PathcompserviceUuidName"].as_view('"Context_PathcompserviceUuidName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_connectionEndPoint/", view_func = globals()["Context_ServiceendpointUuid_Connectionendpoint"].as_view('"Context_ServiceendpointUuid_Connectionendpoint"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/label/", view_func = globals()["Context_PathcompserviceUuidLabel"].as_view('"Context_PathcompserviceUuidLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_schedule/", view_func = globals()["Context_VnwserviceUuid_Schedule"].as_view('"Context_VnwserviceUuid_Schedule"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferTiming/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_Transfertiming"].as_view('"Context_TopologyUuid_LinkLink_Uuid_Transfertiming"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/_notification/<notificationId>/targetObjectName/<valueName>/", view_func = globals()["Context_NotifsubscriptionUuid_NotificationNotificationidTargetobjectnameValuename"].as_view('"Context_NotifsubscriptionUuid_NotificationNotificationidTargetobjectnameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_connectionEndPoint/<connectionEndPoint_uuid>/_layerProtocol/", view_func = globals()["Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_Layerprotocol"].as_view('"Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_Layerprotocol"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/name/<valueName>/", view_func = globals()["Context_ServiceendpointUuidNameValuename"].as_view('"Context_ServiceendpointUuidNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_state/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_State"].as_view('"Context_TopologyUuid_NodeNode_Uuid_State"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/_notification/<notificationId>/changedAttributes/", view_func = globals()["Context_NotifsubscriptionUuid_NotificationNotificationidChangedattributes"].as_view('"Context_NotifsubscriptionUuid_NotificationNotificationidChangedattributes"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connection/<connection_uuid>/name/<valueName>/", view_func = globals()["Context_ConnectivityserviceUuid_ConnectionConnection_UuidNameValuename"].as_view('"Context_ConnectivityserviceUuid_ConnectionConnection_UuidNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/<ownedNodeEdgePoint_uuid>/_layerProtocol/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_Layerprotocol"].as_view('"Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_Layerprotocol"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connection/<connection_uuid>/_route/<localId>/", view_func = globals()["Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_RouteLocalid"].as_view('"Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_RouteLocalid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferTiming/queuingLatency/<latencyValue>/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_TransfertimingQueuinglatencyLatencyvalue"].as_view('"Context_TopologyUuid_NodeNode_Uuid_TransfertimingQueuinglatencyLatencyvalue"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_riskParameter/riskCharacteristic/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_RiskparameterRiskcharacteristic"].as_view('"Context_TopologyUuid_LinkLink_Uuid_RiskparameterRiskcharacteristic"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferTiming/queuingLatency/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_TransfertimingQueuinglatency"].as_view('"Context_TopologyUuid_NodeNode_Uuid_TransfertimingQueuinglatency"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/name/<valueName>/", view_func = globals()["Context_VnwserviceUuidNameValuename"].as_view('"Context_VnwserviceUuidNameValuename"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/", view_func = globals()["Context"].as_view('"Context"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/", view_func = globals()["Context_TopologyUuid_Node"].as_view('"Context_TopologyUuid_Node"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/label/", view_func = globals()["ContextLabel"].as_view('"ContextLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferTiming/queuingLatency/<latencyValue>/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_TransfertimingQueuinglatencyLatencyvalue"].as_view('"Context_TopologyUuid_LinkLink_Uuid_TransfertimingQueuinglatencyLatencyvalue"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferCapacity/capacityAssignedToUserView/<numberingRange>/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_TransfercapacityCapacityassignedtouserviewNumberingrange"].as_view('"Context_TopologyUuid_NodeNode_Uuid_TransfercapacityCapacityassignedtouserviewNumberingrange"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/", view_func = globals()["Context_Pathcompservice"].as_view('"Context_Pathcompservice"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/<ownedNodeEdgePoint_uuid>/_ltpSpecData/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_Ltpspecdata"].as_view('"Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_Ltpspecdata"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid"].as_view('"Context_TopologyUuid_NodeNode_Uuid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_path/<path_uuid>/_routingConstraint/riskCharacteristic/", view_func = globals()["Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintRiskcharacteristic"].as_view('"Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintRiskcharacteristic"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/name/<valueName>/", view_func = globals()["Context_NotifsubscriptionUuidNameValuename"].as_view('"Context_NotifsubscriptionUuidNameValuename"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_vnwConstraint/latencyCharacteristic/<latencyValue>/", view_func = globals()["Context_VnwserviceUuid_VnwconstraintLatencycharacteristicLatencyvalue"].as_view('"Context_VnwserviceUuid_VnwconstraintLatencycharacteristicLatencyvalue"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/<ownedNodeEdgePoint_uuid>/_layerProtocol/<localId>/_lpSpecData/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalid_Lpspecdata"].as_view('"Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalid_Lpspecdata"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/name/<valueName>/", view_func = globals()["Context_TopologyUuidNameValuename"].as_view('"Context_TopologyUuidNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_routingConstraint/latencyCharacteristic/", view_func = globals()["Context_PathcompserviceUuid_RoutingconstraintLatencycharacteristic"].as_view('"Context_PathcompserviceUuid_RoutingconstraintLatencycharacteristic"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notification/<notificationId>/changedAttributes/", view_func = globals()["Context_NotificationNotificationidChangedattributes"].as_view('"Context_NotificationNotificationidChangedattributes"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_connectionEndPoint/<connectionEndPoint_uuid>/_state/", view_func = globals()["Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_State"].as_view('"Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_State"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_vnwConstraint/", view_func = globals()["Context_VnwserviceUuid_Vnwconstraint"].as_view('"Context_VnwserviceUuid_Vnwconstraint"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_routingConstraint/requestedCapacity/", view_func = globals()["Context_PathcompserviceUuid_RoutingconstraintRequestedcapacity"].as_view('"Context_PathcompserviceUuid_RoutingconstraintRequestedcapacity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_path/<path_uuid>/name/", view_func = globals()["Context_PathcompserviceUuid_PathPath_UuidName"].as_view('"Context_PathcompserviceUuid_PathPath_UuidName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connConstraints/requestedCapacity/", view_func = globals()["Context_ConnectivityserviceUuid_ConnconstraintsRequestedcapacity"].as_view('"Context_ConnectivityserviceUuid_ConnconstraintsRequestedcapacity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connConstraints/latencyCharacteristic/<latencyValue>/", view_func = globals()["Context_ConnectivityserviceUuid_ConnconstraintsLatencycharacteristicLatencyvalue"].as_view('"Context_ConnectivityserviceUuid_ConnconstraintsLatencycharacteristicLatencyvalue"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferCost/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_Transfercost"].as_view('"Context_TopologyUuid_LinkLink_Uuid_Transfercost"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_routingConstraint/latencyCharacteristic/<latencyValue>/", view_func = globals()["Context_PathcompserviceUuid_RoutingconstraintLatencycharacteristicLatencyvalue"].as_view('"Context_PathcompserviceUuid_RoutingconstraintLatencycharacteristicLatencyvalue"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/<ownedNodeEdgePoint_uuid>/name/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidName"].as_view('"Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/name/", view_func = globals()["Context_NotifsubscriptionUuidName"].as_view('"Context_NotifsubscriptionUuidName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_servicePort/", view_func = globals()["Context_ConnectivityserviceUuid_Serviceport"].as_view('"Context_ConnectivityserviceUuid_Serviceport"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/_notification/", view_func = globals()["Context_NotifsubscriptionUuid_Notification"].as_view('"Context_NotifsubscriptionUuid_Notification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/label/<valueName>/", view_func = globals()["Context_TopologyUuid_LinkLink_UuidLabelValuename"].as_view('"Context_TopologyUuid_LinkLink_UuidLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_routingConstraint/costCharacteristic/", view_func = globals()["Context_PathcompserviceUuid_RoutingconstraintCostcharacteristic"].as_view('"Context_PathcompserviceUuid_RoutingconstraintCostcharacteristic"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/label/", view_func = globals()["Context_TopologyUuid_NodeNode_UuidLabel"].as_view('"Context_TopologyUuid_NodeNode_UuidLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_servicePort/<localId>/", view_func = globals()["Context_VnwserviceUuid_ServiceportLocalid"].as_view('"Context_VnwserviceUuid_ServiceportLocalid"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_lpTransition/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_Lptransition"].as_view('"Context_TopologyUuid_LinkLink_Uuid_Lptransition"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_validation/validationMechanism/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_ValidationValidationmechanism"].as_view('"Context_TopologyUuid_LinkLink_Uuid_ValidationValidationmechanism"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_path/<path_uuid>/_routingConstraint/latencyCharacteristic/", view_func = globals()["Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintLatencycharacteristic"].as_view('"Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintLatencycharacteristic"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/label/<valueName>/", view_func = globals()["Context_PathcompserviceUuidLabelValuename"].as_view('"Context_PathcompserviceUuidLabelValuename"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_path/", view_func = globals()["Context_PathcompserviceUuid_Path"].as_view('"Context_PathcompserviceUuid_Path"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_path/<path_uuid>/label/", view_func = globals()["Context_PathcompserviceUuid_PathPath_UuidLabel"].as_view('"Context_PathcompserviceUuid_PathPath_UuidLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_routingConstraint/", view_func = globals()["Context_PathcompserviceUuid_Routingconstraint"].as_view('"Context_PathcompserviceUuid_Routingconstraint"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/name/", view_func = globals()["Context_TopologyUuidName"].as_view('"Context_TopologyUuidName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_connectionEndPoint/<connectionEndPoint_uuid>/_layerProtocol/<localId>/_lpSpecData/", view_func = globals()["Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_LayerprotocolLocalid_Lpspecdata"].as_view('"Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_LayerprotocolLocalid_Lpspecdata"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_routingConstraint/riskCharacteristic/<riskCharacteristicName>/", view_func = globals()["Context_PathcompserviceUuid_RoutingconstraintRiskcharacteristicRiskcharacteristicname"].as_view('"Context_PathcompserviceUuid_RoutingconstraintRiskcharacteristicRiskcharacteristicname"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/name/", view_func = globals()["Context_ConnectivityserviceUuidName"].as_view('"Context_ConnectivityserviceUuidName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_linkPort/<localId>/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_LinkportLocalid"].as_view('"Context_TopologyUuid_LinkLink_Uuid_LinkportLocalid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/name/", view_func = globals()["Context_VnwserviceUuidName"].as_view('"Context_VnwserviceUuidName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_connectionEndPoint/<connectionEndPoint_uuid>/name/<valueName>/", view_func = globals()["Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidNameValuename"].as_view('"Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/<ownedNodeEdgePoint_uuid>/name/<valueName>/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidNameValuename"].as_view('"Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_servicePort/<localId>/", view_func = globals()["Context_PathcompserviceUuid_ServiceportLocalid"].as_view('"Context_PathcompserviceUuid_ServiceportLocalid"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/", view_func = globals()["Context_Serviceendpoint"].as_view('"Context_Serviceendpoint"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/name/", view_func = globals()["Context_ServiceendpointUuidName"].as_view('"Context_ServiceendpointUuidName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/name/", view_func = globals()["ContextName"].as_view('"ContextName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_vnwConstraint/costCharacteristic/", view_func = globals()["Context_VnwserviceUuid_VnwconstraintCostcharacteristic"].as_view('"Context_VnwserviceUuid_VnwconstraintCostcharacteristic"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_objectiveFunction/", view_func = globals()["Context_PathcompserviceUuid_Objectivefunction"].as_view('"Context_PathcompserviceUuid_Objectivefunction"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_riskParameter/riskCharacteristic/<riskCharacteristicName>/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_RiskparameterRiskcharacteristicRiskcharacteristicname"].as_view('"Context_TopologyUuid_LinkLink_Uuid_RiskparameterRiskcharacteristicRiskcharacteristicname"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_connectionEndPoint/<connectionEndPoint_uuid>/_layerProtocol/<localId>/", view_func = globals()["Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_LayerprotocolLocalid"].as_view('"Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_LayerprotocolLocalid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/", view_func = globals()["Context_Notifsubscription"].as_view('"Context_Notifsubscription"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_layerProtocol/<localId>/", view_func = globals()["Context_ServiceendpointUuid_LayerprotocolLocalid"].as_view('"Context_ServiceendpointUuid_LayerprotocolLocalid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferCost/costCharacteristic/<costAlgorithm>/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_TransfercostCostcharacteristicCostalgorithm"].as_view('"Context_TopologyUuid_LinkLink_Uuid_TransfercostCostcharacteristicCostalgorithm"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/<ownedNodeEdgePoint_uuid>/label/<valueName>/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidLabelValuename"].as_view('"Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_servicePort/<localId>/", view_func = globals()["Context_ConnectivityserviceUuid_ServiceportLocalid"].as_view('"Context_ConnectivityserviceUuid_ServiceportLocalid"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferTiming/queuingLatency/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_TransfertimingQueuinglatency"].as_view('"Context_TopologyUuid_LinkLink_Uuid_TransfertimingQueuinglatency"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/", view_func = globals()["Context_ConnectivityserviceUuid"].as_view('"Context_ConnectivityserviceUuid"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/", view_func = globals()["Context_TopologyUuid"].as_view('"Context_TopologyUuid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connection/<connection_uuid>/", view_func = globals()["Context_ConnectivityserviceUuid_ConnectionConnection_Uuid"].as_view('"Context_ConnectivityserviceUuid_ConnectionConnection_Uuid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/", view_func = globals()["Context_Connectivityservice"].as_view('"Context_Connectivityservice"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_validation/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_Validation"].as_view('"Context_TopologyUuid_LinkLink_Uuid_Validation"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferCapacity/totalPotentialCapacity/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_TransfercapacityTotalpotentialcapacity"].as_view('"Context_TopologyUuid_LinkLink_Uuid_TransfercapacityTotalpotentialcapacity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_Ownednodeedgepoint"].as_view('"Context_TopologyUuid_NodeNode_Uuid_Ownednodeedgepoint"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/", view_func = globals()["Context_Topology"].as_view('"Context_Topology"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connection/", view_func = globals()["Context_ConnectivityserviceUuid_Connection"].as_view('"Context_ConnectivityserviceUuid_Connection"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connection/<connection_uuid>/_route/", view_func = globals()["Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_Route"].as_view('"Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_Route"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/label/<valueName>/", view_func = globals()["Context_TopologyUuid_NodeNode_UuidLabelValuename"].as_view('"Context_TopologyUuid_NodeNode_UuidLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connection/<connection_uuid>/_state/", view_func = globals()["Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_State"].as_view('"Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_State"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connConstraints/riskCharacteristic/", view_func = globals()["Context_ConnectivityserviceUuid_ConnconstraintsRiskcharacteristic"].as_view('"Context_ConnectivityserviceUuid_ConnconstraintsRiskcharacteristic"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/_notification/<notificationId>/additionalInfo/<valueName>/", view_func = globals()["Context_NotifsubscriptionUuid_NotificationNotificationidAdditionalinfoValuename"].as_view('"Context_NotifsubscriptionUuid_NotificationNotificationidAdditionalinfoValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connection/<connection_uuid>/_connectionPort/<localId>/", view_func = globals()["Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_ConnectionportLocalid"].as_view('"Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_ConnectionportLocalid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/", view_func = globals()["Context_VnwserviceUuid"].as_view('"Context_VnwserviceUuid"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/_subscriptionFilter/", view_func = globals()["Context_NotifsubscriptionUuid_Subscriptionfilter"].as_view('"Context_NotifsubscriptionUuid_Subscriptionfilter"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connection/<connection_uuid>/name/", view_func = globals()["Context_ConnectivityserviceUuid_ConnectionConnection_UuidName"].as_view('"Context_ConnectivityserviceUuid_ConnectionConnection_UuidName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_path/<path_uuid>/_routingConstraint/costCharacteristic/<costAlgorithm>/", view_func = globals()["Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintCostcharacteristicCostalgorithm"].as_view('"Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintCostcharacteristicCostalgorithm"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_routingConstraint/riskCharacteristic/", view_func = globals()["Context_PathcompserviceUuid_RoutingconstraintRiskcharacteristic"].as_view('"Context_PathcompserviceUuid_RoutingconstraintRiskcharacteristic"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_riskParameter/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_Riskparameter"].as_view('"Context_TopologyUuid_LinkLink_Uuid_Riskparameter"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/label/", view_func = globals()["Context_TopologyUuidLabel"].as_view('"Context_TopologyUuidLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/", view_func = globals()["Context_Vnwservice"].as_view('"Context_Vnwservice"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_connectionEndPoint/<connectionEndPoint_uuid>/", view_func = globals()["Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid"].as_view('"Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_layerProtocol/<localId>/_lpSpecData/", view_func = globals()["Context_ServiceendpointUuid_LayerprotocolLocalid_Lpspecdata"].as_view('"Context_ServiceendpointUuid_LayerprotocolLocalid_Lpspecdata"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notification/<notificationId>/additionalInfo/<valueName>/", view_func = globals()["Context_NotificationNotificationidAdditionalinfoValuename"].as_view('"Context_NotificationNotificationidAdditionalinfoValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/label/", view_func = globals()["Context_VnwserviceUuidLabel"].as_view('"Context_VnwserviceUuidLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_path/<path_uuid>/_routingConstraint/riskCharacteristic/<riskCharacteristicName>/", view_func = globals()["Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintRiskcharacteristicRiskcharacteristicname"].as_view('"Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintRiskcharacteristicRiskcharacteristicname"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferCapacity/capacityAssignedToUserView/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_TransfercapacityCapacityassignedtouserview"].as_view('"Context_TopologyUuid_LinkLink_Uuid_TransfercapacityCapacityassignedtouserview"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_vnwConstraint/latencyCharacteristic/", view_func = globals()["Context_VnwserviceUuid_VnwconstraintLatencycharacteristic"].as_view('"Context_VnwserviceUuid_VnwconstraintLatencycharacteristic"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_vnwConstraint/requestedCapacity/", view_func = globals()["Context_VnwserviceUuid_VnwconstraintRequestedcapacity"].as_view('"Context_VnwserviceUuid_VnwconstraintRequestedcapacity"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connConstraints/costCharacteristic/<costAlgorithm>/", view_func = globals()["Context_ConnectivityserviceUuid_ConnconstraintsCostcharacteristicCostalgorithm"].as_view('"Context_ConnectivityserviceUuid_ConnconstraintsCostcharacteristicCostalgorithm"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferCost/costCharacteristic/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_TransfercostCostcharacteristic"].as_view('"Context_TopologyUuid_NodeNode_Uuid_TransfercostCostcharacteristic"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/<ownedNodeEdgePoint_uuid>/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid"].as_view('"Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_path/<path_uuid>/name/<valueName>/", view_func = globals()["Context_PathcompserviceUuid_PathPath_UuidNameValuename"].as_view('"Context_PathcompserviceUuid_PathPath_UuidNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/", view_func = globals()["Context_TopologyUuid_Link"].as_view('"Context_TopologyUuid_Link"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/name/<valueName>/", view_func = globals()["Context_ConnectivityserviceUuidNameValuename"].as_view('"Context_ConnectivityserviceUuidNameValuename"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferCapacity/capacityAssignedToUserView/<numberingRange>/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_TransfercapacityCapacityassignedtouserviewNumberingrange"].as_view('"Context_TopologyUuid_LinkLink_Uuid_TransfercapacityCapacityassignedtouserviewNumberingrange"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_optimizationConstraint/", view_func = globals()["Context_PathcompserviceUuid_Optimizationconstraint"].as_view('"Context_PathcompserviceUuid_Optimizationconstraint"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/_notification/<notificationId>/", view_func = globals()["Context_NotifsubscriptionUuid_NotificationNotificationid"].as_view('"Context_NotifsubscriptionUuid_NotificationNotificationid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_linkPort/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_Linkport"].as_view('"Context_TopologyUuid_LinkLink_Uuid_Linkport"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_servicePort/", view_func = globals()["Context_VnwserviceUuid_Serviceport"].as_view('"Context_VnwserviceUuid_Serviceport"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/<ownedNodeEdgePoint_uuid>/label/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidLabel"].as_view('"Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connection/<connection_uuid>/_connectionPort/", view_func = globals()["Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_Connectionport"].as_view('"Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_Connectionport"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_path/<path_uuid>/_routingConstraint/costCharacteristic/", view_func = globals()["Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintCostcharacteristic"].as_view('"Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintCostcharacteristic"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connConstraints/riskCharacteristic/<riskCharacteristicName>/", view_func = globals()["Context_ConnectivityserviceUuid_ConnconstraintsRiskcharacteristicRiskcharacteristicname"].as_view('"Context_ConnectivityserviceUuid_ConnconstraintsRiskcharacteristicRiskcharacteristicname"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferCapacity/availableCapacity/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_TransfercapacityAvailablecapacity"].as_view('"Context_TopologyUuid_LinkLink_Uuid_TransfercapacityAvailablecapacity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_validation/validationMechanism/<validationRobustness>/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_ValidationValidationmechanismValidationrobustness"].as_view('"Context_TopologyUuid_LinkLink_Uuid_ValidationValidationmechanismValidationrobustness"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connection/<connection_uuid>/label/<valueName>/", view_func = globals()["Context_ConnectivityserviceUuid_ConnectionConnection_UuidLabelValuename"].as_view('"Context_ConnectivityserviceUuid_ConnectionConnection_UuidLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_connectionEndPoint/<connectionEndPoint_uuid>/label/", view_func = globals()["Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidLabel"].as_view('"Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/label/", view_func = globals()["Context_NotifsubscriptionUuidLabel"].as_view('"Context_NotifsubscriptionUuidLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_routingConstraint/costCharacteristic/<costAlgorithm>/", view_func = globals()["Context_PathcompserviceUuid_RoutingconstraintCostcharacteristicCostalgorithm"].as_view('"Context_PathcompserviceUuid_RoutingconstraintCostcharacteristicCostalgorithm"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_connectionEndPoint/<connectionEndPoint_uuid>/name/", view_func = globals()["Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidName"].as_view('"Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/label/<valueName>/", view_func = globals()["Context_TopologyUuidLabelValuename"].as_view('"Context_TopologyUuidLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferCapacity/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_Transfercapacity"].as_view('"Context_TopologyUuid_LinkLink_Uuid_Transfercapacity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/_notification/<notificationId>/targetObjectName/", view_func = globals()["Context_NotifsubscriptionUuid_NotificationNotificationidTargetobjectname"].as_view('"Context_NotifsubscriptionUuid_NotificationNotificationidTargetobjectname"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferCost/costCharacteristic/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_TransfercostCostcharacteristic"].as_view('"Context_TopologyUuid_LinkLink_Uuid_TransfercostCostcharacteristic"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_vnwConstraint/riskCharacteristic/<riskCharacteristicName>/", view_func = globals()["Context_VnwserviceUuid_VnwconstraintRiskcharacteristicRiskcharacteristicname"].as_view('"Context_VnwserviceUuid_VnwconstraintRiskcharacteristicRiskcharacteristicname"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/label/", view_func = globals()["Context_ServiceendpointUuidLabel"].as_view('"Context_ServiceendpointUuidLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/name/", view_func = globals()["Context_TopologyUuid_LinkLink_UuidName"].as_view('"Context_TopologyUuid_LinkLink_UuidName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_path/<path_uuid>/label/<valueName>/", view_func = globals()["Context_PathcompserviceUuid_PathPath_UuidLabelValuename"].as_view('"Context_PathcompserviceUuid_PathPath_UuidLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notification/<notificationId>/", view_func = globals()["Context_NotificationNotificationid"].as_view('"Context_NotificationNotificationid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_path/<path_uuid>/_routingConstraint/requestedCapacity/", view_func = globals()["Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintRequestedcapacity"].as_view('"Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintRequestedcapacity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_state/", view_func = globals()["Context_VnwserviceUuid_State"].as_view('"Context_VnwserviceUuid_State"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_servicePort/", view_func = globals()["Context_PathcompserviceUuid_Serviceport"].as_view('"Context_PathcompserviceUuid_Serviceport"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/<ownedNodeEdgePoint_uuid>/_state/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_State"].as_view('"Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_State"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/label/<valueName>/", view_func = globals()["Context_ConnectivityserviceUuidLabelValuename"].as_view('"Context_ConnectivityserviceUuidLabelValuename"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferIntegrity/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_Transferintegrity"].as_view('"Context_TopologyUuid_NodeNode_Uuid_Transferintegrity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/", view_func = globals()["Context_NotifsubscriptionUuid"].as_view('"Context_NotifsubscriptionUuid"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/label/", view_func = globals()["Context_TopologyUuid_LinkLink_UuidLabel"].as_view('"Context_TopologyUuid_LinkLink_UuidLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_schedule/", view_func = globals()["Context_ConnectivityserviceUuid_Schedule"].as_view('"Context_ConnectivityserviceUuid_Schedule"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connection/<connection_uuid>/label/", view_func = globals()["Context_ConnectivityserviceUuid_ConnectionConnection_UuidLabel"].as_view('"Context_ConnectivityserviceUuid_ConnectionConnection_UuidLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_vnwConstraint/costCharacteristic/<costAlgorithm>/", view_func = globals()["Context_VnwserviceUuid_VnwconstraintCostcharacteristicCostalgorithm"].as_view('"Context_VnwserviceUuid_VnwconstraintCostcharacteristicCostalgorithm"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferCapacity/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_Transfercapacity"].as_view('"Context_TopologyUuid_NodeNode_Uuid_Transfercapacity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connConstraints/costCharacteristic/", view_func = globals()["Context_ConnectivityserviceUuid_ConnconstraintsCostcharacteristic"].as_view('"Context_ConnectivityserviceUuid_ConnconstraintsCostcharacteristic"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/<ownedNodeEdgePoint_uuid>/_layerProtocol/<localId>/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalid"].as_view('"Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/name/<valueName>/", view_func = globals()["ContextNameValuename"].as_view('"ContextNameValuename"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_connectionEndPoint/<connectionEndPoint_uuid>/_ltpSpecData/", view_func = globals()["Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_Ltpspecdata"].as_view('"Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_Ltpspecdata"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connConstraints/", view_func = globals()["Context_ConnectivityserviceUuid_Connconstraints"].as_view('"Context_ConnectivityserviceUuid_Connconstraints"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_path/<path_uuid>/_telink/<localId>/", view_func = globals()["Context_PathcompserviceUuid_PathPath_Uuid_TelinkLocalid"].as_view('"Context_PathcompserviceUuid_PathPath_Uuid_TelinkLocalid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notification/<notificationId>/targetObjectName/", view_func = globals()["Context_NotificationNotificationidTargetobjectname"].as_view('"Context_NotificationNotificationidTargetobjectname"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_path/<path_uuid>/_telink/", view_func = globals()["Context_PathcompserviceUuid_PathPath_Uuid_Telink"].as_view('"Context_PathcompserviceUuid_PathPath_Uuid_Telink"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_path/<path_uuid>/", view_func = globals()["Context_PathcompserviceUuid_PathPath_Uuid"].as_view('"Context_PathcompserviceUuid_PathPath_Uuid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferTiming/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_Transfertiming"].as_view('"Context_TopologyUuid_NodeNode_Uuid_Transfertiming"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/name/", view_func = globals()["Context_TopologyUuid_NodeNode_UuidName"].as_view('"Context_TopologyUuid_NodeNode_UuidName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferCapacity/availableCapacity/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_TransfercapacityAvailablecapacity"].as_view('"Context_TopologyUuid_NodeNode_Uuid_TransfercapacityAvailablecapacity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/label/<valueName>/", view_func = globals()["Context_VnwserviceUuidLabelValuename"].as_view('"Context_VnwserviceUuidLabelValuename"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notification/<notificationId>/additionalInfo/", view_func = globals()["Context_NotificationNotificationidAdditionalinfo"].as_view('"Context_NotificationNotificationidAdditionalinfo"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notification/", view_func = globals()["Context_Notification"].as_view('"Context_Notification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connConstraints/latencyCharacteristic/", view_func = globals()["Context_ConnectivityserviceUuid_ConnconstraintsLatencycharacteristic"].as_view('"Context_ConnectivityserviceUuid_ConnconstraintsLatencycharacteristic"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferCost/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_Transfercost"].as_view('"Context_TopologyUuid_NodeNode_Uuid_Transfercost"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_path/<path_uuid>/_routingConstraint/", view_func = globals()["Context_PathcompserviceUuid_PathPath_Uuid_Routingconstraint"].as_view('"Context_PathcompserviceUuid_PathPath_Uuid_Routingconstraint"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_vnwConstraint/riskCharacteristic/", view_func = globals()["Context_VnwserviceUuid_VnwconstraintRiskcharacteristic"].as_view('"Context_VnwserviceUuid_VnwconstraintRiskcharacteristic"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferCapacity/capacityAssignedToUserView/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_TransfercapacityCapacityassignedtouserview"].as_view('"Context_TopologyUuid_NodeNode_Uuid_TransfercapacityCapacityassignedtouserview"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_path/<path_uuid>/_routingConstraint/latencyCharacteristic/<latencyValue>/", view_func = globals()["Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintLatencycharacteristicLatencyvalue"].as_view('"Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintLatencycharacteristicLatencyvalue"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/label/<valueName>/", view_func = globals()["ContextLabelValuename"].as_view('"ContextLabelValuename"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_ltpSpecData/", view_func = globals()["Context_ServiceendpointUuid_Ltpspecdata"].as_view('"Context_ServiceendpointUuid_Ltpspecdata"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_connectionEndPoint/<connectionEndPoint_uuid>/label/<valueName>/", view_func = globals()["Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidLabelValuename"].as_view('"Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/", view_func = globals()["Context_ServiceendpointUuid"].as_view('"Context_ServiceendpointUuid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid"].as_view('"Context_TopologyUuid_LinkLink_Uuid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferCapacity/totalPotentialCapacity/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_TransfercapacityTotalpotentialcapacity"].as_view('"Context_TopologyUuid_NodeNode_Uuid_TransfercapacityTotalpotentialcapacity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/name/<valueName>/", view_func = globals()["Context_TopologyUuid_LinkLink_UuidNameValuename"].as_view('"Context_TopologyUuid_LinkLink_UuidNameValuename"'+'"_api"'), methods=['GET'])
