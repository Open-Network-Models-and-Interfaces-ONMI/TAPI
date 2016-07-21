from flask import json, Blueprint, request, Response
from flask.views import MethodView
import sys
from objects_common.keyedArrayType import KeyedArrayKeyError

import base64
import re

# BACKEND FUNCTIONS
from funcs_TapiVirtualNetwork.context_VnwserviceUuid_VnwconstraintLocalid_ExtensionsImpl import Context_VnwserviceUuid_VnwconstraintLocalid_ExtensionsImpl
from funcs_TapiVirtualNetwork.context_VnwserviceUuid_StateImpl import Context_VnwserviceUuid_StateImpl
from funcs_TapiVirtualNetwork.context_VnwserviceUuidLabelImpl import Context_VnwserviceUuidLabelImpl
from funcs_TapiVirtualNetwork.context_VnwserviceUuid_ExtensionsExtensionsspecificationImpl import Context_VnwserviceUuid_ExtensionsExtensionsspecificationImpl
from funcs_TapiVirtualNetwork.context_VnwserviceUuid_VnwconstraintLocalidLatencycharacteristicTrafficpropertynameImpl import Context_VnwserviceUuid_VnwconstraintLocalidLatencycharacteristicTrafficpropertynameImpl
from funcs_TapiVirtualNetwork.context_VnwserviceUuid_ScheduleImpl import Context_VnwserviceUuid_ScheduleImpl
from funcs_TapiVirtualNetwork.getvirtualnetworkservicedetailsImpl import GetvirtualnetworkservicedetailsImpl
from funcs_TapiVirtualNetwork.context_VnwserviceUuidNameValuenameImpl import Context_VnwserviceUuidNameValuenameImpl
from funcs_TapiVirtualNetwork.context_VnwserviceUuid_VnwconstraintLocalidLatencycharacteristicImpl import Context_VnwserviceUuid_VnwconstraintLocalidLatencycharacteristicImpl
from funcs_TapiVirtualNetwork.createvirtualnetworkserviceImpl import CreatevirtualnetworkserviceImpl
from funcs_TapiVirtualNetwork.getvirtualnetworkservicelistImpl import GetvirtualnetworkservicelistImpl
from funcs_TapiVirtualNetwork.context_VnwserviceUuidLabelValuenameImpl import Context_VnwserviceUuidLabelValuenameImpl
from funcs_TapiVirtualNetwork.context_VnwserviceUuid_ExtensionsImpl import Context_VnwserviceUuid_ExtensionsImpl
from funcs_TapiVirtualNetwork.context_VnwserviceUuid_VnwconstraintLocalidRequestedcapacityImpl import Context_VnwserviceUuid_VnwconstraintLocalidRequestedcapacityImpl
from funcs_TapiVirtualNetwork.context_VnwserviceUuid_VnwconstraintLocalidImpl import Context_VnwserviceUuid_VnwconstraintLocalidImpl
from funcs_TapiVirtualNetwork.context_VnwserviceUuid_VnwconstraintLocalidCostcharacteristicImpl import Context_VnwserviceUuid_VnwconstraintLocalidCostcharacteristicImpl
from funcs_TapiVirtualNetwork.deletevirtualnetworkserviceImpl import DeletevirtualnetworkserviceImpl
from funcs_TapiVirtualNetwork.context_VnwserviceUuid_ServiceportLocalidImpl import Context_VnwserviceUuid_ServiceportLocalidImpl
from funcs_TapiVirtualNetwork.context_VnwserviceUuid_VnwconstraintLocalidCostcharacteristicCostnameImpl import Context_VnwserviceUuid_VnwconstraintLocalidCostcharacteristicCostnameImpl
from funcs_TapiVirtualNetwork.context_VnwserviceUuid_ServiceportLocalid_ExtensionsExtensionsspecificationImpl import Context_VnwserviceUuid_ServiceportLocalid_ExtensionsExtensionsspecificationImpl
from funcs_TapiVirtualNetwork.context_VnwserviceUuid_ServiceportLocalid_ExtensionsImpl import Context_VnwserviceUuid_ServiceportLocalid_ExtensionsImpl
from funcs_TapiVirtualNetwork.context_VnwserviceUuid_ServiceportImpl import Context_VnwserviceUuid_ServiceportImpl
from funcs_TapiVirtualNetwork.context_VnwserviceUuid_VnwconstraintLocalid_ExtensionsExtensionsspecificationImpl import Context_VnwserviceUuid_VnwconstraintLocalid_ExtensionsExtensionsspecificationImpl
from funcs_TapiVirtualNetwork.context_VnwserviceUuid_VnwconstraintImpl import Context_VnwserviceUuid_VnwconstraintImpl
from funcs_TapiVirtualNetwork.context_VnwserviceImpl import Context_VnwserviceImpl
from funcs_TapiVirtualNetwork.context_VnwserviceUuidImpl import Context_VnwserviceUuidImpl
from funcs_TapiVirtualNetwork.context_VnwserviceUuidNameImpl import Context_VnwserviceUuidNameImpl

