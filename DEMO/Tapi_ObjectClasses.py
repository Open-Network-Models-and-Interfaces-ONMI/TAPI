from flask import json, Blueprint, request, Response
from flask.views import MethodView
import sys
from objects_common.keyedArrayType import KeyedArrayKeyError

import base64
import re

# BACKEND FUNCTIONS
from funcs_Tapi_ObjectClasses.contextExtensionValuenameImpl import ContextExtensionValuenameImpl
from funcs_Tapi_ObjectClasses.context_PathUuidLabelValuenameImpl import Context_PathUuidLabelValuenameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalidImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalidImpl
from funcs_Tapi_ObjectClasses.contextNameValuenameImpl import ContextNameValuenameImpl
from funcs_Tapi_ObjectClasses.context_VnwserviceUuid_VnwconstraintCostcharacteristicCostalgorithmImpl import Context_VnwserviceUuid_VnwconstraintCostcharacteristicCostalgorithmImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_StateImpl import Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_StateImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidExtensionValuenameImpl import Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidExtensionValuenameImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ScheduleImpl import Context_ConnectivityserviceUuid_ScheduleImpl
from funcs_Tapi_ObjectClasses.context_PathUuid_RoutingconstraintImpl import Context_PathUuid_RoutingconstraintImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_UuidNameValuenameImpl import Context_TopologyUuid_NodeNode_UuidNameValuenameImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnectionConnection_Uuid_RouteLocalidImpl import Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_RouteLocalidImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuidNameValuenameImpl import Context_ServiceendpointUuidNameValuenameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_StateImpl import Context_TopologyUuid_NodeNode_Uuid_StateImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_LptransitionImpl import Context_TopologyUuid_LinkLink_Uuid_LptransitionImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_TransfertimingQueuinglatencyLatencyvalueImpl import Context_TopologyUuid_NodeNode_Uuid_TransfertimingQueuinglatencyLatencyvalueImpl
from funcs_Tapi_ObjectClasses.context_PathUuid_OptimizationconstraintImpl import Context_PathUuid_OptimizationconstraintImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnectionConnection_UuidNameValuenameImpl import Context_ConnectivityserviceUuid_ConnectionConnection_UuidNameValuenameImpl
from funcs_Tapi_ObjectClasses.context_PathUuidImpl import Context_PathUuidImpl
from funcs_Tapi_ObjectClasses.context_VnwserviceUuid_ServiceportLocalidImpl import Context_VnwserviceUuid_ServiceportLocalidImpl
from funcs_Tapi_ObjectClasses.context_PathUuidExtensionValuenameImpl import Context_PathUuidExtensionValuenameImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuid_StateImpl import Context_ServiceendpointUuid_StateImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_TransfercapacityAvailablecapacityImpl import Context_TopologyUuid_NodeNode_Uuid_TransfercapacityAvailablecapacityImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuidLabelValuenameImpl import Context_TopologyUuidLabelValuenameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_TransfertimingImpl import Context_TopologyUuid_NodeNode_Uuid_TransfertimingImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_TransferintegrityImpl import Context_TopologyUuid_NodeNode_Uuid_TransferintegrityImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuidImpl import Context_ServiceendpointUuidImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_RiskparameterRiskcharacteristicRiskcharacteristicnameImpl import Context_TopologyUuid_LinkLink_Uuid_RiskparameterRiskcharacteristicRiskcharacteristicnameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_TransferintegrityImpl import Context_TopologyUuid_LinkLink_Uuid_TransferintegrityImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuid_LayerprotocolLocalidImpl import Context_ServiceendpointUuid_LayerprotocolLocalidImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_UuidLabelValuenameImpl import Context_TopologyUuid_LinkLink_UuidLabelValuenameImpl
from funcs_Tapi_ObjectClasses.contextLabelValuenameImpl import ContextLabelValuenameImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnconstraintsLatencycharacteristicLatencyvalueImpl import Context_ConnectivityserviceUuid_ConnconstraintsLatencycharacteristicLatencyvalueImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnconstraintsRequestedcapacityImpl import Context_ConnectivityserviceUuid_ConnconstraintsRequestedcapacityImpl
from funcs_Tapi_ObjectClasses.context_VnwserviceUuid_StateImpl import Context_VnwserviceUuid_StateImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuidLabelValuenameImpl import Context_ConnectivityserviceUuidLabelValuenameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_UuidExtensionValuenameImpl import Context_TopologyUuid_NodeNode_UuidExtensionValuenameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_TransfertimingQueuinglatencyLatencyvalueImpl import Context_TopologyUuid_LinkLink_Uuid_TransfertimingQueuinglatencyLatencyvalueImpl
from funcs_Tapi_ObjectClasses.contextImpl import ContextImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuidExtensionValuenameImpl import Context_ServiceendpointUuidExtensionValuenameImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuidLabelValuenameImpl import Context_ServiceendpointUuidLabelValuenameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_TransfercapacityTotalpotentialcapacityImpl import Context_TopologyUuid_NodeNode_Uuid_TransfercapacityTotalpotentialcapacityImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidLabelValuenameImpl import Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidLabelValuenameImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuid_LtpspecdataImpl import Context_ServiceendpointUuid_LtpspecdataImpl
from funcs_Tapi_ObjectClasses.context_VnwserviceUuid_ScheduleImpl import Context_VnwserviceUuid_ScheduleImpl
from funcs_Tapi_ObjectClasses.context_VnwserviceUuidNameValuenameImpl import Context_VnwserviceUuidNameValuenameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_TransfercapacityImpl import Context_TopologyUuid_NodeNode_Uuid_TransfercapacityImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_UuidImpl import Context_TopologyUuid_LinkLink_UuidImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_TransfertimingImpl import Context_TopologyUuid_LinkLink_Uuid_TransfertimingImpl
from funcs_Tapi_ObjectClasses.context_PathUuid_ObjectivefunctionImpl import Context_PathUuid_ObjectivefunctionImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnectionConnection_UuidExtensionValuenameImpl import Context_ConnectivityserviceUuid_ConnectionConnection_UuidExtensionValuenameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_TransfercostCostcharacteristicCostalgorithmImpl import Context_TopologyUuid_LinkLink_Uuid_TransfercostCostcharacteristicCostalgorithmImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_StateImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_StateImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_TransfercostCostcharacteristicCostalgorithmImpl import Context_TopologyUuid_NodeNode_Uuid_TransfercostCostcharacteristicCostalgorithmImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnectionConnection_Uuid_ConnectionportLocalidImpl import Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_ConnectionportLocalidImpl
from funcs_Tapi_ObjectClasses.context_VnwserviceUuidImpl import Context_VnwserviceUuidImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_UuidLabelValuenameImpl import Context_TopologyUuid_NodeNode_UuidLabelValuenameImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnectionConnection_UuidLabelValuenameImpl import Context_ConnectivityserviceUuid_ConnectionConnection_UuidLabelValuenameImpl
from funcs_Tapi_ObjectClasses.context_VnwserviceUuidLabelValuenameImpl import Context_VnwserviceUuidLabelValuenameImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_LayerprotocolLocalidImpl import Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_LayerprotocolLocalidImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidImpl import Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuid_LayerprotocolLocalid_LpspecdataImpl import Context_ServiceendpointUuid_LayerprotocolLocalid_LpspecdataImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_TransfercostImpl import Context_TopologyUuid_NodeNode_Uuid_TransfercostImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LtpspecdataImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LtpspecdataImpl
from funcs_Tapi_ObjectClasses.context_PathUuid_RoutingconstraintRequestedcapacityImpl import Context_PathUuid_RoutingconstraintRequestedcapacityImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnconstraintsRiskcharacteristicRiskcharacteristicnameImpl import Context_ConnectivityserviceUuid_ConnconstraintsRiskcharacteristicRiskcharacteristicnameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_TransfercapacityAvailablecapacityImpl import Context_TopologyUuid_LinkLink_Uuid_TransfercapacityAvailablecapacityImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_ValidationValidationmechanismValidationrobustnessImpl import Context_TopologyUuid_LinkLink_Uuid_ValidationValidationmechanismValidationrobustnessImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnectionConnection_Uuid_StateImpl import Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_StateImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuidExtensionValuenameImpl import Context_TopologyUuidExtensionValuenameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_TransfercapacityCapacityassignedtouserviewNumberingrangeImpl import Context_TopologyUuid_LinkLink_Uuid_TransfercapacityCapacityassignedtouserviewNumberingrangeImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_UuidExtensionValuenameImpl import Context_TopologyUuid_LinkLink_UuidExtensionValuenameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnconstraintsCostcharacteristicCostalgorithmImpl import Context_ConnectivityserviceUuid_ConnconstraintsCostcharacteristicCostalgorithmImpl
from funcs_Tapi_ObjectClasses.context_VnwserviceUuid_VnwconstraintRiskcharacteristicRiskcharacteristicnameImpl import Context_VnwserviceUuid_VnwconstraintRiskcharacteristicRiskcharacteristicnameImpl
from funcs_Tapi_ObjectClasses.context_PathUuid_RoutingconstraintCostcharacteristicCostalgorithmImpl import Context_PathUuid_RoutingconstraintCostcharacteristicCostalgorithmImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuidNameValuenameImpl import Context_ConnectivityserviceUuidNameValuenameImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuidExtensionValuenameImpl import Context_ConnectivityserviceUuidExtensionValuenameImpl
from funcs_Tapi_ObjectClasses.context_PathUuid_RoutingconstraintLatencycharacteristicLatencyvalueImpl import Context_PathUuid_RoutingconstraintLatencycharacteristicLatencyvalueImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_StateImpl import Context_ConnectivityserviceUuid_StateImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_ValidationImpl import Context_TopologyUuid_LinkLink_Uuid_ValidationImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuidImpl import Context_TopologyUuidImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnectionConnection_UuidImpl import Context_ConnectivityserviceUuid_ConnectionConnection_UuidImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidLabelValuenameImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidLabelValuenameImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ServiceportLocalidImpl import Context_ConnectivityserviceUuid_ServiceportLocalidImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_TransfercapacityTotalpotentialcapacityImpl import Context_TopologyUuid_LinkLink_Uuid_TransfercapacityTotalpotentialcapacityImpl
from funcs_Tapi_ObjectClasses.context_VnwserviceUuidExtensionValuenameImpl import Context_VnwserviceUuidExtensionValuenameImpl
from funcs_Tapi_ObjectClasses.context_PathUuidNameValuenameImpl import Context_PathUuidNameValuenameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidExtensionValuenameImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidExtensionValuenameImpl
from funcs_Tapi_ObjectClasses.context_VnwserviceUuid_VnwconstraintRequestedcapacityImpl import Context_VnwserviceUuid_VnwconstraintRequestedcapacityImpl
from funcs_Tapi_ObjectClasses.context_VnwserviceUuid_VnwconstraintImpl import Context_VnwserviceUuid_VnwconstraintImpl
from funcs_Tapi_ObjectClasses.context_PathUuid_TelinkLocalidImpl import Context_PathUuid_TelinkLocalidImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_TransfercapacityCapacityassignedtouserviewNumberingrangeImpl import Context_TopologyUuid_NodeNode_Uuid_TransfercapacityCapacityassignedtouserviewNumberingrangeImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_TransfercostImpl import Context_TopologyUuid_LinkLink_Uuid_TransfercostImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_TransfercapacityImpl import Context_TopologyUuid_LinkLink_Uuid_TransfercapacityImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_UuidNameValuenameImpl import Context_TopologyUuid_LinkLink_UuidNameValuenameImpl
from funcs_Tapi_ObjectClasses.context_PathUuid_RoutingconstraintRiskcharacteristicRiskcharacteristicnameImpl import Context_PathUuid_RoutingconstraintRiskcharacteristicRiskcharacteristicnameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuidNameValuenameImpl import Context_TopologyUuidNameValuenameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalid_LpspecdataImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalid_LpspecdataImpl
from funcs_Tapi_ObjectClasses.context_VnwserviceUuid_VnwconstraintLatencycharacteristicLatencyvalueImpl import Context_VnwserviceUuid_VnwconstraintLatencycharacteristicLatencyvalueImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_UuidImpl import Context_TopologyUuid_NodeNode_UuidImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_LtpspecdataImpl import Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_LtpspecdataImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_RiskparameterImpl import Context_TopologyUuid_LinkLink_Uuid_RiskparameterImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_LayerprotocolLocalid_LpspecdataImpl import Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_LayerprotocolLocalid_LpspecdataImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_StateImpl import Context_TopologyUuid_LinkLink_Uuid_StateImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuid_ConnconstraintsImpl import Context_ConnectivityserviceUuid_ConnconstraintsImpl
from funcs_Tapi_ObjectClasses.context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidNameValuenameImpl import Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidNameValuenameImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidNameValuenameImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidNameValuenameImpl
from funcs_Tapi_ObjectClasses.context_ConnectivityserviceUuidImpl import Context_ConnectivityserviceUuidImpl
from funcs_Tapi_ObjectClasses.context_TopologyUuid_LinkLink_Uuid_LinkportLocalidImpl import Context_TopologyUuid_LinkLink_Uuid_LinkportLocalidImpl

