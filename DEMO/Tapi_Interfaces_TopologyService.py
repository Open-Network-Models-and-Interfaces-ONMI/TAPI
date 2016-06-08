from flask import json, Blueprint, request, Response
from flask.views import MethodView
import sys
from objects_common.keyedArrayType import KeyedArrayKeyError

import base64
import re

# BACKEND FUNCTIONS
from funcs_Tapi_Interfaces_TopologyService.gettopologylistImpl import GettopologylistImpl
from funcs_Tapi_Interfaces_TopologyService.getnodedetailsImpl import GetnodedetailsImpl
from funcs_Tapi_Interfaces_TopologyService.gettopologydetailsImpl import GettopologydetailsImpl
from funcs_Tapi_Interfaces_TopologyService.getlinkdetailsImpl import GetlinkdetailsImpl
from funcs_Tapi_Interfaces_TopologyService.getnodeedgepointdetailsImpl import GetnodeedgepointdetailsImpl

# CALLABLE OBJECTS
from objects_Tapi_Interfaces_TopologyService.getNodeDetailsRPCInputSchema import GetNodeDetailsRPCInputSchema
from objects_Tapi_Interfaces_TopologyService.linkPort import LinkPort
from objects_Tapi_Interfaces_TopologyService.virtualNetworkServicePort import VirtualNetworkServicePort
from objects_Tapi_Interfaces_TopologyService.capacity import Capacity
from objects_Tapi_Interfaces_TopologyService.transferCostPac import TransferCostPac
from objects_Tapi_Interfaces_TopologyService.notification import Notification
from objects_Tapi_Interfaces_TopologyService.timeRange import TimeRange
from objects_Tapi_Interfaces_TopologyService.layerProtocolTransitionPac import LayerProtocolTransitionPac
from objects_Tapi_Interfaces_TopologyService.getNodeDetailsRPCOutputSchema import GetNodeDetailsRPCOutputSchema
from objects_Tapi_Interfaces_TopologyService.getTopologyDetailsRPCInputSchema import GetTopologyDetailsRPCInputSchema
from objects_Tapi_Interfaces_TopologyService.transferTimingPac import TransferTimingPac
from objects_Tapi_Interfaces_TopologyService.transferIntegrityPac import TransferIntegrityPac
from objects_Tapi_Interfaces_TopologyService.nameAndValue import NameAndValue
from objects_Tapi_Interfaces_TopologyService.adminStatePac import AdminStatePac
from objects_Tapi_Interfaces_TopologyService.getTopologyListRPCOutputSchema import GetTopologyListRPCOutputSchema
from objects_Tapi_Interfaces_TopologyService.serviceEndPoint import ServiceEndPoint
from objects_Tapi_Interfaces_TopologyService.validationMechanism import ValidationMechanism
from objects_Tapi_Interfaces_TopologyService.node import Node
from objects_Tapi_Interfaces_TopologyService.teLink import TeLink
from objects_Tapi_Interfaces_TopologyService.costCharacteristic import CostCharacteristic
from objects_Tapi_Interfaces_TopologyService.transferCapacityPac import TransferCapacityPac
from objects_Tapi_Interfaces_TopologyService.connectivityService import ConnectivityService
from objects_Tapi_Interfaces_TopologyService.connectionPort import ConnectionPort
from objects_Tapi_Interfaces_TopologyService.ltpSpec import LtpSpec
from objects_Tapi_Interfaces_TopologyService.connectionEndPoint import ConnectionEndPoint
from objects_Tapi_Interfaces_TopologyService.link import Link
from objects_Tapi_Interfaces_TopologyService.localClass import LocalClass
from objects_Tapi_Interfaces_TopologyService.path import Path
from objects_Tapi_Interfaces_TopologyService.topology import Topology
from objects_Tapi_Interfaces_TopologyService.queuingLatency import QueuingLatency
from objects_Tapi_Interfaces_TopologyService.connectivityConstraint import ConnectivityConstraint
from objects_Tapi_Interfaces_TopologyService.getNodeEdgePointDetailsRPCOutputSchema import GetNodeEdgePointDetailsRPCOutputSchema
from objects_Tapi_Interfaces_TopologyService.virtualNetworkService import VirtualNetworkService
from objects_Tapi_Interfaces_TopologyService.route import Route
from objects_Tapi_Interfaces_TopologyService.getLinkDetailsRPCOutputSchema import GetLinkDetailsRPCOutputSchema
from objects_Tapi_Interfaces_TopologyService.connection import Connection
from objects_Tapi_Interfaces_TopologyService.getLinkDetailsRPCInputSchema import GetLinkDetailsRPCInputSchema
from objects_Tapi_Interfaces_TopologyService.pathOptimizationConstraint import PathOptimizationConstraint
from objects_Tapi_Interfaces_TopologyService.pathObjectiveFunction import PathObjectiveFunction
from objects_Tapi_Interfaces_TopologyService.virtualNetworkConstraint import VirtualNetworkConstraint
from objects_Tapi_Interfaces_TopologyService.riskCharacteristic import RiskCharacteristic
from objects_Tapi_Interfaces_TopologyService.riskParameterPac import RiskParameterPac
from objects_Tapi_Interfaces_TopologyService.connectivityServicePort import ConnectivityServicePort
from objects_Tapi_Interfaces_TopologyService.nameAndValueChange import NameAndValueChange
from objects_Tapi_Interfaces_TopologyService.operationalStatePac import OperationalStatePac
from objects_Tapi_Interfaces_TopologyService.globalClass import GlobalClass
from objects_Tapi_Interfaces_TopologyService.layerProtocol import LayerProtocol
from objects_Tapi_Interfaces_TopologyService.getTopologyDetailsRPCOutputSchema import GetTopologyDetailsRPCOutputSchema
from objects_Tapi_Interfaces_TopologyService.notificationSubscriptionService import NotificationSubscriptionService
from objects_Tapi_Interfaces_TopologyService.nodeEdgePoint import NodeEdgePoint
from objects_Tapi_Interfaces_TopologyService.getNodeEdgePointDetailsRPCInputSchema import GetNodeEdgePointDetailsRPCInputSchema
from objects_Tapi_Interfaces_TopologyService.lpSpec import LpSpec
from objects_Tapi_Interfaces_TopologyService.lifecycleStatePac import LifecycleStatePac
from objects_Tapi_Interfaces_TopologyService.validationPac import ValidationPac
from objects_Tapi_Interfaces_TopologyService.subscriptionFilter import SubscriptionFilter

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


