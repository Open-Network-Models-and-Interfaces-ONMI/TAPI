from flask import json, Blueprint, request, Response
from flask.views import MethodView
import sys
from objects_common.keyedArrayType import KeyedArrayKeyError

import base64
import re

# BACKEND FUNCTIONS
from funcs_TapiTopology.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidNameImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidNameImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_Uuid_TransfercapacityImpl import Context_TopologyUuid_LinkLink_Uuid_TransfercapacityImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_Uuid_TransfercapacityCapacityassignedtouserviewImpl import Context_TopologyUuid_LinkLink_Uuid_TransfercapacityCapacityassignedtouserviewImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_Uuid_TransfercapacityTotalpotentialcapacityImpl import Context_TopologyUuid_LinkLink_Uuid_TransfercapacityTotalpotentialcapacityImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_Uuid_RiskparameterRiskcharacteristicImpl import Context_TopologyUuid_LinkLink_Uuid_RiskparameterRiskcharacteristicImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_Uuid_TransfercapacityCapacityassignedtouserviewImpl import Context_TopologyUuid_NodeNode_Uuid_TransfercapacityCapacityassignedtouserviewImpl
from funcs_TapiTopology.context_TopologyUuidNameValuenameImpl import Context_TopologyUuidNameValuenameImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_Uuid_TransfercostCostcharacteristicCostnameImpl import Context_TopologyUuid_LinkLink_Uuid_TransfercostCostcharacteristicCostnameImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_UuidNameValuenameImpl import Context_TopologyUuid_LinkLink_UuidNameValuenameImpl
from funcs_TapiTopology.context_TopologyUuidNameImpl import Context_TopologyUuidNameImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_Uuid_ExtensionsExtensionsspecificationImpl import Context_TopologyUuid_LinkLink_Uuid_ExtensionsExtensionsspecificationImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_Uuid_LinkportLocalid_ExtensionsExtensionsspecificationImpl import Context_TopologyUuid_LinkLink_Uuid_LinkportLocalid_ExtensionsExtensionsspecificationImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_Uuid_StateImpl import Context_TopologyUuid_NodeNode_Uuid_StateImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_Uuid_TransfertimingLatencycharacteristicTrafficpropertynameImpl import Context_TopologyUuid_NodeNode_Uuid_TransfertimingLatencycharacteristicTrafficpropertynameImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_UuidLabelImpl import Context_TopologyUuid_NodeNode_UuidLabelImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_Uuid_LptransitionImpl import Context_TopologyUuid_LinkLink_Uuid_LptransitionImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_ExtensionsImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_ExtensionsImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_Uuid_ExtensionsExtensionsspecificationImpl import Context_TopologyUuid_NodeNode_Uuid_ExtensionsExtensionsspecificationImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_ExtensionsExtensionsspecificationImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_ExtensionsExtensionsspecificationImpl
from funcs_TapiTopology.context_NwtopologyserviceLabelValuenameImpl import Context_NwtopologyserviceLabelValuenameImpl
from funcs_TapiTopology.context_TopologyUuidLabelImpl import Context_TopologyUuidLabelImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidLabelImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidLabelImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_Uuid_TransfertimingLatencycharacteristicTrafficpropertynameImpl import Context_TopologyUuid_LinkLink_Uuid_TransfertimingLatencycharacteristicTrafficpropertynameImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_Uuid_TransfercapacityAvailablecapacityImpl import Context_TopologyUuid_LinkLink_Uuid_TransfercapacityAvailablecapacityImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_Uuid_TransfercapacityCapacityassignedtouserviewTotalsizeImpl import Context_TopologyUuid_NodeNode_Uuid_TransfercapacityCapacityassignedtouserviewTotalsizeImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_Uuid_TransfercapacityImpl import Context_TopologyUuid_NodeNode_Uuid_TransfercapacityImpl
from funcs_TapiTopology.getnodedetailsImpl import GetnodedetailsImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_UuidImpl import Context_TopologyUuid_LinkLink_UuidImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_Uuid_TransfercapacityTotalpotentialcapacityImpl import Context_TopologyUuid_NodeNode_Uuid_TransfercapacityTotalpotentialcapacityImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_Uuid_TransfertimingLatencycharacteristicImpl import Context_TopologyUuid_LinkLink_Uuid_TransfertimingLatencycharacteristicImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_Uuid_TransfertimingImpl import Context_TopologyUuid_LinkLink_Uuid_TransfertimingImpl
from funcs_TapiTopology.context_TopologyUuid_NodeImpl import Context_TopologyUuid_NodeImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalid_ExtensionsExtensionsspecificationImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalid_ExtensionsExtensionsspecificationImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_Uuid_RiskparameterImpl import Context_TopologyUuid_LinkLink_Uuid_RiskparameterImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_Uuid_StateImpl import Context_TopologyUuid_LinkLink_Uuid_StateImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_Uuid_RiskparameterRiskcharacteristicRiskcharacteristicnameImpl import Context_TopologyUuid_LinkLink_Uuid_RiskparameterRiskcharacteristicRiskcharacteristicnameImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_Uuid_TransferintegrityImpl import Context_TopologyUuid_LinkLink_Uuid_TransferintegrityImpl
from funcs_TapiTopology.context_TopologyUuid_ExtensionsExtensionsspecificationImpl import Context_TopologyUuid_ExtensionsExtensionsspecificationImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_Uuid_TransfercapacityCapacityassignedtouserviewTotalsizeImpl import Context_TopologyUuid_LinkLink_Uuid_TransfercapacityCapacityassignedtouserviewTotalsizeImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_Uuid_LinkportImpl import Context_TopologyUuid_LinkLink_Uuid_LinkportImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_Uuid_TransfercostCostcharacteristicImpl import Context_TopologyUuid_NodeNode_Uuid_TransfercostCostcharacteristicImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_Uuid_ExtensionsImpl import Context_TopologyUuid_NodeNode_Uuid_ExtensionsImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_Uuid_TransfercapacityAvailablecapacityImpl import Context_TopologyUuid_NodeNode_Uuid_TransfercapacityAvailablecapacityImpl
from funcs_TapiTopology.context_TopologyUuidLabelValuenameImpl import Context_TopologyUuidLabelValuenameImpl
from funcs_TapiTopology.getnodeedgepointdetailsImpl import GetnodeedgepointdetailsImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_Uuid_ValidationValidationmechanismImpl import Context_TopologyUuid_LinkLink_Uuid_ValidationValidationmechanismImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_Uuid_TransfercostCostcharacteristicCostnameImpl import Context_TopologyUuid_NodeNode_Uuid_TransfercostCostcharacteristicCostnameImpl
from funcs_TapiTopology.context_NwtopologyserviceImpl import Context_NwtopologyserviceImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_Uuid_TransfertimingImpl import Context_TopologyUuid_NodeNode_Uuid_TransfertimingImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_Uuid_ExtensionsImpl import Context_TopologyUuid_LinkLink_Uuid_ExtensionsImpl
from funcs_TapiTopology.context_Nwtopologyservice_ExtensionsImpl import Context_Nwtopologyservice_ExtensionsImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_Uuid_TransferintegrityImpl import Context_TopologyUuid_NodeNode_Uuid_TransferintegrityImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_Uuid_TransfercostImpl import Context_TopologyUuid_NodeNode_Uuid_TransfercostImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalid_ExtensionsImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalid_ExtensionsImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_Uuid_TransfertimingLatencycharacteristicImpl import Context_TopologyUuid_NodeNode_Uuid_TransfertimingLatencycharacteristicImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_UuidLabelValuenameImpl import Context_TopologyUuid_LinkLink_UuidLabelValuenameImpl
from funcs_TapiTopology.context_TopologyUuid_ExtensionsImpl import Context_TopologyUuid_ExtensionsImpl
from funcs_TapiTopology.gettopologylistImpl import GettopologylistImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_UuidLabelValuenameImpl import Context_TopologyUuid_NodeNode_UuidLabelValuenameImpl
from funcs_TapiTopology.getlinkdetailsImpl import GetlinkdetailsImpl
from funcs_TapiTopology.context_Nwtopologyservice_ExtensionsExtensionsspecificationImpl import Context_Nwtopologyservice_ExtensionsExtensionsspecificationImpl
from funcs_TapiTopology.gettopologydetailsImpl import GettopologydetailsImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_Uuid_LinkportLocalidImpl import Context_TopologyUuid_LinkLink_Uuid_LinkportLocalidImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_StateImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_StateImpl
from funcs_TapiTopology.context_NwtopologyserviceNameImpl import Context_NwtopologyserviceNameImpl
from funcs_TapiTopology.context_TopologyUuid_LinkImpl import Context_TopologyUuid_LinkImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_Uuid_TransfercostCostcharacteristicImpl import Context_TopologyUuid_LinkLink_Uuid_TransfercostCostcharacteristicImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_UuidNameImpl import Context_TopologyUuid_LinkLink_UuidNameImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_Uuid_ValidationValidationmechanismValidationmechanismImpl import Context_TopologyUuid_LinkLink_Uuid_ValidationValidationmechanismValidationmechanismImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_UuidNameImpl import Context_TopologyUuid_NodeNode_UuidNameImpl
from funcs_TapiTopology.context_NwtopologyserviceNameValuenameImpl import Context_NwtopologyserviceNameValuenameImpl
from funcs_TapiTopology.context_NwtopologyserviceLabelImpl import Context_NwtopologyserviceLabelImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_Uuid_LinkportLocalid_ExtensionsImpl import Context_TopologyUuid_LinkLink_Uuid_LinkportLocalid_ExtensionsImpl
from funcs_TapiTopology.context_TopologyImpl import Context_TopologyImpl
from funcs_TapiTopology.context_TopologyUuidImpl import Context_TopologyUuidImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidLabelValuenameImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidLabelValuenameImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_UuidImpl import Context_TopologyUuid_NodeNode_UuidImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_Uuid_TransfercostImpl import Context_TopologyUuid_LinkLink_Uuid_TransfercostImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidNameValuenameImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidNameValuenameImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_UuidNameValuenameImpl import Context_TopologyUuid_NodeNode_UuidNameValuenameImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_Uuid_ValidationImpl import Context_TopologyUuid_LinkLink_Uuid_ValidationImpl
from funcs_TapiTopology.context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalidImpl import Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalidImpl
from funcs_TapiTopology.context_TopologyUuid_LinkLink_UuidLabelImpl import Context_TopologyUuid_LinkLink_UuidLabelImpl

