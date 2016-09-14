from flask import json, Blueprint, request, Response
from flask.views import MethodView
import sys
from objects_common.keyedArrayType import KeyedArrayKeyError

import base64
import re

# BACKEND FUNCTIONS
from funcs_TapiConnectivity.context_ConnectionUuid_StateImpl import Context_ConnectionUuid_StateImpl
from funcs_TapiConnectivity.context_ConnectivityserviceUuid_ConnconstraintImpl import Context_ConnectivityserviceUuid_ConnconstraintImpl
from funcs_TapiConnectivity.context_ConnectivityserviceUuid_ConnconstraintRequestedcapacityImpl import Context_ConnectivityserviceUuid_ConnconstraintRequestedcapacityImpl
from funcs_TapiConnectivity.context_ConnectionUuidImpl import Context_ConnectionUuidImpl
from funcs_TapiConnectivity.context_ConnectionUuid_ConnectionportLocalid_ConnectionendpointNameValuenameImpl import Context_ConnectionUuid_ConnectionportLocalid_ConnectionendpointNameValuenameImpl
from funcs_TapiConnectivity.getserviceendpointlistImpl import GetserviceendpointlistImpl
from funcs_TapiConnectivity.context_ConnectivityserviceUuid_ExtensionsImpl import Context_ConnectivityserviceUuid_ExtensionsImpl
from funcs_TapiConnectivity.context_ConnectivityserviceUuid_ConnconstraintCostcharacteristicCostnameImpl import Context_ConnectivityserviceUuid_ConnconstraintCostcharacteristicCostnameImpl
from funcs_TapiConnectivity.context_ConnectivityserviceUuid_Connconstraint_IncludepathLocalid_ExtensionsImpl import Context_ConnectivityserviceUuid_Connconstraint_IncludepathLocalid_ExtensionsImpl
from funcs_TapiConnectivity.context_ConnectionUuid_ExtensionsExtensionsspecificationImpl import Context_ConnectionUuid_ExtensionsExtensionsspecificationImpl
from funcs_TapiConnectivity.context_ConnectionUuid_ConnectionportLocalid_ConnectionendpointLabelImpl import Context_ConnectionUuid_ConnectionportLocalid_ConnectionendpointLabelImpl
from funcs_TapiConnectivity.context_ConnectivityserviceUuid_StateImpl import Context_ConnectivityserviceUuid_StateImpl
from funcs_TapiConnectivity.getconnectivityservicelistImpl import GetconnectivityservicelistImpl
from funcs_TapiConnectivity.deleteconnectivityserviceImpl import DeleteconnectivityserviceImpl
from funcs_TapiConnectivity.context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_ExtensionsImpl import Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_ExtensionsImpl
from funcs_TapiConnectivity.context_ConnectivityserviceUuid_ServiceportLocalid_ExtensionsImpl import Context_ConnectivityserviceUuid_ServiceportLocalid_ExtensionsImpl
from funcs_TapiConnectivity.context_ConnectivityserviceUuidLabelImpl import Context_ConnectivityserviceUuidLabelImpl
from funcs_TapiConnectivity.context_ConnectivityserviceUuid_Connconstraint_ExtensionsExtensionsspecificationImpl import Context_ConnectivityserviceUuid_Connconstraint_ExtensionsExtensionsspecificationImpl
from funcs_TapiConnectivity.context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_LayerprotocolImpl import Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_LayerprotocolImpl
from funcs_TapiConnectivity.context_ConnectionUuid_ConnectionportLocalid_ExtensionsImpl import Context_ConnectionUuid_ConnectionportLocalid_ExtensionsImpl
from funcs_TapiConnectivity.context_ConnectivityserviceUuid_Connconstraint_ExcludepathImpl import Context_ConnectivityserviceUuid_Connconstraint_ExcludepathImpl
from funcs_TapiConnectivity.context_ConnectivityserviceUuid_ServiceportImpl import Context_ConnectivityserviceUuid_ServiceportImpl
from funcs_TapiConnectivity.context_ConnectivityserviceUuidNameImpl import Context_ConnectivityserviceUuidNameImpl
from funcs_TapiConnectivity.context_ConnectivityserviceUuidImpl import Context_ConnectivityserviceUuidImpl
from funcs_TapiConnectivity.context_ConnectivityserviceUuid_ConnconstraintCostcharacteristicImpl import Context_ConnectivityserviceUuid_ConnconstraintCostcharacteristicImpl
from funcs_TapiConnectivity.getconnectionendpointdetailsImpl import GetconnectionendpointdetailsImpl
from funcs_TapiConnectivity.context_ConnectivityserviceUuid_ConnconstraintLatencycharacteristicTrafficpropertynameImpl import Context_ConnectivityserviceUuid_ConnconstraintLatencycharacteristicTrafficpropertynameImpl
from funcs_TapiConnectivity.context_ConnectivityserviceUuid_Connconstraint_ExcludepathLocalid_ExtensionsExtensionsspecificationImpl import Context_ConnectivityserviceUuid_Connconstraint_ExcludepathLocalid_ExtensionsExtensionsspecificationImpl
from funcs_TapiConnectivity.context_ConnectionUuid_ConnectionportLocalidImpl import Context_ConnectionUuid_ConnectionportLocalidImpl
from funcs_TapiConnectivity.context_ConnectivityserviceUuid_ServiceportLocalid_ExtensionsExtensionsspecificationImpl import Context_ConnectivityserviceUuid_ServiceportLocalid_ExtensionsExtensionsspecificationImpl
from funcs_TapiConnectivity.context_ConnectivityserviceUuid_Connconstraint_IncludepathLocalidImpl import Context_ConnectivityserviceUuid_Connconstraint_IncludepathLocalidImpl
from funcs_TapiConnectivity.context_ConnectionUuid_ConnectionportLocalid_ConnectionendpointNameImpl import Context_ConnectionUuid_ConnectionportLocalid_ConnectionendpointNameImpl
from funcs_TapiConnectivity.context_ConnectionUuid_RouteLocalid_ExtensionsExtensionsspecificationImpl import Context_ConnectionUuid_RouteLocalid_ExtensionsExtensionsspecificationImpl
from funcs_TapiConnectivity.context_ConnectivityserviceUuid_Connconstraint_IncludepathImpl import Context_ConnectivityserviceUuid_Connconstraint_IncludepathImpl
from funcs_TapiConnectivity.context_ConnectivityserviceUuid_ExtensionsExtensionsspecificationImpl import Context_ConnectivityserviceUuid_ExtensionsExtensionsspecificationImpl
from funcs_TapiConnectivity.context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_StateImpl import Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_StateImpl
from funcs_TapiConnectivity.context_ConnectivityserviceUuid_ScheduleImpl import Context_ConnectivityserviceUuid_ScheduleImpl
from funcs_TapiConnectivity.context_ConnectivityserviceUuid_Connconstraint_ExcludepathLocalidImpl import Context_ConnectivityserviceUuid_Connconstraint_ExcludepathLocalidImpl
from funcs_TapiConnectivity.context_ConnectionUuid_ExtensionsImpl import Context_ConnectionUuid_ExtensionsImpl
from funcs_TapiConnectivity.createconnectivityserviceImpl import CreateconnectivityserviceImpl
from funcs_TapiConnectivity.context_ConnectionUuid_ConnectionportLocalid_ConnectionendpointLabelValuenameImpl import Context_ConnectionUuid_ConnectionportLocalid_ConnectionendpointLabelValuenameImpl
from funcs_TapiConnectivity.context_ConnectivityserviceImpl import Context_ConnectivityserviceImpl
from funcs_TapiConnectivity.context_ConnectionUuidNameValuenameImpl import Context_ConnectionUuidNameValuenameImpl
from funcs_TapiConnectivity.context_ConnectionUuid_ConnectionportLocalid_ConnectionendpointImpl import Context_ConnectionUuid_ConnectionportLocalid_ConnectionendpointImpl
from funcs_TapiConnectivity.context_ConnectionUuid_RouteLocalid_ExtensionsImpl import Context_ConnectionUuid_RouteLocalid_ExtensionsImpl
from funcs_TapiConnectivity.context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_LayerprotocolLocalid_ExtensionsImpl import Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_LayerprotocolLocalid_ExtensionsImpl
from funcs_TapiConnectivity.getserviceendpointdetailsImpl import GetserviceendpointdetailsImpl
from funcs_TapiConnectivity.getconnectivityservicedetailsImpl import GetconnectivityservicedetailsImpl
from funcs_TapiConnectivity.context_ConnectivityserviceUuid_ConnconstraintLatencycharacteristicImpl import Context_ConnectivityserviceUuid_ConnconstraintLatencycharacteristicImpl
from funcs_TapiConnectivity.context_ConnectionUuidNameImpl import Context_ConnectionUuidNameImpl
from funcs_TapiConnectivity.getconnectiondetailsImpl import GetconnectiondetailsImpl
from funcs_TapiConnectivity.context_ConnectivityserviceUuid_Connconstraint_ExtensionsImpl import Context_ConnectivityserviceUuid_Connconstraint_ExtensionsImpl
from funcs_TapiConnectivity.context_ConnectionUuid_RouteLocalidImpl import Context_ConnectionUuid_RouteLocalidImpl
from funcs_TapiConnectivity.context_ConnectionUuid_RouteImpl import Context_ConnectionUuid_RouteImpl
from funcs_TapiConnectivity.context_ConnectivityserviceUuid_Connconstraint_IncludepathLocalid_ExtensionsExtensionsspecificationImpl import Context_ConnectivityserviceUuid_Connconstraint_IncludepathLocalid_ExtensionsExtensionsspecificationImpl
from funcs_TapiConnectivity.context_ConnectionUuid_ConnectionportImpl import Context_ConnectionUuid_ConnectionportImpl
from funcs_TapiConnectivity.context_ConnectivityserviceUuidNameValuenameImpl import Context_ConnectivityserviceUuidNameValuenameImpl
from funcs_TapiConnectivity.context_ConnectionUuidLabelImpl import Context_ConnectionUuidLabelImpl
from funcs_TapiConnectivity.context_ConnectivityserviceUuid_Connconstraint_ExcludepathLocalid_ExtensionsImpl import Context_ConnectivityserviceUuid_Connconstraint_ExcludepathLocalid_ExtensionsImpl
from funcs_TapiConnectivity.context_ConnectionUuid_ConnectionportLocalid_ExtensionsExtensionsspecificationImpl import Context_ConnectionUuid_ConnectionportLocalid_ExtensionsExtensionsspecificationImpl
from funcs_TapiConnectivity.context_ConnectivityserviceUuid_ServiceportLocalidImpl import Context_ConnectivityserviceUuid_ServiceportLocalidImpl
from funcs_TapiConnectivity.context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_ExtensionsExtensionsspecificationImpl import Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_ExtensionsExtensionsspecificationImpl
from funcs_TapiConnectivity.context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_LayerprotocolLocalid_ExtensionsExtensionsspecificationImpl import Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_LayerprotocolLocalid_ExtensionsExtensionsspecificationImpl
from funcs_TapiConnectivity.context_ConnectionUuidLabelValuenameImpl import Context_ConnectionUuidLabelValuenameImpl
from funcs_TapiConnectivity.context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_LayerprotocolLocalidImpl import Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_LayerprotocolLocalidImpl
from funcs_TapiConnectivity.context_ConnectionImpl import Context_ConnectionImpl
from funcs_TapiConnectivity.context_ConnectivityserviceUuidLabelValuenameImpl import Context_ConnectivityserviceUuidLabelValuenameImpl
from funcs_TapiConnectivity.updateconnectivityserviceImpl import UpdateconnectivityserviceImpl

