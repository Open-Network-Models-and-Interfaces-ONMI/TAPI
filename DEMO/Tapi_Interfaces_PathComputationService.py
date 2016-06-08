from flask import json, Blueprint, request, Response
from flask.views import MethodView
import sys
from objects_common.keyedArrayType import KeyedArrayKeyError

import base64
import re

# BACKEND FUNCTIONS
from funcs_Tapi_Interfaces_PathComputationService.computep2PpathImpl import Computep2PpathImpl
from funcs_Tapi_Interfaces_PathComputationService.optimizep2PpathImpl import Optimizep2PpathImpl

# CALLABLE OBJECTS
from objects_Tapi_Interfaces_PathComputationService.linkPort import LinkPort
from objects_Tapi_Interfaces_PathComputationService.virtualNetworkServicePort import VirtualNetworkServicePort
from objects_Tapi_Interfaces_PathComputationService.capacity import Capacity
from objects_Tapi_Interfaces_PathComputationService.transferCostPac import TransferCostPac
from objects_Tapi_Interfaces_PathComputationService.notification import Notification
from objects_Tapi_Interfaces_PathComputationService.timeRange import TimeRange
from objects_Tapi_Interfaces_PathComputationService.layerProtocolTransitionPac import LayerProtocolTransitionPac
from objects_Tapi_Interfaces_PathComputationService.transferTimingPac import TransferTimingPac
from objects_Tapi_Interfaces_PathComputationService.transferIntegrityPac import TransferIntegrityPac
from objects_Tapi_Interfaces_PathComputationService.nameAndValue import NameAndValue
from objects_Tapi_Interfaces_PathComputationService.adminStatePac import AdminStatePac
from objects_Tapi_Interfaces_PathComputationService.serviceEndPoint import ServiceEndPoint
from objects_Tapi_Interfaces_PathComputationService.validationMechanism import ValidationMechanism
from objects_Tapi_Interfaces_PathComputationService.node import Node
from objects_Tapi_Interfaces_PathComputationService.teLink import TeLink
from objects_Tapi_Interfaces_PathComputationService.costCharacteristic import CostCharacteristic
from objects_Tapi_Interfaces_PathComputationService.transferCapacityPac import TransferCapacityPac
from objects_Tapi_Interfaces_PathComputationService.optimizeP2PPathRPCInputSchema import OptimizeP2PPathRPCInputSchema
from objects_Tapi_Interfaces_PathComputationService.connectivityService import ConnectivityService
from objects_Tapi_Interfaces_PathComputationService.connectionPort import ConnectionPort
from objects_Tapi_Interfaces_PathComputationService.ltpSpec import LtpSpec
from objects_Tapi_Interfaces_PathComputationService.connectionEndPoint import ConnectionEndPoint
from objects_Tapi_Interfaces_PathComputationService.link import Link
from objects_Tapi_Interfaces_PathComputationService.localClass import LocalClass
from objects_Tapi_Interfaces_PathComputationService.path import Path
from objects_Tapi_Interfaces_PathComputationService.topology import Topology
from objects_Tapi_Interfaces_PathComputationService.queuingLatency import QueuingLatency
from objects_Tapi_Interfaces_PathComputationService.connectivityConstraint import ConnectivityConstraint
from objects_Tapi_Interfaces_PathComputationService.virtualNetworkService import VirtualNetworkService
from objects_Tapi_Interfaces_PathComputationService.route import Route
from objects_Tapi_Interfaces_PathComputationService.computeP2PPathRPCOutputSchema import ComputeP2PPathRPCOutputSchema
from objects_Tapi_Interfaces_PathComputationService.connection import Connection
from objects_Tapi_Interfaces_PathComputationService.computeP2PPathRPCInputSchema import ComputeP2PPathRPCInputSchema
from objects_Tapi_Interfaces_PathComputationService.pathOptimizationConstraint import PathOptimizationConstraint
from objects_Tapi_Interfaces_PathComputationService.pathObjectiveFunction import PathObjectiveFunction
from objects_Tapi_Interfaces_PathComputationService.virtualNetworkConstraint import VirtualNetworkConstraint
from objects_Tapi_Interfaces_PathComputationService.riskCharacteristic import RiskCharacteristic
from objects_Tapi_Interfaces_PathComputationService.optimizeP2PPathRPCOutputSchema import OptimizeP2PPathRPCOutputSchema
from objects_Tapi_Interfaces_PathComputationService.riskParameterPac import RiskParameterPac
from objects_Tapi_Interfaces_PathComputationService.connectivityServicePort import ConnectivityServicePort
from objects_Tapi_Interfaces_PathComputationService.nameAndValueChange import NameAndValueChange
from objects_Tapi_Interfaces_PathComputationService.operationalStatePac import OperationalStatePac
from objects_Tapi_Interfaces_PathComputationService.globalClass import GlobalClass
from objects_Tapi_Interfaces_PathComputationService.layerProtocol import LayerProtocol
from objects_Tapi_Interfaces_PathComputationService.notificationSubscriptionService import NotificationSubscriptionService
from objects_Tapi_Interfaces_PathComputationService.nodeEdgePoint import NodeEdgePoint
from objects_Tapi_Interfaces_PathComputationService.lpSpec import LpSpec
from objects_Tapi_Interfaces_PathComputationService.lifecycleStatePac import LifecycleStatePac
from objects_Tapi_Interfaces_PathComputationService.validationPac import ValidationPac
from objects_Tapi_Interfaces_PathComputationService.subscriptionFilter import SubscriptionFilter

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


#/restconf/operations/computeP2PPath/
class Computep2Ppath(MethodView):

    def post(self, ):
        print "Create operation of resource: computeP2PPath"
        try:
            response = Computep2PpathImpl.get()
        except KeyError as inst:
            if inst.args[0] != '':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(ComputeP2PPathRPCInputSchema, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Computep2PpathImpl.post(new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))



#/restconf/operations/optimizeP2PPath/
class Optimizep2Ppath(MethodView):

    def post(self, ):
        print "Create operation of resource: optimizeP2PPath"
        try:
            response = Optimizep2PpathImpl.get()
        except KeyError as inst:
            if inst.args[0] != '':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(OptimizeP2PPathRPCInputSchema, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Optimizep2PpathImpl.post(new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))




getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/computeP2PPath/", view_func = globals()["Computep2Ppath"].as_view('"Computep2Ppath"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/optimizeP2PPath/", view_func = globals()["Optimizep2Ppath"].as_view('"Optimizep2Ppath"'+'"_api"'), methods=['POST'])
