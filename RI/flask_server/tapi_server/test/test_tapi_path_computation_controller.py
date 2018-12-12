# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from tapi_server.models.inline_object import InlineObject  # noqa: E501
from tapi_server.models.inline_object11 import InlineObject11  # noqa: E501
from tapi_server.models.inline_object26 import InlineObject26  # noqa: E501
from tapi_server.models.tapi_common_bandwidth_profile import TapiCommonBandwidthProfile  # noqa: E501
from tapi_server.models.tapi_common_capacity import TapiCommonCapacity  # noqa: E501
from tapi_server.models.tapi_common_capacity_value import TapiCommonCapacityValue  # noqa: E501
from tapi_server.models.tapi_common_name_and_value import TapiCommonNameAndValue  # noqa: E501
from tapi_server.models.tapi_common_service_interface_point_ref import TapiCommonServiceInterfacePointRef  # noqa: E501
from tapi_server.models.tapi_path_computation_compute_p2_p_path import TapiPathComputationComputeP2PPath  # noqa: E501
from tapi_server.models.tapi_path_computation_delete_p2_p_path import TapiPathComputationDeleteP2PPath  # noqa: E501
from tapi_server.models.tapi_path_computation_optimize_p2_p_path import TapiPathComputationOptimizeP2PPath  # noqa: E501
from tapi_server.models.tapi_path_computation_path import TapiPathComputationPath  # noqa: E501
from tapi_server.models.tapi_path_computation_path_computation_context import TapiPathComputationPathComputationContext  # noqa: E501
from tapi_server.models.tapi_path_computation_path_computation_service import TapiPathComputationPathComputationService  # noqa: E501
from tapi_server.models.tapi_path_computation_path_objective_function import TapiPathComputationPathObjectiveFunction  # noqa: E501
from tapi_server.models.tapi_path_computation_path_optimization_constraint import TapiPathComputationPathOptimizationConstraint  # noqa: E501
from tapi_server.models.tapi_path_computation_path_ref import TapiPathComputationPathRef  # noqa: E501
from tapi_server.models.tapi_path_computation_path_service_end_point import TapiPathComputationPathServiceEndPoint  # noqa: E501
from tapi_server.models.tapi_path_computation_routing_constraint import TapiPathComputationRoutingConstraint  # noqa: E501
from tapi_server.models.tapi_path_computation_topology_constraint import TapiPathComputationTopologyConstraint  # noqa: E501
from tapi_server.models.tapi_topology_cost_characteristic import TapiTopologyCostCharacteristic  # noqa: E501
from tapi_server.models.tapi_topology_latency_characteristic import TapiTopologyLatencyCharacteristic  # noqa: E501
from tapi_server.models.tapi_topology_link_ref import TapiTopologyLinkRef  # noqa: E501
from tapi_server.models.tapi_topology_node_ref import TapiTopologyNodeRef  # noqa: E501
from tapi_server.models.tapi_topology_risk_characteristic import TapiTopologyRiskCharacteristic  # noqa: E501
from tapi_server.models.tapi_topology_topology_ref import TapiTopologyTopologyRef  # noqa: E501
from tapi_server.test import BaseTestCase


