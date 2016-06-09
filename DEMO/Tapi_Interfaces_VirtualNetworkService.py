from flask import json, Blueprint, request, Response
from flask.views import MethodView
import sys
from objects_common.keyedArrayType import KeyedArrayKeyError

import base64
import re

# BACKEND FUNCTIONS
from funcs_Tapi_Interfaces_VirtualNetworkService.getvirtualnetworkservicedetailsImpl import GetvirtualnetworkservicedetailsImpl
from funcs_Tapi_Interfaces_VirtualNetworkService.getvirtualnetworkservicelistImpl import GetvirtualnetworkservicelistImpl
from funcs_Tapi_Interfaces_VirtualNetworkService.deletevirtualnetworkserviceImpl import DeletevirtualnetworkserviceImpl
from funcs_Tapi_Interfaces_VirtualNetworkService.createvirtualnetworkserviceImpl import CreatevirtualnetworkserviceImpl

# CALLABLE OBJECTS
from objects_Tapi_Interfaces_VirtualNetworkService.linkPort import LinkPort
from objects_Tapi_Interfaces_VirtualNetworkService.virtualNetworkServicePort import VirtualNetworkServicePort
from objects_Tapi_Interfaces_VirtualNetworkService.createVirtualNetworkServiceRPCOutputSchema import CreateVirtualNetworkServiceRPCOutputSchema
from objects_Tapi_Interfaces_VirtualNetworkService.capacity import Capacity
from objects_Tapi_Interfaces_VirtualNetworkService.transferCostPac import TransferCostPac
from objects_Tapi_Interfaces_VirtualNetworkService.notification import Notification
from objects_Tapi_Interfaces_VirtualNetworkService.timeRange import TimeRange
from objects_Tapi_Interfaces_VirtualNetworkService.layerProtocolTransitionPac import LayerProtocolTransitionPac
from objects_Tapi_Interfaces_VirtualNetworkService.transferTimingPac import TransferTimingPac
from objects_Tapi_Interfaces_VirtualNetworkService.transferIntegrityPac import TransferIntegrityPac
from objects_Tapi_Interfaces_VirtualNetworkService.nameAndValue import NameAndValue
from objects_Tapi_Interfaces_VirtualNetworkService.adminStatePac import AdminStatePac
from objects_Tapi_Interfaces_VirtualNetworkService.serviceEndPoint import ServiceEndPoint
from objects_Tapi_Interfaces_VirtualNetworkService.validationMechanism import ValidationMechanism
from objects_Tapi_Interfaces_VirtualNetworkService.node import Node
from objects_Tapi_Interfaces_VirtualNetworkService.teLink import TeLink
from objects_Tapi_Interfaces_VirtualNetworkService.costCharacteristic import CostCharacteristic
from objects_Tapi_Interfaces_VirtualNetworkService.connectionEndPoint import ConnectionEndPoint
from objects_Tapi_Interfaces_VirtualNetworkService.transferCapacityPac import TransferCapacityPac
from objects_Tapi_Interfaces_VirtualNetworkService.connectivityService import ConnectivityService
from objects_Tapi_Interfaces_VirtualNetworkService.getVirtualNetworkServiceListRPCOutputSchema import GetVirtualNetworkServiceListRPCOutputSchema
from objects_Tapi_Interfaces_VirtualNetworkService.connectionPort import ConnectionPort
from objects_Tapi_Interfaces_VirtualNetworkService.ltpSpec import LtpSpec
from objects_Tapi_Interfaces_VirtualNetworkService.pathComputationService import PathComputationService
from objects_Tapi_Interfaces_VirtualNetworkService.link import Link
from objects_Tapi_Interfaces_VirtualNetworkService.localClass import LocalClass
from objects_Tapi_Interfaces_VirtualNetworkService.deleteVirtualNetworkServiceRPCOutputSchema import DeleteVirtualNetworkServiceRPCOutputSchema
from objects_Tapi_Interfaces_VirtualNetworkService.path import Path
from objects_Tapi_Interfaces_VirtualNetworkService.topology import Topology
from objects_Tapi_Interfaces_VirtualNetworkService.queuingLatency import QueuingLatency
from objects_Tapi_Interfaces_VirtualNetworkService.connectivityConstraint import ConnectivityConstraint
from objects_Tapi_Interfaces_VirtualNetworkService.pathCompServicePort import PathCompServicePort
from objects_Tapi_Interfaces_VirtualNetworkService.virtualNetworkService import VirtualNetworkService
from objects_Tapi_Interfaces_VirtualNetworkService.route import Route
from objects_Tapi_Interfaces_VirtualNetworkService.connection import Connection
from objects_Tapi_Interfaces_VirtualNetworkService.pathOptimizationConstraint import PathOptimizationConstraint
from objects_Tapi_Interfaces_VirtualNetworkService.pathObjectiveFunction import PathObjectiveFunction
from objects_Tapi_Interfaces_VirtualNetworkService.virtualNetworkConstraint import VirtualNetworkConstraint
from objects_Tapi_Interfaces_VirtualNetworkService.riskCharacteristic import RiskCharacteristic
from objects_Tapi_Interfaces_VirtualNetworkService.riskParameterPac import RiskParameterPac
from objects_Tapi_Interfaces_VirtualNetworkService.connectivityServicePort import ConnectivityServicePort
from objects_Tapi_Interfaces_VirtualNetworkService.deleteVirtualNetworkServiceRPCInputSchema import DeleteVirtualNetworkServiceRPCInputSchema
from objects_Tapi_Interfaces_VirtualNetworkService.nameAndValueChange import NameAndValueChange
from objects_Tapi_Interfaces_VirtualNetworkService.operationalStatePac import OperationalStatePac
from objects_Tapi_Interfaces_VirtualNetworkService.globalClass import GlobalClass
from objects_Tapi_Interfaces_VirtualNetworkService.layerProtocol import LayerProtocol
from objects_Tapi_Interfaces_VirtualNetworkService.notificationSubscriptionService import NotificationSubscriptionService
from objects_Tapi_Interfaces_VirtualNetworkService.nodeEdgePoint import NodeEdgePoint
from objects_Tapi_Interfaces_VirtualNetworkService.getVirtualNetworkServiceDetailsRPCInputSchema import GetVirtualNetworkServiceDetailsRPCInputSchema
from objects_Tapi_Interfaces_VirtualNetworkService.lpSpec import LpSpec
from objects_Tapi_Interfaces_VirtualNetworkService.lifecycleStatePac import LifecycleStatePac
from objects_Tapi_Interfaces_VirtualNetworkService.getVirtualNetworkServiceDetailsRPCOutputSchema import GetVirtualNetworkServiceDetailsRPCOutputSchema
from objects_Tapi_Interfaces_VirtualNetworkService.validationPac import ValidationPac
from objects_Tapi_Interfaces_VirtualNetworkService.createVirtualNetworkServiceRPCInputSchema import CreateVirtualNetworkServiceRPCInputSchema
from objects_Tapi_Interfaces_VirtualNetworkService.subscriptionFilter import SubscriptionFilter

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


