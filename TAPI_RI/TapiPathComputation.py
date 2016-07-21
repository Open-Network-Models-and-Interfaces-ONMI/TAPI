from flask import json, Blueprint, request, Response
from flask.views import MethodView
import sys
from objects_common.keyedArrayType import KeyedArrayKeyError

import base64
import re

# BACKEND FUNCTIONS
from funcs_TapiPathComputation.context_PathcompserviceUuidNameImpl import Context_PathcompserviceUuidNameImpl
from funcs_TapiPathComputation.context_PathUuid_Routingconstraint_ExcludepathLocalidImpl import Context_PathUuid_Routingconstraint_ExcludepathLocalidImpl
from funcs_TapiPathComputation.context_PathUuid_TelinkLocalidImpl import Context_PathUuid_TelinkLocalidImpl
from funcs_TapiPathComputation.context_PathUuid_TelinkImpl import Context_PathUuid_TelinkImpl
from funcs_TapiPathComputation.context_PathcompserviceUuid_Optimizationconstraint_ExtensionsExtensionsspecificationImpl import Context_PathcompserviceUuid_Optimizationconstraint_ExtensionsExtensionsspecificationImpl
from funcs_TapiPathComputation.context_PathUuid_RoutingconstraintImpl import Context_PathUuid_RoutingconstraintImpl
from funcs_TapiPathComputation.context_PathcompserviceUuid_RoutingconstraintCostcharacteristicCostnameImpl import Context_PathcompserviceUuid_RoutingconstraintCostcharacteristicCostnameImpl
from funcs_TapiPathComputation.context_PathcompserviceUuid_ObjectivefunctionImpl import Context_PathcompserviceUuid_ObjectivefunctionImpl
from funcs_TapiPathComputation.context_PathUuid_TelinkLocalid_ExtensionsExtensionsspecificationImpl import Context_PathUuid_TelinkLocalid_ExtensionsExtensionsspecificationImpl
from funcs_TapiPathComputation.context_PathcompserviceUuid_Routingconstraint_ExcludepathLocalid_ExtensionsImpl import Context_PathcompserviceUuid_Routingconstraint_ExcludepathLocalid_ExtensionsImpl
from funcs_TapiPathComputation.context_PathcompserviceUuid_Optimizationconstraint_ExtensionsImpl import Context_PathcompserviceUuid_Optimizationconstraint_ExtensionsImpl
from funcs_TapiPathComputation.context_PathcompserviceUuid_ExtensionsExtensionsspecificationImpl import Context_PathcompserviceUuid_ExtensionsExtensionsspecificationImpl
from funcs_TapiPathComputation.computep2PpathImpl import Computep2PpathImpl
from funcs_TapiPathComputation.context_PathcompserviceUuid_RoutingconstraintImpl import Context_PathcompserviceUuid_RoutingconstraintImpl
from funcs_TapiPathComputation.context_PathcompserviceUuid_RoutingconstraintLatencycharacteristicImpl import Context_PathcompserviceUuid_RoutingconstraintLatencycharacteristicImpl
from funcs_TapiPathComputation.context_PathUuid_RoutingconstraintLatencycharacteristicTrafficpropertynameImpl import Context_PathUuid_RoutingconstraintLatencycharacteristicTrafficpropertynameImpl
from funcs_TapiPathComputation.context_PathcompserviceUuid_ExtensionsImpl import Context_PathcompserviceUuid_ExtensionsImpl
from funcs_TapiPathComputation.context_PathUuid_Routingconstraint_ExcludepathLocalid_ExtensionsImpl import Context_PathUuid_Routingconstraint_ExcludepathLocalid_ExtensionsImpl
from funcs_TapiPathComputation.context_PathUuid_Routingconstraint_IncludepathImpl import Context_PathUuid_Routingconstraint_IncludepathImpl
from funcs_TapiPathComputation.context_PathcompserviceUuidImpl import Context_PathcompserviceUuidImpl
from funcs_TapiPathComputation.context_PathUuidNameImpl import Context_PathUuidNameImpl
from funcs_TapiPathComputation.context_PathcompserviceUuidNameValuenameImpl import Context_PathcompserviceUuidNameValuenameImpl
from funcs_TapiPathComputation.context_PathcompserviceUuid_Routingconstraint_ExcludepathLocalid_ExtensionsExtensionsspecificationImpl import Context_PathcompserviceUuid_Routingconstraint_ExcludepathLocalid_ExtensionsExtensionsspecificationImpl
from funcs_TapiPathComputation.context_PathcompserviceUuid_Routingconstraint_ExtensionsExtensionsspecificationImpl import Context_PathcompserviceUuid_Routingconstraint_ExtensionsExtensionsspecificationImpl
from funcs_TapiPathComputation.context_PathUuid_ExtensionsExtensionsspecificationImpl import Context_PathUuid_ExtensionsExtensionsspecificationImpl
from funcs_TapiPathComputation.context_PathUuid_RoutingconstraintLatencycharacteristicImpl import Context_PathUuid_RoutingconstraintLatencycharacteristicImpl
from funcs_TapiPathComputation.context_PathImpl import Context_PathImpl
from funcs_TapiPathComputation.context_PathUuid_Routingconstraint_IncludepathLocalid_ExtensionsExtensionsspecificationImpl import Context_PathUuid_Routingconstraint_IncludepathLocalid_ExtensionsExtensionsspecificationImpl
from funcs_TapiPathComputation.context_PathcompserviceImpl import Context_PathcompserviceImpl
from funcs_TapiPathComputation.context_PathUuidLabelValuenameImpl import Context_PathUuidLabelValuenameImpl
from funcs_TapiPathComputation.context_PathUuid_RoutingconstraintCostcharacteristicCostnameImpl import Context_PathUuid_RoutingconstraintCostcharacteristicCostnameImpl
from funcs_TapiPathComputation.context_PathUuid_Routingconstraint_ExcludepathLocalid_ExtensionsExtensionsspecificationImpl import Context_PathUuid_Routingconstraint_ExcludepathLocalid_ExtensionsExtensionsspecificationImpl
from funcs_TapiPathComputation.context_PathcompserviceUuid_Routingconstraint_ExcludepathImpl import Context_PathcompserviceUuid_Routingconstraint_ExcludepathImpl
from funcs_TapiPathComputation.context_PathUuid_Routingconstraint_IncludepathLocalid_ExtensionsImpl import Context_PathUuid_Routingconstraint_IncludepathLocalid_ExtensionsImpl
from funcs_TapiPathComputation.context_PathUuid_Routingconstraint_ExtensionsExtensionsspecificationImpl import Context_PathUuid_Routingconstraint_ExtensionsExtensionsspecificationImpl
from funcs_TapiPathComputation.context_PathcompserviceUuid_OptimizationconstraintImpl import Context_PathcompserviceUuid_OptimizationconstraintImpl
from funcs_TapiPathComputation.context_PathcompserviceUuid_ServiceportImpl import Context_PathcompserviceUuid_ServiceportImpl
from funcs_TapiPathComputation.context_PathcompserviceUuid_Routingconstraint_IncludepathLocalid_ExtensionsExtensionsspecificationImpl import Context_PathcompserviceUuid_Routingconstraint_IncludepathLocalid_ExtensionsExtensionsspecificationImpl
from funcs_TapiPathComputation.context_PathcompserviceUuid_Objectivefunction_ExtensionsExtensionsspecificationImpl import Context_PathcompserviceUuid_Objectivefunction_ExtensionsExtensionsspecificationImpl
from funcs_TapiPathComputation.deletep2PpathImpl import Deletep2PpathImpl
from funcs_TapiPathComputation.context_PathcompserviceUuid_RoutingconstraintCostcharacteristicImpl import Context_PathcompserviceUuid_RoutingconstraintCostcharacteristicImpl
from funcs_TapiPathComputation.context_PathUuid_TelinkLocalid_ExtensionsImpl import Context_PathUuid_TelinkLocalid_ExtensionsImpl
from funcs_TapiPathComputation.context_PathcompserviceUuid_RoutingconstraintRequestedcapacityImpl import Context_PathcompserviceUuid_RoutingconstraintRequestedcapacityImpl
from funcs_TapiPathComputation.context_PathUuid_Routingconstraint_ExcludepathImpl import Context_PathUuid_Routingconstraint_ExcludepathImpl
from funcs_TapiPathComputation.context_PathcompserviceUuid_ServiceportLocalid_ExtensionsImpl import Context_PathcompserviceUuid_ServiceportLocalid_ExtensionsImpl
from funcs_TapiPathComputation.optimizep2PpathImpl import Optimizep2PpathImpl
from funcs_TapiPathComputation.context_PathcompserviceUuid_Routingconstraint_ExtensionsImpl import Context_PathcompserviceUuid_Routingconstraint_ExtensionsImpl
from funcs_TapiPathComputation.context_PathcompserviceUuid_ServiceportLocalid_ExtensionsExtensionsspecificationImpl import Context_PathcompserviceUuid_ServiceportLocalid_ExtensionsExtensionsspecificationImpl
from funcs_TapiPathComputation.context_PathUuid_RoutingconstraintCostcharacteristicImpl import Context_PathUuid_RoutingconstraintCostcharacteristicImpl
from funcs_TapiPathComputation.context_PathcompserviceUuid_Objectivefunction_ExtensionsImpl import Context_PathcompserviceUuid_Objectivefunction_ExtensionsImpl
from funcs_TapiPathComputation.context_PathUuid_RoutingconstraintRequestedcapacityImpl import Context_PathUuid_RoutingconstraintRequestedcapacityImpl
from funcs_TapiPathComputation.context_PathcompserviceUuid_ServiceportLocalidImpl import Context_PathcompserviceUuid_ServiceportLocalidImpl
from funcs_TapiPathComputation.context_PathcompserviceUuid_RoutingconstraintLatencycharacteristicTrafficpropertynameImpl import Context_PathcompserviceUuid_RoutingconstraintLatencycharacteristicTrafficpropertynameImpl
from funcs_TapiPathComputation.context_PathcompserviceUuid_Routingconstraint_IncludepathImpl import Context_PathcompserviceUuid_Routingconstraint_IncludepathImpl
from funcs_TapiPathComputation.context_PathUuid_Routingconstraint_IncludepathLocalidImpl import Context_PathUuid_Routingconstraint_IncludepathLocalidImpl
from funcs_TapiPathComputation.context_PathcompserviceUuidLabelImpl import Context_PathcompserviceUuidLabelImpl
from funcs_TapiPathComputation.context_PathcompserviceUuid_Routingconstraint_IncludepathLocalidImpl import Context_PathcompserviceUuid_Routingconstraint_IncludepathLocalidImpl
from funcs_TapiPathComputation.context_PathUuid_ExtensionsImpl import Context_PathUuid_ExtensionsImpl
from funcs_TapiPathComputation.context_PathUuid_Routingconstraint_ExtensionsImpl import Context_PathUuid_Routingconstraint_ExtensionsImpl
from funcs_TapiPathComputation.context_PathcompserviceUuid_Routingconstraint_IncludepathLocalid_ExtensionsImpl import Context_PathcompserviceUuid_Routingconstraint_IncludepathLocalid_ExtensionsImpl
from funcs_TapiPathComputation.context_PathUuidLabelImpl import Context_PathUuidLabelImpl
from funcs_TapiPathComputation.context_PathUuidNameValuenameImpl import Context_PathUuidNameValuenameImpl
from funcs_TapiPathComputation.context_PathcompserviceUuid_Routingconstraint_ExcludepathLocalidImpl import Context_PathcompserviceUuid_Routingconstraint_ExcludepathLocalidImpl
from funcs_TapiPathComputation.context_PathcompserviceUuidLabelValuenameImpl import Context_PathcompserviceUuidLabelValuenameImpl
from funcs_TapiPathComputation.context_PathUuidImpl import Context_PathUuidImpl

