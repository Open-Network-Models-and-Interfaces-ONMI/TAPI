from flask import json, Blueprint, request, Response
from flask.views import MethodView
import sys
from objects_common.keyedArrayType import KeyedArrayKeyError

import base64
import re

# BACKEND FUNCTIONS
from funcs_Tapi_Interfaces_NotificationSubscriptionService.getnotificationlistImpl import GetnotificationlistImpl
from funcs_Tapi_Interfaces_NotificationSubscriptionService.updatenotificationsubscriptionserviceImpl import UpdatenotificationsubscriptionserviceImpl
from funcs_Tapi_Interfaces_NotificationSubscriptionService.createnotificationsubscriptionserviceImpl import CreatenotificationsubscriptionserviceImpl
from funcs_Tapi_Interfaces_NotificationSubscriptionService.deletenotificationsubscriptionserviceImpl import DeletenotificationsubscriptionserviceImpl
from funcs_Tapi_Interfaces_NotificationSubscriptionService.getsupportednotificationtypesImpl import GetsupportednotificationtypesImpl
from funcs_Tapi_Interfaces_NotificationSubscriptionService.getnotificationsubscriptionservicelistImpl import GetnotificationsubscriptionservicelistImpl
from funcs_Tapi_Interfaces_NotificationSubscriptionService.getnotificationsubscriptionservicedetailsImpl import GetnotificationsubscriptionservicedetailsImpl

