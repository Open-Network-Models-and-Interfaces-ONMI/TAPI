from flask import json, Blueprint, request, Response
from flask.views import MethodView
import sys
from objects_common.keyedArrayType import KeyedArrayKeyError

import base64
import re

# BACKEND FUNCTIONS
from funcs_Tapi_Interfaces_ConnectivityService.getserviceendpointlistImpl import GetserviceendpointlistImpl
from funcs_Tapi_Interfaces_ConnectivityService.getconnectivityservicedetailsImpl import GetconnectivityservicedetailsImpl
from funcs_Tapi_Interfaces_ConnectivityService.getserviceendpointdetailsImpl import GetserviceendpointdetailsImpl
from funcs_Tapi_Interfaces_ConnectivityService.getconnectivityservicelistImpl import GetconnectivityservicelistImpl
from funcs_Tapi_Interfaces_ConnectivityService.createconnectivityserviceImpl import CreateconnectivityserviceImpl
from funcs_Tapi_Interfaces_ConnectivityService.updateconnectivityserviceImpl import UpdateconnectivityserviceImpl
from funcs_Tapi_Interfaces_ConnectivityService.getconnectionendpointdetailsImpl import GetconnectionendpointdetailsImpl
from funcs_Tapi_Interfaces_ConnectivityService.deleteconnectivityserviceImpl import DeleteconnectivityserviceImpl
from funcs_Tapi_Interfaces_ConnectivityService.getconnectiondetailsImpl import GetconnectiondetailsImpl

# CALLABLE OBJECTS
from objects_Tapi_Interfaces_ConnectivityService.linkPort import LinkPort
from objects_Tapi_Interfaces_ConnectivityService.virtualNetworkServicePort import VirtualNetworkServicePort
from objects_Tapi_Interfaces_ConnectivityService.capacity import Capacity
from objects_Tapi_Interfaces_ConnectivityService.transferCostPac import TransferCostPac
from objects_Tapi_Interfaces_ConnectivityService.layerProtocolTransitionPac import LayerProtocolTransitionPac
from objects_Tapi_Interfaces_ConnectivityService.createConnectivityServiceRPCInputSchema import CreateConnectivityServiceRPCInputSchema
from objects_Tapi_Interfaces_ConnectivityService.transferTimingPac import TransferTimingPac
from objects_Tapi_Interfaces_ConnectivityService.getServiceEndPointDetailsRPCInputSchema import GetServiceEndPointDetailsRPCInputSchema
from objects_Tapi_Interfaces_ConnectivityService.transferIntegrityPac import TransferIntegrityPac
from objects_Tapi_Interfaces_ConnectivityService.nameAndValue import NameAndValue
from objects_Tapi_Interfaces_ConnectivityService.adminStatePac import AdminStatePac
from objects_Tapi_Interfaces_ConnectivityService.serviceEndPoint import ServiceEndPoint
from objects_Tapi_Interfaces_ConnectivityService.validationMechanism import ValidationMechanism
from objects_Tapi_Interfaces_ConnectivityService.node import Node
from objects_Tapi_Interfaces_ConnectivityService.teLink import TeLink
from objects_Tapi_Interfaces_ConnectivityService.costCharacteristic import CostCharacteristic
from objects_Tapi_Interfaces_ConnectivityService.getConnectivityServiceDetailsRPCInputSchema import GetConnectivityServiceDetailsRPCInputSchema
from objects_Tapi_Interfaces_ConnectivityService.connectivityService import ConnectivityService
from objects_Tapi_Interfaces_ConnectivityService.updateConnectivityServiceRPCInputSchema import UpdateConnectivityServiceRPCInputSchema
from objects_Tapi_Interfaces_ConnectivityService.connectionPort import ConnectionPort
from objects_Tapi_Interfaces_ConnectivityService.ltpSpec import LtpSpec
from objects_Tapi_Interfaces_ConnectivityService.connectionEndPoint import ConnectionEndPoint
from objects_Tapi_Interfaces_ConnectivityService.link import Link
from objects_Tapi_Interfaces_ConnectivityService.localClass import LocalClass
from objects_Tapi_Interfaces_ConnectivityService.deleteConnectivityServiceRPCOutputSchema import DeleteConnectivityServiceRPCOutputSchema
from objects_Tapi_Interfaces_ConnectivityService.path import Path
from objects_Tapi_Interfaces_ConnectivityService.getConnectionEndPointDetailsRPCOutputSchema import GetConnectionEndPointDetailsRPCOutputSchema
from objects_Tapi_Interfaces_ConnectivityService.topology import Topology
from objects_Tapi_Interfaces_ConnectivityService.queuingLatency import QueuingLatency
from objects_Tapi_Interfaces_ConnectivityService.connectivityConstraint import ConnectivityConstraint
from objects_Tapi_Interfaces_ConnectivityService.virtualNetworkService import VirtualNetworkService
from objects_Tapi_Interfaces_ConnectivityService.route import Route
from objects_Tapi_Interfaces_ConnectivityService.getConnectivityServiceDetailsRPCOutputSchema import GetConnectivityServiceDetailsRPCOutputSchema
from objects_Tapi_Interfaces_ConnectivityService.deleteConnectivityServiceRPCInputSchema import DeleteConnectivityServiceRPCInputSchema
from objects_Tapi_Interfaces_ConnectivityService.getServiceEndPointListRPCOutputSchema import GetServiceEndPointListRPCOutputSchema
from objects_Tapi_Interfaces_ConnectivityService.connection import Connection
from objects_Tapi_Interfaces_ConnectivityService.scheduleInfo import ScheduleInfo
from objects_Tapi_Interfaces_ConnectivityService.pathOptimizationConstraint import PathOptimizationConstraint
from objects_Tapi_Interfaces_ConnectivityService.pathObjectiveFunction import PathObjectiveFunction
from objects_Tapi_Interfaces_ConnectivityService.virtualNetworkConstraint import VirtualNetworkConstraint
from objects_Tapi_Interfaces_ConnectivityService.riskCharacteristic import RiskCharacteristic
from objects_Tapi_Interfaces_ConnectivityService.riskParameterPac import RiskParameterPac
from objects_Tapi_Interfaces_ConnectivityService.connectivityServicePort import ConnectivityServicePort
from objects_Tapi_Interfaces_ConnectivityService.getConnectionDetailsRPCOutputSchema import GetConnectionDetailsRPCOutputSchema
from objects_Tapi_Interfaces_ConnectivityService.getConnectionEndPointDetailsRPCInputSchema import GetConnectionEndPointDetailsRPCInputSchema
from objects_Tapi_Interfaces_ConnectivityService.operationalStatePac import OperationalStatePac
from objects_Tapi_Interfaces_ConnectivityService.globalClass import GlobalClass
from objects_Tapi_Interfaces_ConnectivityService.layerProtocol import LayerProtocol
from objects_Tapi_Interfaces_ConnectivityService.getServiceEndPointDetailsRPCOutputSchema import GetServiceEndPointDetailsRPCOutputSchema
from objects_Tapi_Interfaces_ConnectivityService.transferCapacityPac import TransferCapacityPac
from objects_Tapi_Interfaces_ConnectivityService.nodeEdgePoint import NodeEdgePoint
from objects_Tapi_Interfaces_ConnectivityService.lpSpec import LpSpec
from objects_Tapi_Interfaces_ConnectivityService.lifecycleStatePac import LifecycleStatePac
from objects_Tapi_Interfaces_ConnectivityService.validationPac import ValidationPac
from objects_Tapi_Interfaces_ConnectivityService.getConnectivityServiceListRPCOutputSchema import GetConnectivityServiceListRPCOutputSchema
from objects_Tapi_Interfaces_ConnectivityService.getConnectionDetailsRPCInputSchema import GetConnectionDetailsRPCInputSchema
from objects_Tapi_Interfaces_ConnectivityService.createConnectivityServiceRPCOutputSchema import CreateConnectivityServiceRPCOutputSchema
from objects_Tapi_Interfaces_ConnectivityService.updateConnectivityServiceRPCOutputSchema import UpdateConnectivityServiceRPCOutputSchema

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