# CALLABLE OBJECTS
from objects_Tapi_ObjectClasses.linkPort import LinkPort
from objects_Tapi_ObjectClasses.virtualNetworkServicePort import VirtualNetworkServicePort
from objects_Tapi_ObjectClasses.capacity import Capacity
from objects_Tapi_ObjectClasses.transferCostPac import TransferCostPac
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
from objects_Tapi_ObjectClasses.connectivityService import ConnectivityService
from objects_Tapi_ObjectClasses.connectionPort import ConnectionPort
from objects_Tapi_ObjectClasses.ltpSpec import LtpSpec
from objects_Tapi_ObjectClasses.connectionEndPoint import ConnectionEndPoint
from objects_Tapi_ObjectClasses.link import Link
from objects_Tapi_ObjectClasses.localClass import LocalClass
from objects_Tapi_ObjectClasses.path import Path
from objects_Tapi_ObjectClasses.topology import Topology
from objects_Tapi_ObjectClasses.queuingLatency import QueuingLatency
from objects_Tapi_ObjectClasses.connectivityConstraint import ConnectivityConstraint
from objects_Tapi_ObjectClasses.virtualNetworkService import VirtualNetworkService
from objects_Tapi_ObjectClasses.route import Route
from objects_Tapi_ObjectClasses.contextSchema import ContextSchema
from objects_Tapi_ObjectClasses.connection import Connection
from objects_Tapi_ObjectClasses.scheduleInfo import ScheduleInfo
from objects_Tapi_ObjectClasses.pathOptimizationConstraint import PathOptimizationConstraint
from objects_Tapi_ObjectClasses.pathObjectiveFunction import PathObjectiveFunction
from objects_Tapi_ObjectClasses.virtualNetworkConstraint import VirtualNetworkConstraint
from objects_Tapi_ObjectClasses.riskCharacteristic import RiskCharacteristic
from objects_Tapi_ObjectClasses.riskParameterPac import RiskParameterPac
from objects_Tapi_ObjectClasses.connectivityServicePort import ConnectivityServicePort
from objects_Tapi_ObjectClasses.operationalStatePac import OperationalStatePac
from objects_Tapi_ObjectClasses.globalClass import GlobalClass
from objects_Tapi_ObjectClasses.layerProtocol import LayerProtocol
from objects_Tapi_ObjectClasses.transferCapacityPac import TransferCapacityPac
from objects_Tapi_ObjectClasses.nodeEdgePoint import NodeEdgePoint
from objects_Tapi_ObjectClasses.lpSpec import LpSpec
from objects_Tapi_ObjectClasses.lifecycleStatePac import LifecycleStatePac
from objects_Tapi_ObjectClasses.validationPac import ValidationPac

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


