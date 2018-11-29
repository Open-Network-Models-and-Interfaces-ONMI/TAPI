# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from tapi_server.models.inline_object15 import InlineObject15  # noqa: E501
from tapi_server.models.inline_object17 import InlineObject17  # noqa: E501
from tapi_server.models.inline_object18 import InlineObject18  # noqa: E501
from tapi_server.models.inline_object25 import InlineObject25  # noqa: E501
from tapi_server.models.tapi_common_bandwidth_profile import TapiCommonBandwidthProfile  # noqa: E501
from tapi_server.models.tapi_common_capacity import TapiCommonCapacity  # noqa: E501
from tapi_server.models.tapi_common_capacity_value import TapiCommonCapacityValue  # noqa: E501
from tapi_server.models.tapi_common_name_and_value import TapiCommonNameAndValue  # noqa: E501
from tapi_server.models.tapi_common_service_interface_point_ref import TapiCommonServiceInterfacePointRef  # noqa: E501
from tapi_server.models.tapi_topology_cost_characteristic import TapiTopologyCostCharacteristic  # noqa: E501
from tapi_server.models.tapi_topology_get_link_details import TapiTopologyGetLinkDetails  # noqa: E501
from tapi_server.models.tapi_topology_get_node_details import TapiTopologyGetNodeDetails  # noqa: E501
from tapi_server.models.tapi_topology_get_node_edge_point_details import TapiTopologyGetNodeEdgePointDetails  # noqa: E501
from tapi_server.models.tapi_topology_get_topology_details import TapiTopologyGetTopologyDetails  # noqa: E501
from tapi_server.models.tapi_topology_get_topology_list import TapiTopologyGetTopologyList  # noqa: E501
from tapi_server.models.tapi_topology_inter_rule_group import TapiTopologyInterRuleGroup  # noqa: E501
from tapi_server.models.tapi_topology_latency_characteristic import TapiTopologyLatencyCharacteristic  # noqa: E501
from tapi_server.models.tapi_topology_link import TapiTopologyLink  # noqa: E501
from tapi_server.models.tapi_topology_network_topology_service import TapiTopologyNetworkTopologyService  # noqa: E501
from tapi_server.models.tapi_topology_node_edge_point_ref import TapiTopologyNodeEdgePointRef  # noqa: E501
from tapi_server.models.tapi_topology_node_owned_node_edge_point import TapiTopologyNodeOwnedNodeEdgePoint  # noqa: E501
from tapi_server.models.tapi_topology_node_rule_group import TapiTopologyNodeRuleGroup  # noqa: E501
from tapi_server.models.tapi_topology_node_rule_group_ref import TapiTopologyNodeRuleGroupRef  # noqa: E501
from tapi_server.models.tapi_topology_resilience_type import TapiTopologyResilienceType  # noqa: E501
from tapi_server.models.tapi_topology_risk_characteristic import TapiTopologyRiskCharacteristic  # noqa: E501
from tapi_server.models.tapi_topology_rule import TapiTopologyRule  # noqa: E501
from tapi_server.models.tapi_topology_topology import TapiTopologyTopology  # noqa: E501
from tapi_server.models.tapi_topology_topology_context import TapiTopologyTopologyContext  # noqa: E501
from tapi_server.models.tapi_topology_topology_node import TapiTopologyTopologyNode  # noqa: E501
from tapi_server.models.tapi_topology_topology_ref import TapiTopologyTopologyRef  # noqa: E501
from tapi_server.models.tapi_topology_validation_mechanism import TapiTopologyValidationMechanism  # noqa: E501
from tapi_server.test import BaseTestCase