# CALLABLE OBJECTS
from objects_TapiPathComputation.linkPort import LinkPort
from objects_TapiPathComputation.optimizeP2PPathRPCInputSchema import OptimizeP2PPathRPCInputSchema
from objects_TapiPathComputation.capacity import Capacity
from objects_TapiPathComputation.transferCostPac import TransferCostPac
from objects_TapiPathComputation.networkTopologyService import NetworkTopologyService
from objects_TapiPathComputation.timeRange import TimeRange
from objects_TapiPathComputation.layerProtocolTransitionPac import LayerProtocolTransitionPac
from objects_TapiPathComputation.transferTimingPac import TransferTimingPac
from objects_TapiPathComputation.transferIntegrityPac import TransferIntegrityPac
from objects_TapiPathComputation.nameAndValue import NameAndValue
from objects_TapiPathComputation.adminStatePac import AdminStatePac
from objects_TapiPathComputation.serviceEndPoint import ServiceEndPoint
from objects_TapiPathComputation.validationMechanism import ValidationMechanism
from objects_TapiPathComputation.node import Node
from objects_TapiPathComputation.resourceSpec import ResourceSpec
from objects_TapiPathComputation.teLink import TeLink
from objects_TapiPathComputation.costCharacteristic import CostCharacteristic
from objects_TapiPathComputation.latencyCharacteristic import LatencyCharacteristic
from objects_TapiPathComputation._pathCompServiceSchema import _pathCompServiceSchema
from objects_TapiPathComputation.routingConstraint import RoutingConstraint
from objects_TapiPathComputation.pathComputationService import PathComputationService
from objects_TapiPathComputation.link import Link
from objects_TapiPathComputation.localClass import LocalClass
from objects_TapiPathComputation.path import Path
from objects_TapiPathComputation.topology import Topology
from objects_TapiPathComputation.extensionsSpec import ExtensionsSpec
from objects_TapiPathComputation.pathCompServicePort import PathCompServicePort
from objects_TapiPathComputation.serviceSpec import ServiceSpec
from objects_TapiPathComputation.deleteP2PPathRPCInputSchema import DeleteP2PPathRPCInputSchema
from objects_TapiPathComputation.computeP2PPathRPCOutputSchema import ComputeP2PPathRPCOutputSchema
from objects_TapiPathComputation.nodeEdgePoint import NodeEdgePoint
from objects_TapiPathComputation.computeP2PPathRPCInputSchema import ComputeP2PPathRPCInputSchema
from objects_TapiPathComputation.pathOptimizationConstraint import PathOptimizationConstraint
from objects_TapiPathComputation.pathObjectiveFunction import PathObjectiveFunction
from objects_TapiPathComputation._pathSchema import _pathSchema
from objects_TapiPathComputation.riskCharacteristic import RiskCharacteristic
from objects_TapiPathComputation.optimizeP2PPathRPCOutputSchema import OptimizeP2PPathRPCOutputSchema
from objects_TapiPathComputation.riskParameterPac import RiskParameterPac
from objects_TapiPathComputation.operationalStatePac import OperationalStatePac
from objects_TapiPathComputation.globalClass import GlobalClass
from objects_TapiPathComputation.layerProtocol import LayerProtocol
from objects_TapiPathComputation.deleteP2PPathRPCOutputSchema import DeleteP2PPathRPCOutputSchema
from objects_TapiPathComputation.transferCapacityPac import TransferCapacityPac
from objects_TapiPathComputation.lifecycleStatePac import LifecycleStatePac
from objects_TapiPathComputation.validationPac import ValidationPac

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