#/restconf/operations/getServiceEndPointList/
class Getserviceendpointlist(MethodView):

    def post(self, ):
        print "Create operation of resource: getServiceEndPointList"
        json_struct = request.get_json() #json parser.
        new_object = (json_struct) #It creates an object instance from the json_input data.
        response = GetserviceendpointlistImpl.post( new_object)
        return Successful('Successful operation','{"description":"Create operation of resource: getServiceEndPointList"}')


#/restconf/operations/getConnectivityServiceDetails/
class Getconnectivityservicedetails(MethodView):

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



#/restconf/operations/getServiceEndPointDetails/
class Getserviceendpointdetails(MethodView):

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



#/restconf/operations/getConnectivityServiceList/
class Getconnectivityservicelist(MethodView):

    def post(self, ):
        print "Create operation of resource: getConnectivityServiceList"
        json_struct = request.get_json() #json parser.
        new_object = (json_struct) #It creates an object instance from the json_input data.
        response = GetconnectivityservicelistImpl.post( new_object)
        return Successful('Successful operation','{"description":"Create operation of resource: getConnectivityServiceList"}')


#/restconf/operations/createConnectivityService/
class Createconnectivityservice(MethodView):

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



#/restconf/operations/updateConnectivityService/
class Updateconnectivityservice(MethodView):

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



#/restconf/operations/getConnectionEndPointDetails/
class Getconnectionendpointdetails(MethodView):

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



#/restconf/operations/deleteConnectivityService/
class Deleteconnectivityservice(MethodView):

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



#/restconf/operations/getConnectionDetails/
class Getconnectiondetails(MethodView):

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




getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getServiceEndPointList/", view_func = globals()["Getserviceendpointlist"].as_view('"Getserviceendpointlist"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getConnectivityServiceDetails/", view_func = globals()["Getconnectivityservicedetails"].as_view('"Getconnectivityservicedetails"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getServiceEndPointDetails/", view_func = globals()["Getserviceendpointdetails"].as_view('"Getserviceendpointdetails"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getConnectivityServiceList/", view_func = globals()["Getconnectivityservicelist"].as_view('"Getconnectivityservicelist"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/createConnectivityService/", view_func = globals()["Createconnectivityservice"].as_view('"Createconnectivityservice"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/updateConnectivityService/", view_func = globals()["Updateconnectivityservice"].as_view('"Updateconnectivityservice"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getConnectionEndPointDetails/", view_func = globals()["Getconnectionendpointdetails"].as_view('"Getconnectionendpointdetails"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/deleteConnectivityService/", view_func = globals()["Deleteconnectivityservice"].as_view('"Deleteconnectivityservice"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getConnectionDetails/", view_func = globals()["Getconnectiondetails"].as_view('"Getconnectiondetails"'+'"_api"'), methods=['POST'])