#/restconf/config/Context/extension/(\w+)/
class ContextExtensionValuename(MethodView):

    def get(self, valueName):
        print "Retrieve operation of resource: extension"
        try:
            response = ContextExtensionValuenameImpl.get(valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_path/(\w+)/label/(\w+)/
class Context_PathUuidLabelValuename(MethodView):

    def get(self, uuid, valueName):
        print "Retrieve operation of resource: label"
        try:
            response = Context_PathUuidLabelValuenameImpl.get(uuid, valueName)
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

    def get(self, valueName):
        print "Retrieve operation of resource: name"
        try:
            response = ContextNameValuenameImpl.get(valueName)
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


#/restconf/config/Context/_serviceEndPoint/(\w+)/_connectionEndPoint/(\w+)/extension/(\w+)/
class Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidExtensionValuename(MethodView):

    def get(self, uuid, connectionEndPoint_uuid, valueName):
        print "Retrieve operation of resource: extension"
        try:
            response = Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidExtensionValuenameImpl.get(uuid, connectionEndPoint_uuid, valueName)
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

            new_object = create_instance(ScheduleInfo, json_struct)
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
            new_object = create_instance(ScheduleInfo, json_struct)
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


#/restconf/config/Context/_path/(\w+)/_routingConstraint/
class Context_PathUuid_Routingconstraint(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _routingConstraint"
        try:
            response = Context_PathUuid_RoutingconstraintImpl.get(uuid)
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


#/restconf/config/Context/_path/(\w+)/_optimizationConstraint/
class Context_PathUuid_Optimizationconstraint(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _optimizationConstraint"
        try:
            response = Context_PathUuid_OptimizationconstraintImpl.get(uuid)
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


#/restconf/config/Context/_path/(\w+)/
class Context_PathUuid(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _path"
        try:
            response = Context_PathUuidImpl.get(uuid)
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


#/restconf/config/Context/_path/(\w+)/extension/(\w+)/
class Context_PathUuidExtensionValuename(MethodView):

    def get(self, uuid, valueName):
        print "Retrieve operation of resource: extension"
        try:
            response = Context_PathUuidExtensionValuenameImpl.get(uuid, valueName)
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


#/restconf/config/Context/label/(\w+)/
class ContextLabelValuename(MethodView):

    def get(self, valueName):
        print "Retrieve operation of resource: label"
        try:
            response = ContextLabelValuenameImpl.get(valueName)
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


#/restconf/config/Context/_connectivityService/(\w+)/label/(\w+)/
class Context_ConnectivityserviceUuidLabelValuename(MethodView):

    def get(self, uuid, valueName):
        print "Retrieve operation of resource: label"
        try:
            response = Context_ConnectivityserviceUuidLabelValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/extension/(\w+)/
class Context_TopologyUuid_NodeNode_UuidExtensionValuename(MethodView):

    def get(self, uuid, node_uuid, valueName):
        print "Retrieve operation of resource: extension"
        try:
            response = Context_TopologyUuid_NodeNode_UuidExtensionValuenameImpl.get(uuid, node_uuid, valueName)
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


#/restconf/config/Context/_serviceEndPoint/(\w+)/extension/(\w+)/
class Context_ServiceendpointUuidExtensionValuename(MethodView):

    def get(self, uuid, valueName):
        print "Retrieve operation of resource: extension"
        try:
            response = Context_ServiceendpointUuidExtensionValuenameImpl.get(uuid, valueName)
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

            new_object = create_instance(ScheduleInfo, json_struct)
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
            new_object = create_instance(ScheduleInfo, json_struct)
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


#/restconf/config/Context/_vnwService/(\w+)/name/(\w+)/
class Context_VnwserviceUuidNameValuename(MethodView):

    def get(self, uuid, valueName):
        print "Retrieve operation of resource: name"
        try:
            response = Context_VnwserviceUuidNameValuenameImpl.get(uuid, valueName)
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


#/restconf/config/Context/_path/(\w+)/_objectiveFunction/
class Context_PathUuid_Objectivefunction(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _objectiveFunction"
        try:
            response = Context_PathUuid_ObjectivefunctionImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connection/(\w+)/extension/(\w+)/
class Context_ConnectivityserviceUuid_ConnectionConnection_UuidExtensionValuename(MethodView):

    def get(self, uuid, connection_uuid, valueName):
        print "Retrieve operation of resource: extension"
        try:
            response = Context_ConnectivityserviceUuid_ConnectionConnection_UuidExtensionValuenameImpl.get(uuid, connection_uuid, valueName)
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


#/restconf/config/Context/_vnwService/(\w+)/label/(\w+)/
class Context_VnwserviceUuidLabelValuename(MethodView):

    def get(self, uuid, valueName):
        print "Retrieve operation of resource: label"
        try:
            response = Context_VnwserviceUuidLabelValuenameImpl.get(uuid, valueName)
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


#/restconf/config/Context/_path/(\w+)/_routingConstraint/requestedCapacity/
class Context_PathUuid_RoutingconstraintRequestedcapacity(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: requestedCapacity"
        try:
            response = Context_PathUuid_RoutingconstraintRequestedcapacityImpl.get(uuid)
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


#/restconf/config/Context/_topology/(\w+)/extension/(\w+)/
class Context_TopologyUuidExtensionValuename(MethodView):

    def get(self, uuid, valueName):
        print "Retrieve operation of resource: extension"
        try:
            response = Context_TopologyUuidExtensionValuenameImpl.get(uuid, valueName)
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


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/extension/(\w+)/
class Context_TopologyUuid_LinkLink_UuidExtensionValuename(MethodView):

    def get(self, uuid, link_uuid, valueName):
        print "Retrieve operation of resource: extension"
        try:
            response = Context_TopologyUuid_LinkLink_UuidExtensionValuenameImpl.get(uuid, link_uuid, valueName)
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


#/restconf/config/Context/_path/(\w+)/_routingConstraint/costCharacteristic/(\w+)/
class Context_PathUuid_RoutingconstraintCostcharacteristicCostalgorithm(MethodView):

    def get(self, uuid, costAlgorithm):
        print "Retrieve operation of resource: costCharacteristic"
        try:
            response = Context_PathUuid_RoutingconstraintCostcharacteristicCostalgorithmImpl.get(uuid, costAlgorithm)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/name/(\w+)/
class Context_ConnectivityserviceUuidNameValuename(MethodView):

    def get(self, uuid, valueName):
        print "Retrieve operation of resource: name"
        try:
            response = Context_ConnectivityserviceUuidNameValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/extension/(\w+)/
class Context_ConnectivityserviceUuidExtensionValuename(MethodView):

    def get(self, uuid, valueName):
        print "Retrieve operation of resource: extension"
        try:
            response = Context_ConnectivityserviceUuidExtensionValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_path/(\w+)/_routingConstraint/latencyCharacteristic/(\w+)/
class Context_PathUuid_RoutingconstraintLatencycharacteristicLatencyvalue(MethodView):

    def get(self, uuid, latencyValue):
        print "Retrieve operation of resource: latencyCharacteristic"
        try:
            response = Context_PathUuid_RoutingconstraintLatencycharacteristicLatencyvalueImpl.get(uuid, latencyValue)
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


#/restconf/config/Context/_vnwService/(\w+)/extension/(\w+)/
class Context_VnwserviceUuidExtensionValuename(MethodView):

    def get(self, uuid, valueName):
        print "Retrieve operation of resource: extension"
        try:
            response = Context_VnwserviceUuidExtensionValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_path/(\w+)/name/(\w+)/
class Context_PathUuidNameValuename(MethodView):

    def get(self, uuid, valueName):
        print "Retrieve operation of resource: name"
        try:
            response = Context_PathUuidNameValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_ownedNodeEdgePoint/(\w+)/extension/(\w+)/
class Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidExtensionValuename(MethodView):

    def get(self, uuid, node_uuid, ownedNodeEdgePoint_uuid, valueName):
        print "Retrieve operation of resource: extension"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidExtensionValuenameImpl.get(uuid, node_uuid, ownedNodeEdgePoint_uuid, valueName)
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


#/restconf/config/Context/_path/(\w+)/_telink/(\w+)/
class Context_PathUuid_TelinkLocalid(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _telink"
        try:
            response = Context_PathUuid_TelinkLocalidImpl.get(uuid, localId)
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


#/restconf/config/Context/_path/(\w+)/_routingConstraint/riskCharacteristic/(\w+)/
class Context_PathUuid_RoutingconstraintRiskcharacteristicRiskcharacteristicname(MethodView):

    def get(self, uuid, riskCharacteristicName):
        print "Retrieve operation of resource: riskCharacteristic"
        try:
            response = Context_PathUuid_RoutingconstraintRiskcharacteristicRiskcharacteristicnameImpl.get(uuid, riskCharacteristicName)
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



getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/extension/<valueName>/", view_func = globals()["ContextExtensionValuename"].as_view('"ContextExtensionValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/label/<valueName>/", view_func = globals()["Context_PathUuidLabelValuename"].as_view('"Context_PathUuidLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/<ownedNodeEdgePoint_uuid>/_layerProtocol/<localId>/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalid"].as_view('"Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/name/<valueName>/", view_func = globals()["ContextNameValuename"].as_view('"ContextNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_vnwConstraint/costCharacteristic/<costAlgorithm>/", view_func = globals()["Context_VnwserviceUuid_VnwconstraintCostcharacteristicCostalgorithm"].as_view('"Context_VnwserviceUuid_VnwconstraintCostcharacteristicCostalgorithm"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_connectionEndPoint/<connectionEndPoint_uuid>/_state/", view_func = globals()["Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_State"].as_view('"Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_State"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_connectionEndPoint/<connectionEndPoint_uuid>/extension/<valueName>/", view_func = globals()["Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidExtensionValuename"].as_view('"Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidExtensionValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_schedule/", view_func = globals()["Context_ConnectivityserviceUuid_Schedule"].as_view('"Context_ConnectivityserviceUuid_Schedule"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_routingConstraint/", view_func = globals()["Context_PathUuid_Routingconstraint"].as_view('"Context_PathUuid_Routingconstraint"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/name/<valueName>/", view_func = globals()["Context_TopologyUuid_NodeNode_UuidNameValuename"].as_view('"Context_TopologyUuid_NodeNode_UuidNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connection/<connection_uuid>/_route/<localId>/", view_func = globals()["Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_RouteLocalid"].as_view('"Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_RouteLocalid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/name/<valueName>/", view_func = globals()["Context_ServiceendpointUuidNameValuename"].as_view('"Context_ServiceendpointUuidNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_state/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_State"].as_view('"Context_TopologyUuid_NodeNode_Uuid_State"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_lpTransition/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_Lptransition"].as_view('"Context_TopologyUuid_LinkLink_Uuid_Lptransition"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferTiming/queuingLatency/<latencyValue>/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_TransfertimingQueuinglatencyLatencyvalue"].as_view('"Context_TopologyUuid_NodeNode_Uuid_TransfertimingQueuinglatencyLatencyvalue"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_optimizationConstraint/", view_func = globals()["Context_PathUuid_Optimizationconstraint"].as_view('"Context_PathUuid_Optimizationconstraint"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connection/<connection_uuid>/name/<valueName>/", view_func = globals()["Context_ConnectivityserviceUuid_ConnectionConnection_UuidNameValuename"].as_view('"Context_ConnectivityserviceUuid_ConnectionConnection_UuidNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/", view_func = globals()["Context_PathUuid"].as_view('"Context_PathUuid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_servicePort/<localId>/", view_func = globals()["Context_VnwserviceUuid_ServiceportLocalid"].as_view('"Context_VnwserviceUuid_ServiceportLocalid"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/extension/<valueName>/", view_func = globals()["Context_PathUuidExtensionValuename"].as_view('"Context_PathUuidExtensionValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_state/", view_func = globals()["Context_ServiceendpointUuid_State"].as_view('"Context_ServiceendpointUuid_State"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferCapacity/availableCapacity/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_TransfercapacityAvailablecapacity"].as_view('"Context_TopologyUuid_NodeNode_Uuid_TransfercapacityAvailablecapacity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/label/<valueName>/", view_func = globals()["Context_TopologyUuidLabelValuename"].as_view('"Context_TopologyUuidLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferTiming/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_Transfertiming"].as_view('"Context_TopologyUuid_NodeNode_Uuid_Transfertiming"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferIntegrity/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_Transferintegrity"].as_view('"Context_TopologyUuid_NodeNode_Uuid_Transferintegrity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/", view_func = globals()["Context_ServiceendpointUuid"].as_view('"Context_ServiceendpointUuid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_riskParameter/riskCharacteristic/<riskCharacteristicName>/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_RiskparameterRiskcharacteristicRiskcharacteristicname"].as_view('"Context_TopologyUuid_LinkLink_Uuid_RiskparameterRiskcharacteristicRiskcharacteristicname"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferIntegrity/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_Transferintegrity"].as_view('"Context_TopologyUuid_LinkLink_Uuid_Transferintegrity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_layerProtocol/<localId>/", view_func = globals()["Context_ServiceendpointUuid_LayerprotocolLocalid"].as_view('"Context_ServiceendpointUuid_LayerprotocolLocalid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/label/<valueName>/", view_func = globals()["Context_TopologyUuid_LinkLink_UuidLabelValuename"].as_view('"Context_TopologyUuid_LinkLink_UuidLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/label/<valueName>/", view_func = globals()["ContextLabelValuename"].as_view('"ContextLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connConstraints/latencyCharacteristic/<latencyValue>/", view_func = globals()["Context_ConnectivityserviceUuid_ConnconstraintsLatencycharacteristicLatencyvalue"].as_view('"Context_ConnectivityserviceUuid_ConnconstraintsLatencycharacteristicLatencyvalue"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connConstraints/requestedCapacity/", view_func = globals()["Context_ConnectivityserviceUuid_ConnconstraintsRequestedcapacity"].as_view('"Context_ConnectivityserviceUuid_ConnconstraintsRequestedcapacity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_state/", view_func = globals()["Context_VnwserviceUuid_State"].as_view('"Context_VnwserviceUuid_State"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/label/<valueName>/", view_func = globals()["Context_ConnectivityserviceUuidLabelValuename"].as_view('"Context_ConnectivityserviceUuidLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/extension/<valueName>/", view_func = globals()["Context_TopologyUuid_NodeNode_UuidExtensionValuename"].as_view('"Context_TopologyUuid_NodeNode_UuidExtensionValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferTiming/queuingLatency/<latencyValue>/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_TransfertimingQueuinglatencyLatencyvalue"].as_view('"Context_TopologyUuid_LinkLink_Uuid_TransfertimingQueuinglatencyLatencyvalue"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/", view_func = globals()["Context"].as_view('"Context"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/extension/<valueName>/", view_func = globals()["Context_ServiceendpointUuidExtensionValuename"].as_view('"Context_ServiceendpointUuidExtensionValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/label/<valueName>/", view_func = globals()["Context_ServiceendpointUuidLabelValuename"].as_view('"Context_ServiceendpointUuidLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferCapacity/totalPotentialCapacity/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_TransfercapacityTotalpotentialcapacity"].as_view('"Context_TopologyUuid_NodeNode_Uuid_TransfercapacityTotalpotentialcapacity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_connectionEndPoint/<connectionEndPoint_uuid>/label/<valueName>/", view_func = globals()["Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidLabelValuename"].as_view('"Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_ltpSpecData/", view_func = globals()["Context_ServiceendpointUuid_Ltpspecdata"].as_view('"Context_ServiceendpointUuid_Ltpspecdata"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_schedule/", view_func = globals()["Context_VnwserviceUuid_Schedule"].as_view('"Context_VnwserviceUuid_Schedule"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/name/<valueName>/", view_func = globals()["Context_VnwserviceUuidNameValuename"].as_view('"Context_VnwserviceUuidNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferCapacity/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_Transfercapacity"].as_view('"Context_TopologyUuid_NodeNode_Uuid_Transfercapacity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid"].as_view('"Context_TopologyUuid_LinkLink_Uuid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferTiming/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_Transfertiming"].as_view('"Context_TopologyUuid_LinkLink_Uuid_Transfertiming"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_objectiveFunction/", view_func = globals()["Context_PathUuid_Objectivefunction"].as_view('"Context_PathUuid_Objectivefunction"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connection/<connection_uuid>/extension/<valueName>/", view_func = globals()["Context_ConnectivityserviceUuid_ConnectionConnection_UuidExtensionValuename"].as_view('"Context_ConnectivityserviceUuid_ConnectionConnection_UuidExtensionValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferCost/costCharacteristic/<costAlgorithm>/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_TransfercostCostcharacteristicCostalgorithm"].as_view('"Context_TopologyUuid_LinkLink_Uuid_TransfercostCostcharacteristicCostalgorithm"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/<ownedNodeEdgePoint_uuid>/_state/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_State"].as_view('"Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_State"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferCost/costCharacteristic/<costAlgorithm>/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_TransfercostCostcharacteristicCostalgorithm"].as_view('"Context_TopologyUuid_NodeNode_Uuid_TransfercostCostcharacteristicCostalgorithm"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connection/<connection_uuid>/_connectionPort/<localId>/", view_func = globals()["Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_ConnectionportLocalid"].as_view('"Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_ConnectionportLocalid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/", view_func = globals()["Context_VnwserviceUuid"].as_view('"Context_VnwserviceUuid"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/label/<valueName>/", view_func = globals()["Context_TopologyUuid_NodeNode_UuidLabelValuename"].as_view('"Context_TopologyUuid_NodeNode_UuidLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connection/<connection_uuid>/label/<valueName>/", view_func = globals()["Context_ConnectivityserviceUuid_ConnectionConnection_UuidLabelValuename"].as_view('"Context_ConnectivityserviceUuid_ConnectionConnection_UuidLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/label/<valueName>/", view_func = globals()["Context_VnwserviceUuidLabelValuename"].as_view('"Context_VnwserviceUuidLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_connectionEndPoint/<connectionEndPoint_uuid>/_layerProtocol/<localId>/", view_func = globals()["Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_LayerprotocolLocalid"].as_view('"Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_LayerprotocolLocalid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_connectionEndPoint/<connectionEndPoint_uuid>/", view_func = globals()["Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid"].as_view('"Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_layerProtocol/<localId>/_lpSpecData/", view_func = globals()["Context_ServiceendpointUuid_LayerprotocolLocalid_Lpspecdata"].as_view('"Context_ServiceendpointUuid_LayerprotocolLocalid_Lpspecdata"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferCost/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_Transfercost"].as_view('"Context_TopologyUuid_NodeNode_Uuid_Transfercost"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/<ownedNodeEdgePoint_uuid>/_ltpSpecData/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_Ltpspecdata"].as_view('"Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_Ltpspecdata"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_routingConstraint/requestedCapacity/", view_func = globals()["Context_PathUuid_RoutingconstraintRequestedcapacity"].as_view('"Context_PathUuid_RoutingconstraintRequestedcapacity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connConstraints/riskCharacteristic/<riskCharacteristicName>/", view_func = globals()["Context_ConnectivityserviceUuid_ConnconstraintsRiskcharacteristicRiskcharacteristicname"].as_view('"Context_ConnectivityserviceUuid_ConnconstraintsRiskcharacteristicRiskcharacteristicname"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferCapacity/availableCapacity/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_TransfercapacityAvailablecapacity"].as_view('"Context_TopologyUuid_LinkLink_Uuid_TransfercapacityAvailablecapacity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_validation/validationMechanism/<validationRobustness>/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_ValidationValidationmechanismValidationrobustness"].as_view('"Context_TopologyUuid_LinkLink_Uuid_ValidationValidationmechanismValidationrobustness"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connection/<connection_uuid>/_state/", view_func = globals()["Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_State"].as_view('"Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_State"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/extension/<valueName>/", view_func = globals()["Context_TopologyUuidExtensionValuename"].as_view('"Context_TopologyUuidExtensionValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferCapacity/capacityAssignedToUserView/<numberingRange>/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_TransfercapacityCapacityassignedtouserviewNumberingrange"].as_view('"Context_TopologyUuid_LinkLink_Uuid_TransfercapacityCapacityassignedtouserviewNumberingrange"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/extension/<valueName>/", view_func = globals()["Context_TopologyUuid_LinkLink_UuidExtensionValuename"].as_view('"Context_TopologyUuid_LinkLink_UuidExtensionValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/<ownedNodeEdgePoint_uuid>/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid"].as_view('"Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connConstraints/costCharacteristic/<costAlgorithm>/", view_func = globals()["Context_ConnectivityserviceUuid_ConnconstraintsCostcharacteristicCostalgorithm"].as_view('"Context_ConnectivityserviceUuid_ConnconstraintsCostcharacteristicCostalgorithm"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_vnwConstraint/riskCharacteristic/<riskCharacteristicName>/", view_func = globals()["Context_VnwserviceUuid_VnwconstraintRiskcharacteristicRiskcharacteristicname"].as_view('"Context_VnwserviceUuid_VnwconstraintRiskcharacteristicRiskcharacteristicname"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_routingConstraint/costCharacteristic/<costAlgorithm>/", view_func = globals()["Context_PathUuid_RoutingconstraintCostcharacteristicCostalgorithm"].as_view('"Context_PathUuid_RoutingconstraintCostcharacteristicCostalgorithm"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/name/<valueName>/", view_func = globals()["Context_ConnectivityserviceUuidNameValuename"].as_view('"Context_ConnectivityserviceUuidNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/extension/<valueName>/", view_func = globals()["Context_ConnectivityserviceUuidExtensionValuename"].as_view('"Context_ConnectivityserviceUuidExtensionValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_routingConstraint/latencyCharacteristic/<latencyValue>/", view_func = globals()["Context_PathUuid_RoutingconstraintLatencycharacteristicLatencyvalue"].as_view('"Context_PathUuid_RoutingconstraintLatencycharacteristicLatencyvalue"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_state/", view_func = globals()["Context_ConnectivityserviceUuid_State"].as_view('"Context_ConnectivityserviceUuid_State"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_validation/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_Validation"].as_view('"Context_TopologyUuid_LinkLink_Uuid_Validation"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/", view_func = globals()["Context_TopologyUuid"].as_view('"Context_TopologyUuid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connection/<connection_uuid>/", view_func = globals()["Context_ConnectivityserviceUuid_ConnectionConnection_Uuid"].as_view('"Context_ConnectivityserviceUuid_ConnectionConnection_Uuid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/<ownedNodeEdgePoint_uuid>/label/<valueName>/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidLabelValuename"].as_view('"Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_servicePort/<localId>/", view_func = globals()["Context_ConnectivityserviceUuid_ServiceportLocalid"].as_view('"Context_ConnectivityserviceUuid_ServiceportLocalid"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferCapacity/totalPotentialCapacity/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_TransfercapacityTotalpotentialcapacity"].as_view('"Context_TopologyUuid_LinkLink_Uuid_TransfercapacityTotalpotentialcapacity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/extension/<valueName>/", view_func = globals()["Context_VnwserviceUuidExtensionValuename"].as_view('"Context_VnwserviceUuidExtensionValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/name/<valueName>/", view_func = globals()["Context_PathUuidNameValuename"].as_view('"Context_PathUuidNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/<ownedNodeEdgePoint_uuid>/extension/<valueName>/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidExtensionValuename"].as_view('"Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidExtensionValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_vnwConstraint/requestedCapacity/", view_func = globals()["Context_VnwserviceUuid_VnwconstraintRequestedcapacity"].as_view('"Context_VnwserviceUuid_VnwconstraintRequestedcapacity"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_vnwConstraint/", view_func = globals()["Context_VnwserviceUuid_Vnwconstraint"].as_view('"Context_VnwserviceUuid_Vnwconstraint"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_telink/<localId>/", view_func = globals()["Context_PathUuid_TelinkLocalid"].as_view('"Context_PathUuid_TelinkLocalid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferCapacity/capacityAssignedToUserView/<numberingRange>/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_TransfercapacityCapacityassignedtouserviewNumberingrange"].as_view('"Context_TopologyUuid_NodeNode_Uuid_TransfercapacityCapacityassignedtouserviewNumberingrange"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferCost/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_Transfercost"].as_view('"Context_TopologyUuid_LinkLink_Uuid_Transfercost"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferCapacity/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_Transfercapacity"].as_view('"Context_TopologyUuid_LinkLink_Uuid_Transfercapacity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/name/<valueName>/", view_func = globals()["Context_TopologyUuid_LinkLink_UuidNameValuename"].as_view('"Context_TopologyUuid_LinkLink_UuidNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_routingConstraint/riskCharacteristic/<riskCharacteristicName>/", view_func = globals()["Context_PathUuid_RoutingconstraintRiskcharacteristicRiskcharacteristicname"].as_view('"Context_PathUuid_RoutingconstraintRiskcharacteristicRiskcharacteristicname"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/name/<valueName>/", view_func = globals()["Context_TopologyUuidNameValuename"].as_view('"Context_TopologyUuidNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/<ownedNodeEdgePoint_uuid>/_layerProtocol/<localId>/_lpSpecData/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalid_Lpspecdata"].as_view('"Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalid_Lpspecdata"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_vnwConstraint/latencyCharacteristic/<latencyValue>/", view_func = globals()["Context_VnwserviceUuid_VnwconstraintLatencycharacteristicLatencyvalue"].as_view('"Context_VnwserviceUuid_VnwconstraintLatencycharacteristicLatencyvalue"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid"].as_view('"Context_TopologyUuid_NodeNode_Uuid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_connectionEndPoint/<connectionEndPoint_uuid>/_ltpSpecData/", view_func = globals()["Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_Ltpspecdata"].as_view('"Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_Ltpspecdata"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_riskParameter/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_Riskparameter"].as_view('"Context_TopologyUuid_LinkLink_Uuid_Riskparameter"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_connectionEndPoint/<connectionEndPoint_uuid>/_layerProtocol/<localId>/_lpSpecData/", view_func = globals()["Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_LayerprotocolLocalid_Lpspecdata"].as_view('"Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_LayerprotocolLocalid_Lpspecdata"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_state/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_State"].as_view('"Context_TopologyUuid_LinkLink_Uuid_State"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connConstraints/", view_func = globals()["Context_ConnectivityserviceUuid_Connconstraints"].as_view('"Context_ConnectivityserviceUuid_Connconstraints"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_connectionEndPoint/<connectionEndPoint_uuid>/name/<valueName>/", view_func = globals()["Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidNameValuename"].as_view('"Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_UuidNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/<ownedNodeEdgePoint_uuid>/name/<valueName>/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidNameValuename"].as_view('"Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/", view_func = globals()["Context_ConnectivityserviceUuid"].as_view('"Context_ConnectivityserviceUuid"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_linkPort/<localId>/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_LinkportLocalid"].as_view('"Context_TopologyUuid_LinkLink_Uuid_LinkportLocalid"'+'"_api"'), methods=['GET'])
