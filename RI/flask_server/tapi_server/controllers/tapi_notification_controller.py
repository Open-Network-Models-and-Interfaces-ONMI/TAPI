import connexion
import six

from tapi_server.models.inline_object19 import InlineObject19  # noqa: E501
from tapi_server.models.inline_object2 import InlineObject2  # noqa: E501
from tapi_server.models.inline_object20 import InlineObject20  # noqa: E501
from tapi_server.models.inline_object28 import InlineObject28  # noqa: E501
from tapi_server.models.inline_object7 import InlineObject7  # noqa: E501
from tapi_server.models.tapi_common_name_and_value import TapiCommonNameAndValue  # noqa: E501
from tapi_server.models.tapi_notification_alarm_info import TapiNotificationAlarmInfo  # noqa: E501
from tapi_server.models.tapi_notification_create_notification_subscription_service import TapiNotificationCreateNotificationSubscriptionService  # noqa: E501
from tapi_server.models.tapi_notification_delete_notification_subscription_service import TapiNotificationDeleteNotificationSubscriptionService  # noqa: E501
from tapi_server.models.tapi_notification_get_notification_list import TapiNotificationGetNotificationList  # noqa: E501
from tapi_server.models.tapi_notification_get_notification_subscription_service_details import TapiNotificationGetNotificationSubscriptionServiceDetails  # noqa: E501
from tapi_server.models.tapi_notification_get_notification_subscription_service_list import TapiNotificationGetNotificationSubscriptionServiceList  # noqa: E501
from tapi_server.models.tapi_notification_get_supported_notification_types import TapiNotificationGetSupportedNotificationTypes  # noqa: E501
from tapi_server.models.tapi_notification_name_and_value_change import TapiNotificationNameAndValueChange  # noqa: E501
from tapi_server.models.tapi_notification_notification import TapiNotificationNotification  # noqa: E501
from tapi_server.models.tapi_notification_notification_channel import TapiNotificationNotificationChannel  # noqa: E501
from tapi_server.models.tapi_notification_notification_context import TapiNotificationNotificationContext  # noqa: E501
from tapi_server.models.tapi_notification_notification_subscription_service import TapiNotificationNotificationSubscriptionService  # noqa: E501
from tapi_server.models.tapi_notification_subscription_filter import TapiNotificationSubscriptionFilter  # noqa: E501
from tapi_server.models.tapi_notification_tca_info import TapiNotificationTcaInfo  # noqa: E501
from tapi_server.models.tapi_notification_update_notification_subscription_service import TapiNotificationUpdateNotificationSubscriptionService  # noqa: E501
from tapi_server import util