#/restconf/operations/getTopologyList/
class Gettopologylist(MethodView):

    def post(self, ):
        print "Create operation of resource: getTopologyList"
        json_struct = request.get_json() #json parser.
        new_object = (json_struct) #It creates an object instance from the json_input data.
        response = GettopologylistImpl.post( new_object)
        return Successful('Successful operation','{"description":"Create operation of resource: getTopologyList"}')


#/restconf/operations/getNodeDetails/
class Getnodedetails(MethodView):

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



#/restconf/operations/getTopologyDetails/
class Gettopologydetails(MethodView):

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



#/restconf/operations/getLinkDetails/
class Getlinkdetails(MethodView):

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



#/restconf/operations/getNodeEdgePointDetails/
class Getnodeedgepointdetails(MethodView):

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




getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getTopologyList/", view_func = globals()["Gettopologylist"].as_view('"Gettopologylist"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getNodeDetails/", view_func = globals()["Getnodedetails"].as_view('"Getnodedetails"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getTopologyDetails/", view_func = globals()["Gettopologydetails"].as_view('"Gettopologydetails"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getLinkDetails/", view_func = globals()["Getlinkdetails"].as_view('"Getlinkdetails"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getNodeEdgePointDetails/", view_func = globals()["Getnodeedgepointdetails"].as_view('"Getnodeedgepointdetails"'+'"_api"'), methods=['POST'])