# CALLABLE OBJECTS
from objects_TapiConnectivity.linkPort import LinkPort
from objects_TapiConnectivity.capacity import Capacity
from objects_TapiConnectivity.transferCostPac import TransferCostPac
from objects_TapiConnectivity.transferCapacityPac import TransferCapacityPac
from objects_TapiConnectivity.timeRange import TimeRange
from objects_TapiConnectivity.layerProtocolTransitionPac import LayerProtocolTransitionPac
from objects_TapiConnectivity.transferTimingPac import TransferTimingPac
from objects_TapiConnectivity.getServiceEndPointDetailsRPCInputSchema import GetServiceEndPointDetailsRPCInputSchema
from objects_TapiConnectivity.transferIntegrityPac import TransferIntegrityPac
from objects_TapiConnectivity.nameAndValue import NameAndValue
from objects_TapiConnectivity.adminStatePac import AdminStatePac
from objects_TapiConnectivity._connectionSchema import _connectionSchema
from objects_TapiConnectivity.serviceEndPoint import ServiceEndPoint
from objects_TapiConnectivity.validationMechanism import ValidationMechanism
from objects_TapiConnectivity.node import Node
from objects_TapiConnectivity.resourceSpec import ResourceSpec
from objects_TapiConnectivity.teLink import TeLink
from objects_TapiConnectivity.costCharacteristic import CostCharacteristic
from objects_TapiConnectivity.getConnectivityServiceDetailsRPCInputSchema import GetConnectivityServiceDetailsRPCInputSchema
from objects_TapiConnectivity.latencyCharacteristic import LatencyCharacteristic
from objects_TapiConnectivity._connectivityServiceSchema import _connectivityServiceSchema
from objects_TapiConnectivity.connectivityService import ConnectivityService
from objects_TapiConnectivity.updateConnectivityServiceRPCInputSchema import UpdateConnectivityServiceRPCInputSchema
from objects_TapiConnectivity.connectionPort import ConnectionPort
from objects_TapiConnectivity.connectionEndPoint import ConnectionEndPoint
from objects_TapiConnectivity.link import Link
from objects_TapiConnectivity.localClass import LocalClass
from objects_TapiConnectivity.deleteConnectivityServiceRPCOutputSchema import DeleteConnectivityServiceRPCOutputSchema
from objects_TapiConnectivity.getConnectionEndPointDetailsRPCOutputSchema import GetConnectionEndPointDetailsRPCOutputSchema
from objects_TapiConnectivity.topology import Topology
from objects_TapiConnectivity.extensionsSpec import ExtensionsSpec
from objects_TapiConnectivity.connectivityConstraint import ConnectivityConstraint
from objects_TapiConnectivity.serviceSpec import ServiceSpec
from objects_TapiConnectivity.route import Route
from objects_TapiConnectivity.deleteConnectivityServiceRPCInputSchema import DeleteConnectivityServiceRPCInputSchema
from objects_TapiConnectivity.getServiceEndPointListRPCOutputSchema import GetServiceEndPointListRPCOutputSchema
from objects_TapiConnectivity.connection import Connection
from objects_TapiConnectivity.getConnectivityServiceDetailsRPCOutputSchema import GetConnectivityServiceDetailsRPCOutputSchema
from objects_TapiConnectivity.riskCharacteristic import RiskCharacteristic
from objects_TapiConnectivity.riskParameterPac import RiskParameterPac
from objects_TapiConnectivity.connectivityServicePort import ConnectivityServicePort
from objects_TapiConnectivity.getConnectionDetailsRPCOutputSchema import GetConnectionDetailsRPCOutputSchema
from objects_TapiConnectivity.getConnectionEndPointDetailsRPCInputSchema import GetConnectionEndPointDetailsRPCInputSchema
from objects_TapiConnectivity.operationalStatePac import OperationalStatePac
from objects_TapiConnectivity.globalClass import GlobalClass
from objects_TapiConnectivity.layerProtocol import LayerProtocol
from objects_TapiConnectivity.getServiceEndPointDetailsRPCOutputSchema import GetServiceEndPointDetailsRPCOutputSchema
from objects_TapiConnectivity.networkTopologyService import NetworkTopologyService
from objects_TapiConnectivity.nodeEdgePoint import NodeEdgePoint
from objects_TapiConnectivity.createConnectivityServiceRPCInputSchema import CreateConnectivityServiceRPCInputSchema
from objects_TapiConnectivity.lifecycleStatePac import LifecycleStatePac
from objects_TapiConnectivity.validationPac import ValidationPac
from objects_TapiConnectivity.getConnectivityServiceListRPCOutputSchema import GetConnectivityServiceListRPCOutputSchema
from objects_TapiConnectivity.getConnectionDetailsRPCInputSchema import GetConnectionDetailsRPCInputSchema
from objects_TapiConnectivity.createConnectivityServiceRPCOutputSchema import CreateConnectivityServiceRPCOutputSchema
from objects_TapiConnectivity.updateConnectivityServiceRPCOutputSchema import UpdateConnectivityServiceRPCOutputSchema

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


