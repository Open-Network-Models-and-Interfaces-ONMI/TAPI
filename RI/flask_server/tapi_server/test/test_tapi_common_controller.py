# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from tapi_server.models.inline_object24 import InlineObject24  # noqa: E501
from tapi_server.models.inline_object32 import InlineObject32  # noqa: E501
from tapi_server.models.tapi_common_bandwidth_profile import TapiCommonBandwidthProfile  # noqa: E501
from tapi_server.models.tapi_common_capacity import TapiCommonCapacity  # noqa: E501
from tapi_server.models.tapi_common_capacity_value import TapiCommonCapacityValue  # noqa: E501
from tapi_server.models.tapi_common_context import TapiCommonContext  # noqa: E501
from tapi_server.models.tapi_common_context_service_interface_point import TapiCommonContextServiceInterfacePoint  # noqa: E501
from tapi_server.models.tapi_common_get_service_interface_point_details import TapiCommonGetServiceInterfacePointDetails  # noqa: E501
from tapi_server.models.tapi_common_get_service_interface_point_list import TapiCommonGetServiceInterfacePointList  # noqa: E501
from tapi_server.models.tapi_common_name_and_value import TapiCommonNameAndValue  # noqa: E501
from tapi_server.test import BaseTestCase


class TestTapiCommonController(BaseTestCase):
    """TapiCommonController integration test stubs"""

    def test_data_context_delete(self):
        """Test case for data_context_delete

        
        """
        response = self.client.open(
            '/data/context/',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_get(self):
        """Test case for data_context_get

        
        """
        response = self.client.open(
            '/data/context/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_name_post(self):
        """Test case for data_context_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/name/',
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_namevalue_name_delete(self):
        """Test case for data_context_namevalue_name_delete

        
        """
        response = self.client.open(
            '/data/context/name={value-name}/'.format(value_name='value_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_namevalue_name_get(self):
        """Test case for data_context_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/name={value-name}/'.format(value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_namevalue_name_post(self):
        """Test case for data_context_namevalue_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/name={value-name}/'.format(value_name='value_name_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_namevalue_name_put(self):
        """Test case for data_context_namevalue_name_put

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/name={value-name}/'.format(value_name='value_name_example'),
            method='PUT',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_post(self):
        """Test case for data_context_post

        
        """
        tapi_common_context = TapiCommonContext()
        response = self.client.open(
            '/data/context/',
            method='POST',
            data=json.dumps(tapi_common_context),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_put(self):
        """Test case for data_context_put

        
        """
        tapi_common_context = TapiCommonContext()
        response = self.client.open(
            '/data/context/',
            method='PUT',
            data=json.dumps(tapi_common_context),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_point_post(self):
        """Test case for data_context_service_interface_point_post

        
        """
        tapi_common_context_service_interface_point = TapiCommonContextServiceInterfacePoint()
        response = self.client.open(
            '/data/context/service-interface-point/',
            method='POST',
            data=json.dumps(tapi_common_context_service_interface_point),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_available_capacity_bandwidth_profile_committed_burst_size_get(self):
        """Test case for data_context_service_interface_pointuuid_available_capacity_bandwidth_profile_committed_burst_size_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/available-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_available_capacity_bandwidth_profile_committed_information_rate_get(self):
        """Test case for data_context_service_interface_pointuuid_available_capacity_bandwidth_profile_committed_information_rate_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/available-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_available_capacity_bandwidth_profile_get(self):
        """Test case for data_context_service_interface_pointuuid_available_capacity_bandwidth_profile_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/available-capacity/bandwidth-profile/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_available_capacity_bandwidth_profile_peak_burst_size_get(self):
        """Test case for data_context_service_interface_pointuuid_available_capacity_bandwidth_profile_peak_burst_size_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/available-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_available_capacity_bandwidth_profile_peak_information_rate_get(self):
        """Test case for data_context_service_interface_pointuuid_available_capacity_bandwidth_profile_peak_information_rate_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/available-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_available_capacity_get(self):
        """Test case for data_context_service_interface_pointuuid_available_capacity_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/available-capacity/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_available_capacity_total_size_get(self):
        """Test case for data_context_service_interface_pointuuid_available_capacity_total_size_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/available-capacity/total-size/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_delete(self):
        """Test case for data_context_service_interface_pointuuid_delete

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_get(self):
        """Test case for data_context_service_interface_pointuuid_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_name_post(self):
        """Test case for data_context_service_interface_pointuuid_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/name/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_namevalue_name_delete(self):
        """Test case for data_context_service_interface_pointuuid_namevalue_name_delete

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_namevalue_name_get(self):
        """Test case for data_context_service_interface_pointuuid_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_namevalue_name_post(self):
        """Test case for data_context_service_interface_pointuuid_namevalue_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_namevalue_name_put(self):
        """Test case for data_context_service_interface_pointuuid_namevalue_name_put

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='PUT',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_post(self):
        """Test case for data_context_service_interface_pointuuid_post

        
        """
        tapi_common_context_service_interface_point = TapiCommonContextServiceInterfacePoint()
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_common_context_service_interface_point),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_put(self):
        """Test case for data_context_service_interface_pointuuid_put

        
        """
        tapi_common_context_service_interface_point = TapiCommonContextServiceInterfacePoint()
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(tapi_common_context_service_interface_point),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_total_potential_capacity_bandwidth_profile_committed_burst_size_get(self):
        """Test case for data_context_service_interface_pointuuid_total_potential_capacity_bandwidth_profile_committed_burst_size_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/total-potential-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_total_potential_capacity_bandwidth_profile_committed_information_rate_get(self):
        """Test case for data_context_service_interface_pointuuid_total_potential_capacity_bandwidth_profile_committed_information_rate_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/total-potential-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_total_potential_capacity_bandwidth_profile_get(self):
        """Test case for data_context_service_interface_pointuuid_total_potential_capacity_bandwidth_profile_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/total-potential-capacity/bandwidth-profile/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_total_potential_capacity_bandwidth_profile_peak_burst_size_get(self):
        """Test case for data_context_service_interface_pointuuid_total_potential_capacity_bandwidth_profile_peak_burst_size_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/total-potential-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_total_potential_capacity_bandwidth_profile_peak_information_rate_get(self):
        """Test case for data_context_service_interface_pointuuid_total_potential_capacity_bandwidth_profile_peak_information_rate_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/total-potential-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_total_potential_capacity_get(self):
        """Test case for data_context_service_interface_pointuuid_total_potential_capacity_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/total-potential-capacity/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_total_potential_capacity_total_size_get(self):
        """Test case for data_context_service_interface_pointuuid_total_potential_capacity_total_size_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/total-potential-capacity/total-size/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_get_service_interface_point_details_post(self):
        """Test case for operations_get_service_interface_point_details_post

        
        """
        inline_object24 = InlineObject24()
        response = self.client.open(
            '/operations/get-service-interface-point-details/',
            method='POST',
            data=json.dumps(inline_object24),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_get_service_interface_point_list_post(self):
        """Test case for operations_get_service_interface_point_list_post

        
        """
        response = self.client.open(
            '/operations/get-service-interface-point-list/',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_update_service_interface_point_post(self):
        """Test case for operations_update_service_interface_point_post

        
        """
        inline_object32 = InlineObject32()
        response = self.client.open(
            '/operations/update-service-interface-point/',
            method='POST',
            data=json.dumps(inline_object32),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