#/restconf/config/Context/_pathCompService/(\w+)/name/
class Context_PathcompserviceUuidNameMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: name"
        try:
            response = Context_PathcompserviceUuidNameImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_path/(\w+)/_routingConstraint/_excludePath/(\w+)/
class Context_PathUuid_Routingconstraint_ExcludepathLocalidMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _excludePath"
        try:
            response = Context_PathUuid_Routingconstraint_ExcludepathLocalidImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_path/(\w+)/_telink/(\w+)/
class Context_PathUuid_TelinkLocalidMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _telink"
        try:
            response = Context_PathUuid_TelinkLocalidImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_path/(\w+)/_telink/
class Context_PathUuid_TelinkMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _telink"
        try:
            response = Context_PathUuid_TelinkImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_optimizationConstraint/_extensions/(\w+)/
class Context_PathcompserviceUuid_Optimizationconstraint_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_PathcompserviceUuid_Optimizationconstraint_ExtensionsExtensionsspecificationImpl.get(uuid, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_path/(\w+)/_routingConstraint/
class Context_PathUuid_RoutingconstraintMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _routingConstraint"
        try:
            response = Context_PathUuid_RoutingconstraintImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_routingConstraint/costCharacteristic/(\w+)/
class Context_PathcompserviceUuid_RoutingconstraintCostcharacteristicCostnameMethodView(MethodView):

    def get(self, uuid, costName):
        print "Retrieve operation of resource: costCharacteristic"
        try:
            response = Context_PathcompserviceUuid_RoutingconstraintCostcharacteristicCostnameImpl.get(uuid, costName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_objectiveFunction/
class Context_PathcompserviceUuid_ObjectivefunctionMethodView(MethodView):

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


#/restconf/config/Context/_path/(\w+)/_telink/(\w+)/_extensions/(\w+)/
class Context_PathUuid_TelinkLocalid_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, localId, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_PathUuid_TelinkLocalid_ExtensionsExtensionsspecificationImpl.get(uuid, localId, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_routingConstraint/_excludePath/(\w+)/_extensions/
class Context_PathcompserviceUuid_Routingconstraint_ExcludepathLocalid_ExtensionsMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_PathcompserviceUuid_Routingconstraint_ExcludepathLocalid_ExtensionsImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_optimizationConstraint/_extensions/
class Context_PathcompserviceUuid_Optimizationconstraint_ExtensionsMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_PathcompserviceUuid_Optimizationconstraint_ExtensionsImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_extensions/(\w+)/
class Context_PathcompserviceUuid_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_PathcompserviceUuid_ExtensionsExtensionsspecificationImpl.get(uuid, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/operations/computeP2PPath/
class Computep2PpathMethodView(MethodView):

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



#/restconf/config/Context/_pathCompService/(\w+)/_routingConstraint/
class Context_PathcompserviceUuid_RoutingconstraintMethodView(MethodView):

    def put(self, uuid):
        print "Update operation of resource: _routingConstraint"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_PathcompserviceUuid_RoutingconstraintImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(RoutingConstraint, json_struct)
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
            new_object = create_instance(RoutingConstraint, json_struct)
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


#/restconf/config/Context/_pathCompService/(\w+)/_routingConstraint/latencyCharacteristic/
class Context_PathcompserviceUuid_RoutingconstraintLatencycharacteristicMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: latencyCharacteristic"
        try:
            response = Context_PathcompserviceUuid_RoutingconstraintLatencycharacteristicImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_path/(\w+)/_routingConstraint/latencyCharacteristic/(\w+)/
class Context_PathUuid_RoutingconstraintLatencycharacteristicTrafficpropertynameMethodView(MethodView):

    def get(self, uuid, trafficPropertyName):
        print "Retrieve operation of resource: latencyCharacteristic"
        try:
            response = Context_PathUuid_RoutingconstraintLatencycharacteristicTrafficpropertynameImpl.get(uuid, trafficPropertyName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_extensions/
class Context_PathcompserviceUuid_ExtensionsMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_PathcompserviceUuid_ExtensionsImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_path/(\w+)/_routingConstraint/_excludePath/(\w+)/_extensions/
class Context_PathUuid_Routingconstraint_ExcludepathLocalid_ExtensionsMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_PathUuid_Routingconstraint_ExcludepathLocalid_ExtensionsImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_path/(\w+)/_routingConstraint/_includePath/
class Context_PathUuid_Routingconstraint_IncludepathMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _includePath"
        try:
            response = Context_PathUuid_Routingconstraint_IncludepathImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/
class Context_PathcompserviceUuidMethodView(MethodView):

    def put(self, uuid):
        print "Update operation of resource: _pathCompService"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_PathcompserviceUuidImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(_pathCompServiceSchema, json_struct)
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
            new_object = create_instance(_pathCompServiceSchema, json_struct, (uuid,'uuid'))
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


#/restconf/config/Context/_path/(\w+)/name/
class Context_PathUuidNameMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: name"
        try:
            response = Context_PathUuidNameImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/name/(\w+)/
class Context_PathcompserviceUuidNameValuenameMethodView(MethodView):

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


#/restconf/config/Context/_pathCompService/(\w+)/_routingConstraint/_excludePath/(\w+)/_extensions/(\w+)/
class Context_PathcompserviceUuid_Routingconstraint_ExcludepathLocalid_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, localId, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_PathcompserviceUuid_Routingconstraint_ExcludepathLocalid_ExtensionsExtensionsspecificationImpl.get(uuid, localId, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_routingConstraint/_extensions/(\w+)/
class Context_PathcompserviceUuid_Routingconstraint_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_PathcompserviceUuid_Routingconstraint_ExtensionsExtensionsspecificationImpl.get(uuid, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_path/(\w+)/_extensions/(\w+)/
class Context_PathUuid_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_PathUuid_ExtensionsExtensionsspecificationImpl.get(uuid, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_path/(\w+)/_routingConstraint/latencyCharacteristic/
class Context_PathUuid_RoutingconstraintLatencycharacteristicMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: latencyCharacteristic"
        try:
            response = Context_PathUuid_RoutingconstraintLatencycharacteristicImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_path/
class Context_PathMethodView(MethodView):

    def get(self, ):
        print "Retrieve operation of resource: _path"
        try:
            response = Context_PathImpl.get()
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_path/(\w+)/_routingConstraint/_includePath/(\w+)/_extensions/(\w+)/
class Context_PathUuid_Routingconstraint_IncludepathLocalid_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, localId, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_PathUuid_Routingconstraint_IncludepathLocalid_ExtensionsExtensionsspecificationImpl.get(uuid, localId, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/
class Context_PathcompserviceMethodView(MethodView):

    def get(self, ):
        print "Retrieve operation of resource: _pathCompService"
        try:
            response = Context_PathcompserviceImpl.get()
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_path/(\w+)/label/(\w+)/
class Context_PathUuidLabelValuenameMethodView(MethodView):

    def get(self, uuid, valueName):
        print "Retrieve operation of resource: label"
        try:
            response = Context_PathUuidLabelValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_path/(\w+)/_routingConstraint/costCharacteristic/(\w+)/
class Context_PathUuid_RoutingconstraintCostcharacteristicCostnameMethodView(MethodView):

    def get(self, uuid, costName):
        print "Retrieve operation of resource: costCharacteristic"
        try:
            response = Context_PathUuid_RoutingconstraintCostcharacteristicCostnameImpl.get(uuid, costName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_path/(\w+)/_routingConstraint/_excludePath/(\w+)/_extensions/(\w+)/
class Context_PathUuid_Routingconstraint_ExcludepathLocalid_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, localId, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_PathUuid_Routingconstraint_ExcludepathLocalid_ExtensionsExtensionsspecificationImpl.get(uuid, localId, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_routingConstraint/_excludePath/
class Context_PathcompserviceUuid_Routingconstraint_ExcludepathMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _excludePath"
        try:
            response = Context_PathcompserviceUuid_Routingconstraint_ExcludepathImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_path/(\w+)/_routingConstraint/_includePath/(\w+)/_extensions/
class Context_PathUuid_Routingconstraint_IncludepathLocalid_ExtensionsMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_PathUuid_Routingconstraint_IncludepathLocalid_ExtensionsImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_path/(\w+)/_routingConstraint/_extensions/(\w+)/
class Context_PathUuid_Routingconstraint_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_PathUuid_Routingconstraint_ExtensionsExtensionsspecificationImpl.get(uuid, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_optimizationConstraint/
class Context_PathcompserviceUuid_OptimizationconstraintMethodView(MethodView):

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


#/restconf/config/Context/_pathCompService/(\w+)/_servicePort/
class Context_PathcompserviceUuid_ServiceportMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _servicePort"
        try:
            response = Context_PathcompserviceUuid_ServiceportImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_routingConstraint/_includePath/(\w+)/_extensions/(\w+)/
class Context_PathcompserviceUuid_Routingconstraint_IncludepathLocalid_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, localId, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_PathcompserviceUuid_Routingconstraint_IncludepathLocalid_ExtensionsExtensionsspecificationImpl.get(uuid, localId, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_objectiveFunction/_extensions/(\w+)/
class Context_PathcompserviceUuid_Objectivefunction_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_PathcompserviceUuid_Objectivefunction_ExtensionsExtensionsspecificationImpl.get(uuid, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/operations/deleteP2PPath/
class Deletep2PpathMethodView(MethodView):

    def post(self, ):
        print "Create operation of resource: deleteP2PPath"
        try:
            response = Deletep2PpathImpl.get()
        except KeyError as inst:
            if inst.args[0] != '':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(DeleteP2PPathRPCInputSchema, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Deletep2PpathImpl.post(new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))



#/restconf/config/Context/_pathCompService/(\w+)/_routingConstraint/costCharacteristic/
class Context_PathcompserviceUuid_RoutingconstraintCostcharacteristicMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: costCharacteristic"
        try:
            response = Context_PathcompserviceUuid_RoutingconstraintCostcharacteristicImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_path/(\w+)/_telink/(\w+)/_extensions/
class Context_PathUuid_TelinkLocalid_ExtensionsMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_PathUuid_TelinkLocalid_ExtensionsImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_routingConstraint/requestedCapacity/
class Context_PathcompserviceUuid_RoutingconstraintRequestedcapacityMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: requestedCapacity"
        try:
            response = Context_PathcompserviceUuid_RoutingconstraintRequestedcapacityImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_path/(\w+)/_routingConstraint/_excludePath/
class Context_PathUuid_Routingconstraint_ExcludepathMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _excludePath"
        try:
            response = Context_PathUuid_Routingconstraint_ExcludepathImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_servicePort/(\w+)/_extensions/
class Context_PathcompserviceUuid_ServiceportLocalid_ExtensionsMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_PathcompserviceUuid_ServiceportLocalid_ExtensionsImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/operations/optimizeP2PPath/
class Optimizep2PpathMethodView(MethodView):

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



#/restconf/config/Context/_pathCompService/(\w+)/_routingConstraint/_extensions/
class Context_PathcompserviceUuid_Routingconstraint_ExtensionsMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_PathcompserviceUuid_Routingconstraint_ExtensionsImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_servicePort/(\w+)/_extensions/(\w+)/
class Context_PathcompserviceUuid_ServiceportLocalid_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, localId, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_PathcompserviceUuid_ServiceportLocalid_ExtensionsExtensionsspecificationImpl.get(uuid, localId, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_path/(\w+)/_routingConstraint/costCharacteristic/
class Context_PathUuid_RoutingconstraintCostcharacteristicMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: costCharacteristic"
        try:
            response = Context_PathUuid_RoutingconstraintCostcharacteristicImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_objectiveFunction/_extensions/
class Context_PathcompserviceUuid_Objectivefunction_ExtensionsMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_PathcompserviceUuid_Objectivefunction_ExtensionsImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_path/(\w+)/_routingConstraint/requestedCapacity/
class Context_PathUuid_RoutingconstraintRequestedcapacityMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: requestedCapacity"
        try:
            response = Context_PathUuid_RoutingconstraintRequestedcapacityImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_servicePort/(\w+)/
class Context_PathcompserviceUuid_ServiceportLocalidMethodView(MethodView):

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


#/restconf/config/Context/_pathCompService/(\w+)/_routingConstraint/latencyCharacteristic/(\w+)/
class Context_PathcompserviceUuid_RoutingconstraintLatencycharacteristicTrafficpropertynameMethodView(MethodView):

    def get(self, uuid, trafficPropertyName):
        print "Retrieve operation of resource: latencyCharacteristic"
        try:
            response = Context_PathcompserviceUuid_RoutingconstraintLatencycharacteristicTrafficpropertynameImpl.get(uuid, trafficPropertyName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_routingConstraint/_includePath/
class Context_PathcompserviceUuid_Routingconstraint_IncludepathMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _includePath"
        try:
            response = Context_PathcompserviceUuid_Routingconstraint_IncludepathImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_path/(\w+)/_routingConstraint/_includePath/(\w+)/
class Context_PathUuid_Routingconstraint_IncludepathLocalidMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _includePath"
        try:
            response = Context_PathUuid_Routingconstraint_IncludepathLocalidImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/label/
class Context_PathcompserviceUuidLabelMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: label"
        try:
            response = Context_PathcompserviceUuidLabelImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_routingConstraint/_includePath/(\w+)/
class Context_PathcompserviceUuid_Routingconstraint_IncludepathLocalidMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _includePath"
        try:
            response = Context_PathcompserviceUuid_Routingconstraint_IncludepathLocalidImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_path/(\w+)/_extensions/
class Context_PathUuid_ExtensionsMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_PathUuid_ExtensionsImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_path/(\w+)/_routingConstraint/_extensions/
class Context_PathUuid_Routingconstraint_ExtensionsMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_PathUuid_Routingconstraint_ExtensionsImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_routingConstraint/_includePath/(\w+)/_extensions/
class Context_PathcompserviceUuid_Routingconstraint_IncludepathLocalid_ExtensionsMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_PathcompserviceUuid_Routingconstraint_IncludepathLocalid_ExtensionsImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_path/(\w+)/label/
class Context_PathUuidLabelMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: label"
        try:
            response = Context_PathUuidLabelImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_path/(\w+)/name/(\w+)/
class Context_PathUuidNameValuenameMethodView(MethodView):

    def get(self, uuid, valueName):
        print "Retrieve operation of resource: name"
        try:
            response = Context_PathUuidNameValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/_routingConstraint/_excludePath/(\w+)/
class Context_PathcompserviceUuid_Routingconstraint_ExcludepathLocalidMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _excludePath"
        try:
            response = Context_PathcompserviceUuid_Routingconstraint_ExcludepathLocalidImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_pathCompService/(\w+)/label/(\w+)/
class Context_PathcompserviceUuidLabelValuenameMethodView(MethodView):

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


#/restconf/config/Context/_path/(\w+)/
class Context_PathUuidMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _path"
        try:
            response = Context_PathUuidImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))



getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/name/", view_func = globals()["Context_PathcompserviceUuidNameMethodView"].as_view('"Context_PathcompserviceUuidName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_routingConstraint/_excludePath/<localId>/", view_func = globals()["Context_PathUuid_Routingconstraint_ExcludepathLocalidMethodView"].as_view('"Context_PathUuid_Routingconstraint_ExcludepathLocalid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_telink/<localId>/", view_func = globals()["Context_PathUuid_TelinkLocalidMethodView"].as_view('"Context_PathUuid_TelinkLocalid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_telink/", view_func = globals()["Context_PathUuid_TelinkMethodView"].as_view('"Context_PathUuid_Telink"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_optimizationConstraint/_extensions/<extensionsSpecification>/", view_func = globals()["Context_PathcompserviceUuid_Optimizationconstraint_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_PathcompserviceUuid_Optimizationconstraint_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_routingConstraint/", view_func = globals()["Context_PathUuid_RoutingconstraintMethodView"].as_view('"Context_PathUuid_Routingconstraint"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_routingConstraint/costCharacteristic/<costName>/", view_func = globals()["Context_PathcompserviceUuid_RoutingconstraintCostcharacteristicCostnameMethodView"].as_view('"Context_PathcompserviceUuid_RoutingconstraintCostcharacteristicCostname"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_objectiveFunction/", view_func = globals()["Context_PathcompserviceUuid_ObjectivefunctionMethodView"].as_view('"Context_PathcompserviceUuid_Objectivefunction"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_telink/<localId>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_PathUuid_TelinkLocalid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_PathUuid_TelinkLocalid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_routingConstraint/_excludePath/<localId>/_extensions/", view_func = globals()["Context_PathcompserviceUuid_Routingconstraint_ExcludepathLocalid_ExtensionsMethodView"].as_view('"Context_PathcompserviceUuid_Routingconstraint_ExcludepathLocalid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_optimizationConstraint/_extensions/", view_func = globals()["Context_PathcompserviceUuid_Optimizationconstraint_ExtensionsMethodView"].as_view('"Context_PathcompserviceUuid_Optimizationconstraint_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_PathcompserviceUuid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_PathcompserviceUuid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/computeP2PPath/", view_func = globals()["Computep2PpathMethodView"].as_view('"Computep2Ppath"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_routingConstraint/", view_func = globals()["Context_PathcompserviceUuid_RoutingconstraintMethodView"].as_view('"Context_PathcompserviceUuid_Routingconstraint"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_routingConstraint/latencyCharacteristic/", view_func = globals()["Context_PathcompserviceUuid_RoutingconstraintLatencycharacteristicMethodView"].as_view('"Context_PathcompserviceUuid_RoutingconstraintLatencycharacteristic"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_routingConstraint/latencyCharacteristic/<trafficPropertyName>/", view_func = globals()["Context_PathUuid_RoutingconstraintLatencycharacteristicTrafficpropertynameMethodView"].as_view('"Context_PathUuid_RoutingconstraintLatencycharacteristicTrafficpropertyname"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_extensions/", view_func = globals()["Context_PathcompserviceUuid_ExtensionsMethodView"].as_view('"Context_PathcompserviceUuid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_routingConstraint/_excludePath/<localId>/_extensions/", view_func = globals()["Context_PathUuid_Routingconstraint_ExcludepathLocalid_ExtensionsMethodView"].as_view('"Context_PathUuid_Routingconstraint_ExcludepathLocalid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_routingConstraint/_includePath/", view_func = globals()["Context_PathUuid_Routingconstraint_IncludepathMethodView"].as_view('"Context_PathUuid_Routingconstraint_Includepath"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/", view_func = globals()["Context_PathcompserviceUuidMethodView"].as_view('"Context_PathcompserviceUuid"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/name/", view_func = globals()["Context_PathUuidNameMethodView"].as_view('"Context_PathUuidName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/name/<valueName>/", view_func = globals()["Context_PathcompserviceUuidNameValuenameMethodView"].as_view('"Context_PathcompserviceUuidNameValuename"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_routingConstraint/_excludePath/<localId>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_PathcompserviceUuid_Routingconstraint_ExcludepathLocalid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_PathcompserviceUuid_Routingconstraint_ExcludepathLocalid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_routingConstraint/_extensions/<extensionsSpecification>/", view_func = globals()["Context_PathcompserviceUuid_Routingconstraint_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_PathcompserviceUuid_Routingconstraint_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_PathUuid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_PathUuid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_routingConstraint/latencyCharacteristic/", view_func = globals()["Context_PathUuid_RoutingconstraintLatencycharacteristicMethodView"].as_view('"Context_PathUuid_RoutingconstraintLatencycharacteristic"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/", view_func = globals()["Context_PathMethodView"].as_view('"Context_Path"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_routingConstraint/_includePath/<localId>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_PathUuid_Routingconstraint_IncludepathLocalid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_PathUuid_Routingconstraint_IncludepathLocalid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/", view_func = globals()["Context_PathcompserviceMethodView"].as_view('"Context_Pathcompservice"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/label/<valueName>/", view_func = globals()["Context_PathUuidLabelValuenameMethodView"].as_view('"Context_PathUuidLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_routingConstraint/costCharacteristic/<costName>/", view_func = globals()["Context_PathUuid_RoutingconstraintCostcharacteristicCostnameMethodView"].as_view('"Context_PathUuid_RoutingconstraintCostcharacteristicCostname"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_routingConstraint/_excludePath/<localId>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_PathUuid_Routingconstraint_ExcludepathLocalid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_PathUuid_Routingconstraint_ExcludepathLocalid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_routingConstraint/_excludePath/", view_func = globals()["Context_PathcompserviceUuid_Routingconstraint_ExcludepathMethodView"].as_view('"Context_PathcompserviceUuid_Routingconstraint_Excludepath"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_routingConstraint/_includePath/<localId>/_extensions/", view_func = globals()["Context_PathUuid_Routingconstraint_IncludepathLocalid_ExtensionsMethodView"].as_view('"Context_PathUuid_Routingconstraint_IncludepathLocalid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_routingConstraint/_extensions/<extensionsSpecification>/", view_func = globals()["Context_PathUuid_Routingconstraint_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_PathUuid_Routingconstraint_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_optimizationConstraint/", view_func = globals()["Context_PathcompserviceUuid_OptimizationconstraintMethodView"].as_view('"Context_PathcompserviceUuid_Optimizationconstraint"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_servicePort/", view_func = globals()["Context_PathcompserviceUuid_ServiceportMethodView"].as_view('"Context_PathcompserviceUuid_Serviceport"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_routingConstraint/_includePath/<localId>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_PathcompserviceUuid_Routingconstraint_IncludepathLocalid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_PathcompserviceUuid_Routingconstraint_IncludepathLocalid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_objectiveFunction/_extensions/<extensionsSpecification>/", view_func = globals()["Context_PathcompserviceUuid_Objectivefunction_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_PathcompserviceUuid_Objectivefunction_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/deleteP2PPath/", view_func = globals()["Deletep2PpathMethodView"].as_view('"Deletep2Ppath"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_routingConstraint/costCharacteristic/", view_func = globals()["Context_PathcompserviceUuid_RoutingconstraintCostcharacteristicMethodView"].as_view('"Context_PathcompserviceUuid_RoutingconstraintCostcharacteristic"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_telink/<localId>/_extensions/", view_func = globals()["Context_PathUuid_TelinkLocalid_ExtensionsMethodView"].as_view('"Context_PathUuid_TelinkLocalid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_routingConstraint/requestedCapacity/", view_func = globals()["Context_PathcompserviceUuid_RoutingconstraintRequestedcapacityMethodView"].as_view('"Context_PathcompserviceUuid_RoutingconstraintRequestedcapacity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_routingConstraint/_excludePath/", view_func = globals()["Context_PathUuid_Routingconstraint_ExcludepathMethodView"].as_view('"Context_PathUuid_Routingconstraint_Excludepath"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_servicePort/<localId>/_extensions/", view_func = globals()["Context_PathcompserviceUuid_ServiceportLocalid_ExtensionsMethodView"].as_view('"Context_PathcompserviceUuid_ServiceportLocalid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/optimizeP2PPath/", view_func = globals()["Optimizep2PpathMethodView"].as_view('"Optimizep2Ppath"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_routingConstraint/_extensions/", view_func = globals()["Context_PathcompserviceUuid_Routingconstraint_ExtensionsMethodView"].as_view('"Context_PathcompserviceUuid_Routingconstraint_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_servicePort/<localId>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_PathcompserviceUuid_ServiceportLocalid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_PathcompserviceUuid_ServiceportLocalid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_routingConstraint/costCharacteristic/", view_func = globals()["Context_PathUuid_RoutingconstraintCostcharacteristicMethodView"].as_view('"Context_PathUuid_RoutingconstraintCostcharacteristic"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_objectiveFunction/_extensions/", view_func = globals()["Context_PathcompserviceUuid_Objectivefunction_ExtensionsMethodView"].as_view('"Context_PathcompserviceUuid_Objectivefunction_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_routingConstraint/requestedCapacity/", view_func = globals()["Context_PathUuid_RoutingconstraintRequestedcapacityMethodView"].as_view('"Context_PathUuid_RoutingconstraintRequestedcapacity"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_servicePort/<localId>/", view_func = globals()["Context_PathcompserviceUuid_ServiceportLocalidMethodView"].as_view('"Context_PathcompserviceUuid_ServiceportLocalid"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_routingConstraint/latencyCharacteristic/<trafficPropertyName>/", view_func = globals()["Context_PathcompserviceUuid_RoutingconstraintLatencycharacteristicTrafficpropertynameMethodView"].as_view('"Context_PathcompserviceUuid_RoutingconstraintLatencycharacteristicTrafficpropertyname"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_routingConstraint/_includePath/", view_func = globals()["Context_PathcompserviceUuid_Routingconstraint_IncludepathMethodView"].as_view('"Context_PathcompserviceUuid_Routingconstraint_Includepath"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_routingConstraint/_includePath/<localId>/", view_func = globals()["Context_PathUuid_Routingconstraint_IncludepathLocalidMethodView"].as_view('"Context_PathUuid_Routingconstraint_IncludepathLocalid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/label/", view_func = globals()["Context_PathcompserviceUuidLabelMethodView"].as_view('"Context_PathcompserviceUuidLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_routingConstraint/_includePath/<localId>/", view_func = globals()["Context_PathcompserviceUuid_Routingconstraint_IncludepathLocalidMethodView"].as_view('"Context_PathcompserviceUuid_Routingconstraint_IncludepathLocalid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_extensions/", view_func = globals()["Context_PathUuid_ExtensionsMethodView"].as_view('"Context_PathUuid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_routingConstraint/_extensions/", view_func = globals()["Context_PathUuid_Routingconstraint_ExtensionsMethodView"].as_view('"Context_PathUuid_Routingconstraint_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_routingConstraint/_includePath/<localId>/_extensions/", view_func = globals()["Context_PathcompserviceUuid_Routingconstraint_IncludepathLocalid_ExtensionsMethodView"].as_view('"Context_PathcompserviceUuid_Routingconstraint_IncludepathLocalid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/label/", view_func = globals()["Context_PathUuidLabelMethodView"].as_view('"Context_PathUuidLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/name/<valueName>/", view_func = globals()["Context_PathUuidNameValuenameMethodView"].as_view('"Context_PathUuidNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_routingConstraint/_excludePath/<localId>/", view_func = globals()["Context_PathcompserviceUuid_Routingconstraint_ExcludepathLocalidMethodView"].as_view('"Context_PathcompserviceUuid_Routingconstraint_ExcludepathLocalid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/label/<valueName>/", view_func = globals()["Context_PathcompserviceUuidLabelValuenameMethodView"].as_view('"Context_PathcompserviceUuidLabelValuename"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/", view_func = globals()["Context_PathUuidMethodView"].as_view('"Context_PathUuid"'+'"_api"'), methods=['GET'])
