from flask import json, Blueprint, request, Response
from flask.views import MethodView
import sys
from objects_common.keyedArrayType import KeyedArrayKeyError

import base64
import re

# BACKEND FUNCTIONS
from funcs_Tapi.context_PathcompserviceUuid_ExtensionsExtensionsspecificationImpl import Context_PathcompserviceUuid_ExtensionsExtensionsspecificationImpl
from funcs_Tapi.context_PathUuidNameImpl import Context_PathUuidNameImpl
from funcs_Tapi.context_PathUuidNameValuenameImpl import Context_PathUuidNameValuenameImpl
from funcs_Tapi.context_VnwserviceUuidLabelImpl import Context_VnwserviceUuidLabelImpl
from funcs_Tapi.context_TopologyUuidNameImpl import Context_TopologyUuidNameImpl
from funcs_Tapi.context_TopologyUuidNameValuenameImpl import Context_TopologyUuidNameValuenameImpl
from funcs_Tapi.contextLabelImpl import ContextLabelImpl
from funcs_Tapi.context_NotifsubscriptionUuidNameValuenameImpl import Context_NotifsubscriptionUuidNameValuenameImpl
from funcs_Tapi.contextNameImpl import ContextNameImpl
from funcs_Tapi.context_NotifsubscriptionUuidNameImpl import Context_NotifsubscriptionUuidNameImpl
from funcs_Tapi.context_Nwtopologyservice_ExtensionsImpl import Context_Nwtopologyservice_ExtensionsImpl
from funcs_Tapi.context_VnwserviceUuid_ExtensionsImpl import Context_VnwserviceUuid_ExtensionsImpl
from funcs_Tapi.context_ServiceendpointUuidNameValuenameImpl import Context_ServiceendpointUuidNameValuenameImpl
from funcs_Tapi.context_PathcompserviceUuidLabelValuenameImpl import Context_PathcompserviceUuidLabelValuenameImpl
from funcs_Tapi.context_ConnectionUuid_ExtensionsExtensionsspecificationImpl import Context_ConnectionUuid_ExtensionsExtensionsspecificationImpl
from funcs_Tapi.context_ConnectionImpl import Context_ConnectionImpl
from funcs_Tapi.context_ConnectivityserviceUuid_ExtensionsExtensionsspecificationImpl import Context_ConnectivityserviceUuid_ExtensionsExtensionsspecificationImpl
from funcs_Tapi.context_ServiceendpointUuidLabelValuenameImpl import Context_ServiceendpointUuidLabelValuenameImpl
from funcs_Tapi.context_PathUuidImpl import Context_PathUuidImpl
from funcs_Tapi.context_NwtopologyserviceLabelValuenameImpl import Context_NwtopologyserviceLabelValuenameImpl
from funcs_Tapi.context_ConnectionUuidLabelImpl import Context_ConnectionUuidLabelImpl
from funcs_Tapi.context_PathImpl import Context_PathImpl
from funcs_Tapi.context_PathUuidLabelValuenameImpl import Context_PathUuidLabelValuenameImpl
from funcs_Tapi.context_NotificationUuidNameValuenameImpl import Context_NotificationUuidNameValuenameImpl
from funcs_Tapi.context_NotifsubscriptionUuidLabelImpl import Context_NotifsubscriptionUuidLabelImpl
from funcs_Tapi.context_VnwserviceUuidNameValuenameImpl import Context_VnwserviceUuidNameValuenameImpl
from funcs_Tapi.context_NwtopologyserviceImpl import Context_NwtopologyserviceImpl
from funcs_Tapi.context_ServiceendpointUuid_LayerprotocolLocalid_ExtensionsImpl import Context_ServiceendpointUuid_LayerprotocolLocalid_ExtensionsImpl
from funcs_Tapi.contextImpl import ContextImpl
from funcs_Tapi.context_TopologyUuidLabelImpl import Context_TopologyUuidLabelImpl
from funcs_Tapi.context_VnwserviceImpl import Context_VnwserviceImpl
from funcs_Tapi.context_PathcompserviceUuidNameImpl import Context_PathcompserviceUuidNameImpl
from funcs_Tapi.context_ConnectivityserviceUuidLabelImpl import Context_ConnectivityserviceUuidLabelImpl
from funcs_Tapi.context_NotificationUuid_ExtensionsExtensionsspecificationImpl import Context_NotificationUuid_ExtensionsExtensionsspecificationImpl
from funcs_Tapi.context_ExtensionsImpl import Context_ExtensionsImpl
from funcs_Tapi.context_ConnectivityserviceUuidImpl import Context_ConnectivityserviceUuidImpl
from funcs_Tapi.context_ConnectionUuidNameImpl import Context_ConnectionUuidNameImpl
from funcs_Tapi.context_NotificationUuidImpl import Context_NotificationUuidImpl
from funcs_Tapi.context_PathcompserviceUuidLabelImpl import Context_PathcompserviceUuidLabelImpl
from funcs_Tapi.context_VnwserviceUuidNameImpl import Context_VnwserviceUuidNameImpl
from funcs_Tapi.context_ConnectivityserviceUuidNameImpl import Context_ConnectivityserviceUuidNameImpl
from funcs_Tapi.context_PathcompserviceUuidNameValuenameImpl import Context_PathcompserviceUuidNameValuenameImpl
from funcs_Tapi.context_ServiceendpointUuid_LayerprotocolImpl import Context_ServiceendpointUuid_LayerprotocolImpl
from funcs_Tapi.context_TopologyUuid_ExtensionsExtensionsspecificationImpl import Context_TopologyUuid_ExtensionsExtensionsspecificationImpl
from funcs_Tapi.context_PathcompserviceUuidImpl import Context_PathcompserviceUuidImpl
from funcs_Tapi.context_ConnectionUuidNameValuenameImpl import Context_ConnectionUuidNameValuenameImpl
from funcs_Tapi.context_ServiceendpointUuid_ExtensionsExtensionsspecificationImpl import Context_ServiceendpointUuid_ExtensionsExtensionsspecificationImpl
from funcs_Tapi.context_TopologyUuid_ExtensionsImpl import Context_TopologyUuid_ExtensionsImpl
from funcs_Tapi.context_NwtopologyserviceNameImpl import Context_NwtopologyserviceNameImpl
from funcs_Tapi.context_NotifsubscriptionUuid_ExtensionsExtensionsspecificationImpl import Context_NotifsubscriptionUuid_ExtensionsExtensionsspecificationImpl
from funcs_Tapi.context_NotificationUuid_ExtensionsImpl import Context_NotificationUuid_ExtensionsImpl
from funcs_Tapi.context_ServiceendpointUuid_LayerprotocolLocalid_ExtensionsExtensionsspecificationImpl import Context_ServiceendpointUuid_LayerprotocolLocalid_ExtensionsExtensionsspecificationImpl
from funcs_Tapi.context_NotificationImpl import Context_NotificationImpl
from funcs_Tapi.context_ServiceendpointUuid_StateImpl import Context_ServiceendpointUuid_StateImpl
from funcs_Tapi.context_ConnectionUuidLabelValuenameImpl import Context_ConnectionUuidLabelValuenameImpl
from funcs_Tapi.context_NotifsubscriptionUuidLabelValuenameImpl import Context_NotifsubscriptionUuidLabelValuenameImpl
from funcs_Tapi.context_ServiceendpointUuidImpl import Context_ServiceendpointUuidImpl
from funcs_Tapi.context_TopologyUuidLabelValuenameImpl import Context_TopologyUuidLabelValuenameImpl
from funcs_Tapi.context_VnwserviceUuidLabelValuenameImpl import Context_VnwserviceUuidLabelValuenameImpl
from funcs_Tapi.context_ConnectivityserviceUuidLabelValuenameImpl import Context_ConnectivityserviceUuidLabelValuenameImpl
from funcs_Tapi.context_PathUuidLabelImpl import Context_PathUuidLabelImpl
from funcs_Tapi.context_NotificationUuidLabelImpl import Context_NotificationUuidLabelImpl
from funcs_Tapi.context_ConnectionUuid_ExtensionsImpl import Context_ConnectionUuid_ExtensionsImpl
from funcs_Tapi.context_Nwtopologyservice_ExtensionsExtensionsspecificationImpl import Context_Nwtopologyservice_ExtensionsExtensionsspecificationImpl
from funcs_Tapi.context_ConnectivityserviceUuid_ExtensionsImpl import Context_ConnectivityserviceUuid_ExtensionsImpl
from funcs_Tapi.context_VnwserviceUuidImpl import Context_VnwserviceUuidImpl
from funcs_Tapi.context_TopologyImpl import Context_TopologyImpl
from funcs_Tapi.context_ExtensionsExtensionsspecificationImpl import Context_ExtensionsExtensionsspecificationImpl
from funcs_Tapi.context_ServiceendpointUuid_ExtensionsImpl import Context_ServiceendpointUuid_ExtensionsImpl
from funcs_Tapi.context_VnwserviceUuid_ExtensionsExtensionsspecificationImpl import Context_VnwserviceUuid_ExtensionsExtensionsspecificationImpl
from funcs_Tapi.context_PathUuid_ExtensionsImpl import Context_PathUuid_ExtensionsImpl
from funcs_Tapi.context_ConnectivityserviceUuidNameValuenameImpl import Context_ConnectivityserviceUuidNameValuenameImpl
from funcs_Tapi.context_NotifsubscriptionUuid_ExtensionsImpl import Context_NotifsubscriptionUuid_ExtensionsImpl
from funcs_Tapi.context_PathcompserviceUuid_ExtensionsImpl import Context_PathcompserviceUuid_ExtensionsImpl
from funcs_Tapi.context_PathUuid_ExtensionsExtensionsspecificationImpl import Context_PathUuid_ExtensionsExtensionsspecificationImpl
from funcs_Tapi.context_NwtopologyserviceNameValuenameImpl import Context_NwtopologyserviceNameValuenameImpl
from funcs_Tapi.context_NwtopologyserviceLabelImpl import Context_NwtopologyserviceLabelImpl
from funcs_Tapi.context_ServiceendpointImpl import Context_ServiceendpointImpl
from funcs_Tapi.context_NotificationUuidNameImpl import Context_NotificationUuidNameImpl
from funcs_Tapi.context_NotifsubscriptionImpl import Context_NotifsubscriptionImpl
from funcs_Tapi.context_ServiceendpointUuid_LayerprotocolLocalidImpl import Context_ServiceendpointUuid_LayerprotocolLocalidImpl
from funcs_Tapi.context_TopologyUuidImpl import Context_TopologyUuidImpl
from funcs_Tapi.context_PathcompserviceImpl import Context_PathcompserviceImpl
from funcs_Tapi.context_ConnectionUuidImpl import Context_ConnectionUuidImpl
from funcs_Tapi.context_ServiceendpointUuidLabelImpl import Context_ServiceendpointUuidLabelImpl
from funcs_Tapi.context_ServiceendpointUuidNameImpl import Context_ServiceendpointUuidNameImpl
from funcs_Tapi.contextNameValuenameImpl import ContextNameValuenameImpl
from funcs_Tapi.context_ConnectivityserviceImpl import Context_ConnectivityserviceImpl
from funcs_Tapi.contextLabelValuenameImpl import ContextLabelValuenameImpl
from funcs_Tapi.context_NotificationUuidLabelValuenameImpl import Context_NotificationUuidLabelValuenameImpl
from funcs_Tapi.context_NotifsubscriptionUuidImpl import Context_NotifsubscriptionUuidImpl