#/restconf/operations/getVirtualNetworkServiceDetails/
class Getvirtualnetworkservicedetails(MethodView):

    def post(self, ):
        print "Create operation of resource: getVirtualNetworkServiceDetails"
        try:
            response = GetvirtualnetworkservicedetailsImpl.get()
        except KeyError as inst:
            if inst.args[0] != '':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(GetVirtualNetworkServiceDetailsRPCInputSchema, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    GetvirtualnetworkservicedetailsImpl.post(new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))



#/restconf/operations/getVirtualNetworkServiceList/
class Getvirtualnetworkservicelist(MethodView):

    def post(self, ):
        print "Create operation of resource: getVirtualNetworkServiceList"
        json_struct = request.get_json() #json parser.
        new_object = (json_struct) #It creates an object instance from the json_input data.
        response = GetvirtualnetworkservicelistImpl.post( new_object)
        return Successful('Successful operation','{"description":"Create operation of resource: getVirtualNetworkServiceList"}')


#/restconf/operations/deleteVirtualNetworkService/
class Deletevirtualnetworkservice(MethodView):

    def post(self, ):
        print "Create operation of resource: deleteVirtualNetworkService"
        try:
            response = DeletevirtualnetworkserviceImpl.get()
        except KeyError as inst:
            if inst.args[0] != '':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(DeleteVirtualNetworkServiceRPCInputSchema, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    DeletevirtualnetworkserviceImpl.post(new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))



#/restconf/operations/createVirtualNetworkService/
class Createvirtualnetworkservice(MethodView):

    def post(self, ):
        print "Create operation of resource: createVirtualNetworkService"
        try:
            response = CreatevirtualnetworkserviceImpl.get()
        except KeyError as inst:
            if inst.args[0] != '':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(CreateVirtualNetworkServiceRPCInputSchema, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    CreatevirtualnetworkserviceImpl.post(new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))




getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getVirtualNetworkServiceDetails/", view_func = globals()["Getvirtualnetworkservicedetails"].as_view('"Getvirtualnetworkservicedetails"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getVirtualNetworkServiceList/", view_func = globals()["Getvirtualnetworkservicelist"].as_view('"Getvirtualnetworkservicelist"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/deleteVirtualNetworkService/", view_func = globals()["Deletevirtualnetworkservice"].as_view('"Deletevirtualnetworkservice"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/createVirtualNetworkService/", view_func = globals()["Createvirtualnetworkservice"].as_view('"Createvirtualnetworkservice"'+'"_api"'), methods=['POST'])
