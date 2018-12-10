# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

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
from tapi_server.test import BaseTestCase


class TestTapiNotificationController(BaseTestCase):
    """TapiNotificationController integration test stubs"""

    def test_data_context_notification_context_delete(self):
        """Test case for data_context_notification_context_delete

        
        """
        response = self.client.open(
            '/data/context/notification-context/',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_get(self):
        """Test case for data_context_notification_context_get

        
        """
        response = self.client.open(
            '/data/context/notification-context/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscription_post(self):
        """Test case for data_context_notification_context_notif_subscription_post

        
        """
        tapi_notification_notification_subscription_service = TapiNotificationNotificationSubscriptionService()
        response = self.client.open(
            '/data/context/notification-context/notif-subscription/',
            method='POST',
            data=json.dumps(tapi_notification_notification_subscription_service),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_delete(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_delete

        
        """
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_get(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_get

        
        """
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_name_post(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/name/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_namevalue_name_delete(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_namevalue_name_delete

        
        """
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_namevalue_name_get(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_namevalue_name_post(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_namevalue_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_namevalue_name_put(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_namevalue_name_put

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='PUT',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_notification_channel_delete(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_notification_channel_delete

        
        """
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/notification-channel/'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_notification_channel_get(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_notification_channel_get

        
        """
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/notification-channel/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_notification_channel_name_post(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_notification_channel_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/notification-channel/name/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_notification_channel_namevalue_name_delete(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_notification_channel_namevalue_name_delete

        
        """
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/notification-channel/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_notification_channel_namevalue_name_get(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_notification_channel_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/notification-channel/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_notification_channel_namevalue_name_post(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_notification_channel_namevalue_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/notification-channel/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_notification_channel_namevalue_name_put(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_notification_channel_namevalue_name_put

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/notification-channel/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='PUT',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_notification_channel_post(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_notification_channel_post

        
        """
        tapi_notification_notification_channel = TapiNotificationNotificationChannel()
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/notification-channel/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_notification_notification_channel),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_notification_channel_put(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_notification_channel_put

        
        """
        tapi_notification_notification_channel = TapiNotificationNotificationChannel()
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/notification-channel/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(tapi_notification_notification_channel),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_notificationnotification_uuid_additional_infovalue_name_get(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_notificationnotification_uuid_additional_infovalue_name_get

        
        """
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/notification={notification-uuid}/additional-info={value-name}/'.format(uuid='uuid_example', notification_uuid='notification_uuid_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_notificationnotification_uuid_alarm_info_get(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_notificationnotification_uuid_alarm_info_get

        
        """
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/notification={notification-uuid}/alarm-info/'.format(uuid='uuid_example', notification_uuid='notification_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_notificationnotification_uuid_changed_attributesvalue_name_get(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_notificationnotification_uuid_changed_attributesvalue_name_get

        
        """
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/notification={notification-uuid}/changed-attributes={value-name}/'.format(uuid='uuid_example', notification_uuid='notification_uuid_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_notificationnotification_uuid_get(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_notificationnotification_uuid_get

        
        """
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/notification={notification-uuid}/'.format(uuid='uuid_example', notification_uuid='notification_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_notificationnotification_uuid_namevalue_name_get(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_notificationnotification_uuid_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/notification={notification-uuid}/name={value-name}/'.format(uuid='uuid_example', notification_uuid='notification_uuid_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_notificationnotification_uuid_target_object_namevalue_name_get(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_notificationnotification_uuid_target_object_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/notification={notification-uuid}/target-object-name={value-name}/'.format(uuid='uuid_example', notification_uuid='notification_uuid_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_notificationnotification_uuid_tca_info_get(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_notificationnotification_uuid_tca_info_get

        
        """
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/notification={notification-uuid}/tca-info/'.format(uuid='uuid_example', notification_uuid='notification_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_post(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_post

        
        """
        tapi_notification_notification_subscription_service = TapiNotificationNotificationSubscriptionService()
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_notification_notification_subscription_service),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_put(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_put

        
        """
        tapi_notification_notification_subscription_service = TapiNotificationNotificationSubscriptionService()
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(tapi_notification_notification_subscription_service),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_subscription_filter_delete(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_subscription_filter_delete

        
        """
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/subscription-filter/'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_subscription_filter_get(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_subscription_filter_get

        
        """
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/subscription-filter/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_subscription_filter_name_post(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_subscription_filter_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/subscription-filter/name/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_subscription_filter_namevalue_name_delete(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_subscription_filter_namevalue_name_delete

        
        """
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/subscription-filter/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_subscription_filter_namevalue_name_get(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_subscription_filter_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/subscription-filter/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_subscription_filter_namevalue_name_post(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_subscription_filter_namevalue_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/subscription-filter/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_subscription_filter_namevalue_name_put(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_subscription_filter_namevalue_name_put

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/subscription-filter/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='PUT',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_subscription_filter_post(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_subscription_filter_post

        
        """
        tapi_notification_subscription_filter = TapiNotificationSubscriptionFilter()
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/subscription-filter/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_notification_subscription_filter),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notif_subscriptionuuid_subscription_filter_put(self):
        """Test case for data_context_notification_context_notif_subscriptionuuid_subscription_filter_put

        
        """
        tapi_notification_subscription_filter = TapiNotificationSubscriptionFilter()
        response = self.client.open(
            '/data/context/notification-context/notif-subscription={uuid}/subscription-filter/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(tapi_notification_subscription_filter),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notificationuuid_additional_infovalue_name_get(self):
        """Test case for data_context_notification_context_notificationuuid_additional_infovalue_name_get

        
        """
        response = self.client.open(
            '/data/context/notification-context/notification={uuid}/additional-info={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notificationuuid_alarm_info_get(self):
        """Test case for data_context_notification_context_notificationuuid_alarm_info_get

        
        """
        response = self.client.open(
            '/data/context/notification-context/notification={uuid}/alarm-info/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notificationuuid_changed_attributesvalue_name_get(self):
        """Test case for data_context_notification_context_notificationuuid_changed_attributesvalue_name_get

        
        """
        response = self.client.open(
            '/data/context/notification-context/notification={uuid}/changed-attributes={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notificationuuid_get(self):
        """Test case for data_context_notification_context_notificationuuid_get

        
        """
        response = self.client.open(
            '/data/context/notification-context/notification={uuid}/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notificationuuid_namevalue_name_get(self):
        """Test case for data_context_notification_context_notificationuuid_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/notification-context/notification={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notificationuuid_target_object_namevalue_name_get(self):
        """Test case for data_context_notification_context_notificationuuid_target_object_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/notification-context/notification={uuid}/target-object-name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_notificationuuid_tca_info_get(self):
        """Test case for data_context_notification_context_notificationuuid_tca_info_get

        
        """
        response = self.client.open(
            '/data/context/notification-context/notification={uuid}/tca-info/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_post(self):
        """Test case for data_context_notification_context_post

        
        """
        tapi_notification_notification_context = TapiNotificationNotificationContext()
        response = self.client.open(
            '/data/context/notification-context/',
            method='POST',
            data=json.dumps(tapi_notification_notification_context),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_notification_context_put(self):
        """Test case for data_context_notification_context_put

        
        """
        tapi_notification_notification_context = TapiNotificationNotificationContext()
        response = self.client.open(
            '/data/context/notification-context/',
            method='PUT',
            data=json.dumps(tapi_notification_notification_context),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_create_notification_subscription_service_post(self):
        """Test case for operations_create_notification_subscription_service_post

        
        """
        inline_object2 = InlineObject2()
        response = self.client.open(
            '/operations/create-notification-subscription-service/',
            method='POST',
            data=json.dumps(inline_object2),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_delete_notification_subscription_service_post(self):
        """Test case for operations_delete_notification_subscription_service_post

        
        """
        inline_object7 = InlineObject7()
        response = self.client.open(
            '/operations/delete-notification-subscription-service/',
            method='POST',
            data=json.dumps(inline_object7),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_get_notification_list_post(self):
        """Test case for operations_get_notification_list_post

        
        """
        inline_object19 = InlineObject19()
        response = self.client.open(
            '/operations/get-notification-list/',
            method='POST',
            data=json.dumps(inline_object19),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_get_notification_subscription_service_details_post(self):
        """Test case for operations_get_notification_subscription_service_details_post

        
        """
        inline_object20 = InlineObject20()
        response = self.client.open(
            '/operations/get-notification-subscription-service-details/',
            method='POST',
            data=json.dumps(inline_object20),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_get_notification_subscription_service_list_post(self):
        """Test case for operations_get_notification_subscription_service_list_post

        
        """
        response = self.client.open(
            '/operations/get-notification-subscription-service-list/',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_get_supported_notification_types_post(self):
        """Test case for operations_get_supported_notification_types_post

        
        """
        response = self.client.open(
            '/operations/get-supported-notification-types/',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_update_notification_subscription_service_post(self):
        """Test case for operations_update_notification_subscription_service_post

        
        """
        inline_object28 = InlineObject28()
        response = self.client.open(
            '/operations/update-notification-subscription-service/',
            method='POST',
            data=json.dumps(inline_object28),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