# CALLABLE OBJECTS
from objects_Tapi_Interfaces_NotificationSubscriptionService.linkPort import LinkPort
from objects_Tapi_Interfaces_NotificationSubscriptionService.virtualNetworkServicePort import VirtualNetworkServicePort
from objects_Tapi_Interfaces_NotificationSubscriptionService.capacity import Capacity
from objects_Tapi_Interfaces_NotificationSubscriptionService.transferCostPac import TransferCostPac
from objects_Tapi_Interfaces_NotificationSubscriptionService.notification import Notification
from objects_Tapi_Interfaces_NotificationSubscriptionService.timeRange import TimeRange
from objects_Tapi_Interfaces_NotificationSubscriptionService.layerProtocolTransitionPac import LayerProtocolTransitionPac
from objects_Tapi_Interfaces_NotificationSubscriptionService.transferTimingPac import TransferTimingPac
from objects_Tapi_Interfaces_NotificationSubscriptionService.deleteNotificationSubscriptionServiceRPCInputSchema import DeleteNotificationSubscriptionServiceRPCInputSchema
from objects_Tapi_Interfaces_NotificationSubscriptionService.transferIntegrityPac import TransferIntegrityPac
from objects_Tapi_Interfaces_NotificationSubscriptionService.nameAndValue import NameAndValue
from objects_Tapi_Interfaces_NotificationSubscriptionService.adminStatePac import AdminStatePac
from objects_Tapi_Interfaces_NotificationSubscriptionService.getNotificationListRPCInputSchema import GetNotificationListRPCInputSchema
from objects_Tapi_Interfaces_NotificationSubscriptionService.serviceEndPoint import ServiceEndPoint
from objects_Tapi_Interfaces_NotificationSubscriptionService.validationMechanism import ValidationMechanism
from objects_Tapi_Interfaces_NotificationSubscriptionService.node import Node
from objects_Tapi_Interfaces_NotificationSubscriptionService.teLink import TeLink
from objects_Tapi_Interfaces_NotificationSubscriptionService.costCharacteristic import CostCharacteristic
from objects_Tapi_Interfaces_NotificationSubscriptionService.connectionEndPoint import ConnectionEndPoint
from objects_Tapi_Interfaces_NotificationSubscriptionService.transferCapacityPac import TransferCapacityPac
from objects_Tapi_Interfaces_NotificationSubscriptionService.createNotificationSubscriptionServiceRPCOutputSchema import CreateNotificationSubscriptionServiceRPCOutputSchema
from objects_Tapi_Interfaces_NotificationSubscriptionService.connectivityService import ConnectivityService
from objects_Tapi_Interfaces_NotificationSubscriptionService.getNotificationSubscriptionServiceDetailsRPCInputSchema import GetNotificationSubscriptionServiceDetailsRPCInputSchema
from objects_Tapi_Interfaces_NotificationSubscriptionService.connectionPort import ConnectionPort
from objects_Tapi_Interfaces_NotificationSubscriptionService.ltpSpec import LtpSpec
from objects_Tapi_Interfaces_NotificationSubscriptionService.pathComputationService import PathComputationService
from objects_Tapi_Interfaces_NotificationSubscriptionService.updateNotificationSubscriptionServiceRPCInputSchema import UpdateNotificationSubscriptionServiceRPCInputSchema
from objects_Tapi_Interfaces_NotificationSubscriptionService.link import Link
from objects_Tapi_Interfaces_NotificationSubscriptionService.localClass import LocalClass
from objects_Tapi_Interfaces_NotificationSubscriptionService.path import Path
from objects_Tapi_Interfaces_NotificationSubscriptionService.getNotificationSubscriptionServiceDetailsRPCOutputSchema import GetNotificationSubscriptionServiceDetailsRPCOutputSchema
from objects_Tapi_Interfaces_NotificationSubscriptionService.topology import Topology
from objects_Tapi_Interfaces_NotificationSubscriptionService.queuingLatency import QueuingLatency
from objects_Tapi_Interfaces_NotificationSubscriptionService.connectivityConstraint import ConnectivityConstraint
from objects_Tapi_Interfaces_NotificationSubscriptionService.pathCompServicePort import PathCompServicePort
from objects_Tapi_Interfaces_NotificationSubscriptionService.virtualNetworkService import VirtualNetworkService
from objects_Tapi_Interfaces_NotificationSubscriptionService.route import Route
from objects_Tapi_Interfaces_NotificationSubscriptionService.connection import Connection
from objects_Tapi_Interfaces_NotificationSubscriptionService.deleteNotificationSubscriptionServiceRPCOutputSchema import DeleteNotificationSubscriptionServiceRPCOutputSchema
from objects_Tapi_Interfaces_NotificationSubscriptionService.pathOptimizationConstraint import PathOptimizationConstraint
from objects_Tapi_Interfaces_NotificationSubscriptionService.pathObjectiveFunction import PathObjectiveFunction
from objects_Tapi_Interfaces_NotificationSubscriptionService.virtualNetworkConstraint import VirtualNetworkConstraint
from objects_Tapi_Interfaces_NotificationSubscriptionService.getNotificationSubscriptionServiceListRPCOutputSchema import GetNotificationSubscriptionServiceListRPCOutputSchema
from objects_Tapi_Interfaces_NotificationSubscriptionService.riskCharacteristic import RiskCharacteristic
from objects_Tapi_Interfaces_NotificationSubscriptionService.riskParameterPac import RiskParameterPac
from objects_Tapi_Interfaces_NotificationSubscriptionService.connectivityServicePort import ConnectivityServicePort
from objects_Tapi_Interfaces_NotificationSubscriptionService.createNotificationSubscriptionServiceRPCInputSchema import CreateNotificationSubscriptionServiceRPCInputSchema
from objects_Tapi_Interfaces_NotificationSubscriptionService.nameAndValueChange import NameAndValueChange
from objects_Tapi_Interfaces_NotificationSubscriptionService.operationalStatePac import OperationalStatePac
from objects_Tapi_Interfaces_NotificationSubscriptionService.globalClass import GlobalClass
from objects_Tapi_Interfaces_NotificationSubscriptionService.layerProtocol import LayerProtocol
from objects_Tapi_Interfaces_NotificationSubscriptionService.notificationSubscriptionService import NotificationSubscriptionService
from objects_Tapi_Interfaces_NotificationSubscriptionService.nodeEdgePoint import NodeEdgePoint
from objects_Tapi_Interfaces_NotificationSubscriptionService.getSupportedNotificationTypesRPCOutputSchema import GetSupportedNotificationTypesRPCOutputSchema
from objects_Tapi_Interfaces_NotificationSubscriptionService.getNotificationListRPCOutputSchema import GetNotificationListRPCOutputSchema
from objects_Tapi_Interfaces_NotificationSubscriptionService.lpSpec import LpSpec
from objects_Tapi_Interfaces_NotificationSubscriptionService.lifecycleStatePac import LifecycleStatePac
from objects_Tapi_Interfaces_NotificationSubscriptionService.validationPac import ValidationPac
from objects_Tapi_Interfaces_NotificationSubscriptionService.subscriptionFilter import SubscriptionFilter
from objects_Tapi_Interfaces_NotificationSubscriptionService.updateNotificationSubscriptionServiceRPCOutputSchema import UpdateNotificationSubscriptionServiceRPCOutputSchema

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