# CALLABLE OBJECTS
from objects_TapiVirtualNetwork.linkPort import LinkPort
from objects_TapiVirtualNetwork.virtualNetworkServicePort import VirtualNetworkServicePort
from objects_TapiVirtualNetwork.createVirtualNetworkServiceRPCOutputSchema import CreateVirtualNetworkServiceRPCOutputSchema
from objects_TapiVirtualNetwork.capacity import Capacity
from objects_TapiVirtualNetwork.transferCostPac import TransferCostPac
from objects_TapiVirtualNetwork.networkTopologyService import NetworkTopologyService
from objects_TapiVirtualNetwork.timeRange import TimeRange
from objects_TapiVirtualNetwork.layerProtocolTransitionPac import LayerProtocolTransitionPac
from objects_TapiVirtualNetwork.transferTimingPac import TransferTimingPac
from objects_TapiVirtualNetwork.transferIntegrityPac import TransferIntegrityPac
from objects_TapiVirtualNetwork.nameAndValue import NameAndValue
from objects_TapiVirtualNetwork.adminStatePac import AdminStatePac
from objects_TapiVirtualNetwork.serviceEndPoint import ServiceEndPoint
from objects_TapiVirtualNetwork.validationMechanism import ValidationMechanism
from objects_TapiVirtualNetwork.node import Node
from objects_TapiVirtualNetwork.resourceSpec import ResourceSpec
from objects_TapiVirtualNetwork.teLink import TeLink
from objects_TapiVirtualNetwork.costCharacteristic import CostCharacteristic
from objects_TapiVirtualNetwork.latencyCharacteristic import LatencyCharacteristic
from objects_TapiVirtualNetwork.createVirtualNetworkServiceRPCInputSchema import CreateVirtualNetworkServiceRPCInputSchema
from objects_TapiVirtualNetwork.serviceSpec import ServiceSpec
from objects_TapiVirtualNetwork.getVirtualNetworkServiceListRPCOutputSchema import GetVirtualNetworkServiceListRPCOutputSchema
from objects_TapiVirtualNetwork.link import Link
from objects_TapiVirtualNetwork.localClass import LocalClass
from objects_TapiVirtualNetwork.deleteVirtualNetworkServiceRPCOutputSchema import DeleteVirtualNetworkServiceRPCOutputSchema
from objects_TapiVirtualNetwork.topology import Topology
from objects_TapiVirtualNetwork.extensionsSpec import ExtensionsSpec
from objects_TapiVirtualNetwork._vnwServiceSchema import _vnwServiceSchema
from objects_TapiVirtualNetwork.virtualNetworkService import VirtualNetworkService
from objects_TapiVirtualNetwork.nodeEdgePoint import NodeEdgePoint
from objects_TapiVirtualNetwork.virtualNetworkConstraint import VirtualNetworkConstraint
from objects_TapiVirtualNetwork.riskCharacteristic import RiskCharacteristic
from objects_TapiVirtualNetwork.riskParameterPac import RiskParameterPac
from objects_TapiVirtualNetwork.deleteVirtualNetworkServiceRPCInputSchema import DeleteVirtualNetworkServiceRPCInputSchema
from objects_TapiVirtualNetwork.operationalStatePac import OperationalStatePac
from objects_TapiVirtualNetwork.globalClass import GlobalClass
from objects_TapiVirtualNetwork.layerProtocol import LayerProtocol
from objects_TapiVirtualNetwork.transferCapacityPac import TransferCapacityPac
from objects_TapiVirtualNetwork.getVirtualNetworkServiceDetailsRPCInputSchema import GetVirtualNetworkServiceDetailsRPCInputSchema
from objects_TapiVirtualNetwork.lifecycleStatePac import LifecycleStatePac
from objects_TapiVirtualNetwork.getVirtualNetworkServiceDetailsRPCOutputSchema import GetVirtualNetworkServiceDetailsRPCOutputSchema
from objects_TapiVirtualNetwork.validationPac import ValidationPac

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