#/restconf/config/Context/_connection/(\w+)/_state/
class Context_ConnectionUuid_StateMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _state"
        try:
            response = Context_ConnectionUuid_StateImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connConstraint/
class Context_ConnectivityserviceUuid_ConnconstraintMethodView(MethodView):

    def put(self, uuid):
        print "Update operation of resource: _connConstraint"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_ConnectivityserviceUuid_ConnconstraintImpl.get(uuid)
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
                    Context_ConnectivityserviceUuid_ConnconstraintImpl.put(uuid, new_object)
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
                    Context_ConnectivityserviceUuid_ConnconstraintImpl.put(uuid, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid):
        print "Create operation of resource: _connConstraint"
        try:
            response = Context_ConnectivityserviceUuid_ConnconstraintImpl.get(uuid)
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
                    Context_ConnectivityserviceUuid_ConnconstraintImpl.post(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid):
        print "Delete operation of resource: _connConstraint"
        try:
            response=Context_ConnectivityserviceUuid_ConnconstraintImpl.delete(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid):
        print "Retrieve operation of resource: _connConstraint"
        try:
            response = Context_ConnectivityserviceUuid_ConnconstraintImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connConstraint/requestedCapacity/
class Context_ConnectivityserviceUuid_ConnconstraintRequestedcapacityMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: requestedCapacity"
        try:
            response = Context_ConnectivityserviceUuid_ConnconstraintRequestedcapacityImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connection/(\w+)/