# CALLABLE OBJECTS
from objects_Tapi.extensionsSpec import ExtensionsSpec
from objects_Tapi.timeRange import TimeRange
from objects_Tapi.operationalStatePac import OperationalStatePac
from objects_Tapi.resourceSpec import ResourceSpec
from objects_Tapi.globalClass import GlobalClass
from objects_Tapi.layerProtocol import LayerProtocol
from objects_Tapi.serviceSpec import ServiceSpec
from objects_Tapi.contextSchema import ContextSchema
from objects_Tapi.nameAndValue import NameAndValue
from objects_Tapi.lifecycleStatePac import LifecycleStatePac
from objects_Tapi.adminStatePac import AdminStatePac
from objects_Tapi._serviceEndPointSchema import _serviceEndPointSchema
from objects_Tapi.serviceEndPoint import ServiceEndPoint
from objects_Tapi.localClass import LocalClass

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

#/restconf/config/Context/label/
class ContextLabelMethodView(MethodView):

    def get(self, ):
        print "Retrieve operation of resource: label"
        try:
            response = ContextLabelImpl.get()
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notifSubscription/(\w+)/name/(\w+)/
class Context_NotifsubscriptionUuidNameValuenameMethodView(MethodView):

    def put(self, uuid, valueName):
        print "Update operation of resource: name"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_NotifsubscriptionUuidNameValuenameImpl.get(uuid, valueName)
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
                    Context_NotifsubscriptionUuidNameValuenameImpl.put(uuid, valueName, new_object)
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
                    Context_NotifsubscriptionUuidNameValuenameImpl.put(uuid, valueName, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid, valueName):
        print "Create operation of resource: name"
        try:
            response = Context_NotifsubscriptionUuidNameValuenameImpl.get(uuid, valueName)
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
                    Context_NotifsubscriptionUuidNameValuenameImpl.post(uuid, valueName, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid, valueName):
        print "Delete operation of resource: name"
        try:
            response=Context_NotifsubscriptionUuidNameValuenameImpl.delete(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid, valueName):
        print "Retrieve operation of resource: name"
        try:
            response = Context_NotifsubscriptionUuidNameValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/name/
