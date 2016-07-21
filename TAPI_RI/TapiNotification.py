from flask import json, Blueprint, request, Response
from flask.views import MethodView
import sys
from objects_common.keyedArrayType import KeyedArrayKeyError

import base64
import re

# BACKEND FUNCTIONS
from funcs_TapiNotification.context_NotificationImpl import Context_NotificationImpl
from funcs_TapiNotification.deletenotificationsubscriptionserviceImpl import DeletenotificationsubscriptionserviceImpl
from funcs_TapiNotification.context_NotifsubscriptionUuidImpl import Context_NotifsubscriptionUuidImpl
from funcs_TapiNotification.context_NotifsubscriptionUuid_SubscriptionfilterImpl import Context_NotifsubscriptionUuid_SubscriptionfilterImpl
from funcs_TapiNotification.context_NotificationUuidAdditionalinfoImpl import Context_NotificationUuidAdditionalinfoImpl
from funcs_TapiNotification.context_NotifsubscriptionUuid_NotificationNotification_UuidTargetobjectnameValuenameImpl import Context_NotifsubscriptionUuid_NotificationNotification_UuidTargetobjectnameValuenameImpl
from funcs_TapiNotification.context_NotificationUuid_ExtensionsExtensionsspecificationImpl import Context_NotificationUuid_ExtensionsExtensionsspecificationImpl
from funcs_TapiNotification.context_NotifsubscriptionUuid_NotificationNotification_UuidLabelImpl import Context_NotifsubscriptionUuid_NotificationNotification_UuidLabelImpl
from funcs_TapiNotification.context_NotifsubscriptionImpl import Context_NotifsubscriptionImpl
from funcs_TapiNotification.context_NotifsubscriptionUuid_NotificationNotification_Uuid_ExtensionsImpl import Context_NotifsubscriptionUuid_NotificationNotification_Uuid_ExtensionsImpl
from funcs_TapiNotification.context_NotifsubscriptionUuid_NotificationNotification_UuidAdditionalinfoValuenameImpl import Context_NotifsubscriptionUuid_NotificationNotification_UuidAdditionalinfoValuenameImpl
from funcs_TapiNotification.context_NotifsubscriptionUuid_NotificationNotification_Uuid_ExtensionsExtensionsspecificationImpl import Context_NotifsubscriptionUuid_NotificationNotification_Uuid_ExtensionsExtensionsspecificationImpl
from funcs_TapiNotification.context_NotifsubscriptionUuid_NotificationNotification_UuidNameImpl import Context_NotifsubscriptionUuid_NotificationNotification_UuidNameImpl
from funcs_TapiNotification.getnotificationlistImpl import GetnotificationlistImpl
from funcs_TapiNotification.context_NotifsubscriptionUuidNameValuenameImpl import Context_NotifsubscriptionUuidNameValuenameImpl
from funcs_TapiNotification.context_NotifsubscriptionUuid_ExtensionsImpl import Context_NotifsubscriptionUuid_ExtensionsImpl
from funcs_TapiNotification.context_NotifsubscriptionUuidNameImpl import Context_NotifsubscriptionUuidNameImpl
from funcs_TapiNotification.context_NotifsubscriptionUuid_NotificationNotification_UuidAdditionalinfoImpl import Context_NotifsubscriptionUuid_NotificationNotification_UuidAdditionalinfoImpl
from funcs_TapiNotification.context_NotificationUuidImpl import Context_NotificationUuidImpl
from funcs_TapiNotification.createnotificationsubscriptionserviceImpl import CreatenotificationsubscriptionserviceImpl
from funcs_TapiNotification.context_NotifsubscriptionUuidLabelImpl import Context_NotifsubscriptionUuidLabelImpl
from funcs_TapiNotification.getnotificationsubscriptionservicelistImpl import GetnotificationsubscriptionservicelistImpl
from funcs_TapiNotification.context_NotifsubscriptionUuidLabelValuenameImpl import Context_NotifsubscriptionUuidLabelValuenameImpl
from funcs_TapiNotification.context_NotifsubscriptionUuid_NotificationNotification_UuidNameValuenameImpl import Context_NotifsubscriptionUuid_NotificationNotification_UuidNameValuenameImpl
from funcs_TapiNotification.context_NotificationUuid_ExtensionsImpl import Context_NotificationUuid_ExtensionsImpl
from funcs_TapiNotification.context_NotifsubscriptionUuid_NotificationNotification_UuidLabelValuenameImpl import Context_NotifsubscriptionUuid_NotificationNotification_UuidLabelValuenameImpl
from funcs_TapiNotification.context_NotifsubscriptionUuid_NotificationchannelImpl import Context_NotifsubscriptionUuid_NotificationchannelImpl
from funcs_TapiNotification.context_NotificationUuidChangedattributesImpl import Context_NotificationUuidChangedattributesImpl
from funcs_TapiNotification.context_NotifsubscriptionUuid_NotificationNotification_UuidChangedattributesImpl import Context_NotifsubscriptionUuid_NotificationNotification_UuidChangedattributesImpl
from funcs_TapiNotification.context_NotificationUuidTargetobjectnameImpl import Context_NotificationUuidTargetobjectnameImpl
from funcs_TapiNotification.context_NotificationUuidLabelValuenameImpl import Context_NotificationUuidLabelValuenameImpl
from funcs_TapiNotification.context_NotificationUuidAdditionalinfoValuenameImpl import Context_NotificationUuidAdditionalinfoValuenameImpl
from funcs_TapiNotification.context_NotifsubscriptionUuid_ExtensionsExtensionsspecificationImpl import Context_NotifsubscriptionUuid_ExtensionsExtensionsspecificationImpl
from funcs_TapiNotification.context_NotifsubscriptionUuid_NotificationImpl import Context_NotifsubscriptionUuid_NotificationImpl
from funcs_TapiNotification.context_NotifsubscriptionUuid_NotificationNotification_UuidImpl import Context_NotifsubscriptionUuid_NotificationNotification_UuidImpl
from funcs_TapiNotification.context_NotificationUuidLabelImpl import Context_NotificationUuidLabelImpl
from funcs_TapiNotification.getsupportednotificationtypesImpl import GetsupportednotificationtypesImpl
from funcs_TapiNotification.context_NotificationUuidNameImpl import Context_NotificationUuidNameImpl
from funcs_TapiNotification.context_NotificationUuidTargetobjectnameValuenameImpl import Context_NotificationUuidTargetobjectnameValuenameImpl
from funcs_TapiNotification.context_NotificationUuidNameValuenameImpl import Context_NotificationUuidNameValuenameImpl
from funcs_TapiNotification.updatenotificationsubscriptionserviceImpl import UpdatenotificationsubscriptionserviceImpl
from funcs_TapiNotification.context_NotifsubscriptionUuid_NotificationNotification_UuidTargetobjectnameImpl import Context_NotifsubscriptionUuid_NotificationNotification_UuidTargetobjectnameImpl
from funcs_TapiNotification.getnotificationsubscriptionservicedetailsImpl import GetnotificationsubscriptionservicedetailsImpl