#/restconf/operations/getNotificationList/
class Getnotificationlist(MethodView):

    def post(self, ):
        print "Create operation of resource: getNotificationList"
        try:
            response = GetnotificationlistImpl.get()
        except KeyError as inst:
            if inst.args[0] != '':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(GetNotificationListRPCInputSchema, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    GetnotificationlistImpl.post(new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))



#/restconf/operations/updateNotificationSubscriptionService/
class Updatenotificationsubscriptionservice(MethodView):

    def post(self, ):
        print "Create operation of resource: updateNotificationSubscriptionService"
        try:
            response = UpdatenotificationsubscriptionserviceImpl.get()
        except KeyError as inst:
            if inst.args[0] != '':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(UpdateNotificationSubscriptionServiceRPCInputSchema, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    UpdatenotificationsubscriptionserviceImpl.post(new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))



#/restconf/operations/createNotificationSubscriptionService/
class Createnotificationsubscriptionservice(MethodView):

    def post(self, ):
        print "Create operation of resource: createNotificationSubscriptionService"
        try:
            response = CreatenotificationsubscriptionserviceImpl.get()
        except KeyError as inst:
            if inst.args[0] != '':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(CreateNotificationSubscriptionServiceRPCInputSchema, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    CreatenotificationsubscriptionserviceImpl.post(new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))



#/restconf/operations/deleteNotificationSubscriptionService/
class Deletenotificationsubscriptionservice(MethodView):

    def post(self, ):
        print "Create operation of resource: deleteNotificationSubscriptionService"
        try:
            response = DeletenotificationsubscriptionserviceImpl.get()
        except KeyError as inst:
            if inst.args[0] != '':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(DeleteNotificationSubscriptionServiceRPCInputSchema, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    DeletenotificationsubscriptionserviceImpl.post(new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))



#/restconf/operations/getSupportedNotificationTypes/
class Getsupportednotificationtypes(MethodView):

    def post(self, ):
        print "Create operation of resource: getSupportedNotificationTypes"
        json_struct = request.get_json() #json parser.
        new_object = (json_struct) #It creates an object instance from the json_input data.
        response = GetsupportednotificationtypesImpl.post( new_object)
        return Successful('Successful operation','{"description":"Create operation of resource: getSupportedNotificationTypes"}')


#/restconf/operations/getNotificationSubscriptionServiceList/
class Getnotificationsubscriptionservicelist(MethodView):

    def post(self, ):
        print "Create operation of resource: getNotificationSubscriptionServiceList"
        json_struct = request.get_json() #json parser.
        new_object = (json_struct) #It creates an object instance from the json_input data.
        response = GetnotificationsubscriptionservicelistImpl.post( new_object)
        return Successful('Successful operation','{"description":"Create operation of resource: getNotificationSubscriptionServiceList"}')


#/restconf/operations/getNotificationSubscriptionServiceDetails/
class Getnotificationsubscriptionservicedetails(MethodView):

    def post(self, ):
        print "Create operation of resource: getNotificationSubscriptionServiceDetails"
        try:
            response = GetnotificationsubscriptionservicedetailsImpl.get()
        except KeyError as inst:
            if inst.args[0] != '':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(GetNotificationSubscriptionServiceDetailsRPCInputSchema, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    GetnotificationsubscriptionservicedetailsImpl.post(new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))




getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getNotificationList/", view_func = globals()["Getnotificationlist"].as_view('"Getnotificationlist"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/updateNotificationSubscriptionService/", view_func = globals()["Updatenotificationsubscriptionservice"].as_view('"Updatenotificationsubscriptionservice"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/createNotificationSubscriptionService/", view_func = globals()["Createnotificationsubscriptionservice"].as_view('"Createnotificationsubscriptionservice"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/deleteNotificationSubscriptionService/", view_func = globals()["Deletenotificationsubscriptionservice"].as_view('"Deletenotificationsubscriptionservice"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getSupportedNotificationTypes/", view_func = globals()["Getsupportednotificationtypes"].as_view('"Getsupportednotificationtypes"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getNotificationSubscriptionServiceList/", view_func = globals()["Getnotificationsubscriptionservicelist"].as_view('"Getnotificationsubscriptionservicelist"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getNotificationSubscriptionServiceDetails/", view_func = globals()["Getnotificationsubscriptionservicedetails"].as_view('"Getnotificationsubscriptionservicedetails"'+'"_api"'), methods=['POST'])