class ContextNameMethodView(MethodView):

    def get(self, ):
        print "Retrieve operation of resource: name"
        try:
            response = ContextNameImpl.get()
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notifSubscription/(\w+)/name/
class Context_NotifsubscriptionUuidNameMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: name"
        try:
            response = Context_NotifsubscriptionUuidNameImpl.get(uuid)
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


#/restconf/config/Context/_serviceEndPoint/(\w+)/name/(\w+)/
class Context_ServiceendpointUuidNameValuenameMethodView(MethodView):

    def get(self, uuid, valueName):
        print "Retrieve operation of resource: name"
        try:
            response = Context_ServiceendpointUuidNameValuenameImpl.get(uuid, valueName)
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


#/restconf/config/Context/_serviceEndPoint/(\w+)/label/(\w+)/
class Context_ServiceendpointUuidLabelValuenameMethodView(MethodView):

    def get(self, uuid, valueName):
        print "Retrieve operation of resource: label"
        try:
            response = Context_ServiceendpointUuidLabelValuenameImpl.get(uuid, valueName)
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


#/restconf/config/Context/_notification/(\w+)/name/(\w+)/
class Context_NotificationUuidNameValuenameMethodView(MethodView):

    def get(self, uuid, valueName):
        print "Retrieve operation of resource: name"
        try:
            response = Context_NotificationUuidNameValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notifSubscription/(\w+)/label/
class Context_NotifsubscriptionUuidLabelMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: label"
        try:
            response = Context_NotifsubscriptionUuidLabelImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
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


#/restconf/config/Context/_serviceEndPoint/(\w+)/_layerProtocol/(\w+)/_extensions/
class Context_ServiceendpointUuid_LayerprotocolLocalid_ExtensionsMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_ServiceendpointUuid_LayerprotocolLocalid_ExtensionsImpl.get(uuid, localId)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/
class ContextMethodView(MethodView):

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



#/restconf/config/Context/_notification/(\w+)/_extensions/(\w+)/
class Context_NotificationUuid_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_NotificationUuid_ExtensionsExtensionsspecificationImpl.get(uuid, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_extensions/
class Context_ExtensionsMethodView(MethodView):

    def get(self, ):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_ExtensionsImpl.get()
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notification/(\w+)/
class Context_NotificationUuidMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _notification"
        try:
            response = Context_NotificationUuidImpl.get(uuid)
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


#/restconf/config/Context/_serviceEndPoint/(\w+)/_layerProtocol/
class Context_ServiceendpointUuid_LayerprotocolMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _layerProtocol"
        try:
            response = Context_ServiceendpointUuid_LayerprotocolImpl.get(uuid)
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

            new_object = create_instance(ServiceSpec, json_struct)
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
            new_object = create_instance(ServiceSpec, json_struct, (uuid,'uuid'))
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


#/restconf/config/Context/_serviceEndPoint/(\w+)/_extensions/(\w+)/
class Context_ServiceendpointUuid_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_ServiceendpointUuid_ExtensionsExtensionsspecificationImpl.get(uuid, extensionsSpecification)
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


#/restconf/config/Context/_notifSubscription/(\w+)/_extensions/(\w+)/
class Context_NotifsubscriptionUuid_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_NotifsubscriptionUuid_ExtensionsExtensionsspecificationImpl.get(uuid, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notification/(\w+)/_extensions/
class Context_NotificationUuid_ExtensionsMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_NotificationUuid_ExtensionsImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_serviceEndPoint/(\w+)/_layerProtocol/(\w+)/_extensions/(\w+)/
class Context_ServiceendpointUuid_LayerprotocolLocalid_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, localId, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_ServiceendpointUuid_LayerprotocolLocalid_ExtensionsExtensionsspecificationImpl.get(uuid, localId, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notification/
class Context_NotificationMethodView(MethodView):

    def get(self, ):
        print "Retrieve operation of resource: _notification"
        try:
            response = Context_NotificationImpl.get()
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_serviceEndPoint/(\w+)/_state/
class Context_ServiceendpointUuid_StateMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _state"
        try:
            response = Context_ServiceendpointUuid_StateImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notifSubscription/(\w+)/label/(\w+)/
class Context_NotifsubscriptionUuidLabelValuenameMethodView(MethodView):

    def put(self, uuid, valueName):
        print "Update operation of resource: label"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_NotifsubscriptionUuidLabelValuenameImpl.get(uuid, valueName)
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
                    Context_NotifsubscriptionUuidLabelValuenameImpl.put(uuid, valueName, new_object)
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
                    Context_NotifsubscriptionUuidLabelValuenameImpl.put(uuid, valueName, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid, valueName):
        print "Create operation of resource: label"
        try:
            response = Context_NotifsubscriptionUuidLabelValuenameImpl.get(uuid, valueName)
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
                    Context_NotifsubscriptionUuidLabelValuenameImpl.post(uuid, valueName, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid, valueName):
        print "Delete operation of resource: label"
        try:
            response=Context_NotifsubscriptionUuidLabelValuenameImpl.delete(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid, valueName):
        print "Retrieve operation of resource: label"
        try:
            response = Context_NotifsubscriptionUuidLabelValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_serviceEndPoint/(\w+)/
class Context_ServiceendpointUuidMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _serviceEndPoint"
        try:
            response = Context_ServiceendpointUuidImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


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


#/restconf/config/Context/_notification/(\w+)/label/
class Context_NotificationUuidLabelMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: label"
        try:
            response = Context_NotificationUuidLabelImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
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

            new_object = create_instance(ServiceSpec, json_struct)
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
            new_object = create_instance(ServiceSpec, json_struct, (uuid,'uuid'))
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


#/restconf/config/Context/_extensions/(\w+)/
class Context_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_ExtensionsExtensionsspecificationImpl.get(extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_serviceEndPoint/(\w+)/_extensions/
class Context_ServiceendpointUuid_ExtensionsMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_ServiceendpointUuid_ExtensionsImpl.get(uuid)
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


#/restconf/config/Context/_notifSubscription/(\w+)/_extensions/
class Context_NotifsubscriptionUuid_ExtensionsMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_NotifsubscriptionUuid_ExtensionsImpl.get(uuid)
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


#/restconf/config/Context/_serviceEndPoint/
class Context_ServiceendpointMethodView(MethodView):

    def get(self, ):
        print "Retrieve operation of resource: _serviceEndPoint"
        try:
            response = Context_ServiceendpointImpl.get()
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notification/(\w+)/name/
class Context_NotificationUuidNameMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: name"
        try:
            response = Context_NotificationUuidNameImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notifSubscription/
class Context_NotifsubscriptionMethodView(MethodView):

    def get(self, ):
        print "Retrieve operation of resource: _notifSubscription"
        try:
            response = Context_NotifsubscriptionImpl.get()
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_serviceEndPoint/(\w+)/_layerProtocol/(\w+)/
class Context_ServiceendpointUuid_LayerprotocolLocalidMethodView(MethodView):

    def get(self, uuid, localId):
        print "Retrieve operation of resource: _layerProtocol"
        try:
            response = Context_ServiceendpointUuid_LayerprotocolLocalidImpl.get(uuid, localId)
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


#/restconf/config/Context/_serviceEndPoint/(\w+)/label/
class Context_ServiceendpointUuidLabelMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: label"
        try:
            response = Context_ServiceendpointUuidLabelImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_serviceEndPoint/(\w+)/name/
class Context_ServiceendpointUuidNameMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: name"
        try:
            response = Context_ServiceendpointUuidNameImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/name/(\w+)/
class ContextNameValuenameMethodView(MethodView):

    def put(self, valueName):
        print "Update operation of resource: name"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = ContextNameValuenameImpl.get(valueName)
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
                    ContextNameValuenameImpl.put(valueName, new_object)
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
                    ContextNameValuenameImpl.put(valueName, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, valueName):
        print "Create operation of resource: name"
        try:
            response = ContextNameValuenameImpl.get(valueName)
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
                    ContextNameValuenameImpl.post(valueName, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, valueName):
        print "Delete operation of resource: name"
        try:
            response=ContextNameValuenameImpl.delete(valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, valueName):
        print "Retrieve operation of resource: name"
        try:
            response = ContextNameValuenameImpl.get(valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/label/(\w+)/
class ContextLabelValuenameMethodView(MethodView):

    def put(self, valueName):
        print "Update operation of resource: label"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = ContextLabelValuenameImpl.get(valueName)
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
                    ContextLabelValuenameImpl.put(valueName, new_object)
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
                    ContextLabelValuenameImpl.put(valueName, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, valueName):
        print "Create operation of resource: label"
        try:
            response = ContextLabelValuenameImpl.get(valueName)
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
                    ContextLabelValuenameImpl.post(valueName, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, valueName):
        print "Delete operation of resource: label"
        try:
            response=ContextLabelValuenameImpl.delete(valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, valueName):
        print "Retrieve operation of resource: label"
        try:
            response = ContextLabelValuenameImpl.get(valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notification/(\w+)/label/(\w+)/
class Context_NotificationUuidLabelValuenameMethodView(MethodView):

    def get(self, uuid, valueName):
        print "Retrieve operation of resource: label"
        try:
            response = Context_NotificationUuidLabelValuenameImpl.get(uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notifSubscription/(\w+)/
class Context_NotifsubscriptionUuidMethodView(MethodView):

    def put(self, uuid):
        print "Update operation of resource: _notifSubscription"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_NotifsubscriptionUuidImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(ServiceSpec, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_NotifsubscriptionUuidImpl.put(uuid, new_object)
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
                    Context_NotifsubscriptionUuidImpl.put(uuid, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid):
        print "Create operation of resource: _notifSubscription"
        try:
            response = Context_NotifsubscriptionUuidImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(ServiceSpec, json_struct, (uuid,'uuid'))
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_NotifsubscriptionUuidImpl.post(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid):
        print "Delete operation of resource: _notifSubscription"
        try:
            response=Context_NotifsubscriptionUuidImpl.delete(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid):
        print "Retrieve operation of resource: _notifSubscription"
        try:
            response = Context_NotifsubscriptionUuidImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))



getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_PathcompserviceUuid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_PathcompserviceUuid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/name/", view_func = globals()["Context_PathUuidNameMethodView"].as_view('"Context_PathUuidName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/name/<valueName>/", view_func = globals()["Context_PathUuidNameValuenameMethodView"].as_view('"Context_PathUuidNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/label/", view_func = globals()["Context_VnwserviceUuidLabelMethodView"].as_view('"Context_VnwserviceUuidLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/label/", view_func = globals()["ContextLabelMethodView"].as_view('"ContextLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/name/<valueName>/", view_func = globals()["Context_NotifsubscriptionUuidNameValuenameMethodView"].as_view('"Context_NotifsubscriptionUuidNameValuename"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/name/", view_func = globals()["ContextNameMethodView"].as_view('"ContextName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/name/", view_func = globals()["Context_NotifsubscriptionUuidNameMethodView"].as_view('"Context_NotifsubscriptionUuidName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_nwTopologyService/_extensions/", view_func = globals()["Context_Nwtopologyservice_ExtensionsMethodView"].as_view('"Context_Nwtopologyservice_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_extensions/", view_func = globals()["Context_VnwserviceUuid_ExtensionsMethodView"].as_view('"Context_VnwserviceUuid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/name/<valueName>/", view_func = globals()["Context_ServiceendpointUuidNameValuenameMethodView"].as_view('"Context_ServiceendpointUuidNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/label/<valueName>/", view_func = globals()["Context_PathcompserviceUuidLabelValuenameMethodView"].as_view('"Context_PathcompserviceUuidLabelValuename"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/label/<valueName>/", view_func = globals()["Context_ServiceendpointUuidLabelValuenameMethodView"].as_view('"Context_ServiceendpointUuidLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/", view_func = globals()["Context_PathUuidMethodView"].as_view('"Context_PathUuid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_nwTopologyService/label/<valueName>/", view_func = globals()["Context_NwtopologyserviceLabelValuenameMethodView"].as_view('"Context_NwtopologyserviceLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/", view_func = globals()["Context_PathMethodView"].as_view('"Context_Path"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/label/<valueName>/", view_func = globals()["Context_PathUuidLabelValuenameMethodView"].as_view('"Context_PathUuidLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notification/<uuid>/name/<valueName>/", view_func = globals()["Context_NotificationUuidNameValuenameMethodView"].as_view('"Context_NotificationUuidNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/label/", view_func = globals()["Context_NotifsubscriptionUuidLabelMethodView"].as_view('"Context_NotifsubscriptionUuidLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/name/<valueName>/", view_func = globals()["Context_VnwserviceUuidNameValuenameMethodView"].as_view('"Context_VnwserviceUuidNameValuename"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_nwTopologyService/", view_func = globals()["Context_NwtopologyserviceMethodView"].as_view('"Context_Nwtopologyservice"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_layerProtocol/<localId>/_extensions/", view_func = globals()["Context_ServiceendpointUuid_LayerprotocolLocalid_ExtensionsMethodView"].as_view('"Context_ServiceendpointUuid_LayerprotocolLocalid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/", view_func = globals()["ContextMethodView"].as_view('"Context"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/", view_func = globals()["Context_VnwserviceMethodView"].as_view('"Context_Vnwservice"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/name/", view_func = globals()["Context_PathcompserviceUuidNameMethodView"].as_view('"Context_PathcompserviceUuidName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notification/<uuid>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_NotificationUuid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_NotificationUuid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_extensions/", view_func = globals()["Context_ExtensionsMethodView"].as_view('"Context_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notification/<uuid>/", view_func = globals()["Context_NotificationUuidMethodView"].as_view('"Context_NotificationUuid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/label/", view_func = globals()["Context_PathcompserviceUuidLabelMethodView"].as_view('"Context_PathcompserviceUuidLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/name/", view_func = globals()["Context_VnwserviceUuidNameMethodView"].as_view('"Context_VnwserviceUuidName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/name/<valueName>/", view_func = globals()["Context_PathcompserviceUuidNameValuenameMethodView"].as_view('"Context_PathcompserviceUuidNameValuename"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_layerProtocol/", view_func = globals()["Context_ServiceendpointUuid_LayerprotocolMethodView"].as_view('"Context_ServiceendpointUuid_Layerprotocol"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/", view_func = globals()["Context_PathcompserviceUuidMethodView"].as_view('"Context_PathcompserviceUuid"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_ServiceendpointUuid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_ServiceendpointUuid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_nwTopologyService/name/", view_func = globals()["Context_NwtopologyserviceNameMethodView"].as_view('"Context_NwtopologyserviceName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_NotifsubscriptionUuid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_NotifsubscriptionUuid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notification/<uuid>/_extensions/", view_func = globals()["Context_NotificationUuid_ExtensionsMethodView"].as_view('"Context_NotificationUuid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_layerProtocol/<localId>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_ServiceendpointUuid_LayerprotocolLocalid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_ServiceendpointUuid_LayerprotocolLocalid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notification/", view_func = globals()["Context_NotificationMethodView"].as_view('"Context_Notification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_state/", view_func = globals()["Context_ServiceendpointUuid_StateMethodView"].as_view('"Context_ServiceendpointUuid_State"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/label/<valueName>/", view_func = globals()["Context_NotifsubscriptionUuidLabelValuenameMethodView"].as_view('"Context_NotifsubscriptionUuidLabelValuename"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/", view_func = globals()["Context_ServiceendpointUuidMethodView"].as_view('"Context_ServiceendpointUuid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/label/<valueName>/", view_func = globals()["Context_VnwserviceUuidLabelValuenameMethodView"].as_view('"Context_VnwserviceUuidLabelValuename"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/label/", view_func = globals()["Context_PathUuidLabelMethodView"].as_view('"Context_PathUuidLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notification/<uuid>/label/", view_func = globals()["Context_NotificationUuidLabelMethodView"].as_view('"Context_NotificationUuidLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_nwTopologyService/_extensions/<extensionsSpecification>/", view_func = globals()["Context_Nwtopologyservice_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_Nwtopologyservice_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/", view_func = globals()["Context_VnwserviceUuidMethodView"].as_view('"Context_VnwserviceUuid"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_extensions/<extensionsSpecification>/", view_func = globals()["Context_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_extensions/", view_func = globals()["Context_ServiceendpointUuid_ExtensionsMethodView"].as_view('"Context_ServiceendpointUuid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_vnwService/<uuid>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_VnwserviceUuid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_VnwserviceUuid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_extensions/", view_func = globals()["Context_PathUuid_ExtensionsMethodView"].as_view('"Context_PathUuid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/_extensions/", view_func = globals()["Context_NotifsubscriptionUuid_ExtensionsMethodView"].as_view('"Context_NotifsubscriptionUuid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/<uuid>/_extensions/", view_func = globals()["Context_PathcompserviceUuid_ExtensionsMethodView"].as_view('"Context_PathcompserviceUuid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_path/<uuid>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_PathUuid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_PathUuid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_nwTopologyService/name/<valueName>/", view_func = globals()["Context_NwtopologyserviceNameValuenameMethodView"].as_view('"Context_NwtopologyserviceNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_nwTopologyService/label/", view_func = globals()["Context_NwtopologyserviceLabelMethodView"].as_view('"Context_NwtopologyserviceLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/", view_func = globals()["Context_ServiceendpointMethodView"].as_view('"Context_Serviceendpoint"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notification/<uuid>/name/", view_func = globals()["Context_NotificationUuidNameMethodView"].as_view('"Context_NotificationUuidName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/", view_func = globals()["Context_NotifsubscriptionMethodView"].as_view('"Context_Notifsubscription"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/_layerProtocol/<localId>/", view_func = globals()["Context_ServiceendpointUuid_LayerprotocolLocalidMethodView"].as_view('"Context_ServiceendpointUuid_LayerprotocolLocalid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_pathCompService/", view_func = globals()["Context_PathcompserviceMethodView"].as_view('"Context_Pathcompservice"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/label/", view_func = globals()["Context_ServiceendpointUuidLabelMethodView"].as_view('"Context_ServiceendpointUuidLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_serviceEndPoint/<uuid>/name/", view_func = globals()["Context_ServiceendpointUuidNameMethodView"].as_view('"Context_ServiceendpointUuidName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/name/<valueName>/", view_func = globals()["ContextNameValuenameMethodView"].as_view('"ContextNameValuename"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/label/<valueName>/", view_func = globals()["ContextLabelValuenameMethodView"].as_view('"ContextLabelValuename"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notification/<uuid>/label/<valueName>/", view_func = globals()["Context_NotificationUuidLabelValuenameMethodView"].as_view('"Context_NotificationUuidLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/", view_func = globals()["Context_NotifsubscriptionUuidMethodView"].as_view('"Context_NotifsubscriptionUuid"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