# CALLABLE OBJECTS
from objects_TapiNotification.notification import Notification
from objects_TapiNotification.timeRange import TimeRange
from objects_TapiNotification.deleteNotificationSubscriptionServiceRPCInputSchema import DeleteNotificationSubscriptionServiceRPCInputSchema
from objects_TapiNotification.nameAndValue import NameAndValue
from objects_TapiNotification.adminStatePac import AdminStatePac
from objects_TapiNotification.getNotificationListRPCInputSchema import GetNotificationListRPCInputSchema
from objects_TapiNotification.serviceEndPoint import ServiceEndPoint
from objects_TapiNotification.resourceSpec import ResourceSpec
from objects_TapiNotification.createNotificationSubscriptionServiceRPCOutputSchema import CreateNotificationSubscriptionServiceRPCOutputSchema
from objects_TapiNotification.getNotificationSubscriptionServiceDetailsRPCInputSchema import GetNotificationSubscriptionServiceDetailsRPCInputSchema
from objects_TapiNotification.updateNotificationSubscriptionServiceRPCOutputSchema import UpdateNotificationSubscriptionServiceRPCOutputSchema
from objects_TapiNotification.updateNotificationSubscriptionServiceRPCInputSchema import UpdateNotificationSubscriptionServiceRPCInputSchema
from objects_TapiNotification.localClass import LocalClass
from objects_TapiNotification.notificationChannel import NotificationChannel
from objects_TapiNotification.getNotificationSubscriptionServiceDetailsRPCOutputSchema import GetNotificationSubscriptionServiceDetailsRPCOutputSchema
from objects_TapiNotification.getNotificationSubscriptionServiceListRPCOutputSchema import GetNotificationSubscriptionServiceListRPCOutputSchema
from objects_TapiNotification.extensionsSpec import ExtensionsSpec
from objects_TapiNotification.serviceSpec import ServiceSpec
from objects_TapiNotification.deleteNotificationSubscriptionServiceRPCOutputSchema import DeleteNotificationSubscriptionServiceRPCOutputSchema
from objects_TapiNotification.createNotificationSubscriptionServiceRPCInputSchema import CreateNotificationSubscriptionServiceRPCInputSchema
from objects_TapiNotification.nameAndValueChange import NameAndValueChange
from objects_TapiNotification.operationalStatePac import OperationalStatePac
from objects_TapiNotification.globalClass import GlobalClass
from objects_TapiNotification.layerProtocol import LayerProtocol
from objects_TapiNotification.notificationSubscriptionService import NotificationSubscriptionService
from objects_TapiNotification._notifSubscriptionSchema import _notifSubscriptionSchema
from objects_TapiNotification._notificationSchema import _notificationSchema
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

            new_object = create_instance(_notifSubscriptionSchema, json_struct)
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
            new_object = create_instance(_notifSubscriptionSchema, json_struct, (uuid,'uuid'))
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