def data_context_notification_context_delete():  # noqa: E501
    """data_context_notification_context_delete

    removes tapi.notification.NotificationContext # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def data_context_notification_context_get():  # noqa: E501
    """data_context_notification_context_get

    returns tapi.notification.NotificationContext # noqa: E501


    :rtype: TapiNotificationNotificationContext
    """
    return 'do some magic!'


def data_context_notification_context_notif_subscription_post(tapi_notification_notification_subscription_service=None):  # noqa: E501
    """data_context_notification_context_notif_subscription_post

    creates tapi.notification.NotificationSubscriptionService # noqa: E501

    :param tapi_notification_notification_subscription_service: tapi.notification.NotificationSubscriptionService to be added to list
    :type tapi_notification_notification_subscription_service: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_notification_notification_subscription_service = TapiNotificationNotificationSubscriptionService.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_delete(uuid):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_delete

    removes tapi.notification.NotificationSubscriptionService # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_get(uuid):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_get

    returns tapi.notification.NotificationSubscriptionService # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str

    :rtype: TapiNotificationNotificationSubscriptionService
    """
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_name_post(uuid, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str
    :param tapi_common_name_and_value: tapi.common.NameAndValue to be added to list
    :type tapi_common_name_and_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_name_and_value = TapiCommonNameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_namevalue_name_delete(uuid, value_name):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_namevalue_name_delete

    removes tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_namevalue_name_get(uuid, value_name):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_namevalue_name_post(uuid, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_namevalue_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str
    :param tapi_common_name_and_value: tapi.common.NameAndValue to be added to list
    :type tapi_common_name_and_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_name_and_value = TapiCommonNameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_namevalue_name_put(uuid, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_namevalue_name_put

    creates or updates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str
    :param tapi_common_name_and_value: tapi.common.NameAndValue to be added or updated
    :type tapi_common_name_and_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_name_and_value = TapiCommonNameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_notification_channel_delete(uuid):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_notification_channel_delete

    removes tapi.notification.NotificationChannel # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_notification_channel_get(uuid):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_notification_channel_get

    returns tapi.notification.NotificationChannel # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str

    :rtype: TapiNotificationNotificationChannel
    """
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_notification_channel_name_post(uuid, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_notification_channel_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str
    :param tapi_common_name_and_value: tapi.common.NameAndValue to be added to list
    :type tapi_common_name_and_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_name_and_value = TapiCommonNameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_notification_channel_namevalue_name_delete(uuid, value_name):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_notification_channel_namevalue_name_delete

    removes tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_notification_channel_namevalue_name_get(uuid, value_name):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_notification_channel_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_notification_channel_namevalue_name_post(uuid, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_notification_channel_namevalue_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str
    :param tapi_common_name_and_value: tapi.common.NameAndValue to be added to list
    :type tapi_common_name_and_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_name_and_value = TapiCommonNameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_notification_channel_namevalue_name_put(uuid, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_notification_channel_namevalue_name_put

    creates or updates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str
    :param tapi_common_name_and_value: tapi.common.NameAndValue to be added or updated
    :type tapi_common_name_and_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_name_and_value = TapiCommonNameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_notification_channel_post(uuid, tapi_notification_notification_channel=None):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_notification_channel_post

    creates tapi.notification.NotificationChannel # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str
    :param tapi_notification_notification_channel: tapi.notification.NotificationChannel to be added to list
    :type tapi_notification_notification_channel: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_notification_notification_channel = TapiNotificationNotificationChannel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_notification_channel_put(uuid, tapi_notification_notification_channel=None):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_notification_channel_put

    creates or updates tapi.notification.NotificationChannel # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str
    :param tapi_notification_notification_channel: tapi.notification.NotificationChannel to be added or updated
    :type tapi_notification_notification_channel: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_notification_notification_channel = TapiNotificationNotificationChannel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_notificationnotification_uuid_additional_infovalue_name_get(uuid, notification_uuid, value_name):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_notificationnotification_uuid_additional_infovalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str
    :param notification_uuid: Id of notification
    :type notification_uuid: str
    :param value_name: Id of additional-info
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_notificationnotification_uuid_alarm_info_get(uuid, notification_uuid):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_notificationnotification_uuid_alarm_info_get

    returns tapi.notification.AlarmInfo # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str
    :param notification_uuid: Id of notification
    :type notification_uuid: str

    :rtype: TapiNotificationAlarmInfo
    """
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_notificationnotification_uuid_changed_attributesvalue_name_get(uuid, notification_uuid, value_name):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_notificationnotification_uuid_changed_attributesvalue_name_get

    returns tapi.notification.NameAndValueChange # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str
    :param notification_uuid: Id of notification
    :type notification_uuid: str
    :param value_name: Id of changed-attributes
    :type value_name: str

    :rtype: TapiNotificationNameAndValueChange
    """
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_notificationnotification_uuid_get(uuid, notification_uuid):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_notificationnotification_uuid_get

    returns tapi.notification.Notification # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str
    :param notification_uuid: Id of notification
    :type notification_uuid: str

    :rtype: TapiNotificationNotification
    """
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_notificationnotification_uuid_namevalue_name_get(uuid, notification_uuid, value_name):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_notificationnotification_uuid_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str
    :param notification_uuid: Id of notification
    :type notification_uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_notificationnotification_uuid_target_object_namevalue_name_get(uuid, notification_uuid, value_name):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_notificationnotification_uuid_target_object_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str
    :param notification_uuid: Id of notification
    :type notification_uuid: str
    :param value_name: Id of target-object-name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_notificationnotification_uuid_tca_info_get(uuid, notification_uuid):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_notificationnotification_uuid_tca_info_get

    returns tapi.notification.TcaInfo # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str
    :param notification_uuid: Id of notification
    :type notification_uuid: str

    :rtype: TapiNotificationTcaInfo
    """
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_post(uuid, tapi_notification_notification_subscription_service=None):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_post

    creates tapi.notification.NotificationSubscriptionService # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str
    :param tapi_notification_notification_subscription_service: tapi.notification.NotificationSubscriptionService to be added to list
    :type tapi_notification_notification_subscription_service: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_notification_notification_subscription_service = TapiNotificationNotificationSubscriptionService.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_put(uuid, tapi_notification_notification_subscription_service=None):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_put

    creates or updates tapi.notification.NotificationSubscriptionService # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str
    :param tapi_notification_notification_subscription_service: tapi.notification.NotificationSubscriptionService to be added or updated
    :type tapi_notification_notification_subscription_service: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_notification_notification_subscription_service = TapiNotificationNotificationSubscriptionService.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_subscription_filter_delete(uuid):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_subscription_filter_delete

    removes tapi.notification.SubscriptionFilter # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_subscription_filter_get(uuid):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_subscription_filter_get

    returns tapi.notification.SubscriptionFilter # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str

    :rtype: TapiNotificationSubscriptionFilter
    """
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_subscription_filter_name_post(uuid, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_subscription_filter_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str
    :param tapi_common_name_and_value: tapi.common.NameAndValue to be added to list
    :type tapi_common_name_and_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_name_and_value = TapiCommonNameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_subscription_filter_namevalue_name_delete(uuid, value_name):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_subscription_filter_namevalue_name_delete

    removes tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_subscription_filter_namevalue_name_get(uuid, value_name):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_subscription_filter_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_subscription_filter_namevalue_name_post(uuid, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_subscription_filter_namevalue_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str
    :param tapi_common_name_and_value: tapi.common.NameAndValue to be added to list
    :type tapi_common_name_and_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_name_and_value = TapiCommonNameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_subscription_filter_namevalue_name_put(uuid, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_subscription_filter_namevalue_name_put

    creates or updates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str
    :param tapi_common_name_and_value: tapi.common.NameAndValue to be added or updated
    :type tapi_common_name_and_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_name_and_value = TapiCommonNameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_subscription_filter_post(uuid, tapi_notification_subscription_filter=None):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_subscription_filter_post

    creates tapi.notification.SubscriptionFilter # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str
    :param tapi_notification_subscription_filter: tapi.notification.SubscriptionFilter to be added to list
    :type tapi_notification_subscription_filter: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_notification_subscription_filter = TapiNotificationSubscriptionFilter.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_notification_context_notif_subscriptionuuid_subscription_filter_put(uuid, tapi_notification_subscription_filter=None):  # noqa: E501
    """data_context_notification_context_notif_subscriptionuuid_subscription_filter_put

    creates or updates tapi.notification.SubscriptionFilter # noqa: E501

    :param uuid: Id of notif-subscription
    :type uuid: str
    :param tapi_notification_subscription_filter: tapi.notification.SubscriptionFilter to be added or updated
    :type tapi_notification_subscription_filter: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_notification_subscription_filter = TapiNotificationSubscriptionFilter.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_notification_context_notificationuuid_additional_infovalue_name_get(uuid, value_name):  # noqa: E501
    """data_context_notification_context_notificationuuid_additional_infovalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of notification
    :type uuid: str
    :param value_name: Id of additional-info
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_notification_context_notificationuuid_alarm_info_get(uuid):  # noqa: E501
    """data_context_notification_context_notificationuuid_alarm_info_get

    returns tapi.notification.AlarmInfo # noqa: E501

    :param uuid: Id of notification
    :type uuid: str

    :rtype: TapiNotificationAlarmInfo
    """
    return 'do some magic!'


def data_context_notification_context_notificationuuid_changed_attributesvalue_name_get(uuid, value_name):  # noqa: E501
    """data_context_notification_context_notificationuuid_changed_attributesvalue_name_get

    returns tapi.notification.NameAndValueChange # noqa: E501

    :param uuid: Id of notification
    :type uuid: str
    :param value_name: Id of changed-attributes
    :type value_name: str

    :rtype: TapiNotificationNameAndValueChange
    """
    return 'do some magic!'


def data_context_notification_context_notificationuuid_get(uuid):  # noqa: E501
    """data_context_notification_context_notificationuuid_get

    returns tapi.notification.Notification # noqa: E501

    :param uuid: Id of notification
    :type uuid: str

    :rtype: TapiNotificationNotification
    """
    return 'do some magic!'


def data_context_notification_context_notificationuuid_namevalue_name_get(uuid, value_name):  # noqa: E501
    """data_context_notification_context_notificationuuid_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of notification
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_notification_context_notificationuuid_target_object_namevalue_name_get(uuid, value_name):  # noqa: E501
    """data_context_notification_context_notificationuuid_target_object_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of notification
    :type uuid: str
    :param value_name: Id of target-object-name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_notification_context_notificationuuid_tca_info_get(uuid):  # noqa: E501
    """data_context_notification_context_notificationuuid_tca_info_get

    returns tapi.notification.TcaInfo # noqa: E501

    :param uuid: Id of notification
    :type uuid: str

    :rtype: TapiNotificationTcaInfo
    """
    return 'do some magic!'


def data_context_notification_context_post(tapi_notification_notification_context=None):  # noqa: E501
    """data_context_notification_context_post

    creates tapi.notification.NotificationContext # noqa: E501

    :param tapi_notification_notification_context: tapi.notification.NotificationContext to be added to list
    :type tapi_notification_notification_context: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_notification_notification_context = TapiNotificationNotificationContext.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_notification_context_put(tapi_notification_notification_context=None):  # noqa: E501
    """data_context_notification_context_put

    creates or updates tapi.notification.NotificationContext # noqa: E501

    :param tapi_notification_notification_context: tapi.notification.NotificationContext to be added or updated
    :type tapi_notification_notification_context: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_notification_notification_context = TapiNotificationNotificationContext.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def operations_create_notification_subscription_service_post(inline_object2=None):  # noqa: E501
    """operations_create_notification_subscription_service_post

     # noqa: E501

    :param inline_object2: 
    :type inline_object2: dict | bytes

    :rtype: TapiNotificationCreateNotificationSubscriptionService
    """
    if connexion.request.is_json:
        inline_object2 = InlineObject2.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def operations_delete_notification_subscription_service_post(inline_object7=None):  # noqa: E501
    """operations_delete_notification_subscription_service_post

     # noqa: E501

    :param inline_object7: 
    :type inline_object7: dict | bytes

    :rtype: TapiNotificationDeleteNotificationSubscriptionService
    """
    if connexion.request.is_json:
        inline_object7 = InlineObject7.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def operations_get_notification_list_post(inline_object19=None):  # noqa: E501
    """operations_get_notification_list_post

     # noqa: E501

    :param inline_object19: 
    :type inline_object19: dict | bytes

    :rtype: TapiNotificationGetNotificationList
    """
    if connexion.request.is_json:
        inline_object19 = InlineObject19.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def operations_get_notification_subscription_service_details_post(inline_object20=None):  # noqa: E501
    """operations_get_notification_subscription_service_details_post

     # noqa: E501

    :param inline_object20: 
    :type inline_object20: dict | bytes

    :rtype: TapiNotificationGetNotificationSubscriptionServiceDetails
    """
    if connexion.request.is_json:
        inline_object20 = InlineObject20.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def operations_get_notification_subscription_service_list_post():  # noqa: E501
    """operations_get_notification_subscription_service_list_post

     # noqa: E501


    :rtype: TapiNotificationGetNotificationSubscriptionServiceList
    """
    return 'do some magic!'


def operations_get_supported_notification_types_post():  # noqa: E501
    """operations_get_supported_notification_types_post

     # noqa: E501


    :rtype: TapiNotificationGetSupportedNotificationTypes
    """
    return 'do some magic!'


def operations_update_notification_subscription_service_post(inline_object28=None):  # noqa: E501
    """operations_update_notification_subscription_service_post

     # noqa: E501

    :param inline_object28: 
    :type inline_object28: dict | bytes

    :rtype: TapiNotificationUpdateNotificationSubscriptionService
    """
    if connexion.request.is_json:
        inline_object28 = InlineObject28.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