class Context_ConnectionUuidMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _connection"
        try:
            response = Context_ConnectionUuidImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connection/(\w+)/_connectionPort/(\w+)/_connectionEndPoint/name/(\w+)/
class Context_ConnectionUuid_ConnectionportLocalid_ConnectionendpointNameValuenameMethodView(MethodView):

    def get(self, uuid, localId, valueName):
        print "Retrieve operation of resource: name"
        try:
            response = Context_ConnectionUuid_ConnectionportLocalid_ConnectionendpointNameValuenameImpl.get(uuid, localId, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/operations/getServiceEndPointList/
class GetserviceendpointlistMethodView(MethodView):

    def post(self, ):
        print "Create operation of resource: getServiceEndPointList"
        json_struct = request.get_json() #json parser.
        new_object = (json_struct) #It creates an object instance from the json_input data.
        response = GetserviceendpointlistImpl.post( new_object)
        return Successful('Successful operation','{"description":"Create operation of resource: getServiceEndPointList"}')


#/restconf/config/Context/_connectivityService/(\w+)/_extensions/
class Context_ConnectivityserviceUuid_ExtensionsMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_ConnectivityserviceUuid_ExtensionsImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connConstraint/costCharacteristic/(\w+)/
class Context_ConnectivityserviceUuid_ConnconstraintCostcharacteristicCostnameMethodView(MethodView):

    def get(self, uuid, costName):
        print "Retrieve operation of resource: costCharacteristic"
        try:
            response = Context_ConnectivityserviceUuid_ConnconstraintCostcharacteristicCostnameImpl.get(uuid, costName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connConstraint/_includePath/(\w+)/_extensions/
class Context_ConnectivityserviceUuid_Connconstraint_IncludepathLocalid_ExtensionsMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_ConnectivityserviceUuid_Connconstraint_IncludepathLocalid_ExtensionsImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connection/(\w+)/_extensions/(\w+)/
class Context_ConnectionUuid_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_ConnectionUuid_ExtensionsExtensionsspecificationImpl.get(uuid, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connection/(\w+)/_connectionPort/(\w+)/_connectionEndPoint/label/
class Context_ConnectionUuid_ConnectionportLocalid_ConnectionendpointLabelMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: label"
        try:
            response = Context_ConnectionUuid_ConnectionportLocalid_ConnectionendpointLabelImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_state/
class Context_ConnectivityserviceUuid_StateMethodView(MethodView):

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


#/restconf/operations/getConnectivityServiceList/
class GetconnectivityservicelistMethodView(MethodView):

    def post(self, ):
        print "Create operation of resource: getConnectivityServiceList"
        json_struct = request.get_json() #json parser.
        new_object = (json_struct) #It creates an object instance from the json_input data.
        response = GetconnectivityservicelistImpl.post( new_object)
        return Successful('Successful operation','{"description":"Create operation of resource: getConnectivityServiceList"}')


#/restconf/operations/deleteConnectivityService/
class DeleteconnectivityserviceMethodView(MethodView):

    def post(self, ):
        print "Create operation of resource: deleteConnectivityService"
        try:
            response = DeleteconnectivityserviceImpl.get()
        except KeyError as inst:
            if inst.args[0] != '':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(DeleteConnectivityServiceRPCInputSchema, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    DeleteconnectivityserviceImpl.post(new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))



#/restconf/config/Context/_connection/(\w+)/_connectionPort/(\w+)/_connectionEndPoint/_extensions/
class Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_ExtensionsMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_ExtensionsImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_servicePort/(\w+)/_extensions/
class Context_ConnectivityserviceUuid_ServiceportLocalid_ExtensionsMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_ConnectivityserviceUuid_ServiceportLocalid_ExtensionsImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/label/
class Context_ConnectivityserviceUuidLabelMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: label"
        try:
            response = Context_ConnectivityserviceUuidLabelImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connConstraint/_extensions/(\w+)/
class Context_ConnectivityserviceUuid_Connconstraint_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_ConnectivityserviceUuid_Connconstraint_ExtensionsExtensionsspecificationImpl.get(uuid, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connection/(\w+)/_connectionPort/(\w+)/_connectionEndPoint/_layerProtocol/
class Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_LayerprotocolMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _layerProtocol"
        try:
            response = Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_LayerprotocolImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connection/(\w+)/_connectionPort/(\w+)/_extensions/
class Context_ConnectionUuid_ConnectionportLocalid_ExtensionsMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_ConnectionUuid_ConnectionportLocalid_ExtensionsImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connConstraint/_excludePath/
class Context_ConnectivityserviceUuid_Connconstraint_ExcludepathMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _excludePath"
        try:
            response = Context_ConnectivityserviceUuid_Connconstraint_ExcludepathImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_servicePort/
class Context_ConnectivityserviceUuid_ServiceportMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _servicePort"
        try:
            response = Context_ConnectivityserviceUuid_ServiceportImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/name/
class Context_ConnectivityserviceUuidNameMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: name"
        try:
            response = Context_ConnectivityserviceUuidNameImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/
class Context_ConnectivityserviceUuidMethodView(MethodView):

    def put(self, uuid):
        print "Update operation of resource: _connectivityService"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_ConnectivityserviceUuidImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(_connectivityServiceSchema, json_struct)
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
            new_object = create_instance(_connectivityServiceSchema, json_struct, (uuid,'uuid'))
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


#/restconf/config/Context/_connectivityService/(\w+)/_connConstraint/costCharacteristic/
class Context_ConnectivityserviceUuid_ConnconstraintCostcharacteristicMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: costCharacteristic"
        try:
            response = Context_ConnectivityserviceUuid_ConnconstraintCostcharacteristicImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/operations/getConnectionEndPointDetails/
class GetconnectionendpointdetailsMethodView(MethodView):

    def post(self, ):
        print "Create operation of resource: getConnectionEndPointDetails"
        try:
            response = GetconnectionendpointdetailsImpl.get()
        except KeyError as inst:
            if inst.args[0] != '':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(GetConnectionEndPointDetailsRPCInputSchema, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    GetconnectionendpointdetailsImpl.post(new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))



#/restconf/config/Context/_connectivityService/(\w+)/_connConstraint/latencyCharacteristic/(\w+)/
class Context_ConnectivityserviceUuid_ConnconstraintLatencycharacteristicTrafficpropertynameMethodView(MethodView):

    def get(self, uuid, trafficPropertyName):
        print "Retrieve operation of resource: latencyCharacteristic"
        try:
            response = Context_ConnectivityserviceUuid_ConnconstraintLatencycharacteristicTrafficpropertynameImpl.get(uuid, trafficPropertyName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connConstraint/_excludePath/(\w+)/_extensions/(\w+)/
class Context_ConnectivityserviceUuid_Connconstraint_ExcludepathLocalid_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, localId, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_ConnectivityserviceUuid_Connconstraint_ExcludepathLocalid_ExtensionsExtensionsspecificationImpl.get(uuid, localId, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connection/(\w+)/_connectionPort/(\w+)/
class Context_ConnectionUuid_ConnectionportLocalidMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _connectionPort"
        try:
            response = Context_ConnectionUuid_ConnectionportLocalidImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_servicePort/(\w+)/_extensions/(\w+)/
class Context_ConnectivityserviceUuid_ServiceportLocalid_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, localId, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_ConnectivityserviceUuid_ServiceportLocalid_ExtensionsExtensionsspecificationImpl.get(uuid, localId, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connConstraint/_includePath/(\w+)/
class Context_ConnectivityserviceUuid_Connconstraint_IncludepathLocalidMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _includePath"
        try:
            response = Context_ConnectivityserviceUuid_Connconstraint_IncludepathLocalidImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connection/(\w+)/_connectionPort/(\w+)/_connectionEndPoint/name/
class Context_ConnectionUuid_ConnectionportLocalid_ConnectionendpointNameMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: name"
        try:
            response = Context_ConnectionUuid_ConnectionportLocalid_ConnectionendpointNameImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connection/(\w+)/_route/(\w+)/_extensions/(\w+)/
class Context_ConnectionUuid_RouteLocalid_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, localId, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_ConnectionUuid_RouteLocalid_ExtensionsExtensionsspecificationImpl.get(uuid, localId, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connConstraint/_includePath/
class Context_ConnectivityserviceUuid_Connconstraint_IncludepathMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _includePath"
        try:
            response = Context_ConnectivityserviceUuid_Connconstraint_IncludepathImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_extensions/(\w+)/
class Context_ConnectivityserviceUuid_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_ConnectivityserviceUuid_ExtensionsExtensionsspecificationImpl.get(uuid, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connection/(\w+)/_connectionPort/(\w+)/_connectionEndPoint/_state/
class Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_StateMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _state"
        try:
            response = Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_StateImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_schedule/
class Context_ConnectivityserviceUuid_ScheduleMethodView(MethodView):

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


#/restconf/config/Context/_connectivityService/(\w+)/_connConstraint/_excludePath/(\w+)/
class Context_ConnectivityserviceUuid_Connconstraint_ExcludepathLocalidMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _excludePath"
        try:
            response = Context_ConnectivityserviceUuid_Connconstraint_ExcludepathLocalidImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connection/(\w+)/_extensions/
class Context_ConnectionUuid_ExtensionsMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_ConnectionUuid_ExtensionsImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/operations/createConnectivityService/
class CreateconnectivityserviceMethodView(MethodView):

    def post(self, ):
        print "Create operation of resource: createConnectivityService"
        try:
            response = CreateconnectivityserviceImpl.get()
        except KeyError as inst:
            if inst.args[0] != '':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(CreateConnectivityServiceRPCInputSchema, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    CreateconnectivityserviceImpl.post(new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))



#/restconf/config/Context/_connection/(\w+)/_connectionPort/(\w+)/_connectionEndPoint/label/(\w+)/
class Context_ConnectionUuid_ConnectionportLocalid_ConnectionendpointLabelValuenameMethodView(MethodView):

    def get(self, uuid, localId, valueName):
        print "Retrieve operation of resource: label"
        try:
            response = Context_ConnectionUuid_ConnectionportLocalid_ConnectionendpointLabelValuenameImpl.get(uuid, localId, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/
class Context_ConnectivityserviceMethodView(MethodView):

    def get(self, ):
        print "Retrieve operation of resource: _connectivityService"
        try:
            response = Context_ConnectivityserviceImpl.get()
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connection/(\w+)/name/(\w+)/
class Context_ConnectionUuidNameValuenameMethodView(MethodView):

    def get(self, uuid, valueName):
        print "Retrieve operation of resource: name"
        try:
            response = Context_ConnectionUuidNameValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connection/(\w+)/_connectionPort/(\w+)/_connectionEndPoint/
class Context_ConnectionUuid_ConnectionportLocalid_ConnectionendpointMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _connectionEndPoint"
        try:
            response = Context_ConnectionUuid_ConnectionportLocalid_ConnectionendpointImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connection/(\w+)/_route/(\w+)/_extensions/
class Context_ConnectionUuid_RouteLocalid_ExtensionsMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_ConnectionUuid_RouteLocalid_ExtensionsImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connection/(\w+)/_connectionPort/(\w+)/_connectionEndPoint/_layerProtocol/(\w+)/_extensions/
class Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_LayerprotocolLocalid_ExtensionsMethodView(MethodView):

    def get(self, uuid, localId, localId2):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_LayerprotocolLocalid_ExtensionsImpl.get(uuid, localId, localId2)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/operations/getServiceEndPointDetails/
class GetserviceendpointdetailsMethodView(MethodView):

    def post(self, ):
        print "Create operation of resource: getServiceEndPointDetails"
        try:
            response = GetserviceendpointdetailsImpl.get()
        except KeyError as inst:
            if inst.args[0] != '':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(GetServiceEndPointDetailsRPCInputSchema, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    GetserviceendpointdetailsImpl.post(new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))



#/restconf/operations/getConnectivityServiceDetails/
class GetconnectivityservicedetailsMethodView(MethodView):

    def post(self, ):
        print "Create operation of resource: getConnectivityServiceDetails"
        try:
            response = GetconnectivityservicedetailsImpl.get()
        except KeyError as inst:
            if inst.args[0] != '':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(GetConnectivityServiceDetailsRPCInputSchema, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    GetconnectivityservicedetailsImpl.post(new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))



#/restconf/config/Context/_connectivityService/(\w+)/_connConstraint/latencyCharacteristic/
class Context_ConnectivityserviceUuid_ConnconstraintLatencycharacteristicMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: latencyCharacteristic"
        try:
            response = Context_ConnectivityserviceUuid_ConnconstraintLatencycharacteristicImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connection/(\w+)/name/
class Context_ConnectionUuidNameMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: name"
        try:
            response = Context_ConnectionUuidNameImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/operations/getConnectionDetails/
class GetconnectiondetailsMethodView(MethodView):

    def post(self, ):
        print "Create operation of resource: getConnectionDetails"
        try:
            response = GetconnectiondetailsImpl.get()
        except KeyError as inst:
            if inst.args[0] != '':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(GetConnectionDetailsRPCInputSchema, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    GetconnectiondetailsImpl.post(new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))



#/restconf/config/Context/_connectivityService/(\w+)/_connConstraint/_extensions/
class Context_ConnectivityserviceUuid_Connconstraint_ExtensionsMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_ConnectivityserviceUuid_Connconstraint_ExtensionsImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connection/(\w+)/_route/(\w+)/
class Context_ConnectionUuid_RouteLocalidMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _route"
        try:
            response = Context_ConnectionUuid_RouteLocalidImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connection/(\w+)/_route/
class Context_ConnectionUuid_RouteMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _route"
        try:
            response = Context_ConnectionUuid_RouteImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connConstraint/_includePath/(\w+)/_extensions/(\w+)/
class Context_ConnectivityserviceUuid_Connconstraint_IncludepathLocalid_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, localId, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_ConnectivityserviceUuid_Connconstraint_IncludepathLocalid_ExtensionsExtensionsspecificationImpl.get(uuid, localId, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connection/(\w+)/_connectionPort/
class Context_ConnectionUuid_ConnectionportMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _connectionPort"
        try:
            response = Context_ConnectionUuid_ConnectionportImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/name/(\w+)/
class Context_ConnectivityserviceUuidNameValuenameMethodView(MethodView):

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


#/restconf/config/Context/_connection/(\w+)/label/
class Context_ConnectionUuidLabelMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: label"
        try:
            response = Context_ConnectionUuidLabelImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_connConstraint/_excludePath/(\w+)/_extensions/
class Context_ConnectivityserviceUuid_Connconstraint_ExcludepathLocalid_ExtensionsMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_ConnectivityserviceUuid_Connconstraint_ExcludepathLocalid_ExtensionsImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connection/(\w+)/_connectionPort/(\w+)/_extensions/(\w+)/
class Context_ConnectionUuid_ConnectionportLocalid_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, localId, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_ConnectionUuid_ConnectionportLocalid_ExtensionsExtensionsspecificationImpl.get(uuid, localId, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/_servicePort/(\w+)/
class Context_ConnectivityserviceUuid_ServiceportLocalidMethodView(MethodView):

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


#/restconf/config/Context/_connection/(\w+)/_connectionPort/(\w+)/_connectionEndPoint/_extensions/(\w+)/
class Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, localId, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_ExtensionsExtensionsspecificationImpl.get(uuid, localId, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connection/(\w+)/_connectionPort/(\w+)/_connectionEndPoint/_layerProtocol/(\w+)/_extensions/(\w+)/
class Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_LayerprotocolLocalid_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, localId, localId2, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_LayerprotocolLocalid_ExtensionsExtensionsspecificationImpl.get(uuid, localId, localId2, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connection/(\w+)/label/(\w+)/
class Context_ConnectionUuidLabelValuenameMethodView(MethodView):

    def get(self, uuid, valueName):
        print "Retrieve operation of resource: label"
        try:
            response = Context_ConnectionUuidLabelValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connection/(\w+)/_connectionPort/(\w+)/_connectionEndPoint/_layerProtocol/(\w+)/
class Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_LayerprotocolLocalidMethodView(MethodView):

    def get(self, uuid, localId, localId2):
        print "Retrieve operation of resource: _layerProtocol"
        try:
            response = Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_LayerprotocolLocalidImpl.get(uuid, localId, localId2)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connection/
class Context_ConnectionMethodView(MethodView):

    def get(self, ):
        print "Retrieve operation of resource: _connection"
        try:
            response = Context_ConnectionImpl.get()
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_connectivityService/(\w+)/label/(\w+)/
class Context_ConnectivityserviceUuidLabelValuenameMethodView(MethodView):

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


#/restconf/operations/updateConnectivityService/
class UpdateconnectivityserviceMethodView(MethodView):

    def post(self, ):
        print "Create operation of resource: updateConnectivityService"
        try:
            response = UpdateconnectivityserviceImpl.get()
        except KeyError as inst:
            if inst.args[0] != '':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(UpdateConnectivityServiceRPCInputSchema, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    UpdateconnectivityserviceImpl.post(new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))




getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connection/<uuid>/_state/", view_func = globals()["Context_ConnectionUuid_StateMethodView"].as_view('"Context_ConnectionUuid_State"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connConstraint/", view_func = globals()["Context_ConnectivityserviceUuid_ConnconstraintMethodView"].as_view('"Context_ConnectivityserviceUuid_Connconstraint"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connConstraint/requestedCapacity/", view_func = globals()["Context_ConnectivityserviceUuid_ConnconstraintRequestedcapacityMethodView"].as_view('"Context_ConnectivityserviceUuid_ConnconstraintRequestedcapacity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connection/<uuid>/", view_func = globals()["Context_ConnectionUuidMethodView"].as_view('"Context_ConnectionUuid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connection/<uuid>/_connectionPort/<localId>/_connectionEndPoint/name/<valueName>/", view_func = globals()["Context_ConnectionUuid_ConnectionportLocalid_ConnectionendpointNameValuenameMethodView"].as_view('"Context_ConnectionUuid_ConnectionportLocalid_ConnectionendpointNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getServiceEndPointList/", view_func = globals()["GetserviceendpointlistMethodView"].as_view('"Getserviceendpointlist"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_extensions/", view_func = globals()["Context_ConnectivityserviceUuid_ExtensionsMethodView"].as_view('"Context_ConnectivityserviceUuid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connConstraint/costCharacteristic/<costName>/", view_func = globals()["Context_ConnectivityserviceUuid_ConnconstraintCostcharacteristicCostnameMethodView"].as_view('"Context_ConnectivityserviceUuid_ConnconstraintCostcharacteristicCostname"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connConstraint/_includePath/<localId>/_extensions/", view_func = globals()["Context_ConnectivityserviceUuid_Connconstraint_IncludepathLocalid_ExtensionsMethodView"].as_view('"Context_ConnectivityserviceUuid_Connconstraint_IncludepathLocalid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connection/<uuid>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_ConnectionUuid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_ConnectionUuid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connection/<uuid>/_connectionPort/<localId>/_connectionEndPoint/label/", view_func = globals()["Context_ConnectionUuid_ConnectionportLocalid_ConnectionendpointLabelMethodView"].as_view('"Context_ConnectionUuid_ConnectionportLocalid_ConnectionendpointLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_state/", view_func = globals()["Context_ConnectivityserviceUuid_StateMethodView"].as_view('"Context_ConnectivityserviceUuid_State"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getConnectivityServiceList/", view_func = globals()["GetconnectivityservicelistMethodView"].as_view('"Getconnectivityservicelist"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/deleteConnectivityService/", view_func = globals()["DeleteconnectivityserviceMethodView"].as_view('"Deleteconnectivityservice"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connection/<uuid>/_connectionPort/<localId>/_connectionEndPoint/_extensions/", view_func = globals()["Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_ExtensionsMethodView"].as_view('"Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_servicePort/<localId>/_extensions/", view_func = globals()["Context_ConnectivityserviceUuid_ServiceportLocalid_ExtensionsMethodView"].as_view('"Context_ConnectivityserviceUuid_ServiceportLocalid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/label/", view_func = globals()["Context_ConnectivityserviceUuidLabelMethodView"].as_view('"Context_ConnectivityserviceUuidLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connConstraint/_extensions/<extensionsSpecification>/", view_func = globals()["Context_ConnectivityserviceUuid_Connconstraint_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_ConnectivityserviceUuid_Connconstraint_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connection/<uuid>/_connectionPort/<localId>/_connectionEndPoint/_layerProtocol/", view_func = globals()["Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_LayerprotocolMethodView"].as_view('"Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_Layerprotocol"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connection/<uuid>/_connectionPort/<localId>/_extensions/", view_func = globals()["Context_ConnectionUuid_ConnectionportLocalid_ExtensionsMethodView"].as_view('"Context_ConnectionUuid_ConnectionportLocalid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connConstraint/_excludePath/", view_func = globals()["Context_ConnectivityserviceUuid_Connconstraint_ExcludepathMethodView"].as_view('"Context_ConnectivityserviceUuid_Connconstraint_Excludepath"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_servicePort/", view_func = globals()["Context_ConnectivityserviceUuid_ServiceportMethodView"].as_view('"Context_ConnectivityserviceUuid_Serviceport"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/name/", view_func = globals()["Context_ConnectivityserviceUuidNameMethodView"].as_view('"Context_ConnectivityserviceUuidName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/", view_func = globals()["Context_ConnectivityserviceUuidMethodView"].as_view('"Context_ConnectivityserviceUuid"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connConstraint/costCharacteristic/", view_func = globals()["Context_ConnectivityserviceUuid_ConnconstraintCostcharacteristicMethodView"].as_view('"Context_ConnectivityserviceUuid_ConnconstraintCostcharacteristic"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getConnectionEndPointDetails/", view_func = globals()["GetconnectionendpointdetailsMethodView"].as_view('"Getconnectionendpointdetails"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connConstraint/latencyCharacteristic/<trafficPropertyName>/", view_func = globals()["Context_ConnectivityserviceUuid_ConnconstraintLatencycharacteristicTrafficpropertynameMethodView"].as_view('"Context_ConnectivityserviceUuid_ConnconstraintLatencycharacteristicTrafficpropertyname"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connConstraint/_excludePath/<localId>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_ConnectivityserviceUuid_Connconstraint_ExcludepathLocalid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_ConnectivityserviceUuid_Connconstraint_ExcludepathLocalid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connection/<uuid>/_connectionPort/<localId>/", view_func = globals()["Context_ConnectionUuid_ConnectionportLocalidMethodView"].as_view('"Context_ConnectionUuid_ConnectionportLocalid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_servicePort/<localId>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_ConnectivityserviceUuid_ServiceportLocalid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_ConnectivityserviceUuid_ServiceportLocalid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connConstraint/_includePath/<localId>/", view_func = globals()["Context_ConnectivityserviceUuid_Connconstraint_IncludepathLocalidMethodView"].as_view('"Context_ConnectivityserviceUuid_Connconstraint_IncludepathLocalid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connection/<uuid>/_connectionPort/<localId>/_connectionEndPoint/name/", view_func = globals()["Context_ConnectionUuid_ConnectionportLocalid_ConnectionendpointNameMethodView"].as_view('"Context_ConnectionUuid_ConnectionportLocalid_ConnectionendpointName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connection/<uuid>/_route/<localId>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_ConnectionUuid_RouteLocalid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_ConnectionUuid_RouteLocalid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connConstraint/_includePath/", view_func = globals()["Context_ConnectivityserviceUuid_Connconstraint_IncludepathMethodView"].as_view('"Context_ConnectivityserviceUuid_Connconstraint_Includepath"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_ConnectivityserviceUuid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_ConnectivityserviceUuid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connection/<uuid>/_connectionPort/<localId>/_connectionEndPoint/_state/", view_func = globals()["Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_StateMethodView"].as_view('"Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_State"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_schedule/", view_func = globals()["Context_ConnectivityserviceUuid_ScheduleMethodView"].as_view('"Context_ConnectivityserviceUuid_Schedule"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connConstraint/_excludePath/<localId>/", view_func = globals()["Context_ConnectivityserviceUuid_Connconstraint_ExcludepathLocalidMethodView"].as_view('"Context_ConnectivityserviceUuid_Connconstraint_ExcludepathLocalid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connection/<uuid>/_extensions/", view_func = globals()["Context_ConnectionUuid_ExtensionsMethodView"].as_view('"Context_ConnectionUuid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/createConnectivityService/", view_func = globals()["CreateconnectivityserviceMethodView"].as_view('"Createconnectivityservice"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connection/<uuid>/_connectionPort/<localId>/_connectionEndPoint/label/<valueName>/", view_func = globals()["Context_ConnectionUuid_ConnectionportLocalid_ConnectionendpointLabelValuenameMethodView"].as_view('"Context_ConnectionUuid_ConnectionportLocalid_ConnectionendpointLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/", view_func = globals()["Context_ConnectivityserviceMethodView"].as_view('"Context_Connectivityservice"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connection/<uuid>/name/<valueName>/", view_func = globals()["Context_ConnectionUuidNameValuenameMethodView"].as_view('"Context_ConnectionUuidNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connection/<uuid>/_connectionPort/<localId>/_connectionEndPoint/", view_func = globals()["Context_ConnectionUuid_ConnectionportLocalid_ConnectionendpointMethodView"].as_view('"Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connection/<uuid>/_route/<localId>/_extensions/", view_func = globals()["Context_ConnectionUuid_RouteLocalid_ExtensionsMethodView"].as_view('"Context_ConnectionUuid_RouteLocalid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connection/<uuid>/_connectionPort/<localId>/_connectionEndPoint/_layerProtocol/<localId2>/_extensions/", view_func = globals()["Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_LayerprotocolLocalid_ExtensionsMethodView"].as_view('"Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_LayerprotocolLocalid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getServiceEndPointDetails/", view_func = globals()["GetserviceendpointdetailsMethodView"].as_view('"Getserviceendpointdetails"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getConnectivityServiceDetails/", view_func = globals()["GetconnectivityservicedetailsMethodView"].as_view('"Getconnectivityservicedetails"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connConstraint/latencyCharacteristic/", view_func = globals()["Context_ConnectivityserviceUuid_ConnconstraintLatencycharacteristicMethodView"].as_view('"Context_ConnectivityserviceUuid_ConnconstraintLatencycharacteristic"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connection/<uuid>/name/", view_func = globals()["Context_ConnectionUuidNameMethodView"].as_view('"Context_ConnectionUuidName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getConnectionDetails/", view_func = globals()["GetconnectiondetailsMethodView"].as_view('"Getconnectiondetails"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connConstraint/_extensions/", view_func = globals()["Context_ConnectivityserviceUuid_Connconstraint_ExtensionsMethodView"].as_view('"Context_ConnectivityserviceUuid_Connconstraint_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connection/<uuid>/_route/<localId>/", view_func = globals()["Context_ConnectionUuid_RouteLocalidMethodView"].as_view('"Context_ConnectionUuid_RouteLocalid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connection/<uuid>/_route/", view_func = globals()["Context_ConnectionUuid_RouteMethodView"].as_view('"Context_ConnectionUuid_Route"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connConstraint/_includePath/<localId>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_ConnectivityserviceUuid_Connconstraint_IncludepathLocalid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_ConnectivityserviceUuid_Connconstraint_IncludepathLocalid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connection/<uuid>/_connectionPort/", view_func = globals()["Context_ConnectionUuid_ConnectionportMethodView"].as_view('"Context_ConnectionUuid_Connectionport"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/name/<valueName>/", view_func = globals()["Context_ConnectivityserviceUuidNameValuenameMethodView"].as_view('"Context_ConnectivityserviceUuidNameValuename"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connection/<uuid>/label/", view_func = globals()["Context_ConnectionUuidLabelMethodView"].as_view('"Context_ConnectionUuidLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_connConstraint/_excludePath/<localId>/_extensions/", view_func = globals()["Context_ConnectivityserviceUuid_Connconstraint_ExcludepathLocalid_ExtensionsMethodView"].as_view('"Context_ConnectivityserviceUuid_Connconstraint_ExcludepathLocalid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connection/<uuid>/_connectionPort/<localId>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_ConnectionUuid_ConnectionportLocalid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_ConnectionUuid_ConnectionportLocalid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/_servicePort/<localId>/", view_func = globals()["Context_ConnectivityserviceUuid_ServiceportLocalidMethodView"].as_view('"Context_ConnectivityserviceUuid_ServiceportLocalid"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connection/<uuid>/_connectionPort/<localId>/_connectionEndPoint/_extensions/<extensionsSpecification>/", view_func = globals()["Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connection/<uuid>/_connectionPort/<localId>/_connectionEndPoint/_layerProtocol/<localId2>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_LayerprotocolLocalid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_LayerprotocolLocalid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connection/<uuid>/label/<valueName>/", view_func = globals()["Context_ConnectionUuidLabelValuenameMethodView"].as_view('"Context_ConnectionUuidLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connection/<uuid>/_connectionPort/<localId>/_connectionEndPoint/_layerProtocol/<localId2>/", view_func = globals()["Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_LayerprotocolLocalidMethodView"].as_view('"Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_LayerprotocolLocalid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connection/", view_func = globals()["Context_ConnectionMethodView"].as_view('"Context_Connection"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_connectivityService/<uuid>/label/<valueName>/", view_func = globals()["Context_ConnectivityserviceUuidLabelValuenameMethodView"].as_view('"Context_ConnectivityserviceUuidLabelValuename"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/updateConnectivityService/", view_func = globals()["UpdateconnectivityserviceMethodView"].as_view('"Updateconnectivityservice"'+'"_api"'), methods=['POST'])