class TestTapiPathComputationController(BaseTestCase):
    """TapiPathComputationController integration test stubs"""

    def test_data_context_path_computation_context_delete(self):
        """Test case for data_context_path_computation_context_delete

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_get(self):
        """Test case for data_context_path_computation_context_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_service_post(self):
        """Test case for data_context_path_computation_context_path_comp_service_post

        
        """
        tapi_path_computation_path_computation_service = TapiPathComputationPathComputationService()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service/',
            method='POST',
            data=json.dumps(tapi_path_computation_path_computation_service),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_delete(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_delete

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_point_post(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_point_post

        
        """
        tapi_path_computation_path_service_end_point = TapiPathComputationPathServiceEndPoint()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_path_computation_path_service_end_point),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_delete(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_delete

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_get(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_post(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_post

        
        """
        tapi_common_capacity_value = TapiCommonCapacityValue()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_common_capacity_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_put(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_put

        
        """
        tapi_common_capacity_value = TapiCommonCapacityValue()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_common_capacity_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_delete(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_delete

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_get(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_post(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_post

        
        """
        tapi_common_capacity_value = TapiCommonCapacityValue()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_common_capacity_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_put(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_put

        
        """
        tapi_common_capacity_value = TapiCommonCapacityValue()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_common_capacity_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_delete(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_delete

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_get(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_delete(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_delete

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_get(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_post(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_post

        
        """
        tapi_common_capacity_value = TapiCommonCapacityValue()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_common_capacity_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_put(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_put

        
        """
        tapi_common_capacity_value = TapiCommonCapacityValue()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_common_capacity_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_delete(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_delete

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_get(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_post(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_post

        
        """
        tapi_common_capacity_value = TapiCommonCapacityValue()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_common_capacity_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_put(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_put

        
        """
        tapi_common_capacity_value = TapiCommonCapacityValue()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_common_capacity_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_post(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_post

        
        """
        tapi_common_bandwidth_profile = TapiCommonBandwidthProfile()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_common_bandwidth_profile),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_put(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_put

        
        """
        tapi_common_bandwidth_profile = TapiCommonBandwidthProfile()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_common_bandwidth_profile),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_delete(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_delete

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/capacity/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_get(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/capacity/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_post(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_post

        
        """
        tapi_common_capacity = TapiCommonCapacity()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/capacity/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_common_capacity),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_put(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_put

        
        """
        tapi_common_capacity = TapiCommonCapacity()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/capacity/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_common_capacity),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_total_size_delete(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_total_size_delete

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/capacity/total-size/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_total_size_get(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_total_size_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/capacity/total-size/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_total_size_post(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_total_size_post

        
        """
        tapi_common_capacity_value = TapiCommonCapacityValue()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/capacity/total-size/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_common_capacity_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_total_size_put(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_total_size_put

        
        """
        tapi_common_capacity_value = TapiCommonCapacityValue()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/capacity/total-size/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_common_capacity_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_delete(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_delete

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_get(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_name_post(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/name/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_namevalue_name_delete(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_namevalue_name_delete

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/name={value-name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_namevalue_name_get(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/name={value-name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_namevalue_name_post(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_namevalue_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/name={value-name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_namevalue_name_put(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_namevalue_name_put

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/name={value-name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='PUT',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_post(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_post

        
        """
        tapi_path_computation_path_service_end_point = TapiPathComputationPathServiceEndPoint()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_path_computation_path_service_end_point),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_put(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_put

        
        """
        tapi_path_computation_path_service_end_point = TapiPathComputationPathServiceEndPoint()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_path_computation_path_service_end_point),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_service_interface_point_get(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_service_interface_point_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/end-point={local-id}/service-interface-point/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_get(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_name_post(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/name/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_namevalue_name_delete(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_namevalue_name_delete

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_namevalue_name_get(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_namevalue_name_post(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_namevalue_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_namevalue_name_put(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_namevalue_name_put

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='PUT',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_objective_function_delete(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_objective_function_delete

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/objective-function/'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_objective_function_get(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_objective_function_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/objective-function/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_objective_function_name_post(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_objective_function_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/objective-function/name/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_objective_function_namevalue_name_delete(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_objective_function_namevalue_name_delete

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/objective-function/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_objective_function_namevalue_name_get(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_objective_function_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/objective-function/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_objective_function_namevalue_name_post(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_objective_function_namevalue_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/objective-function/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_objective_function_namevalue_name_put(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_objective_function_namevalue_name_put

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/objective-function/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='PUT',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_objective_function_post(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_objective_function_post

        
        """
        tapi_path_computation_path_objective_function = TapiPathComputationPathObjectiveFunction()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/objective-function/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_path_computation_path_objective_function),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_objective_function_put(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_objective_function_put

        
        """
        tapi_path_computation_path_objective_function = TapiPathComputationPathObjectiveFunction()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/objective-function/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(tapi_path_computation_path_objective_function),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_delete(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_delete

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/optimization-constraint/'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_get(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/optimization-constraint/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_name_post(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/optimization-constraint/name/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_namevalue_name_delete(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_namevalue_name_delete

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/optimization-constraint/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_namevalue_name_get(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/optimization-constraint/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_namevalue_name_post(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_namevalue_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/optimization-constraint/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_namevalue_name_put(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_namevalue_name_put

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/optimization-constraint/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='PUT',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_post(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_post

        
        """
        tapi_path_computation_path_optimization_constraint = TapiPathComputationPathOptimizationConstraint()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/optimization-constraint/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_path_computation_path_optimization_constraint),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_put(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_put

        
        """
        tapi_path_computation_path_optimization_constraint = TapiPathComputationPathOptimizationConstraint()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/optimization-constraint/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(tapi_path_computation_path_optimization_constraint),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_pathpath_uuid_get(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_pathpath_uuid_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/path={path-uuid}/'.format(uuid='uuid_example', path_uuid='path_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_post(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_post

        
        """
        tapi_path_computation_path_computation_service = TapiPathComputationPathComputationService()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_path_computation_path_computation_service),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_put(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_put

        
        """
        tapi_path_computation_path_computation_service = TapiPathComputationPathComputationService()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(tapi_path_computation_path_computation_service),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_cost_characteristic_post(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_cost_characteristic_post

        
        """
        tapi_topology_cost_characteristic = TapiTopologyCostCharacteristic()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/routing-constraint/cost-characteristic/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_topology_cost_characteristic),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_cost_characteristiccost_name_delete(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_cost_characteristiccost_name_delete

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/routing-constraint/cost-characteristic={cost-name}/'.format(uuid='uuid_example', cost_name='cost_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_cost_characteristiccost_name_get(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_cost_characteristiccost_name_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/routing-constraint/cost-characteristic={cost-name}/'.format(uuid='uuid_example', cost_name='cost_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_cost_characteristiccost_name_post(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_cost_characteristiccost_name_post

        
        """
        tapi_topology_cost_characteristic = TapiTopologyCostCharacteristic()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/routing-constraint/cost-characteristic={cost-name}/'.format(uuid='uuid_example', cost_name='cost_name_example'),
            method='POST',
            data=json.dumps(tapi_topology_cost_characteristic),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_cost_characteristiccost_name_put(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_cost_characteristiccost_name_put

        
        """
        tapi_topology_cost_characteristic = TapiTopologyCostCharacteristic()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/routing-constraint/cost-characteristic={cost-name}/'.format(uuid='uuid_example', cost_name='cost_name_example'),
            method='PUT',
            data=json.dumps(tapi_topology_cost_characteristic),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_delete(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_delete

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/routing-constraint/'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_get(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/routing-constraint/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_latency_characteristic_post(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_latency_characteristic_post

        
        """
        tapi_topology_latency_characteristic = TapiTopologyLatencyCharacteristic()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/routing-constraint/latency-characteristic/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_topology_latency_characteristic),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_latency_characteristictraffic_property_name_delete(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_latency_characteristictraffic_property_name_delete

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/routing-constraint/latency-characteristic={traffic-property-name}/'.format(uuid='uuid_example', traffic_property_name='traffic_property_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_latency_characteristictraffic_property_name_get(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_latency_characteristictraffic_property_name_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/routing-constraint/latency-characteristic={traffic-property-name}/'.format(uuid='uuid_example', traffic_property_name='traffic_property_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_latency_characteristictraffic_property_name_post(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_latency_characteristictraffic_property_name_post

        
        """
        tapi_topology_latency_characteristic = TapiTopologyLatencyCharacteristic()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/routing-constraint/latency-characteristic={traffic-property-name}/'.format(uuid='uuid_example', traffic_property_name='traffic_property_name_example'),
            method='POST',
            data=json.dumps(tapi_topology_latency_characteristic),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_latency_characteristictraffic_property_name_put(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_latency_characteristictraffic_property_name_put

        
        """
        tapi_topology_latency_characteristic = TapiTopologyLatencyCharacteristic()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/routing-constraint/latency-characteristic={traffic-property-name}/'.format(uuid='uuid_example', traffic_property_name='traffic_property_name_example'),
            method='PUT',
            data=json.dumps(tapi_topology_latency_characteristic),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_post(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_post

        
        """
        tapi_path_computation_routing_constraint = TapiPathComputationRoutingConstraint()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/routing-constraint/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_path_computation_routing_constraint),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_put(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_put

        
        """
        tapi_path_computation_routing_constraint = TapiPathComputationRoutingConstraint()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/routing-constraint/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(tapi_path_computation_routing_constraint),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_risk_diversity_characteristic_post(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_risk_diversity_characteristic_post

        
        """
        tapi_topology_risk_characteristic = TapiTopologyRiskCharacteristic()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/routing-constraint/risk-diversity-characteristic/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_topology_risk_characteristic),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_risk_diversity_characteristicrisk_characteristic_name_delete(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_risk_diversity_characteristicrisk_characteristic_name_delete

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/routing-constraint/risk-diversity-characteristic={risk-characteristic-name}/'.format(uuid='uuid_example', risk_characteristic_name='risk_characteristic_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_risk_diversity_characteristicrisk_characteristic_name_get(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_risk_diversity_characteristicrisk_characteristic_name_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/routing-constraint/risk-diversity-characteristic={risk-characteristic-name}/'.format(uuid='uuid_example', risk_characteristic_name='risk_characteristic_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_risk_diversity_characteristicrisk_characteristic_name_post(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_risk_diversity_characteristicrisk_characteristic_name_post

        
        """
        tapi_topology_risk_characteristic = TapiTopologyRiskCharacteristic()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/routing-constraint/risk-diversity-characteristic={risk-characteristic-name}/'.format(uuid='uuid_example', risk_characteristic_name='risk_characteristic_name_example'),
            method='POST',
            data=json.dumps(tapi_topology_risk_characteristic),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_risk_diversity_characteristicrisk_characteristic_name_put(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_risk_diversity_characteristicrisk_characteristic_name_put

        
        """
        tapi_topology_risk_characteristic = TapiTopologyRiskCharacteristic()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/routing-constraint/risk-diversity-characteristic={risk-characteristic-name}/'.format(uuid='uuid_example', risk_characteristic_name='risk_characteristic_name_example'),
            method='PUT',
            data=json.dumps(tapi_topology_risk_characteristic),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_avoid_topologytopology_uuid_get(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_avoid_topologytopology_uuid_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/topology-constraint/avoid-topology={topology-uuid}/'.format(uuid='uuid_example', topology_uuid='topology_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_delete(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_delete

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/topology-constraint/'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_exclude_linktopology_uuidlink_uuid_get(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_exclude_linktopology_uuidlink_uuid_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/topology-constraint/exclude-link={topology-uuid},{link-uuid}/'.format(uuid='uuid_example', topology_uuid='topology_uuid_example', link_uuid='link_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_exclude_nodetopology_uuidnode_uuid_get(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_exclude_nodetopology_uuidnode_uuid_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/topology-constraint/exclude-node={topology-uuid},{node-uuid}/'.format(uuid='uuid_example', topology_uuid='topology_uuid_example', node_uuid='node_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_exclude_pathpath_uuid_get(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_exclude_pathpath_uuid_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/topology-constraint/exclude-path={path-uuid}/'.format(uuid='uuid_example', path_uuid='path_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_get(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/topology-constraint/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_include_linktopology_uuidlink_uuid_get(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_include_linktopology_uuidlink_uuid_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/topology-constraint/include-link={topology-uuid},{link-uuid}/'.format(uuid='uuid_example', topology_uuid='topology_uuid_example', link_uuid='link_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_include_nodetopology_uuidnode_uuid_get(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_include_nodetopology_uuidnode_uuid_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/topology-constraint/include-node={topology-uuid},{node-uuid}/'.format(uuid='uuid_example', topology_uuid='topology_uuid_example', node_uuid='node_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_include_pathpath_uuid_get(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_include_pathpath_uuid_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/topology-constraint/include-path={path-uuid}/'.format(uuid='uuid_example', path_uuid='path_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_include_topologytopology_uuid_get(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_include_topologytopology_uuid_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/topology-constraint/include-topology={topology-uuid}/'.format(uuid='uuid_example', topology_uuid='topology_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_post(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_post

        
        """
        tapi_path_computation_topology_constraint = TapiPathComputationTopologyConstraint()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/topology-constraint/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_path_computation_topology_constraint),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_put(self):
        """Test case for data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_put

        
        """
        tapi_path_computation_topology_constraint = TapiPathComputationTopologyConstraint()
        response = self.client.open(
            '/data/context/path-computation-context/path-comp-service={uuid}/topology-constraint/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(tapi_path_computation_topology_constraint),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_pathuuid_get(self):
        """Test case for data_context_path_computation_context_pathuuid_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path={uuid}/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_pathuuid_linktopology_uuidlink_uuid_get(self):
        """Test case for data_context_path_computation_context_pathuuid_linktopology_uuidlink_uuid_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path={uuid}/link={topology-uuid},{link-uuid}/'.format(uuid='uuid_example', topology_uuid='topology_uuid_example', link_uuid='link_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_pathuuid_namevalue_name_get(self):
        """Test case for data_context_path_computation_context_pathuuid_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_pathuuid_routing_constraint_cost_characteristiccost_name_get(self):
        """Test case for data_context_path_computation_context_pathuuid_routing_constraint_cost_characteristiccost_name_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path={uuid}/routing-constraint/cost-characteristic={cost-name}/'.format(uuid='uuid_example', cost_name='cost_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_pathuuid_routing_constraint_get(self):
        """Test case for data_context_path_computation_context_pathuuid_routing_constraint_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path={uuid}/routing-constraint/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_pathuuid_routing_constraint_latency_characteristictraffic_property_name_get(self):
        """Test case for data_context_path_computation_context_pathuuid_routing_constraint_latency_characteristictraffic_property_name_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path={uuid}/routing-constraint/latency-characteristic={traffic-property-name}/'.format(uuid='uuid_example', traffic_property_name='traffic_property_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_pathuuid_routing_constraint_risk_diversity_characteristicrisk_characteristic_name_get(self):
        """Test case for data_context_path_computation_context_pathuuid_routing_constraint_risk_diversity_characteristicrisk_characteristic_name_get

        
        """
        response = self.client.open(
            '/data/context/path-computation-context/path={uuid}/routing-constraint/risk-diversity-characteristic={risk-characteristic-name}/'.format(uuid='uuid_example', risk_characteristic_name='risk_characteristic_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_post(self):
        """Test case for data_context_path_computation_context_post

        
        """
        tapi_path_computation_path_computation_context = TapiPathComputationPathComputationContext()
        response = self.client.open(
            '/data/context/path-computation-context/',
            method='POST',
            data=json.dumps(tapi_path_computation_path_computation_context),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_path_computation_context_put(self):
        """Test case for data_context_path_computation_context_put

        
        """
        tapi_path_computation_path_computation_context = TapiPathComputationPathComputationContext()
        response = self.client.open(
            '/data/context/path-computation-context/',
            method='PUT',
            data=json.dumps(tapi_path_computation_path_computation_context),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_compute_p2_p_path_post(self):
        """Test case for operations_compute_p2_p_path_post

        
        """
        inline_object = InlineObject()
        response = self.client.open(
            '/operations/compute-p-2-p-path/',
            method='POST',
            data=json.dumps(inline_object),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_delete_p2_p_path_post(self):
        """Test case for operations_delete_p2_p_path_post

        
        """
        inline_object11 = InlineObject11()
        response = self.client.open(
            '/operations/delete-p-2-p-path/',
            method='POST',
            data=json.dumps(inline_object11),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_optimize_p2_p_path_post(self):
        """Test case for operations_optimize_p2_p_path_post

        
        """
        inline_object26 = InlineObject26()
        response = self.client.open(
            '/operations/optimize-p-2-p-path/',
            method='POST',
            data=json.dumps(inline_object26),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