# CALLABLE OBJECTS
from objects_TapiTopology.getNodeDetailsRPCInputSchema import GetNodeDetailsRPCInputSchema
from objects_TapiTopology.linkPort import LinkPort
from objects_TapiTopology.capacity import Capacity
from objects_TapiTopology.transferCostPac import TransferCostPac
from objects_TapiTopology.networkTopologyService import NetworkTopologyService
from objects_TapiTopology.timeRange import TimeRange
from objects_TapiTopology.layerProtocolTransitionPac import LayerProtocolTransitionPac
from objects_TapiTopology.getNodeDetailsRPCOutputSchema import GetNodeDetailsRPCOutputSchema
from objects_TapiTopology.transferTimingPac import TransferTimingPac
from objects_TapiTopology.transferIntegrityPac import TransferIntegrityPac
from objects_TapiTopology.nameAndValue import NameAndValue
from objects_TapiTopology.adminStatePac import AdminStatePac
from objects_TapiTopology._nwTopologyServiceSchema import _nwTopologyServiceSchema
from objects_TapiTopology.getTopologyListRPCOutputSchema import GetTopologyListRPCOutputSchema
from objects_TapiTopology.serviceEndPoint import ServiceEndPoint
from objects_TapiTopology.validationMechanism import ValidationMechanism
from objects_TapiTopology.node import Node
from objects_TapiTopology.resourceSpec import ResourceSpec
from objects_TapiTopology.teLink import TeLink
from objects_TapiTopology.costCharacteristic import CostCharacteristic
from objects_TapiTopology.latencyCharacteristic import LatencyCharacteristic
from objects_TapiTopology.link import Link
from objects_TapiTopology.localClass import LocalClass
from objects_TapiTopology.topology import Topology
from objects_TapiTopology.extensionsSpec import ExtensionsSpec
from objects_TapiTopology.getNodeEdgePointDetailsRPCOutputSchema import GetNodeEdgePointDetailsRPCOutputSchema
from objects_TapiTopology.serviceSpec import ServiceSpec
from objects_TapiTopology.getLinkDetailsRPCOutputSchema import GetLinkDetailsRPCOutputSchema
from objects_TapiTopology.nodeEdgePoint import NodeEdgePoint
from objects_TapiTopology.getLinkDetailsRPCInputSchema import GetLinkDetailsRPCInputSchema
from objects_TapiTopology.riskCharacteristic import RiskCharacteristic
from objects_TapiTopology.riskParameterPac import RiskParameterPac
from objects_TapiTopology.getTopologyDetailsRPCInputSchema import GetTopologyDetailsRPCInputSchema
from objects_TapiTopology.operationalStatePac import OperationalStatePac
from objects_TapiTopology.globalClass import GlobalClass
from objects_TapiTopology.layerProtocol import LayerProtocol
from objects_TapiTopology.getTopologyDetailsRPCOutputSchema import GetTopologyDetailsRPCOutputSchema
from objects_TapiTopology.transferCapacityPac import TransferCapacityPac
from objects_TapiTopology._topologySchema import _topologySchema
from objects_TapiTopology.getNodeEdgePointDetailsRPCInputSchema import GetNodeEdgePointDetailsRPCInputSchema
from objects_TapiTopology.lifecycleStatePac import LifecycleStatePac
from objects_TapiTopology.validationPac import ValidationPac

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


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_ownedNodeEdgePoint/(\w+)/name/
class Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidNameMethodView(MethodView):

    def get(self, uuid, node_uuid, ownedNodeEdgePoint_uuid):
        print "Retrieve operation of resource: name"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidNameImpl.get(uuid, node_uuid, ownedNodeEdgePoint_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_transferCapacity/
class Context_TopologyUuid_LinkLink_Uuid_TransfercapacityMethodView(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: _transferCapacity"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_TransfercapacityImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_transferCapacity/capacityAssignedToUserView/
class Context_TopologyUuid_LinkLink_Uuid_TransfercapacityCapacityassignedtouserviewMethodView(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: capacityAssignedToUserView"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_TransfercapacityCapacityassignedtouserviewImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_transferCapacity/totalPotentialCapacity/
class Context_TopologyUuid_LinkLink_Uuid_TransfercapacityTotalpotentialcapacityMethodView(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: totalPotentialCapacity"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_TransfercapacityTotalpotentialcapacityImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_riskParameter/riskCharacteristic/
class Context_TopologyUuid_LinkLink_Uuid_RiskparameterRiskcharacteristicMethodView(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: riskCharacteristic"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_RiskparameterRiskcharacteristicImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_transferCapacity/capacityAssignedToUserView/
class Context_TopologyUuid_NodeNode_Uuid_TransfercapacityCapacityassignedtouserviewMethodView(MethodView):

    def get(self, uuid, node_uuid):
        print "Retrieve operation of resource: capacityAssignedToUserView"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_TransfercapacityCapacityassignedtouserviewImpl.get(uuid, node_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/name/(\w+)/
class Context_TopologyUuidNameValuenameMethodView(MethodView):

    def get(self, uuid, valueName):
        print "Retrieve operation of resource: name"
        try:
            response = Context_TopologyUuidNameValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_transferCost/costCharacteristic/(\w+)/
class Context_TopologyUuid_LinkLink_Uuid_TransfercostCostcharacteristicCostnameMethodView(MethodView):

    def get(self, uuid, link_uuid, costName):
        print "Retrieve operation of resource: costCharacteristic"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_TransfercostCostcharacteristicCostnameImpl.get(uuid, link_uuid, costName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/name/(\w+)/
class Context_TopologyUuid_LinkLink_UuidNameValuenameMethodView(MethodView):

    def get(self, uuid, link_uuid, valueName):
        print "Retrieve operation of resource: name"
        try:
            response = Context_TopologyUuid_LinkLink_UuidNameValuenameImpl.get(uuid, link_uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/name/
class Context_TopologyUuidNameMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: name"
        try:
            response = Context_TopologyUuidNameImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_extensions/(\w+)/
class Context_TopologyUuid_LinkLink_Uuid_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, link_uuid, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_ExtensionsExtensionsspecificationImpl.get(uuid, link_uuid, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_linkPort/(\w+)/_extensions/(\w+)/
class Context_TopologyUuid_LinkLink_Uuid_LinkportLocalid_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, link_uuid, localId, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_LinkportLocalid_ExtensionsExtensionsspecificationImpl.get(uuid, link_uuid, localId, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_state/
class Context_TopologyUuid_NodeNode_Uuid_StateMethodView(MethodView):

    def get(self, uuid, node_uuid):
        print "Retrieve operation of resource: _state"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_StateImpl.get(uuid, node_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_transferTiming/latencyCharacteristic/(\w+)/
class Context_TopologyUuid_NodeNode_Uuid_TransfertimingLatencycharacteristicTrafficpropertynameMethodView(MethodView):

    def get(self, uuid, node_uuid, trafficPropertyName):
        print "Retrieve operation of resource: latencyCharacteristic"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_TransfertimingLatencycharacteristicTrafficpropertynameImpl.get(uuid, node_uuid, trafficPropertyName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/label/
class Context_TopologyUuid_NodeNode_UuidLabelMethodView(MethodView):

    def get(self, uuid, node_uuid):
        print "Retrieve operation of resource: label"
        try:
            response = Context_TopologyUuid_NodeNode_UuidLabelImpl.get(uuid, node_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_lpTransition/
class Context_TopologyUuid_LinkLink_Uuid_LptransitionMethodView(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: _lpTransition"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_LptransitionImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_ownedNodeEdgePoint/(\w+)/_layerProtocol/
class Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolMethodView(MethodView):

    def get(self, uuid, node_uuid, ownedNodeEdgePoint_uuid):
        print "Retrieve operation of resource: _layerProtocol"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolImpl.get(uuid, node_uuid, ownedNodeEdgePoint_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_ownedNodeEdgePoint/(\w+)/_extensions/
class Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_ExtensionsMethodView(MethodView):

    def get(self, uuid, node_uuid, ownedNodeEdgePoint_uuid):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_ExtensionsImpl.get(uuid, node_uuid, ownedNodeEdgePoint_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_extensions/(\w+)/
class Context_TopologyUuid_NodeNode_Uuid_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, node_uuid, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_ExtensionsExtensionsspecificationImpl.get(uuid, node_uuid, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_ownedNodeEdgePoint/(\w+)/_extensions/(\w+)/
class Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, node_uuid, ownedNodeEdgePoint_uuid, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_ExtensionsExtensionsspecificationImpl.get(uuid, node_uuid, ownedNodeEdgePoint_uuid, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_nwTopologyService/label/(\w+)/
class Context_NwtopologyserviceLabelValuenameMethodView(MethodView):

    def get(self, valueName):
        print "Retrieve operation of resource: label"
        try:
            response = Context_NwtopologyserviceLabelValuenameImpl.get(valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/label/
class Context_TopologyUuidLabelMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: label"
        try:
            response = Context_TopologyUuidLabelImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_ownedNodeEdgePoint/(\w+)/label/
class Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidLabelMethodView(MethodView):

    def get(self, uuid, node_uuid, ownedNodeEdgePoint_uuid):
        print "Retrieve operation of resource: label"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidLabelImpl.get(uuid, node_uuid, ownedNodeEdgePoint_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_transferTiming/latencyCharacteristic/(\w+)/
class Context_TopologyUuid_LinkLink_Uuid_TransfertimingLatencycharacteristicTrafficpropertynameMethodView(MethodView):

    def get(self, uuid, link_uuid, trafficPropertyName):
        print "Retrieve operation of resource: latencyCharacteristic"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_TransfertimingLatencycharacteristicTrafficpropertynameImpl.get(uuid, link_uuid, trafficPropertyName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_transferCapacity/availableCapacity/
class Context_TopologyUuid_LinkLink_Uuid_TransfercapacityAvailablecapacityMethodView(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: availableCapacity"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_TransfercapacityAvailablecapacityImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_transferCapacity/capacityAssignedToUserView/(\w+)/
class Context_TopologyUuid_NodeNode_Uuid_TransfercapacityCapacityassignedtouserviewTotalsizeMethodView(MethodView):

    def get(self, uuid, node_uuid, totalSize):
        print "Retrieve operation of resource: capacityAssignedToUserView"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_TransfercapacityCapacityassignedtouserviewTotalsizeImpl.get(uuid, node_uuid, totalSize)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_transferCapacity/
class Context_TopologyUuid_NodeNode_Uuid_TransfercapacityMethodView(MethodView):

    def get(self, uuid, node_uuid):
        print "Retrieve operation of resource: _transferCapacity"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_TransfercapacityImpl.get(uuid, node_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/operations/getNodeDetails/
class GetnodedetailsMethodView(MethodView):

    def post(self, ):
        print "Create operation of resource: getNodeDetails"
        try:
            response = GetnodedetailsImpl.get()
        except KeyError as inst:
            if inst.args[0] != '':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(GetNodeDetailsRPCInputSchema, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    GetnodedetailsImpl.post(new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))



#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/
class Context_TopologyUuid_LinkLink_UuidMethodView(MethodView):

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
class Context_TopologyUuid_NodeNode_Uuid_TransfercapacityTotalpotentialcapacityMethodView(MethodView):

    def get(self, uuid, node_uuid):
        print "Retrieve operation of resource: totalPotentialCapacity"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_TransfercapacityTotalpotentialcapacityImpl.get(uuid, node_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_transferTiming/latencyCharacteristic/
class Context_TopologyUuid_LinkLink_Uuid_TransfertimingLatencycharacteristicMethodView(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: latencyCharacteristic"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_TransfertimingLatencycharacteristicImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_transferTiming/
class Context_TopologyUuid_LinkLink_Uuid_TransfertimingMethodView(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: _transferTiming"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_TransfertimingImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/
class Context_TopologyUuid_NodeMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _node"
        try:
            response = Context_TopologyUuid_NodeImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_ownedNodeEdgePoint/(\w+)/_layerProtocol/(\w+)/_extensions/(\w+)/
class Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalid_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, node_uuid, ownedNodeEdgePoint_uuid, localId, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalid_ExtensionsExtensionsspecificationImpl.get(uuid, node_uuid, ownedNodeEdgePoint_uuid, localId, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_riskParameter/
class Context_TopologyUuid_LinkLink_Uuid_RiskparameterMethodView(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: _riskParameter"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_RiskparameterImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_state/
class Context_TopologyUuid_LinkLink_Uuid_StateMethodView(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: _state"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_StateImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_riskParameter/riskCharacteristic/(\w+)/
class Context_TopologyUuid_LinkLink_Uuid_RiskparameterRiskcharacteristicRiskcharacteristicnameMethodView(MethodView):

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
class Context_TopologyUuid_LinkLink_Uuid_TransferintegrityMethodView(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: _transferIntegrity"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_TransferintegrityImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_extensions/(\w+)/
class Context_TopologyUuid_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_TopologyUuid_ExtensionsExtensionsspecificationImpl.get(uuid, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_transferCapacity/capacityAssignedToUserView/(\w+)/
class Context_TopologyUuid_LinkLink_Uuid_TransfercapacityCapacityassignedtouserviewTotalsizeMethodView(MethodView):

    def get(self, uuid, link_uuid, totalSize):
        print "Retrieve operation of resource: capacityAssignedToUserView"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_TransfercapacityCapacityassignedtouserviewTotalsizeImpl.get(uuid, link_uuid, totalSize)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_ownedNodeEdgePoint/(\w+)/
class Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidMethodView(MethodView):

    def get(self, uuid, node_uuid, ownedNodeEdgePoint_uuid):
        print "Retrieve operation of resource: _ownedNodeEdgePoint"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidImpl.get(uuid, node_uuid, ownedNodeEdgePoint_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_linkPort/
class Context_TopologyUuid_LinkLink_Uuid_LinkportMethodView(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: _linkPort"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_LinkportImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_transferCost/costCharacteristic/
class Context_TopologyUuid_NodeNode_Uuid_TransfercostCostcharacteristicMethodView(MethodView):

    def get(self, uuid, node_uuid):
        print "Retrieve operation of resource: costCharacteristic"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_TransfercostCostcharacteristicImpl.get(uuid, node_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_extensions/
class Context_TopologyUuid_NodeNode_Uuid_ExtensionsMethodView(MethodView):

    def get(self, uuid, node_uuid):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_ExtensionsImpl.get(uuid, node_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_transferCapacity/availableCapacity/
class Context_TopologyUuid_NodeNode_Uuid_TransfercapacityAvailablecapacityMethodView(MethodView):

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
class Context_TopologyUuidLabelValuenameMethodView(MethodView):

    def get(self, uuid, valueName):
        print "Retrieve operation of resource: label"
        try:
            response = Context_TopologyUuidLabelValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/operations/getNodeEdgePointDetails/
class GetnodeedgepointdetailsMethodView(MethodView):

    def post(self, ):
        print "Create operation of resource: getNodeEdgePointDetails"
        try:
            response = GetnodeedgepointdetailsImpl.get()
        except KeyError as inst:
            if inst.args[0] != '':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(GetNodeEdgePointDetailsRPCInputSchema, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    GetnodeedgepointdetailsImpl.post(new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))



#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_validation/validationMechanism/
class Context_TopologyUuid_LinkLink_Uuid_ValidationValidationmechanismMethodView(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: validationMechanism"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_ValidationValidationmechanismImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_transferCost/costCharacteristic/(\w+)/
class Context_TopologyUuid_NodeNode_Uuid_TransfercostCostcharacteristicCostnameMethodView(MethodView):

    def get(self, uuid, node_uuid, costName):
        print "Retrieve operation of resource: costCharacteristic"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_TransfercostCostcharacteristicCostnameImpl.get(uuid, node_uuid, costName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_nwTopologyService/
class Context_NwtopologyserviceMethodView(MethodView):

    def get(self, ):
        print "Retrieve operation of resource: _nwTopologyService"
        try:
            response = Context_NwtopologyserviceImpl.get()
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_transferTiming/
class Context_TopologyUuid_NodeNode_Uuid_TransfertimingMethodView(MethodView):

    def get(self, uuid, node_uuid):
        print "Retrieve operation of resource: _transferTiming"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_TransfertimingImpl.get(uuid, node_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_extensions/
class Context_TopologyUuid_LinkLink_Uuid_ExtensionsMethodView(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_ExtensionsImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_nwTopologyService/_extensions/
class Context_Nwtopologyservice_ExtensionsMethodView(MethodView):

    def get(self, ):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_Nwtopologyservice_ExtensionsImpl.get()
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_transferIntegrity/
class Context_TopologyUuid_NodeNode_Uuid_TransferintegrityMethodView(MethodView):

    def get(self, uuid, node_uuid):
        print "Retrieve operation of resource: _transferIntegrity"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_TransferintegrityImpl.get(uuid, node_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_transferCost/
class Context_TopologyUuid_NodeNode_Uuid_TransfercostMethodView(MethodView):

    def get(self, uuid, node_uuid):
        print "Retrieve operation of resource: _transferCost"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_TransfercostImpl.get(uuid, node_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_ownedNodeEdgePoint/(\w+)/_layerProtocol/(\w+)/_extensions/
class Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalid_ExtensionsMethodView(MethodView):

    def get(self, uuid, node_uuid, ownedNodeEdgePoint_uuid, localId):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalid_ExtensionsImpl.get(uuid, node_uuid, ownedNodeEdgePoint_uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_transferTiming/latencyCharacteristic/
class Context_TopologyUuid_NodeNode_Uuid_TransfertimingLatencycharacteristicMethodView(MethodView):

    def get(self, uuid, node_uuid):
        print "Retrieve operation of resource: latencyCharacteristic"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_TransfertimingLatencycharacteristicImpl.get(uuid, node_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/label/(\w+)/
class Context_TopologyUuid_LinkLink_UuidLabelValuenameMethodView(MethodView):

    def get(self, uuid, link_uuid, valueName):
        print "Retrieve operation of resource: label"
        try:
            response = Context_TopologyUuid_LinkLink_UuidLabelValuenameImpl.get(uuid, link_uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_extensions/
class Context_TopologyUuid_ExtensionsMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_TopologyUuid_ExtensionsImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/operations/getTopologyList/
class GettopologylistMethodView(MethodView):

    def post(self, ):
        print "Create operation of resource: getTopologyList"
        json_struct = request.get_json() #json parser.
        new_object = (json_struct) #It creates an object instance from the json_input data.
        response = GettopologylistImpl.post( new_object)
        return Successful('Successful operation','{"description":"Create operation of resource: getTopologyList"}')


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/label/(\w+)/
class Context_TopologyUuid_NodeNode_UuidLabelValuenameMethodView(MethodView):

    def get(self, uuid, node_uuid, valueName):
        print "Retrieve operation of resource: label"
        try:
            response = Context_TopologyUuid_NodeNode_UuidLabelValuenameImpl.get(uuid, node_uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/operations/getLinkDetails/
class GetlinkdetailsMethodView(MethodView):

    def post(self, ):
        print "Create operation of resource: getLinkDetails"
        try:
            response = GetlinkdetailsImpl.get()
        except KeyError as inst:
            if inst.args[0] != '':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(GetLinkDetailsRPCInputSchema, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    GetlinkdetailsImpl.post(new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))



#/restconf/config/Context/_nwTopologyService/_extensions/(\w+)/
class Context_Nwtopologyservice_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_Nwtopologyservice_ExtensionsExtensionsspecificationImpl.get(extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/operations/getTopologyDetails/
class GettopologydetailsMethodView(MethodView):

    def post(self, ):
        print "Create operation of resource: getTopologyDetails"
        try:
            response = GettopologydetailsImpl.get()
        except KeyError as inst:
            if inst.args[0] != '':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(GetTopologyDetailsRPCInputSchema, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    GettopologydetailsImpl.post(new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))



#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_linkPort/(\w+)/
class Context_TopologyUuid_LinkLink_Uuid_LinkportLocalidMethodView(MethodView):

    def get(self, uuid, link_uuid, localId):
        print "Retrieve operation of resource: _linkPort"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_LinkportLocalidImpl.get(uuid, link_uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_ownedNodeEdgePoint/(\w+)/_state/
class Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_StateMethodView(MethodView):

    def get(self, uuid, node_uuid, ownedNodeEdgePoint_uuid):
        print "Retrieve operation of resource: _state"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_StateImpl.get(uuid, node_uuid, ownedNodeEdgePoint_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_nwTopologyService/name/
class Context_NwtopologyserviceNameMethodView(MethodView):

    def get(self, ):
        print "Retrieve operation of resource: name"
        try:
            response = Context_NwtopologyserviceNameImpl.get()
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/
class Context_TopologyUuid_LinkMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _link"
        try:
            response = Context_TopologyUuid_LinkImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_transferCost/costCharacteristic/
class Context_TopologyUuid_LinkLink_Uuid_TransfercostCostcharacteristicMethodView(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: costCharacteristic"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_TransfercostCostcharacteristicImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/name/
class Context_TopologyUuid_LinkLink_UuidNameMethodView(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: name"
        try:
            response = Context_TopologyUuid_LinkLink_UuidNameImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_validation/validationMechanism/(\w+)/
class Context_TopologyUuid_LinkLink_Uuid_ValidationValidationmechanismValidationmechanismMethodView(MethodView):

    def get(self, uuid, link_uuid, validationMechanism):
        print "Retrieve operation of resource: validationMechanism"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_ValidationValidationmechanismValidationmechanismImpl.get(uuid, link_uuid, validationMechanism)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/name/
class Context_TopologyUuid_NodeNode_UuidNameMethodView(MethodView):

    def get(self, uuid, node_uuid):
        print "Retrieve operation of resource: name"
        try:
            response = Context_TopologyUuid_NodeNode_UuidNameImpl.get(uuid, node_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_nwTopologyService/name/(\w+)/
class Context_NwtopologyserviceNameValuenameMethodView(MethodView):

    def get(self, valueName):
        print "Retrieve operation of resource: name"
        try:
            response = Context_NwtopologyserviceNameValuenameImpl.get(valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_nwTopologyService/label/
class Context_NwtopologyserviceLabelMethodView(MethodView):

    def get(self, ):
        print "Retrieve operation of resource: label"
        try:
            response = Context_NwtopologyserviceLabelImpl.get()
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_linkPort/(\w+)/_extensions/
class Context_TopologyUuid_LinkLink_Uuid_LinkportLocalid_ExtensionsMethodView(MethodView):

    def get(self, uuid, link_uuid, localId):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_LinkportLocalid_ExtensionsImpl.get(uuid, link_uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/
class Context_TopologyMethodView(MethodView):

    def get(self, ):
        print "Retrieve operation of resource: _topology"
        try:
            response = Context_TopologyImpl.get()
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/
class Context_TopologyUuidMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _topology"
        try:
            response = Context_TopologyUuidImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_ownedNodeEdgePoint/(\w+)/label/(\w+)/
class Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidLabelValuenameMethodView(MethodView):

    def get(self, uuid, node_uuid, ownedNodeEdgePoint_uuid, valueName):
        print "Retrieve operation of resource: label"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidLabelValuenameImpl.get(uuid, node_uuid, ownedNodeEdgePoint_uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/
class Context_TopologyUuid_NodeNode_UuidMethodView(MethodView):

    def get(self, uuid, node_uuid):
        print "Retrieve operation of resource: _node"
        try:
            response = Context_TopologyUuid_NodeNode_UuidImpl.get(uuid, node_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_transferCost/
class Context_TopologyUuid_LinkLink_Uuid_TransfercostMethodView(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: _transferCost"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_TransfercostImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_ownedNodeEdgePoint/
class Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointMethodView(MethodView):

    def get(self, uuid, node_uuid):
        print "Retrieve operation of resource: _ownedNodeEdgePoint"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointImpl.get(uuid, node_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_ownedNodeEdgePoint/(\w+)/name/(\w+)/
class Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidNameValuenameMethodView(MethodView):

    def get(self, uuid, node_uuid, ownedNodeEdgePoint_uuid, valueName):
        print "Retrieve operation of resource: name"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidNameValuenameImpl.get(uuid, node_uuid, ownedNodeEdgePoint_uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/name/(\w+)/
class Context_TopologyUuid_NodeNode_UuidNameValuenameMethodView(MethodView):

    def get(self, uuid, node_uuid, valueName):
        print "Retrieve operation of resource: name"
        try:
            response = Context_TopologyUuid_NodeNode_UuidNameValuenameImpl.get(uuid, node_uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/_validation/
class Context_TopologyUuid_LinkLink_Uuid_ValidationMethodView(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: _validation"
        try:
            response = Context_TopologyUuid_LinkLink_Uuid_ValidationImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_node/(\w+)/_ownedNodeEdgePoint/(\w+)/_layerProtocol/(\w+)/
class Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalidMethodView(MethodView):

    def get(self, uuid, node_uuid, ownedNodeEdgePoint_uuid, localId):
        print "Retrieve operation of resource: _layerProtocol"
        try:
            response = Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalidImpl.get(uuid, node_uuid, ownedNodeEdgePoint_uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_topology/(\w+)/_link/(\w+)/label/
class Context_TopologyUuid_LinkLink_UuidLabelMethodView(MethodView):

    def get(self, uuid, link_uuid):
        print "Retrieve operation of resource: label"
        try:
            response = Context_TopologyUuid_LinkLink_UuidLabelImpl.get(uuid, link_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))



getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/<ownedNodeEdgePoint_uuid>/name/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidNameMethodView"].as_view('"Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferCapacity/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_TransfercapacityMethodView"].as_view('"Context_TopologyUuid_LinkLink_Uuid_Transfercapacity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferCapacity/capacityAssignedToUserView/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_TransfercapacityCapacityassignedtouserviewMethodView"].as_view('"Context_TopologyUuid_LinkLink_Uuid_TransfercapacityCapacityassignedtouserview"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferCapacity/totalPotentialCapacity/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_TransfercapacityTotalpotentialcapacityMethodView"].as_view('"Context_TopologyUuid_LinkLink_Uuid_TransfercapacityTotalpotentialcapacity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_riskParameter/riskCharacteristic/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_RiskparameterRiskcharacteristicMethodView"].as_view('"Context_TopologyUuid_LinkLink_Uuid_RiskparameterRiskcharacteristic"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferCapacity/capacityAssignedToUserView/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_TransfercapacityCapacityassignedtouserviewMethodView"].as_view('"Context_TopologyUuid_NodeNode_Uuid_TransfercapacityCapacityassignedtouserview"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/name/<valueName>/", view_func = globals()["Context_TopologyUuidNameValuenameMethodView"].as_view('"Context_TopologyUuidNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferCost/costCharacteristic/<costName>/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_TransfercostCostcharacteristicCostnameMethodView"].as_view('"Context_TopologyUuid_LinkLink_Uuid_TransfercostCostcharacteristicCostname"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/name/<valueName>/", view_func = globals()["Context_TopologyUuid_LinkLink_UuidNameValuenameMethodView"].as_view('"Context_TopologyUuid_LinkLink_UuidNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/name/", view_func = globals()["Context_TopologyUuidNameMethodView"].as_view('"Context_TopologyUuidName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_TopologyUuid_LinkLink_Uuid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_linkPort/<localId>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_LinkportLocalid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_TopologyUuid_LinkLink_Uuid_LinkportLocalid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_state/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_StateMethodView"].as_view('"Context_TopologyUuid_NodeNode_Uuid_State"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferTiming/latencyCharacteristic/<trafficPropertyName>/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_TransfertimingLatencycharacteristicTrafficpropertynameMethodView"].as_view('"Context_TopologyUuid_NodeNode_Uuid_TransfertimingLatencycharacteristicTrafficpropertyname"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/label/", view_func = globals()["Context_TopologyUuid_NodeNode_UuidLabelMethodView"].as_view('"Context_TopologyUuid_NodeNode_UuidLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_lpTransition/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_LptransitionMethodView"].as_view('"Context_TopologyUuid_LinkLink_Uuid_Lptransition"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/<ownedNodeEdgePoint_uuid>/_layerProtocol/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolMethodView"].as_view('"Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_Layerprotocol"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/<ownedNodeEdgePoint_uuid>/_extensions/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_ExtensionsMethodView"].as_view('"Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_TopologyUuid_NodeNode_Uuid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/<ownedNodeEdgePoint_uuid>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_nwTopologyService/label/<valueName>/", view_func = globals()["Context_NwtopologyserviceLabelValuenameMethodView"].as_view('"Context_NwtopologyserviceLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/label/", view_func = globals()["Context_TopologyUuidLabelMethodView"].as_view('"Context_TopologyUuidLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/<ownedNodeEdgePoint_uuid>/label/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidLabelMethodView"].as_view('"Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferTiming/latencyCharacteristic/<trafficPropertyName>/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_TransfertimingLatencycharacteristicTrafficpropertynameMethodView"].as_view('"Context_TopologyUuid_LinkLink_Uuid_TransfertimingLatencycharacteristicTrafficpropertyname"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferCapacity/availableCapacity/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_TransfercapacityAvailablecapacityMethodView"].as_view('"Context_TopologyUuid_LinkLink_Uuid_TransfercapacityAvailablecapacity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferCapacity/capacityAssignedToUserView/<totalSize>/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_TransfercapacityCapacityassignedtouserviewTotalsizeMethodView"].as_view('"Context_TopologyUuid_NodeNode_Uuid_TransfercapacityCapacityassignedtouserviewTotalsize"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferCapacity/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_TransfercapacityMethodView"].as_view('"Context_TopologyUuid_NodeNode_Uuid_Transfercapacity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getNodeDetails/", view_func = globals()["GetnodedetailsMethodView"].as_view('"Getnodedetails"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/", view_func = globals()["Context_TopologyUuid_LinkLink_UuidMethodView"].as_view('"Context_TopologyUuid_LinkLink_Uuid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferCapacity/totalPotentialCapacity/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_TransfercapacityTotalpotentialcapacityMethodView"].as_view('"Context_TopologyUuid_NodeNode_Uuid_TransfercapacityTotalpotentialcapacity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferTiming/latencyCharacteristic/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_TransfertimingLatencycharacteristicMethodView"].as_view('"Context_TopologyUuid_LinkLink_Uuid_TransfertimingLatencycharacteristic"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferTiming/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_TransfertimingMethodView"].as_view('"Context_TopologyUuid_LinkLink_Uuid_Transfertiming"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/", view_func = globals()["Context_TopologyUuid_NodeMethodView"].as_view('"Context_TopologyUuid_Node"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/<ownedNodeEdgePoint_uuid>/_layerProtocol/<localId>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_riskParameter/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_RiskparameterMethodView"].as_view('"Context_TopologyUuid_LinkLink_Uuid_Riskparameter"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_state/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_StateMethodView"].as_view('"Context_TopologyUuid_LinkLink_Uuid_State"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_riskParameter/riskCharacteristic/<riskCharacteristicName>/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_RiskparameterRiskcharacteristicRiskcharacteristicnameMethodView"].as_view('"Context_TopologyUuid_LinkLink_Uuid_RiskparameterRiskcharacteristicRiskcharacteristicname"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferIntegrity/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_TransferintegrityMethodView"].as_view('"Context_TopologyUuid_LinkLink_Uuid_Transferintegrity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_TopologyUuid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_TopologyUuid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferCapacity/capacityAssignedToUserView/<totalSize>/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_TransfercapacityCapacityassignedtouserviewTotalsizeMethodView"].as_view('"Context_TopologyUuid_LinkLink_Uuid_TransfercapacityCapacityassignedtouserviewTotalsize"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/<ownedNodeEdgePoint_uuid>/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidMethodView"].as_view('"Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_linkPort/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_LinkportMethodView"].as_view('"Context_TopologyUuid_LinkLink_Uuid_Linkport"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferCost/costCharacteristic/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_TransfercostCostcharacteristicMethodView"].as_view('"Context_TopologyUuid_NodeNode_Uuid_TransfercostCostcharacteristic"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_extensions/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_ExtensionsMethodView"].as_view('"Context_TopologyUuid_NodeNode_Uuid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferCapacity/availableCapacity/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_TransfercapacityAvailablecapacityMethodView"].as_view('"Context_TopologyUuid_NodeNode_Uuid_TransfercapacityAvailablecapacity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/label/<valueName>/", view_func = globals()["Context_TopologyUuidLabelValuenameMethodView"].as_view('"Context_TopologyUuidLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getNodeEdgePointDetails/", view_func = globals()["GetnodeedgepointdetailsMethodView"].as_view('"Getnodeedgepointdetails"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_validation/validationMechanism/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_ValidationValidationmechanismMethodView"].as_view('"Context_TopologyUuid_LinkLink_Uuid_ValidationValidationmechanism"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferCost/costCharacteristic/<costName>/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_TransfercostCostcharacteristicCostnameMethodView"].as_view('"Context_TopologyUuid_NodeNode_Uuid_TransfercostCostcharacteristicCostname"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_nwTopologyService/", view_func = globals()["Context_NwtopologyserviceMethodView"].as_view('"Context_Nwtopologyservice"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferTiming/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_TransfertimingMethodView"].as_view('"Context_TopologyUuid_NodeNode_Uuid_Transfertiming"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_extensions/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_ExtensionsMethodView"].as_view('"Context_TopologyUuid_LinkLink_Uuid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_nwTopologyService/_extensions/", view_func = globals()["Context_Nwtopologyservice_ExtensionsMethodView"].as_view('"Context_Nwtopologyservice_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferIntegrity/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_TransferintegrityMethodView"].as_view('"Context_TopologyUuid_NodeNode_Uuid_Transferintegrity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferCost/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_TransfercostMethodView"].as_view('"Context_TopologyUuid_NodeNode_Uuid_Transfercost"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/<ownedNodeEdgePoint_uuid>/_layerProtocol/<localId>/_extensions/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalid_ExtensionsMethodView"].as_view('"Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_transferTiming/latencyCharacteristic/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_TransfertimingLatencycharacteristicMethodView"].as_view('"Context_TopologyUuid_NodeNode_Uuid_TransfertimingLatencycharacteristic"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/label/<valueName>/", view_func = globals()["Context_TopologyUuid_LinkLink_UuidLabelValuenameMethodView"].as_view('"Context_TopologyUuid_LinkLink_UuidLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_extensions/", view_func = globals()["Context_TopologyUuid_ExtensionsMethodView"].as_view('"Context_TopologyUuid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getTopologyList/", view_func = globals()["GettopologylistMethodView"].as_view('"Gettopologylist"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/label/<valueName>/", view_func = globals()["Context_TopologyUuid_NodeNode_UuidLabelValuenameMethodView"].as_view('"Context_TopologyUuid_NodeNode_UuidLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getLinkDetails/", view_func = globals()["GetlinkdetailsMethodView"].as_view('"Getlinkdetails"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_nwTopologyService/_extensions/<extensionsSpecification>/", view_func = globals()["Context_Nwtopologyservice_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_Nwtopologyservice_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getTopologyDetails/", view_func = globals()["GettopologydetailsMethodView"].as_view('"Gettopologydetails"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_linkPort/<localId>/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_LinkportLocalidMethodView"].as_view('"Context_TopologyUuid_LinkLink_Uuid_LinkportLocalid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/<ownedNodeEdgePoint_uuid>/_state/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_StateMethodView"].as_view('"Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_State"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_nwTopologyService/name/", view_func = globals()["Context_NwtopologyserviceNameMethodView"].as_view('"Context_NwtopologyserviceName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/", view_func = globals()["Context_TopologyUuid_LinkMethodView"].as_view('"Context_TopologyUuid_Link"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferCost/costCharacteristic/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_TransfercostCostcharacteristicMethodView"].as_view('"Context_TopologyUuid_LinkLink_Uuid_TransfercostCostcharacteristic"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/name/", view_func = globals()["Context_TopologyUuid_LinkLink_UuidNameMethodView"].as_view('"Context_TopologyUuid_LinkLink_UuidName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_validation/validationMechanism/<validationMechanism>/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_ValidationValidationmechanismValidationmechanismMethodView"].as_view('"Context_TopologyUuid_LinkLink_Uuid_ValidationValidationmechanismValidationmechanism"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/name/", view_func = globals()["Context_TopologyUuid_NodeNode_UuidNameMethodView"].as_view('"Context_TopologyUuid_NodeNode_UuidName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_nwTopologyService/name/<valueName>/", view_func = globals()["Context_NwtopologyserviceNameValuenameMethodView"].as_view('"Context_NwtopologyserviceNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_nwTopologyService/label/", view_func = globals()["Context_NwtopologyserviceLabelMethodView"].as_view('"Context_NwtopologyserviceLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_linkPort/<localId>/_extensions/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_LinkportLocalid_ExtensionsMethodView"].as_view('"Context_TopologyUuid_LinkLink_Uuid_LinkportLocalid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/", view_func = globals()["Context_TopologyMethodView"].as_view('"Context_Topology"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/", view_func = globals()["Context_TopologyUuidMethodView"].as_view('"Context_TopologyUuid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/<ownedNodeEdgePoint_uuid>/label/<valueName>/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidLabelValuenameMethodView"].as_view('"Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/", view_func = globals()["Context_TopologyUuid_NodeNode_UuidMethodView"].as_view('"Context_TopologyUuid_NodeNode_Uuid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_transferCost/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_TransfercostMethodView"].as_view('"Context_TopologyUuid_LinkLink_Uuid_Transfercost"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointMethodView"].as_view('"Context_TopologyUuid_NodeNode_Uuid_Ownednodeedgepoint"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/<ownedNodeEdgePoint_uuid>/name/<valueName>/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidNameValuenameMethodView"].as_view('"Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/name/<valueName>/", view_func = globals()["Context_TopologyUuid_NodeNode_UuidNameValuenameMethodView"].as_view('"Context_TopologyUuid_NodeNode_UuidNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/_validation/", view_func = globals()["Context_TopologyUuid_LinkLink_Uuid_ValidationMethodView"].as_view('"Context_TopologyUuid_LinkLink_Uuid_Validation"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_node/<node_uuid>/_ownedNodeEdgePoint/<ownedNodeEdgePoint_uuid>/_layerProtocol/<localId>/", view_func = globals()["Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalidMethodView"].as_view('"Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_Uuid_LayerprotocolLocalid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_topology/<uuid>/_link/<link_uuid>/label/", view_func = globals()["Context_TopologyUuid_LinkLink_UuidLabelMethodView"].as_view('"Context_TopologyUuid_LinkLink_UuidLabel"'+'"_api"'), methods=['GET'])