#/restconf/config/Context/_notifSubscription/(\w+)/_subscriptionFilter/
class Context_NotifsubscriptionUuid_SubscriptionfilterMethodView(MethodView):

    def put(self, uuid):
        print "Update operation of resource: _subscriptionFilter"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_NotifsubscriptionUuid_SubscriptionfilterImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(SubscriptionFilter, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_NotifsubscriptionUuid_SubscriptionfilterImpl.put(uuid, new_object)
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
                    Context_NotifsubscriptionUuid_SubscriptionfilterImpl.put(uuid, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid):
        print "Create operation of resource: _subscriptionFilter"
        try:
            response = Context_NotifsubscriptionUuid_SubscriptionfilterImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(SubscriptionFilter, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_NotifsubscriptionUuid_SubscriptionfilterImpl.post(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid):
        print "Delete operation of resource: _subscriptionFilter"
        try:
            response=Context_NotifsubscriptionUuid_SubscriptionfilterImpl.delete(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid):
        print "Retrieve operation of resource: _subscriptionFilter"
        try:
            response = Context_NotifsubscriptionUuid_SubscriptionfilterImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notification/(\w+)/additionalInfo/
class Context_NotificationUuidAdditionalinfoMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: additionalInfo"
        try:
            response = Context_NotificationUuidAdditionalinfoImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notifSubscription/(\w+)/_notification/(\w+)/targetObjectName/(\w+)/
class Context_NotifsubscriptionUuid_NotificationNotification_UuidTargetobjectnameValuenameMethodView(MethodView):

    def get(self, uuid, notification_uuid, valueName):
        print "Retrieve operation of resource: targetObjectName"
        try:
            response = Context_NotifsubscriptionUuid_NotificationNotification_UuidTargetobjectnameValuenameImpl.get(uuid, notification_uuid, valueName)
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


#/restconf/config/Context/_notifSubscription/(\w+)/_notification/(\w+)/label/
class Context_NotifsubscriptionUuid_NotificationNotification_UuidLabelMethodView(MethodView):

    def get(self, uuid, notification_uuid):
        print "Retrieve operation of resource: label"
        try:
            response = Context_NotifsubscriptionUuid_NotificationNotification_UuidLabelImpl.get(uuid, notification_uuid)
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


#/restconf/config/Context/_notifSubscription/(\w+)/_notification/(\w+)/_extensions/
class Context_NotifsubscriptionUuid_NotificationNotification_Uuid_ExtensionsMethodView(MethodView):

    def get(self, uuid, notification_uuid):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_NotifsubscriptionUuid_NotificationNotification_Uuid_ExtensionsImpl.get(uuid, notification_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notifSubscription/(\w+)/_notification/(\w+)/additionalInfo/(\w+)/
class Context_NotifsubscriptionUuid_NotificationNotification_UuidAdditionalinfoValuenameMethodView(MethodView):

    def get(self, uuid, notification_uuid, valueName):
        print "Retrieve operation of resource: additionalInfo"
        try:
            response = Context_NotifsubscriptionUuid_NotificationNotification_UuidAdditionalinfoValuenameImpl.get(uuid, notification_uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notifSubscription/(\w+)/_notification/(\w+)/_extensions/(\w+)/
class Context_NotifsubscriptionUuid_NotificationNotification_Uuid_ExtensionsExtensionsspecificationMethodView(MethodView):

    def get(self, uuid, notification_uuid, extensionsSpecification):
        print "Retrieve operation of resource: _extensions"
        try:
            response = Context_NotifsubscriptionUuid_NotificationNotification_Uuid_ExtensionsExtensionsspecificationImpl.get(uuid, notification_uuid, extensionsSpecification)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notifSubscription/(\w+)/_notification/(\w+)/name/
class Context_NotifsubscriptionUuid_NotificationNotification_UuidNameMethodView(MethodView):

    def get(self, uuid, notification_uuid):
        print "Retrieve operation of resource: name"
        try:
            response = Context_NotifsubscriptionUuid_NotificationNotification_UuidNameImpl.get(uuid, notification_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


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


#/restconf/config/Context/_notifSubscription/(\w+)/_notification/(\w+)/additionalInfo/
class Context_NotifsubscriptionUuid_NotificationNotification_UuidAdditionalinfoMethodView(MethodView):

    def get(self, uuid, notification_uuid):
        print "Retrieve operation of resource: additionalInfo"
        try:
            response = Context_NotifsubscriptionUuid_NotificationNotification_UuidAdditionalinfoImpl.get(uuid, notification_uuid)
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


#/restconf/operations/getNotificationSubscriptionServiceList/
class GetnotificationsubscriptionservicelistMethodView(MethodView):

    def post(self, ):
        print "Create operation of resource: getNotificationSubscriptionServiceList"
        json_struct = request.get_json() #json parser.
        new_object = (json_struct) #It creates an object instance from the json_input data.
        response = GetnotificationsubscriptionservicelistImpl.post( new_object)
        return Successful('Successful operation','{"description":"Create operation of resource: getNotificationSubscriptionServiceList"}')


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


#/restconf/config/Context/_notifSubscription/(\w+)/_notification/(\w+)/name/(\w+)/
class Context_NotifsubscriptionUuid_NotificationNotification_UuidNameValuenameMethodView(MethodView):

    def get(self, uuid, notification_uuid, valueName):
        print "Retrieve operation of resource: name"
        try:
            response = Context_NotifsubscriptionUuid_NotificationNotification_UuidNameValuenameImpl.get(uuid, notification_uuid, valueName)
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


#/restconf/config/Context/_notifSubscription/(\w+)/_notification/(\w+)/label/(\w+)/
class Context_NotifsubscriptionUuid_NotificationNotification_UuidLabelValuenameMethodView(MethodView):

    def get(self, uuid, notification_uuid, valueName):
        print "Retrieve operation of resource: label"
        try:
            response = Context_NotifsubscriptionUuid_NotificationNotification_UuidLabelValuenameImpl.get(uuid, notification_uuid, valueName)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notifSubscription/(\w+)/_notificationChannel/
class Context_NotifsubscriptionUuid_NotificationchannelMethodView(MethodView):

    def put(self, uuid):
        print "Update operation of resource: _notificationChannel"
        json_struct = request.get_json() #json parser.
        try:
            existing_object = Context_NotifsubscriptionUuid_NotificationchannelImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            new_object = create_instance(NotificationChannel, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_NotifsubscriptionUuid_NotificationchannelImpl.put(uuid, new_object)
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
                    Context_NotifsubscriptionUuid_NotificationchannelImpl.put(uuid, existing_object)
                    js=existing_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")

        return Successful("Successful operation",json_dumps(js))



    def post(self, uuid):
        print "Create operation of resource: _notificationChannel"
        try:
            response = Context_NotifsubscriptionUuid_NotificationchannelImpl.get(uuid)
        except KeyError as inst:
            if inst.args[0] != 'uuid':
                return NotFoundError(inst.args[0] + " not found")

            json_struct = request.get_json() #json parser.
            new_object = create_instance(NotificationChannel, json_struct)
            if isinstance(new_object, BadRequestError):
                return new_object
            elif isinstance(new_object, NotFoundError):
                return new_object
            else:
                try:
                    Context_NotifsubscriptionUuid_NotificationchannelImpl.post(uuid, new_object)
                    js=new_object.json_serializer()
                except KeyError as inst:
                    return NotFoundError(inst.args[0] + " not found")
        else:
            return BadRequestError("Object already exists. For updates use PUT.")
        return Successful("Successful operation",json_dumps(js))


    def delete(self, uuid):
        print "Delete operation of resource: _notificationChannel"
        try:
            response=Context_NotifsubscriptionUuid_NotificationchannelImpl.delete(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            return Successful('Successful operation')


    def get(self, uuid):
        print "Retrieve operation of resource: _notificationChannel"
        try:
            response = Context_NotifsubscriptionUuid_NotificationchannelImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notification/(\w+)/changedAttributes/
class Context_NotificationUuidChangedattributesMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: changedAttributes"
        try:
            response = Context_NotificationUuidChangedattributesImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notifSubscription/(\w+)/_notification/(\w+)/changedAttributes/
class Context_NotifsubscriptionUuid_NotificationNotification_UuidChangedattributesMethodView(MethodView):

    def get(self, uuid, notification_uuid):
        print "Retrieve operation of resource: changedAttributes"
        try:
            response = Context_NotifsubscriptionUuid_NotificationNotification_UuidChangedattributesImpl.get(uuid, notification_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notification/(\w+)/targetObjectName/
class Context_NotificationUuidTargetobjectnameMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: targetObjectName"
        try:
            response = Context_NotificationUuidTargetobjectnameImpl.get(uuid)
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


#/restconf/config/Context/_notification/(\w+)/additionalInfo/(\w+)/
class Context_NotificationUuidAdditionalinfoValuenameMethodView(MethodView):

    def get(self, uuid, valueName):
        print "Retrieve operation of resource: additionalInfo"
        try:
            response = Context_NotificationUuidAdditionalinfoValuenameImpl.get(uuid, valueName)
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


#/restconf/config/Context/_notifSubscription/(\w+)/_notification/
class Context_NotifsubscriptionUuid_NotificationMethodView(MethodView):

    def get(self, uuid):
        print "Retrieve operation of resource: _notification"
        try:
            response = Context_NotifsubscriptionUuid_NotificationImpl.get(uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


#/restconf/config/Context/_notifSubscription/(\w+)/_notification/(\w+)/
class Context_NotifsubscriptionUuid_NotificationNotification_UuidMethodView(MethodView):

    def get(self, uuid, notification_uuid):
        print "Retrieve operation of resource: _notification"
        try:
            response = Context_NotifsubscriptionUuid_NotificationNotification_UuidImpl.get(uuid, notification_uuid)
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


#/restconf/operations/getSupportedNotificationTypes/
class GetsupportednotificationtypesMethodView(MethodView):

    def post(self, ):
        print "Create operation of resource: getSupportedNotificationTypes"
        json_struct = request.get_json() #json parser.
        new_object = (json_struct) #It creates an object instance from the json_input data.
        response = GetsupportednotificationtypesImpl.post( new_object)
        return Successful('Successful operation','{"description":"Create operation of resource: getSupportedNotificationTypes"}')


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


#/restconf/config/Context/_notification/(\w+)/targetObjectName/(\w+)/
class Context_NotificationUuidTargetobjectnameValuenameMethodView(MethodView):

    def get(self, uuid, valueName):
        print "Retrieve operation of resource: targetObjectName"
        try:
            response = Context_NotificationUuidTargetobjectnameValuenameImpl.get(uuid, valueName)
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



#/restconf/config/Context/_notifSubscription/(\w+)/_notification/(\w+)/targetObjectName/
class Context_NotifsubscriptionUuid_NotificationNotification_UuidTargetobjectnameMethodView(MethodView):

    def get(self, uuid, notification_uuid):
        print "Retrieve operation of resource: targetObjectName"
        try:
            response = Context_NotifsubscriptionUuid_NotificationNotification_UuidTargetobjectnameImpl.get(uuid, notification_uuid)
        except KeyError as inst:
            return NotFoundError(inst.args[0] + " not found")
        else:
            js = response.json_serializer()
            return Successful("Successful operation",json_dumps(js))


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




getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notification/", view_func = globals()["Context_NotificationMethodView"].as_view('"Context_Notification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/deleteNotificationSubscriptionService/", view_func = globals()["DeletenotificationsubscriptionserviceMethodView"].as_view('"Deletenotificationsubscriptionservice"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/", view_func = globals()["Context_NotifsubscriptionUuidMethodView"].as_view('"Context_NotifsubscriptionUuid"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/_subscriptionFilter/", view_func = globals()["Context_NotifsubscriptionUuid_SubscriptionfilterMethodView"].as_view('"Context_NotifsubscriptionUuid_Subscriptionfilter"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notification/<uuid>/additionalInfo/", view_func = globals()["Context_NotificationUuidAdditionalinfoMethodView"].as_view('"Context_NotificationUuidAdditionalinfo"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/_notification/<notification_uuid>/targetObjectName/<valueName>/", view_func = globals()["Context_NotifsubscriptionUuid_NotificationNotification_UuidTargetobjectnameValuenameMethodView"].as_view('"Context_NotifsubscriptionUuid_NotificationNotification_UuidTargetobjectnameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notification/<uuid>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_NotificationUuid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_NotificationUuid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/_notification/<notification_uuid>/label/", view_func = globals()["Context_NotifsubscriptionUuid_NotificationNotification_UuidLabelMethodView"].as_view('"Context_NotifsubscriptionUuid_NotificationNotification_UuidLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/", view_func = globals()["Context_NotifsubscriptionMethodView"].as_view('"Context_Notifsubscription"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/_notification/<notification_uuid>/_extensions/", view_func = globals()["Context_NotifsubscriptionUuid_NotificationNotification_Uuid_ExtensionsMethodView"].as_view('"Context_NotifsubscriptionUuid_NotificationNotification_Uuid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/_notification/<notification_uuid>/additionalInfo/<valueName>/", view_func = globals()["Context_NotifsubscriptionUuid_NotificationNotification_UuidAdditionalinfoValuenameMethodView"].as_view('"Context_NotifsubscriptionUuid_NotificationNotification_UuidAdditionalinfoValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/_notification/<notification_uuid>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_NotifsubscriptionUuid_NotificationNotification_Uuid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_NotifsubscriptionUuid_NotificationNotification_Uuid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/_notification/<notification_uuid>/name/", view_func = globals()["Context_NotifsubscriptionUuid_NotificationNotification_UuidNameMethodView"].as_view('"Context_NotifsubscriptionUuid_NotificationNotification_UuidName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getNotificationList/", view_func = globals()["GetnotificationlistMethodView"].as_view('"Getnotificationlist"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/name/<valueName>/", view_func = globals()["Context_NotifsubscriptionUuidNameValuenameMethodView"].as_view('"Context_NotifsubscriptionUuidNameValuename"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/_extensions/", view_func = globals()["Context_NotifsubscriptionUuid_ExtensionsMethodView"].as_view('"Context_NotifsubscriptionUuid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/name/", view_func = globals()["Context_NotifsubscriptionUuidNameMethodView"].as_view('"Context_NotifsubscriptionUuidName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/_notification/<notification_uuid>/additionalInfo/", view_func = globals()["Context_NotifsubscriptionUuid_NotificationNotification_UuidAdditionalinfoMethodView"].as_view('"Context_NotifsubscriptionUuid_NotificationNotification_UuidAdditionalinfo"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notification/<uuid>/", view_func = globals()["Context_NotificationUuidMethodView"].as_view('"Context_NotificationUuid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/createNotificationSubscriptionService/", view_func = globals()["CreatenotificationsubscriptionserviceMethodView"].as_view('"Createnotificationsubscriptionservice"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/label/", view_func = globals()["Context_NotifsubscriptionUuidLabelMethodView"].as_view('"Context_NotifsubscriptionUuidLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getNotificationSubscriptionServiceList/", view_func = globals()["GetnotificationsubscriptionservicelistMethodView"].as_view('"Getnotificationsubscriptionservicelist"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/label/<valueName>/", view_func = globals()["Context_NotifsubscriptionUuidLabelValuenameMethodView"].as_view('"Context_NotifsubscriptionUuidLabelValuename"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/_notification/<notification_uuid>/name/<valueName>/", view_func = globals()["Context_NotifsubscriptionUuid_NotificationNotification_UuidNameValuenameMethodView"].as_view('"Context_NotifsubscriptionUuid_NotificationNotification_UuidNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notification/<uuid>/_extensions/", view_func = globals()["Context_NotificationUuid_ExtensionsMethodView"].as_view('"Context_NotificationUuid_Extensions"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/_notification/<notification_uuid>/label/<valueName>/", view_func = globals()["Context_NotifsubscriptionUuid_NotificationNotification_UuidLabelValuenameMethodView"].as_view('"Context_NotifsubscriptionUuid_NotificationNotification_UuidLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/_notificationChannel/", view_func = globals()["Context_NotifsubscriptionUuid_NotificationchannelMethodView"].as_view('"Context_NotifsubscriptionUuid_Notificationchannel"'+'"_api"'), methods=['PUT', 'POST', 'DELETE', 'GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notification/<uuid>/changedAttributes/", view_func = globals()["Context_NotificationUuidChangedattributesMethodView"].as_view('"Context_NotificationUuidChangedattributes"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/_notification/<notification_uuid>/changedAttributes/", view_func = globals()["Context_NotifsubscriptionUuid_NotificationNotification_UuidChangedattributesMethodView"].as_view('"Context_NotifsubscriptionUuid_NotificationNotification_UuidChangedattributes"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notification/<uuid>/targetObjectName/", view_func = globals()["Context_NotificationUuidTargetobjectnameMethodView"].as_view('"Context_NotificationUuidTargetobjectname"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notification/<uuid>/label/<valueName>/", view_func = globals()["Context_NotificationUuidLabelValuenameMethodView"].as_view('"Context_NotificationUuidLabelValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notification/<uuid>/additionalInfo/<valueName>/", view_func = globals()["Context_NotificationUuidAdditionalinfoValuenameMethodView"].as_view('"Context_NotificationUuidAdditionalinfoValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/_extensions/<extensionsSpecification>/", view_func = globals()["Context_NotifsubscriptionUuid_ExtensionsExtensionsspecificationMethodView"].as_view('"Context_NotifsubscriptionUuid_ExtensionsExtensionsspecification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/_notification/", view_func = globals()["Context_NotifsubscriptionUuid_NotificationMethodView"].as_view('"Context_NotifsubscriptionUuid_Notification"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/_notification/<notification_uuid>/", view_func = globals()["Context_NotifsubscriptionUuid_NotificationNotification_UuidMethodView"].as_view('"Context_NotifsubscriptionUuid_NotificationNotification_Uuid"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notification/<uuid>/label/", view_func = globals()["Context_NotificationUuidLabelMethodView"].as_view('"Context_NotificationUuidLabel"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getSupportedNotificationTypes/", view_func = globals()["GetsupportednotificationtypesMethodView"].as_view('"Getsupportednotificationtypes"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notification/<uuid>/name/", view_func = globals()["Context_NotificationUuidNameMethodView"].as_view('"Context_NotificationUuidName"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notification/<uuid>/targetObjectName/<valueName>/", view_func = globals()["Context_NotificationUuidTargetobjectnameValuenameMethodView"].as_view('"Context_NotificationUuidTargetobjectnameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notification/<uuid>/name/<valueName>/", view_func = globals()["Context_NotificationUuidNameValuenameMethodView"].as_view('"Context_NotificationUuidNameValuename"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/updateNotificationSubscriptionService/", view_func = globals()["UpdatenotificationsubscriptionserviceMethodView"].as_view('"Updatenotificationsubscriptionservice"'+'"_api"'), methods=['POST'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/config/Context/_notifSubscription/<uuid>/_notification/<notification_uuid>/targetObjectName/", view_func = globals()["Context_NotifsubscriptionUuid_NotificationNotification_UuidTargetobjectnameMethodView"].as_view('"Context_NotifsubscriptionUuid_NotificationNotification_UuidTargetobjectname"'+'"_api"'), methods=['GET'])
getattr(sys.modules[__name__], __name__).add_url_rule("/restconf/operations/getNotificationSubscriptionServiceDetails/", view_func = globals()["GetnotificationsubscriptionservicedetailsMethodView"].as_view('"Getnotificationsubscriptionservicedetails"'+'"_api"'), methods=['POST'])