class TestTapiTopologyController(BaseTestCase):
    """TapiTopologyController integration test stubs"""

    def test_data_context_topology_context_delete(self):
        """Test case for data_context_topology_context_delete

        
        """
        response = self.client.open(
            '/data/context/topology-context/',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_get(self):
        """Test case for data_context_topology_context_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_nw_topology_service_get(self):
        """Test case for data_context_topology_context_nw_topology_service_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/nw-topology-service/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_nw_topology_service_namevalue_name_get(self):
        """Test case for data_context_topology_context_nw_topology_service_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/nw-topology-service/name={value-name}/'.format(value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_nw_topology_service_topologytopology_uuid_get(self):
        """Test case for data_context_topology_context_nw_topology_service_topologytopology_uuid_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/nw-topology-service/topology={topology-uuid}/'.format(topology_uuid='topology_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_post(self):
        """Test case for data_context_topology_context_post

        
        """
        tapi_topology_topology_context = TapiTopologyTopologyContext()
        response = self.client.open(
            '/data/context/topology-context/',
            method='POST',
            data=json.dumps(tapi_topology_topology_context),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_put(self):
        """Test case for data_context_topology_context_put

        
        """
        tapi_topology_topology_context = TapiTopologyTopologyContext()
        response = self.client.open(
            '/data/context/topology-context/',
            method='PUT',
            data=json.dumps(tapi_topology_topology_context),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_get(self):
        """Test case for data_context_topology_context_topologyuuid_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_linklink_uuid_available_capacity_bandwidth_profile_committed_burst_size_get(self):
        """Test case for data_context_topology_context_topologyuuid_linklink_uuid_available_capacity_bandwidth_profile_committed_burst_size_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/link={link-uuid}/available-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_linklink_uuid_available_capacity_bandwidth_profile_committed_information_rate_get(self):
        """Test case for data_context_topology_context_topologyuuid_linklink_uuid_available_capacity_bandwidth_profile_committed_information_rate_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/link={link-uuid}/available-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_linklink_uuid_available_capacity_bandwidth_profile_get(self):
        """Test case for data_context_topology_context_topologyuuid_linklink_uuid_available_capacity_bandwidth_profile_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/link={link-uuid}/available-capacity/bandwidth-profile/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_linklink_uuid_available_capacity_bandwidth_profile_peak_burst_size_get(self):
        """Test case for data_context_topology_context_topologyuuid_linklink_uuid_available_capacity_bandwidth_profile_peak_burst_size_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/link={link-uuid}/available-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_linklink_uuid_available_capacity_bandwidth_profile_peak_information_rate_get(self):
        """Test case for data_context_topology_context_topologyuuid_linklink_uuid_available_capacity_bandwidth_profile_peak_information_rate_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/link={link-uuid}/available-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_linklink_uuid_available_capacity_get(self):
        """Test case for data_context_topology_context_topologyuuid_linklink_uuid_available_capacity_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/link={link-uuid}/available-capacity/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_linklink_uuid_available_capacity_total_size_get(self):
        """Test case for data_context_topology_context_topologyuuid_linklink_uuid_available_capacity_total_size_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/link={link-uuid}/available-capacity/total-size/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_linklink_uuid_cost_characteristiccost_name_get(self):
        """Test case for data_context_topology_context_topologyuuid_linklink_uuid_cost_characteristiccost_name_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/link={link-uuid}/cost-characteristic={cost-name}/'.format(uuid='uuid_example', link_uuid='link_uuid_example', cost_name='cost_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_linklink_uuid_get(self):
        """Test case for data_context_topology_context_topologyuuid_linklink_uuid_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/link={link-uuid}/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_linklink_uuid_latency_characteristictraffic_property_name_get(self):
        """Test case for data_context_topology_context_topologyuuid_linklink_uuid_latency_characteristictraffic_property_name_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/link={link-uuid}/latency-characteristic={traffic-property-name}/'.format(uuid='uuid_example', link_uuid='link_uuid_example', traffic_property_name='traffic_property_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_linklink_uuid_namevalue_name_get(self):
        """Test case for data_context_topology_context_topologyuuid_linklink_uuid_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/link={link-uuid}/name={value-name}/'.format(uuid='uuid_example', link_uuid='link_uuid_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_linklink_uuid_node_edge_pointtopology_uuidnode_uuidnode_edge_point_uuid_get(self):
        """Test case for data_context_topology_context_topologyuuid_linklink_uuid_node_edge_pointtopology_uuidnode_uuidnode_edge_point_uuid_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/link={link-uuid}/node-edge-point={topology-uuid},{node-uuid},{node-edge-point-uuid}/'.format(uuid='uuid_example', link_uuid='link_uuid_example', topology_uuid='topology_uuid_example', node_uuid='node_uuid_example', node_edge_point_uuid='node_edge_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_linklink_uuid_resilience_type_get(self):
        """Test case for data_context_topology_context_topologyuuid_linklink_uuid_resilience_type_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/link={link-uuid}/resilience-type/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_linklink_uuid_risk_characteristicrisk_characteristic_name_get(self):
        """Test case for data_context_topology_context_topologyuuid_linklink_uuid_risk_characteristicrisk_characteristic_name_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/link={link-uuid}/risk-characteristic={risk-characteristic-name}/'.format(uuid='uuid_example', link_uuid='link_uuid_example', risk_characteristic_name='risk_characteristic_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_linklink_uuid_total_potential_capacity_bandwidth_profile_committed_burst_size_get(self):
        """Test case for data_context_topology_context_topologyuuid_linklink_uuid_total_potential_capacity_bandwidth_profile_committed_burst_size_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/link={link-uuid}/total-potential-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_linklink_uuid_total_potential_capacity_bandwidth_profile_committed_information_rate_get(self):
        """Test case for data_context_topology_context_topologyuuid_linklink_uuid_total_potential_capacity_bandwidth_profile_committed_information_rate_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/link={link-uuid}/total-potential-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_linklink_uuid_total_potential_capacity_bandwidth_profile_get(self):
        """Test case for data_context_topology_context_topologyuuid_linklink_uuid_total_potential_capacity_bandwidth_profile_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/link={link-uuid}/total-potential-capacity/bandwidth-profile/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_linklink_uuid_total_potential_capacity_bandwidth_profile_peak_burst_size_get(self):
        """Test case for data_context_topology_context_topologyuuid_linklink_uuid_total_potential_capacity_bandwidth_profile_peak_burst_size_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/link={link-uuid}/total-potential-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_linklink_uuid_total_potential_capacity_bandwidth_profile_peak_information_rate_get(self):
        """Test case for data_context_topology_context_topologyuuid_linklink_uuid_total_potential_capacity_bandwidth_profile_peak_information_rate_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/link={link-uuid}/total-potential-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_linklink_uuid_total_potential_capacity_get(self):
        """Test case for data_context_topology_context_topologyuuid_linklink_uuid_total_potential_capacity_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/link={link-uuid}/total-potential-capacity/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_linklink_uuid_total_potential_capacity_total_size_get(self):
        """Test case for data_context_topology_context_topologyuuid_linklink_uuid_total_potential_capacity_total_size_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/link={link-uuid}/total-potential-capacity/total-size/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_linklink_uuid_validation_mechanismvalidation_mechanism_get(self):
        """Test case for data_context_topology_context_topologyuuid_linklink_uuid_validation_mechanismvalidation_mechanism_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/link={link-uuid}/validation-mechanism={validation-mechanism}/'.format(uuid='uuid_example', link_uuid='link_uuid_example', validation_mechanism='validation_mechanism_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_namevalue_name_get(self):
        """Test case for data_context_topology_context_topologyuuid_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_aggregated_node_edge_pointtopology_uuidaggregated_node_edge_point_node_uuidnode_edge_point_uuid_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_aggregated_node_edge_pointtopology_uuidaggregated_node_edge_point_node_uuidnode_edge_point_uuid_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/aggregated-node-edge-point={topology-uuid},{aggregated-node-edge-point-node-uuid},{node-edge-point-uuid}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', topology_uuid='topology_uuid_example', aggregated_node_edge_point_node_uuid='aggregated_node_edge_point_node_uuid_example', node_edge_point_uuid='node_edge_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_available_capacity_bandwidth_profile_committed_burst_size_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_available_capacity_bandwidth_profile_committed_burst_size_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/available-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_available_capacity_bandwidth_profile_committed_information_rate_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_available_capacity_bandwidth_profile_committed_information_rate_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/available-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_available_capacity_bandwidth_profile_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_available_capacity_bandwidth_profile_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/available-capacity/bandwidth-profile/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_available_capacity_bandwidth_profile_peak_burst_size_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_available_capacity_bandwidth_profile_peak_burst_size_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/available-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_available_capacity_bandwidth_profile_peak_information_rate_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_available_capacity_bandwidth_profile_peak_information_rate_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/available-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_available_capacity_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_available_capacity_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/available-capacity/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_available_capacity_total_size_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_available_capacity_total_size_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/available-capacity/total-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_cost_characteristiccost_name_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_cost_characteristiccost_name_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/cost-characteristic={cost-name}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', cost_name='cost_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_encap_topology_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_encap_topology_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/encap-topology/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_latency_characteristictraffic_property_name_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_latency_characteristictraffic_property_name_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/latency-characteristic={traffic-property-name}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', traffic_property_name='traffic_property_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_namevalue_name_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/name={value-name}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_available_capacity_bandwidth_profile_committed_burst_size_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_available_capacity_bandwidth_profile_committed_burst_size_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/available-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_available_capacity_bandwidth_profile_committed_information_rate_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_available_capacity_bandwidth_profile_committed_information_rate_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/available-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_available_capacity_bandwidth_profile_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_available_capacity_bandwidth_profile_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/available-capacity/bandwidth-profile/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_available_capacity_bandwidth_profile_peak_burst_size_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_available_capacity_bandwidth_profile_peak_burst_size_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/available-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_available_capacity_bandwidth_profile_peak_information_rate_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_available_capacity_bandwidth_profile_peak_information_rate_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/available-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_available_capacity_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_available_capacity_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/available-capacity/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_available_capacity_total_size_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_available_capacity_total_size_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/available-capacity/total-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_composed_rule_grouptopology_uuidcomposed_rule_group_node_uuidcomposed_rule_group_node_rule_group_uuid_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_composed_rule_grouptopology_uuidcomposed_rule_group_node_uuidcomposed_rule_group_node_rule_group_uuid_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/composed-rule-group={topology-uuid},{composed-rule-group-node-uuid},{composed-rule-group-node-rule-group-uuid}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', topology_uuid='topology_uuid_example', composed_rule_group_node_uuid='composed_rule_group_node_uuid_example', composed_rule_group_node_rule_group_uuid='composed_rule_group_node_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_cost_characteristiccost_name_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_cost_characteristiccost_name_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/cost-characteristic={cost-name}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', cost_name='cost_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_associated_node_rule_grouptopology_uuidassociated_node_rule_group_node_uuidassociated_node_rule_group_node_rule_group_uuid_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_associated_node_rule_grouptopology_uuidassociated_node_rule_group_node_uuidassociated_node_rule_group_node_rule_group_uuid_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/inter-rule-group={inter-rule-group-uuid}/associated-node-rule-group={topology-uuid},{associated-node-rule-group-node-uuid},{associated-node-rule-group-node-rule-group-uuid}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example', topology_uuid='topology_uuid_example', associated_node_rule_group_node_uuid='associated_node_rule_group_node_uuid_example', associated_node_rule_group_node_rule_group_uuid='associated_node_rule_group_node_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_available_capacity_bandwidth_profile_committed_burst_size_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_available_capacity_bandwidth_profile_committed_burst_size_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/inter-rule-group={inter-rule-group-uuid}/available-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_available_capacity_bandwidth_profile_committed_information_rate_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_available_capacity_bandwidth_profile_committed_information_rate_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/inter-rule-group={inter-rule-group-uuid}/available-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_available_capacity_bandwidth_profile_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_available_capacity_bandwidth_profile_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/inter-rule-group={inter-rule-group-uuid}/available-capacity/bandwidth-profile/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_available_capacity_bandwidth_profile_peak_burst_size_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_available_capacity_bandwidth_profile_peak_burst_size_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/inter-rule-group={inter-rule-group-uuid}/available-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_available_capacity_bandwidth_profile_peak_information_rate_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_available_capacity_bandwidth_profile_peak_information_rate_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/inter-rule-group={inter-rule-group-uuid}/available-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_available_capacity_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_available_capacity_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/inter-rule-group={inter-rule-group-uuid}/available-capacity/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_available_capacity_total_size_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_available_capacity_total_size_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/inter-rule-group={inter-rule-group-uuid}/available-capacity/total-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_cost_characteristiccost_name_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_cost_characteristiccost_name_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/inter-rule-group={inter-rule-group-uuid}/cost-characteristic={cost-name}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example', cost_name='cost_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/inter-rule-group={inter-rule-group-uuid}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_latency_characteristictraffic_property_name_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_latency_characteristictraffic_property_name_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/inter-rule-group={inter-rule-group-uuid}/latency-characteristic={traffic-property-name}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example', traffic_property_name='traffic_property_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_namevalue_name_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/inter-rule-group={inter-rule-group-uuid}/name={value-name}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_risk_characteristicrisk_characteristic_name_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_risk_characteristicrisk_characteristic_name_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/inter-rule-group={inter-rule-group-uuid}/risk-characteristic={risk-characteristic-name}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example', risk_characteristic_name='risk_characteristic_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_rulelocal_id_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_rulelocal_id_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/inter-rule-group={inter-rule-group-uuid}/rule={local-id}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_rulelocal_id_namevalue_name_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_rulelocal_id_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/inter-rule-group={inter-rule-group-uuid}/rule={local-id}/name={value-name}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_total_potential_capacity_bandwidth_profile_committed_burst_size_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_total_potential_capacity_bandwidth_profile_committed_burst_size_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/inter-rule-group={inter-rule-group-uuid}/total-potential-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_total_potential_capacity_bandwidth_profile_committed_information_rate_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_total_potential_capacity_bandwidth_profile_committed_information_rate_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/inter-rule-group={inter-rule-group-uuid}/total-potential-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_total_potential_capacity_bandwidth_profile_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_total_potential_capacity_bandwidth_profile_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/inter-rule-group={inter-rule-group-uuid}/total-potential-capacity/bandwidth-profile/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_total_potential_capacity_bandwidth_profile_peak_burst_size_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_total_potential_capacity_bandwidth_profile_peak_burst_size_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/inter-rule-group={inter-rule-group-uuid}/total-potential-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_total_potential_capacity_bandwidth_profile_peak_information_rate_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_total_potential_capacity_bandwidth_profile_peak_information_rate_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/inter-rule-group={inter-rule-group-uuid}/total-potential-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_total_potential_capacity_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_total_potential_capacity_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/inter-rule-group={inter-rule-group-uuid}/total-potential-capacity/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_total_potential_capacity_total_size_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_total_potential_capacity_total_size_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/inter-rule-group={inter-rule-group-uuid}/total-potential-capacity/total-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_latency_characteristictraffic_property_name_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_latency_characteristictraffic_property_name_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/latency-characteristic={traffic-property-name}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', traffic_property_name='traffic_property_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_namevalue_name_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/name={value-name}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_node_edge_pointtopology_uuidnode_edge_point_node_uuidnode_edge_point_uuid_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_node_edge_pointtopology_uuidnode_edge_point_node_uuidnode_edge_point_uuid_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/node-edge-point={topology-uuid},{node-edge-point-node-uuid},{node-edge-point-uuid}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', topology_uuid='topology_uuid_example', node_edge_point_node_uuid='node_edge_point_node_uuid_example', node_edge_point_uuid='node_edge_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_risk_characteristicrisk_characteristic_name_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_risk_characteristicrisk_characteristic_name_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/risk-characteristic={risk-characteristic-name}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', risk_characteristic_name='risk_characteristic_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_rulelocal_id_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_rulelocal_id_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/rule={local-id}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_rulelocal_id_namevalue_name_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_rulelocal_id_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/rule={local-id}/name={value-name}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_total_potential_capacity_bandwidth_profile_committed_burst_size_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_total_potential_capacity_bandwidth_profile_committed_burst_size_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/total-potential-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_total_potential_capacity_bandwidth_profile_committed_information_rate_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_total_potential_capacity_bandwidth_profile_committed_information_rate_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/total-potential-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_total_potential_capacity_bandwidth_profile_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_total_potential_capacity_bandwidth_profile_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/total-potential-capacity/bandwidth-profile/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_total_potential_capacity_bandwidth_profile_peak_burst_size_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_total_potential_capacity_bandwidth_profile_peak_burst_size_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/total-potential-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_total_potential_capacity_bandwidth_profile_peak_information_rate_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_total_potential_capacity_bandwidth_profile_peak_information_rate_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/total-potential-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_total_potential_capacity_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_total_potential_capacity_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/total-potential-capacity/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_total_potential_capacity_total_size_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_total_potential_capacity_total_size_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/node-rule-group={node-rule-group-uuid}/total-potential-capacity/total-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_aggregated_node_edge_pointtopology_uuidaggregated_node_edge_point_node_uuidnode_edge_point_uuid_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_aggregated_node_edge_pointtopology_uuidaggregated_node_edge_point_node_uuidnode_edge_point_uuid_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/aggregated-node-edge-point={topology-uuid},{aggregated-node-edge-point-node-uuid},{node-edge-point-uuid}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', topology_uuid='topology_uuid_example', aggregated_node_edge_point_node_uuid='aggregated_node_edge_point_node_uuid_example', node_edge_point_uuid='node_edge_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_available_capacity_bandwidth_profile_committed_burst_size_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_available_capacity_bandwidth_profile_committed_burst_size_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/available-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_available_capacity_bandwidth_profile_committed_information_rate_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_available_capacity_bandwidth_profile_committed_information_rate_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/available-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_available_capacity_bandwidth_profile_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_available_capacity_bandwidth_profile_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/available-capacity/bandwidth-profile/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_available_capacity_bandwidth_profile_peak_burst_size_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_available_capacity_bandwidth_profile_peak_burst_size_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/available-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_available_capacity_bandwidth_profile_peak_information_rate_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_available_capacity_bandwidth_profile_peak_information_rate_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/available-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_available_capacity_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_available_capacity_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/available-capacity/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_available_capacity_total_size_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_available_capacity_total_size_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/available-capacity/total-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_mapped_service_interface_pointservice_interface_point_uuid_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_mapped_service_interface_pointservice_interface_point_uuid_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/mapped-service-interface-point={service-interface-point-uuid}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', service_interface_point_uuid='service_interface_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_namevalue_name_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/name={value-name}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_total_potential_capacity_bandwidth_profile_committed_burst_size_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_total_potential_capacity_bandwidth_profile_committed_burst_size_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/total-potential-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_total_potential_capacity_bandwidth_profile_committed_information_rate_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_total_potential_capacity_bandwidth_profile_committed_information_rate_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/total-potential-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_total_potential_capacity_bandwidth_profile_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_total_potential_capacity_bandwidth_profile_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/total-potential-capacity/bandwidth-profile/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_total_potential_capacity_bandwidth_profile_peak_burst_size_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_total_potential_capacity_bandwidth_profile_peak_burst_size_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/total-potential-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_total_potential_capacity_bandwidth_profile_peak_information_rate_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_total_potential_capacity_bandwidth_profile_peak_information_rate_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/total-potential-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_total_potential_capacity_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_total_potential_capacity_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/total-potential-capacity/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_total_potential_capacity_total_size_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_total_potential_capacity_total_size_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/total-potential-capacity/total-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_total_potential_capacity_bandwidth_profile_committed_burst_size_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_total_potential_capacity_bandwidth_profile_committed_burst_size_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/total-potential-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_total_potential_capacity_bandwidth_profile_committed_information_rate_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_total_potential_capacity_bandwidth_profile_committed_information_rate_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/total-potential-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_total_potential_capacity_bandwidth_profile_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_total_potential_capacity_bandwidth_profile_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/total-potential-capacity/bandwidth-profile/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_total_potential_capacity_bandwidth_profile_peak_burst_size_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_total_potential_capacity_bandwidth_profile_peak_burst_size_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/total-potential-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_total_potential_capacity_bandwidth_profile_peak_information_rate_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_total_potential_capacity_bandwidth_profile_peak_information_rate_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/total-potential-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_total_potential_capacity_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_total_potential_capacity_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/total-potential-capacity/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_total_potential_capacity_total_size_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_total_potential_capacity_total_size_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/total-potential-capacity/total-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_get_link_details_post(self):
        """Test case for operations_get_link_details_post

        
        """
        inline_object15 = InlineObject15()
        response = self.client.open(
            '/operations/get-link-details/',
            method='POST',
            data=json.dumps(inline_object15),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_get_node_details_post(self):
        """Test case for operations_get_node_details_post

        
        """
        inline_object17 = InlineObject17()
        response = self.client.open(
            '/operations/get-node-details/',
            method='POST',
            data=json.dumps(inline_object17),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_get_node_edge_point_details_post(self):
        """Test case for operations_get_node_edge_point_details_post

        
        """
        inline_object18 = InlineObject18()
        response = self.client.open(
            '/operations/get-node-edge-point-details/',
            method='POST',
            data=json.dumps(inline_object18),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_get_topology_details_post(self):
        """Test case for operations_get_topology_details_post

        
        """
        inline_object25 = InlineObject25()
        response = self.client.open(
            '/operations/get-topology-details/',
            method='POST',
            data=json.dumps(inline_object25),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_get_topology_list_post(self):
        """Test case for operations_get_topology_list_post

        
        """
        response = self.client.open(
            '/operations/get-topology-list/',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
