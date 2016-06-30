from flask import json, Blueprint, request, Response
from flask.views import MethodView
import sys
from objects_common.keyedArrayType import KeyedArrayKeyError

import base64
import re

# BACKEND FUNCTIONS
from funcs_TapiNotification.getnotificationlistImpl import GetnotificationlistImpl
from funcs_TapiNotification.updatenotificationsubscriptionserviceImpl import UpdatenotificationsubscriptionserviceImpl
from funcs_TapiNotification.createnotificationsubscriptionserviceImpl import CreatenotificationsubscriptionserviceImpl
from funcs_TapiNotification.deletenotificationsubscriptionserviceImpl import DeletenotificationsubscriptionserviceImpl
from funcs_TapiNotification.getsupportednotificationtypesImpl import GetsupportednotificationtypesImpl
from funcs_TapiNotification.getnotificationsubscriptionservicelistImpl import GetnotificationsubscriptionservicelistImpl
from funcs_TapiNotification.getnotificationsubscriptionservicedetailsImpl import GetnotificationsubscriptionservicedetailsImpl

# CALLABLE OBJECTS
from objects_TapiNotification.service import Service
from objects_TapiNotification.notification import Notification
from objects_TapiNotification.timeRange import TimeRange
from objects_TapiNotification.deleteNotificationSubscriptionServiceRPCInputSchema import DeleteNotificationSubscriptionServiceRPCInputSchema
from objects_TapiNotification.nameAndValue import NameAndValue
from objects_TapiNotification.adminStatePac import AdminStatePac
from objects_TapiNotification.getNotificationListRPCInputSchema import GetNotificationListRPCInputSchema
from objects_TapiNotification.updateNotificationSubscriptionServiceRPCOutputSchema import UpdateNotificationSubscriptionServiceRPCOutputSchema
from objects_TapiNotification.createNotificationSubscriptionServiceRPCOutputSchema import CreateNotificationSubscriptionServiceRPCOutputSchema
from objects_TapiNotification.getNotificationSubscriptionServiceDetailsRPCInputSchema import GetNotificationSubscriptionServiceDetailsRPCInputSchema
from objects_TapiNotification.updateNotificationSubscriptionServiceRPCInputSchema import UpdateNotificationSubscriptionServiceRPCInputSchema
from objects_TapiNotification.localClass import LocalClass
from objects_TapiNotification.getNotificationSubscriptionServiceDetailsRPCOutputSchema import GetNotificationSubscriptionServiceDetailsRPCOutputSchema
from objects_TapiNotification.getNotificationSubscriptionServiceListRPCOutputSchema import GetNotificationSubscriptionServiceListRPCOutputSchema
from objects_TapiNotification.extensionsSpec import ExtensionsSpec
from objects_TapiNotification.resource import Resource
from objects_TapiNotification.deleteNotificationSubscriptionServiceRPCOutputSchema import DeleteNotificationSubscriptionServiceRPCOutputSchema
from objects_TapiNotification.createNotificationSubscriptionServiceRPCInputSchema import CreateNotificationSubscriptionServiceRPCInputSchema
from objects_TapiNotification.nameAndValueChange import NameAndValueChange
from objects_TapiNotification.operationalStatePac import OperationalStatePac
from objects_TapiNotification.globalClass import GlobalClass
from objects_TapiNotification.layerProtocol import LayerProtocol
from objects_TapiNotification.notificationSubscriptionService import NotificationSubscriptionService
from objects_TapiNotification.getSupportedNotificationTypesRPCOutputSchema import GetSupportedNotificationTypesRPCOutputSchema
from objects_TapiNotification.getNotificationListRPCOutputSchema import GetNotificationListRPCOutputSchema
from objects_TapiNotification.lifecycleStatePac import LifecycleStatePac
from objects_TapiNotification.subscriptionFilter import SubscriptionFilter

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
class GetnotificationlistMethodView(MethodView):

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
class UpdatenotificationsubscriptionserviceMethodView(MethodView):

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
class CreatenotificationsubscriptionserviceMethodView(MethodView):

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
class DeletenotificationsubscriptionserviceMethodView(MethodView):

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
class GetsupportednotificationtypesMethodView(MethodView):

    def post(self, ):
        print "Create operation of resource: getSupportedNotificationTypes"
        json_struct = request.get_json() #json parser.
        new_object = (json_struct) #It creates an object instance from the json_input data.
        response = GetsupportednotificationtypesImpl.post( new_object)
        return Successful('Successful operation','{"description":"Create operation of resource: getSupportedNotificationTypes"}')


#/restconf/operations/getNotificationSubscriptionServiceList/
class GetnotificationsubscriptionservicelistMethodView(MethodView):

    def post(self, ):
        print "Create operation of resource: getNotificationSubscriptionServiceList"
        json_struct = request.get_json() #json parser.
        new_object = (json_struct) #It creates an object instance from the json_input data.
        response = GetnotificationsubscriptionservicelistImpl.post( new_object)
        return Successful('Successful operation','{"description":"Create operation of resource: getNotificationSubscriptionServiceList"}')


#/restconf/operations/getNotificationSubscriptionServiceDetails/
class GetnotificationsubscriptionservicedetailsMethodView(MethodView):

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




getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getNotificationList/", view_func = globals()["GetnotificationlistMethodView"].as_view('"Getnotificationlist"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/updateNotificationSubscriptionService/", view_func = globals()["UpdatenotificationsubscriptionserviceMethodView"].as_view('"Updatenotificationsubscriptionservice"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/createNotificationSubscriptionService/", view_func = globals()["CreatenotificationsubscriptionserviceMethodView"].as_view('"Createnotificationsubscriptionservice"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/deleteNotificationSubscriptionService/", view_func = globals()["DeletenotificationsubscriptionserviceMethodView"].as_view('"Deletenotificationsubscriptionservice"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getSupportedNotificationTypes/", view_func = globals()["GetsupportednotificationtypesMethodView"].as_view('"Getsupportednotificationtypes"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getNotificationSubscriptionServiceList/", view_func = globals()["GetnotificationsubscriptionservicelistMethodView"].as_view('"Getnotificationsubscriptionservicelist"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getNotificationSubscriptionServiceDetails/", view_func = globals()["GetnotificationsubscriptionservicedetailsMethodView"].as_view('"Getnotificationsubscriptionservicedetails"'+'"_api"'), methods=['POST'])