#/restconf/config/Context/_vnwService/(\w+)/_vnwConstraint/(\w+)/_extensions/
class Context_VnwserviceUuid_VnwconstraintLocalid_ExtensionsMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_VnwserviceUuid_VnwconstraintLocalid_ExtensionsImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/(\w+)/_state/
class Context_VnwserviceUuid_StateMethodView(MethodView):

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


#/restconf/config/Context/_vnwService/(\w+)/label/
class Context_VnwserviceUuidLabelMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: label"
        try:
            response = Context_VnwserviceUuidLabelImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/(\w+)/_extensions/(\w+)/
class Context_VnwserviceUuid_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_VnwserviceUuid_ExtensionsExtensionsspecificationImpl.get(uuid, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/(\w+)/_vnwConstraint/(\w+)/latencyCharacteristic/(\w+)/
class Context_VnwserviceUuid_VnwconstraintLocalidLatencycharacteristicTrafficpropertynameMethodView(MethodView):

    def put(self, uuid, localId, trafficPropertyName):
        print "Update operation of resource: latencyCharacteristic"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_VnwserviceUuid_VnwconstraintLocalidLatencycharacteristicTrafficpropertynameImpl.get(uuid, localId, trafficPropertyName)
        except KeyError as inst:
            if inst.args[0] != 'trafficPropertyName':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(LatencyCharacteristic, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_VnwserviceUuid_VnwconstraintLocalidLatencycharacteristicTrafficpropertynameImpl.put(uuid, localId, trafficPropertyName, new_object)
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
                    Context_VnwserviceUuid_VnwconstraintLocalidLatencycharacteristicTrafficpropertynameImpl.put(uuid, localId, trafficPropertyName, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid, localId, trafficPropertyName):
        print "Create operation of resource: latencyCharacteristic"
        try:
            response = Context_VnwserviceUuid_VnwconstraintLocalidLatencycharacteristicTrafficpropertynameImpl.get(uuid, localId, trafficPropertyName)
        except KeyError as inst:
            if inst.args[0] != 'trafficPropertyName':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(LatencyCharacteristic, json_struct, (trafficPropertyName,'trafficPropertyName'))
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_VnwserviceUuid_VnwconstraintLocalidLatencycharacteristicTrafficpropertynameImpl.post(uuid, localId, trafficPropertyName, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid, localId, trafficPropertyName):
        print "Delete operation of resource: latencyCharacteristic"
        try:
            response=Context_VnwserviceUuid_VnwconstraintLocalidLatencycharacteristicTrafficpropertynameImpl.delete(uuid, localId, trafficPropertyName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid, localId, trafficPropertyName):
        print "Retrieve operation of resource: latencyCharacteristic"
        try:
            response = Context_VnwserviceUuid_VnwconstraintLocalidLatencycharacteristicTrafficpropertynameImpl.get(uuid, localId, trafficPropertyName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/(\w+)/_schedule/
class Context_VnwserviceUuid_ScheduleMethodView(MethodView):

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


#/restconf/operations/getVirtualNetworkServiceDetails/
class GetvirtualnetworkservicedetailsMethodView(MethodView):

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



#/restconf/config/Context/_vnwService/(\w+)/name/(\w+)/
class Context_VnwserviceUuidNameValuenameMethodView(MethodView):

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


#/restconf/config/Context/_vnwService/(\w+)/_vnwConstraint/(\w+)/latencyCharacteristic/
class Context_VnwserviceUuid_VnwconstraintLocalidLatencycharacteristicMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: latencyCharacteristic"
        try:
            response = Context_VnwserviceUuid_VnwconstraintLocalidLatencycharacteristicImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/operations/createVirtualNetworkService/
class CreatevirtualnetworkserviceMethodView(MethodView):

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



#/restconf/operations/getVirtualNetworkServiceList/
class GetvirtualnetworkservicelistMethodView(MethodView):

    def post(self, ):
        print "Create operation of resource: getVirtualNetworkServiceList"
        json_struct = request.get_json() #json parser.
        new_object = (json_struct) #It creates an object instance from the json_input data.
        response = GetvirtualnetworkservicelistImpl.post( new_object)
        return Successful('Successful operation','{"description":"Create operation of resource: getVirtualNetworkServiceList"}')


#/restconf/config/Context/_vnwService/(\w+)/label/(\w+)/
class Context_VnwserviceUuidLabelValuenameMethodView(MethodView):

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


#/restconf/config/Context/_vnwService/(\w+)/_extensions/
class Context_VnwserviceUuid_ExtensionsMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_VnwserviceUuid_ExtensionsImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/(\w+)/_vnwConstraint/(\w+)/requestedCapacity/
class Context_VnwserviceUuid_VnwconstraintLocalidRequestedcapacityMethodView(MethodView):

    def put(self, uuid, localId):
        print "Update operation of resource: requestedCapacity"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_VnwserviceUuid_VnwconstraintLocalidRequestedcapacityImpl.get(uuid, localId)
        except KeyError as inst:
            if inst.args[0] != 'localId':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(Capacity, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_VnwserviceUuid_VnwconstraintLocalidRequestedcapacityImpl.put(uuid, localId, new_object)
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
                    Context_VnwserviceUuid_VnwconstraintLocalidRequestedcapacityImpl.put(uuid, localId, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid, localId):
        print "Create operation of resource: requestedCapacity"
        try:
            response = Context_VnwserviceUuid_VnwconstraintLocalidRequestedcapacityImpl.get(uuid, localId)
        except KeyError as inst:
            if inst.args[0] != 'localId':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(Capacity, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_VnwserviceUuid_VnwconstraintLocalidRequestedcapacityImpl.post(uuid, localId, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid, localId):
        print "Delete operation of resource: requestedCapacity"
        try:
            response=Context_VnwserviceUuid_VnwconstraintLocalidRequestedcapacityImpl.delete(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid, localId):
        print "Retrieve operation of resource: requestedCapacity"
        try:
            response = Context_VnwserviceUuid_VnwconstraintLocalidRequestedcapacityImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/(\w+)/_vnwConstraint/(\w+)/
class Context_VnwserviceUuid_VnwconstraintLocalidMethodView(MethodView):

    def put(self, uuid, localId):
        print "Update operation of resource: _vnwConstraint"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_VnwserviceUuid_VnwconstraintLocalidImpl.get(uuid, localId)
        except KeyError as inst:
            if inst.args[0] != 'localId':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(VirtualNetworkConstraint, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_VnwserviceUuid_VnwconstraintLocalidImpl.put(uuid, localId, new_object)
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
                    Context_VnwserviceUuid_VnwconstraintLocalidImpl.put(uuid, localId, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid, localId):
        print "Create operation of resource: _vnwConstraint"
        try:
            response = Context_VnwserviceUuid_VnwconstraintLocalidImpl.get(uuid, localId)
        except KeyError as inst:
            if inst.args[0] != 'localId':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(VirtualNetworkConstraint, json_struct, (localId,'localId'))
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_VnwserviceUuid_VnwconstraintLocalidImpl.post(uuid, localId, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid, localId):
        print "Delete operation of resource: _vnwConstraint"
        try:
            response=Context_VnwserviceUuid_VnwconstraintLocalidImpl.delete(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid, localId):
        print "Retrieve operation of resource: _vnwConstraint"
        try:
            response = Context_VnwserviceUuid_VnwconstraintLocalidImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/(\w+)/_vnwConstraint/(\w+)/costCharacteristic/
class Context_VnwserviceUuid_VnwconstraintLocalidCostcharacteristicMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: costCharacteristic"
        try:
            response = Context_VnwserviceUuid_VnwconstraintLocalidCostcharacteristicImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/operations/deleteVirtualNetworkService/
class DeletevirtualnetworkserviceMethodView(MethodView):

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



#/restconf/config/Context/_vnwService/(\w+)/_servicePort/(\w+)/
class Context_VnwserviceUuid_ServiceportLocalidMethodView(MethodView):

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


#/restconf/config/Context/_vnwService/(\w+)/_vnwConstraint/(\w+)/costCharacteristic/(\w+)/
class Context_VnwserviceUuid_VnwconstraintLocalidCostcharacteristicCostnameMethodView(MethodView):

    def put(self, uuid, localId, costName):
        print "Update operation of resource: costCharacteristic"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_VnwserviceUuid_VnwconstraintLocalidCostcharacteristicCostnameImpl.get(uuid, localId, costName)
        except KeyError as inst:
            if inst.args[0] != 'costName':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(CostCharacteristic, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_VnwserviceUuid_VnwconstraintLocalidCostcharacteristicCostnameImpl.put(uuid, localId, costName, new_object)
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
                    Context_VnwserviceUuid_VnwconstraintLocalidCostcharacteristicCostnameImpl.put(uuid, localId, costName, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid, localId, costName):
        print "Create operation of resource: costCharacteristic"
        try:
            response = Context_VnwserviceUuid_VnwconstraintLocalidCostcharacteristicCostnameImpl.get(uuid, localId, costName)
        except KeyError as inst:
            if inst.args[0] != 'costName':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(CostCharacteristic, json_struct, (costName,'costName'))
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_VnwserviceUuid_VnwconstraintLocalidCostcharacteristicCostnameImpl.post(uuid, localId, costName, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid, localId, costName):
        print "Delete operation of resource: costCharacteristic"
        try:
            response=Context_VnwserviceUuid_VnwconstraintLocalidCostcharacteristicCostnameImpl.delete(uuid, localId, costName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid, localId, costName):
        print "Retrieve operation of resource: costCharacteristic"
        try:
            response = Context_VnwserviceUuid_VnwconstraintLocalidCostcharacteristicCostnameImpl.get(uuid, localId, costName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/(\w+)/_servicePort/(\w+)/_extensions/(\w+)/
class Context_VnwserviceUuid_ServiceportLocalid_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, localId, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_VnwserviceUuid_ServiceportLocalid_ExtensionsExtensionsspecificationImpl.get(uuid, localId, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/(\w+)/_servicePort/(\w+)/_extensions/
class Context_VnwserviceUuid_ServiceportLocalid_ExtensionsMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_VnwserviceUuid_ServiceportLocalid_ExtensionsImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/(\w+)/_servicePort/
class Context_VnwserviceUuid_ServiceportMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _servicePort"
        try:
            response = Context_VnwserviceUuid_ServiceportImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/(\w+)/_vnwConstraint/(\w+)/_extensions/(\w+)/
class Context_VnwserviceUuid_VnwconstraintLocalid_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, localId, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_VnwserviceUuid_VnwconstraintLocalid_ExtensionsExtensionsspecificationImpl.get(uuid, localId, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/(\w+)/_vnwConstraint/
class Context_VnwserviceUuid_VnwconstraintMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _vnwConstraint"
        try:
            response = Context_VnwserviceUuid_VnwconstraintImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/
class Context_VnwserviceMethodView(MethodView):

    def get(self, ):
        print "Retrieve operation of resource: _vnwService"
        try:
            response = Context_VnwserviceImpl.get()
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_vnwService/(\w+)/
class Context_VnwserviceUuidMethodView(MethodView):

    def put(self, uuid):
        print "Update operation of resource: _vnwService"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_VnwserviceUuidImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(_vnwServiceSchema, json_struct)
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
            new_object = create_instance(_vnwServiceSchema, json_struct, (uuid,'uuid'))
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


#/restconf/config/Context/_vnwService/(\w+)/name/
class Context_VnwserviceUuidNameMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: name"
        try:
            response = Context_VnwserviceUuidNameImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))



getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_vnwConstraint/<localId>/_extensions/", view_func = globals()["Context_VnwserviceUuid_VnwconstraintLocalid_ExtensionsMethodView"].as_view('"Context_VnwserviceUuid_VnwconstraintLocalid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_state/", view_func = globals()["Context_VnwserviceUuid_StateMethodView"].as_view('"Context_VnwserviceUuid_State"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/label/", view_func = globals()["Context_VnwserviceUuidLabelMethodView"].as_view('"Context_VnwserviceUuidLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_VnwserviceUuid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_VnwserviceUuid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_vnwConstraint/<localId>/latencyCharacteristic/<trafficPropertyName>/", view_func = globals()["Context_VnwserviceUuid_VnwconstraintLocalidLatencycharacteristicTrafficpropertynameMethodView"].as_view('"Context_VnwserviceUuid_VnwconstraintLocalidLatencycharacteristicTrafficpropertyname"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_schedule/", view_func = globals()["Context_VnwserviceUuid_ScheduleMethodView"].as_view('"Context_VnwserviceUuid_Schedule"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getVirtualNetworkServiceDetails/", view_func = globals()["GetvirtualnetworkservicedetailsMethodView"].as_view('"Getvirtualnetworkservicedetails"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/name/<valueName>/", view_func = globals()["Context_VnwserviceUuidNameValuenameMethodView"].as_view('"Context_VnwserviceUuidNameValuename"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_vnwConstraint/<localId>/latencyCharacteristic/", view_func = globals()["Context_VnwserviceUuid_VnwconstraintLocalidLatencycharacteristicMethodView"].as_view('"Context_VnwserviceUuid_VnwconstraintLocalidLatencycharacteristic"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/createVirtualNetworkService/", view_func = globals()["CreatevirtualnetworkserviceMethodView"].as_view('"Createvirtualnetworkservice"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getVirtualNetworkServiceList/", view_func = globals()["GetvirtualnetworkservicelistMethodView"].as_view('"Getvirtualnetworkservicelist"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/label/<valueName>/", view_func = globals()["Context_VnwserviceUuidLabelValuenameMethodView"].as_view('"Context_VnwserviceUuidLabelValuename"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_extensions/", view_func = globals()["Context_VnwserviceUuid_ExtensionsMethodView"].as_view('"Context_VnwserviceUuid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_vnwConstraint/<localId>/requestedCapacity/", view_func = globals()["Context_VnwserviceUuid_VnwconstraintLocalidRequestedcapacityMethodView"].as_view('"Context_VnwserviceUuid_VnwconstraintLocalidRequestedcapacity"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_vnwConstraint/<localId>/", view_func = globals()["Context_VnwserviceUuid_VnwconstraintLocalidMethodView"].as_view('"Context_VnwserviceUuid_VnwconstraintLocalid"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_vnwConstraint/<localId>/costCharacteristic/", view_func = globals()["Context_VnwserviceUuid_VnwconstraintLocalidCostcharacteristicMethodView"].as_view('"Context_VnwserviceUuid_VnwconstraintLocalidCostcharacteristic"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/deleteVirtualNetworkService/", view_func = globals()["DeletevirtualnetworkserviceMethodView"].as_view('"Deletevirtualnetworkservice"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_servicePort/<localId>/", view_func = globals()["Context_VnwserviceUuid_ServiceportLocalidMethodView"].as_view('"Context_VnwserviceUuid_ServiceportLocalid"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_vnwConstraint/<localId>/costCharacteristic/<costName>/", view_func = globals()["Context_VnwserviceUuid_VnwconstraintLocalidCostcharacteristicCostnameMethodView"].as_view('"Context_VnwserviceUuid_VnwconstraintLocalidCostcharacteristicCostname"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_servicePort/<localId>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_VnwserviceUuid_ServiceportLocalid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_VnwserviceUuid_ServiceportLocalid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_servicePort/<localId>/_extensions/", view_func = globals()["Context_VnwserviceUuid_ServiceportLocalid_ExtensionsMethodView"].as_view('"Context_VnwserviceUuid_ServiceportLocalid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_servicePort/", view_func = globals()["Context_VnwserviceUuid_ServiceportMethodView"].as_view('"Context_VnwserviceUuid_Serviceport"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_vnwConstraint/<localId>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_VnwserviceUuid_VnwconstraintLocalid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_VnwserviceUuid_VnwconstraintLocalid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_vnwConstraint/", view_func = globals()["Context_VnwserviceUuid_VnwconstraintMethodView"].as_view('"Context_VnwserviceUuid_Vnwconstraint"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/", view_func = globals()["Context_VnwserviceMethodView"].as_view('"Context_Vnwservice"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/", view_func = globals()["Context_VnwserviceUuidMethodView"].as_view('"Context_VnwserviceUuid"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/name/", view_func = globals()["Context_VnwserviceUuidNameMethodView"].as_view('"Context_VnwserviceUuidName"'+'"_api"'), methods=['GET'])
