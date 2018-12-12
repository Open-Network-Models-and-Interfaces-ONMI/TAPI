# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from tapi_server.models.inline_object1 import InlineObject1  # noqa: E501
from tapi_server.models.inline_object12 import InlineObject12  # noqa: E501
from tapi_server.models.inline_object13 import InlineObject13  # noqa: E501
from tapi_server.models.inline_object14 import InlineObject14  # noqa: E501
from tapi_server.models.inline_object27 import InlineObject27  # noqa: E501
from tapi_server.models.inline_object6 import InlineObject6  # noqa: E501
from tapi_server.models.tapi_common_bandwidth_profile import TapiCommonBandwidthProfile  # noqa: E501
from tapi_server.models.tapi_common_capacity import TapiCommonCapacity  # noqa: E501
from tapi_server.models.tapi_common_capacity_value import TapiCommonCapacityValue  # noqa: E501
from tapi_server.models.tapi_common_name_and_value import TapiCommonNameAndValue  # noqa: E501
from tapi_server.models.tapi_common_service_interface_point_ref import TapiCommonServiceInterfacePointRef  # noqa: E501
from tapi_server.models.tapi_common_time_range import TapiCommonTimeRange  # noqa: E501
from tapi_server.models.tapi_connectivity_ceplist_connection_end_point import TapiConnectivityCeplistConnectionEndPoint  # noqa: E501
from tapi_server.models.tapi_connectivity_connection import TapiConnectivityConnection  # noqa: E501
from tapi_server.models.tapi_connectivity_connection_end_point_ref import TapiConnectivityConnectionEndPointRef  # noqa: E501
from tapi_server.models.tapi_connectivity_connection_ref import TapiConnectivityConnectionRef  # noqa: E501
from tapi_server.models.tapi_connectivity_connectivity_context import TapiConnectivityConnectivityContext  # noqa: E501
from tapi_server.models.tapi_connectivity_connectivity_service_ref import TapiConnectivityConnectivityServiceRef  # noqa: E501
from tapi_server.models.tapi_connectivity_connectivitycontext_connectivity_service import TapiConnectivityConnectivitycontextConnectivityService  # noqa: E501
from tapi_server.models.tapi_connectivity_connectivityservice_end_point import TapiConnectivityConnectivityserviceEndPoint  # noqa: E501
from tapi_server.models.tapi_connectivity_context_topologycontext_topology_node_ownednodeedgepoint_cep_list import TapiConnectivityContextTopologycontextTopologyNodeOwnednodeedgepointCepList  # noqa: E501
from tapi_server.models.tapi_connectivity_create_connectivity_service import TapiConnectivityCreateConnectivityService  # noqa: E501
from tapi_server.models.tapi_connectivity_get_connection_details import TapiConnectivityGetConnectionDetails  # noqa: E501
from tapi_server.models.tapi_connectivity_get_connection_end_point_details import TapiConnectivityGetConnectionEndPointDetails  # noqa: E501
from tapi_server.models.tapi_connectivity_get_connectivity_service_details import TapiConnectivityGetConnectivityServiceDetails  # noqa: E501
from tapi_server.models.tapi_connectivity_get_connectivity_service_list import TapiConnectivityGetConnectivityServiceList  # noqa: E501
from tapi_server.models.tapi_connectivity_route import TapiConnectivityRoute  # noqa: E501
from tapi_server.models.tapi_connectivity_route_ref import TapiConnectivityRouteRef  # noqa: E501
from tapi_server.models.tapi_connectivity_switch import TapiConnectivitySwitch  # noqa: E501
from tapi_server.models.tapi_connectivity_switch_control import TapiConnectivitySwitchControl  # noqa: E501
from tapi_server.models.tapi_connectivity_switch_control_ref import TapiConnectivitySwitchControlRef  # noqa: E501
from tapi_server.models.tapi_connectivity_update_connectivity_service import TapiConnectivityUpdateConnectivityService  # noqa: E501
from tapi_server.models.tapi_path_computation_path_ref import TapiPathComputationPathRef  # noqa: E501
from tapi_server.models.tapi_topology_cost_characteristic import TapiTopologyCostCharacteristic  # noqa: E501
from tapi_server.models.tapi_topology_latency_characteristic import TapiTopologyLatencyCharacteristic  # noqa: E501
from tapi_server.models.tapi_topology_link_ref import TapiTopologyLinkRef  # noqa: E501
from tapi_server.models.tapi_topology_node_edge_point_ref import TapiTopologyNodeEdgePointRef  # noqa: E501
from tapi_server.models.tapi_topology_node_ref import TapiTopologyNodeRef  # noqa: E501
from tapi_server.models.tapi_topology_resilience_type import TapiTopologyResilienceType  # noqa: E501
from tapi_server.models.tapi_topology_risk_characteristic import TapiTopologyRiskCharacteristic  # noqa: E501
from tapi_server.models.tapi_topology_topology_ref import TapiTopologyTopologyRef  # noqa: E501
from tapi_server.test import BaseTestCase


class TestTapiConnectivityController(BaseTestCase):
    """TapiConnectivityController integration test stubs"""

    def test_data_context_connectivity_context_connectionuuid_connection_end_pointtopology_uuidnode_uuidnode_edge_point_uuidconnection_end_point_uuid_get(self):
        """Test case for data_context_connectivity_context_connectionuuid_connection_end_pointtopology_uuidnode_uuidnode_edge_point_uuidconnection_end_point_uuid_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connection={uuid}/connection-end-point={topology-uuid},{node-uuid},{node-edge-point-uuid},{connection-end-point-uuid}/'.format(uuid='uuid_example', topology_uuid='topology_uuid_example', node_uuid='node_uuid_example', node_edge_point_uuid='node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectionuuid_get(self):
        """Test case for data_context_connectivity_context_connectionuuid_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connection={uuid}/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectionuuid_lower_connectionconnection_uuid_get(self):
        """Test case for data_context_connectivity_context_connectionuuid_lower_connectionconnection_uuid_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connection={uuid}/lower-connection={connection-uuid}/'.format(uuid='uuid_example', connection_uuid='connection_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectionuuid_namevalue_name_get(self):
        """Test case for data_context_connectivity_context_connectionuuid_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connection={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectionuuid_routelocal_id_connection_end_pointtopology_uuidnode_uuidnode_edge_point_uuidconnection_end_point_uuid_get(self):
        """Test case for data_context_connectivity_context_connectionuuid_routelocal_id_connection_end_pointtopology_uuidnode_uuidnode_edge_point_uuidconnection_end_point_uuid_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connection={uuid}/route={local-id}/connection-end-point={topology-uuid},{node-uuid},{node-edge-point-uuid},{connection-end-point-uuid}/'.format(uuid='uuid_example', local_id='local_id_example', topology_uuid='topology_uuid_example', node_uuid='node_uuid_example', node_edge_point_uuid='node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectionuuid_routelocal_id_get(self):
        """Test case for data_context_connectivity_context_connectionuuid_routelocal_id_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connection={uuid}/route={local-id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectionuuid_routelocal_id_namevalue_name_get(self):
        """Test case for data_context_connectivity_context_connectionuuid_routelocal_id_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connection={uuid}/route={local-id}/name={value-name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectionuuid_supported_client_linktopology_uuidlink_uuid_get(self):
        """Test case for data_context_connectivity_context_connectionuuid_supported_client_linktopology_uuidlink_uuid_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connection={uuid}/supported-client-link={topology-uuid},{link-uuid}/'.format(uuid='uuid_example', topology_uuid='topology_uuid_example', link_uuid='link_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_get(self):
        """Test case for data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connection={uuid}/switch-control={switch-control-uuid}/'.format(uuid='uuid_example', switch_control_uuid='switch_control_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_namevalue_name_get(self):
        """Test case for data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connection={uuid}/switch-control={switch-control-uuid}/name={value-name}/'.format(uuid='uuid_example', switch_control_uuid='switch_control_uuid_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_resilience_type_get(self):
        """Test case for data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_resilience_type_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connection={uuid}/switch-control={switch-control-uuid}/resilience-type/'.format(uuid='uuid_example', switch_control_uuid='switch_control_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_sub_switch_controlconnection_uuidsub_switch_control_switch_control_uuid_get(self):
        """Test case for data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_sub_switch_controlconnection_uuidsub_switch_control_switch_control_uuid_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connection={uuid}/switch-control={switch-control-uuid}/sub-switch-control={connection-uuid},{sub-switch-control-switch-control-uuid}/'.format(uuid='uuid_example', switch_control_uuid='switch_control_uuid_example', connection_uuid='connection_uuid_example', sub_switch_control_switch_control_uuid='sub_switch_control_switch_control_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_switchlocal_id_get(self):
        """Test case for data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_switchlocal_id_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connection={uuid}/switch-control={switch-control-uuid}/switch={local-id}/'.format(uuid='uuid_example', switch_control_uuid='switch_control_uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_switchlocal_id_namevalue_name_get(self):
        """Test case for data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_switchlocal_id_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connection={uuid}/switch-control={switch-control-uuid}/switch={local-id}/name={value-name}/'.format(uuid='uuid_example', switch_control_uuid='switch_control_uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_switchlocal_id_selected_connection_end_pointtopology_uuidnode_uuidnode_edge_point_uuidconnection_end_point_uuid_get(self):
        """Test case for data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_switchlocal_id_selected_connection_end_pointtopology_uuidnode_uuidnode_edge_point_uuidconnection_end_point_uuid_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connection={uuid}/switch-control={switch-control-uuid}/switch={local-id}/selected-connection-end-point={topology-uuid},{node-uuid},{node-edge-point-uuid},{connection-end-point-uuid}/'.format(uuid='uuid_example', switch_control_uuid='switch_control_uuid_example', local_id='local_id_example', topology_uuid='topology_uuid_example', node_uuid='node_uuid_example', node_edge_point_uuid='node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_switchlocal_id_selected_routeconnection_uuidroute_local_id_get(self):
        """Test case for data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_switchlocal_id_selected_routeconnection_uuidroute_local_id_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connection={uuid}/switch-control={switch-control-uuid}/switch={local-id}/selected-route={connection-uuid},{route-local-id}/'.format(uuid='uuid_example', switch_control_uuid='switch_control_uuid_example', local_id='local_id_example', connection_uuid='connection_uuid_example', route_local_id='route_local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_service_post(self):
        """Test case for data_context_connectivity_context_connectivity_service_post

        
        """
        tapi_connectivity_connectivitycontext_connectivity_service = TapiConnectivityConnectivitycontextConnectivityService()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service/',
            method='POST',
            data=json.dumps(tapi_connectivity_connectivitycontext_connectivity_service),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_avoid_topologytopology_uuid_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_avoid_topologytopology_uuid_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/avoid-topology={topology-uuid}/'.format(uuid='uuid_example', topology_uuid='topology_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_connectionconnection_uuid_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_connectionconnection_uuid_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/connection={connection-uuid}/'.format(uuid='uuid_example', connection_uuid='connection_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_coroute_inclusion_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_coroute_inclusion_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/coroute-inclusion/'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_coroute_inclusion_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_coroute_inclusion_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/coroute-inclusion/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_coroute_inclusion_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_coroute_inclusion_post

        
        """
        tapi_connectivity_connectivity_service_ref = TapiConnectivityConnectivityServiceRef()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/coroute-inclusion/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_connectivity_connectivity_service_ref),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_coroute_inclusion_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_coroute_inclusion_put

        
        """
        tapi_connectivity_connectivity_service_ref = TapiConnectivityConnectivityServiceRef()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/coroute-inclusion/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(tapi_connectivity_connectivity_service_ref),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_cost_characteristic_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_cost_characteristic_post

        
        """
        tapi_topology_cost_characteristic = TapiTopologyCostCharacteristic()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/cost-characteristic/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_topology_cost_characteristic),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_cost_characteristiccost_name_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_cost_characteristiccost_name_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/cost-characteristic={cost-name}/'.format(uuid='uuid_example', cost_name='cost_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_cost_characteristiccost_name_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_cost_characteristiccost_name_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/cost-characteristic={cost-name}/'.format(uuid='uuid_example', cost_name='cost_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_cost_characteristiccost_name_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_cost_characteristiccost_name_post

        
        """
        tapi_topology_cost_characteristic = TapiTopologyCostCharacteristic()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/cost-characteristic={cost-name}/'.format(uuid='uuid_example', cost_name='cost_name_example'),
            method='POST',
            data=json.dumps(tapi_topology_cost_characteristic),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_cost_characteristiccost_name_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_cost_characteristiccost_name_put

        
        """
        tapi_topology_cost_characteristic = TapiTopologyCostCharacteristic()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/cost-characteristic={cost-name}/'.format(uuid='uuid_example', cost_name='cost_name_example'),
            method='PUT',
            data=json.dumps(tapi_topology_cost_characteristic),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_diversity_exclusion_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_diversity_exclusion_post

        
        """
        tapi_connectivity_connectivity_service_ref = TapiConnectivityConnectivityServiceRef()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/diversity-exclusion/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_connectivity_connectivity_service_ref),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_diversity_exclusionconnectivity_service_uuid_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_diversity_exclusionconnectivity_service_uuid_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/diversity-exclusion={connectivity-service-uuid}/'.format(uuid='uuid_example', connectivity_service_uuid='connectivity_service_uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_diversity_exclusionconnectivity_service_uuid_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_diversity_exclusionconnectivity_service_uuid_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/diversity-exclusion={connectivity-service-uuid}/'.format(uuid='uuid_example', connectivity_service_uuid='connectivity_service_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_diversity_exclusionconnectivity_service_uuid_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_diversity_exclusionconnectivity_service_uuid_post

        
        """
        tapi_connectivity_connectivity_service_ref = TapiConnectivityConnectivityServiceRef()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/diversity-exclusion={connectivity-service-uuid}/'.format(uuid='uuid_example', connectivity_service_uuid='connectivity_service_uuid_example'),
            method='POST',
            data=json.dumps(tapi_connectivity_connectivity_service_ref),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_diversity_exclusionconnectivity_service_uuid_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_diversity_exclusionconnectivity_service_uuid_put

        
        """
        tapi_connectivity_connectivity_service_ref = TapiConnectivityConnectivityServiceRef()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/diversity-exclusion={connectivity-service-uuid}/'.format(uuid='uuid_example', connectivity_service_uuid='connectivity_service_uuid_example'),
            method='PUT',
            data=json.dumps(tapi_connectivity_connectivity_service_ref),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_point_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_point_post

        
        """
        tapi_connectivity_connectivityservice_end_point = TapiConnectivityConnectivityserviceEndPoint()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_connectivity_connectivityservice_end_point),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_post

        
        """
        tapi_common_capacity_value = TapiCommonCapacityValue()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_common_capacity_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_put

        
        """
        tapi_common_capacity_value = TapiCommonCapacityValue()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_common_capacity_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_post

        
        """
        tapi_common_capacity_value = TapiCommonCapacityValue()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_common_capacity_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_put

        
        """
        tapi_common_capacity_value = TapiCommonCapacityValue()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_common_capacity_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_post

        
        """
        tapi_common_capacity_value = TapiCommonCapacityValue()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_common_capacity_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_put

        
        """
        tapi_common_capacity_value = TapiCommonCapacityValue()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_common_capacity_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_post

        
        """
        tapi_common_capacity_value = TapiCommonCapacityValue()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_common_capacity_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_put

        
        """
        tapi_common_capacity_value = TapiCommonCapacityValue()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_common_capacity_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_post

        
        """
        tapi_common_bandwidth_profile = TapiCommonBandwidthProfile()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_common_bandwidth_profile),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_put

        
        """
        tapi_common_bandwidth_profile = TapiCommonBandwidthProfile()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/capacity/bandwidth-profile/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_common_bandwidth_profile),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/capacity/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/capacity/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_post

        
        """
        tapi_common_capacity = TapiCommonCapacity()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/capacity/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_common_capacity),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_put

        
        """
        tapi_common_capacity = TapiCommonCapacity()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/capacity/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_common_capacity),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_total_size_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_total_size_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/capacity/total-size/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_total_size_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_total_size_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/capacity/total-size/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_total_size_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_total_size_post

        
        """
        tapi_common_capacity_value = TapiCommonCapacityValue()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/capacity/total-size/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_common_capacity_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_total_size_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_total_size_put

        
        """
        tapi_common_capacity_value = TapiCommonCapacityValue()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/capacity/total-size/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_common_capacity_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_connection_end_pointtopology_uuidnode_uuidnode_edge_point_uuidconnection_end_point_uuid_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_connection_end_pointtopology_uuidnode_uuidnode_edge_point_uuidconnection_end_point_uuid_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/connection-end-point={topology-uuid},{node-uuid},{node-edge-point-uuid},{connection-end-point-uuid}/'.format(uuid='uuid_example', local_id='local_id_example', topology_uuid='topology_uuid_example', node_uuid='node_uuid_example', node_edge_point_uuid='node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_name_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/name/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_namevalue_name_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_namevalue_name_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/name={value-name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_namevalue_name_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/name={value-name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_namevalue_name_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_namevalue_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/name={value-name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_namevalue_name_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_namevalue_name_put

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/name={value-name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='PUT',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_post

        
        """
        tapi_connectivity_connectivityservice_end_point = TapiConnectivityConnectivityserviceEndPoint()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_connectivity_connectivityservice_end_point),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_put

        
        """
        tapi_connectivity_connectivityservice_end_point = TapiConnectivityConnectivityserviceEndPoint()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_connectivity_connectivityservice_end_point),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_service_interface_point_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_service_interface_point_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/service-interface-point/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_service_interface_point_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_service_interface_point_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/service-interface-point/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_service_interface_point_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_service_interface_point_post

        
        """
        tapi_common_service_interface_point_ref = TapiCommonServiceInterfacePointRef()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/service-interface-point/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_common_service_interface_point_ref),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_service_interface_point_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_service_interface_point_put

        
        """
        tapi_common_service_interface_point_ref = TapiCommonServiceInterfacePointRef()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/service-interface-point/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_common_service_interface_point_ref),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_exclude_linktopology_uuidlink_uuid_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_exclude_linktopology_uuidlink_uuid_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/exclude-link={topology-uuid},{link-uuid}/'.format(uuid='uuid_example', topology_uuid='topology_uuid_example', link_uuid='link_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_exclude_nodetopology_uuidnode_uuid_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_exclude_nodetopology_uuidnode_uuid_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/exclude-node={topology-uuid},{node-uuid}/'.format(uuid='uuid_example', topology_uuid='topology_uuid_example', node_uuid='node_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_exclude_pathpath_uuid_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_exclude_pathpath_uuid_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/exclude-path={path-uuid}/'.format(uuid='uuid_example', path_uuid='path_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_include_linktopology_uuidlink_uuid_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_include_linktopology_uuidlink_uuid_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/include-link={topology-uuid},{link-uuid}/'.format(uuid='uuid_example', topology_uuid='topology_uuid_example', link_uuid='link_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_include_nodetopology_uuidnode_uuid_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_include_nodetopology_uuidnode_uuid_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/include-node={topology-uuid},{node-uuid}/'.format(uuid='uuid_example', topology_uuid='topology_uuid_example', node_uuid='node_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_include_pathpath_uuid_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_include_pathpath_uuid_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/include-path={path-uuid}/'.format(uuid='uuid_example', path_uuid='path_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_include_topologytopology_uuid_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_include_topologytopology_uuid_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/include-topology={topology-uuid}/'.format(uuid='uuid_example', topology_uuid='topology_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_latency_characteristic_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_latency_characteristic_post

        
        """
        tapi_topology_latency_characteristic = TapiTopologyLatencyCharacteristic()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/latency-characteristic/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_topology_latency_characteristic),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_latency_characteristictraffic_property_name_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_latency_characteristictraffic_property_name_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/latency-characteristic={traffic-property-name}/'.format(uuid='uuid_example', traffic_property_name='traffic_property_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_latency_characteristictraffic_property_name_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_latency_characteristictraffic_property_name_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/latency-characteristic={traffic-property-name}/'.format(uuid='uuid_example', traffic_property_name='traffic_property_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_latency_characteristictraffic_property_name_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_latency_characteristictraffic_property_name_post

        
        """
        tapi_topology_latency_characteristic = TapiTopologyLatencyCharacteristic()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/latency-characteristic={traffic-property-name}/'.format(uuid='uuid_example', traffic_property_name='traffic_property_name_example'),
            method='POST',
            data=json.dumps(tapi_topology_latency_characteristic),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_latency_characteristictraffic_property_name_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_latency_characteristictraffic_property_name_put

        
        """
        tapi_topology_latency_characteristic = TapiTopologyLatencyCharacteristic()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/latency-characteristic={traffic-property-name}/'.format(uuid='uuid_example', traffic_property_name='traffic_property_name_example'),
            method='PUT',
            data=json.dumps(tapi_topology_latency_characteristic),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_name_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/name/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_namevalue_name_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_namevalue_name_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_namevalue_name_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_namevalue_name_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_namevalue_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_namevalue_name_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_namevalue_name_put

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='PUT',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_post

        
        """
        tapi_connectivity_connectivitycontext_connectivity_service = TapiConnectivityConnectivitycontextConnectivityService()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_connectivity_connectivitycontext_connectivity_service),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_put

        
        """
        tapi_connectivity_connectivitycontext_connectivity_service = TapiConnectivityConnectivitycontextConnectivityService()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(tapi_connectivity_connectivitycontext_connectivity_service),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_burst_size_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_burst_size_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/requested-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_burst_size_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_burst_size_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/requested-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_burst_size_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_burst_size_post

        
        """
        tapi_common_capacity_value = TapiCommonCapacityValue()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/requested-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_common_capacity_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_burst_size_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_burst_size_put

        
        """
        tapi_common_capacity_value = TapiCommonCapacityValue()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/requested-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(tapi_common_capacity_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_information_rate_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_information_rate_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/requested-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_information_rate_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_information_rate_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/requested-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_information_rate_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_information_rate_post

        
        """
        tapi_common_capacity_value = TapiCommonCapacityValue()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/requested-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_common_capacity_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_information_rate_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_information_rate_put

        
        """
        tapi_common_capacity_value = TapiCommonCapacityValue()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/requested-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(tapi_common_capacity_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/requested-capacity/bandwidth-profile/'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/requested-capacity/bandwidth-profile/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_burst_size_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_burst_size_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/requested-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_burst_size_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_burst_size_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/requested-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_burst_size_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_burst_size_post

        
        """
        tapi_common_capacity_value = TapiCommonCapacityValue()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/requested-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_common_capacity_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_burst_size_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_burst_size_put

        
        """
        tapi_common_capacity_value = TapiCommonCapacityValue()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/requested-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(tapi_common_capacity_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_information_rate_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_information_rate_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/requested-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_information_rate_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_information_rate_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/requested-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_information_rate_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_information_rate_post

        
        """
        tapi_common_capacity_value = TapiCommonCapacityValue()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/requested-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_common_capacity_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_information_rate_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_information_rate_put

        
        """
        tapi_common_capacity_value = TapiCommonCapacityValue()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/requested-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(tapi_common_capacity_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_post

        
        """
        tapi_common_bandwidth_profile = TapiCommonBandwidthProfile()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/requested-capacity/bandwidth-profile/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_common_bandwidth_profile),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_put

        
        """
        tapi_common_bandwidth_profile = TapiCommonBandwidthProfile()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/requested-capacity/bandwidth-profile/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(tapi_common_bandwidth_profile),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/requested-capacity/'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/requested-capacity/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_post

        
        """
        tapi_common_capacity = TapiCommonCapacity()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/requested-capacity/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_common_capacity),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_put

        
        """
        tapi_common_capacity = TapiCommonCapacity()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/requested-capacity/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(tapi_common_capacity),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_total_size_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_total_size_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/requested-capacity/total-size/'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_total_size_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_total_size_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/requested-capacity/total-size/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_total_size_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_total_size_post

        
        """
        tapi_common_capacity_value = TapiCommonCapacityValue()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/requested-capacity/total-size/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_common_capacity_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_total_size_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_total_size_put

        
        """
        tapi_common_capacity_value = TapiCommonCapacityValue()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/requested-capacity/total-size/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(tapi_common_capacity_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_resilience_type_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_resilience_type_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/resilience-type/'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_resilience_type_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_resilience_type_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/resilience-type/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_resilience_type_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_resilience_type_post

        
        """
        tapi_topology_resilience_type = TapiTopologyResilienceType()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/resilience-type/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_topology_resilience_type),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_resilience_type_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_resilience_type_put

        
        """
        tapi_topology_resilience_type = TapiTopologyResilienceType()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/resilience-type/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(tapi_topology_resilience_type),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_risk_diversity_characteristic_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_risk_diversity_characteristic_post

        
        """
        tapi_topology_risk_characteristic = TapiTopologyRiskCharacteristic()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/risk-diversity-characteristic/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_topology_risk_characteristic),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_risk_diversity_characteristicrisk_characteristic_name_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_risk_diversity_characteristicrisk_characteristic_name_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/risk-diversity-characteristic={risk-characteristic-name}/'.format(uuid='uuid_example', risk_characteristic_name='risk_characteristic_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_risk_diversity_characteristicrisk_characteristic_name_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_risk_diversity_characteristicrisk_characteristic_name_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/risk-diversity-characteristic={risk-characteristic-name}/'.format(uuid='uuid_example', risk_characteristic_name='risk_characteristic_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_risk_diversity_characteristicrisk_characteristic_name_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_risk_diversity_characteristicrisk_characteristic_name_post

        
        """
        tapi_topology_risk_characteristic = TapiTopologyRiskCharacteristic()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/risk-diversity-characteristic={risk-characteristic-name}/'.format(uuid='uuid_example', risk_characteristic_name='risk_characteristic_name_example'),
            method='POST',
            data=json.dumps(tapi_topology_risk_characteristic),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_risk_diversity_characteristicrisk_characteristic_name_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_risk_diversity_characteristicrisk_characteristic_name_put

        
        """
        tapi_topology_risk_characteristic = TapiTopologyRiskCharacteristic()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/risk-diversity-characteristic={risk-characteristic-name}/'.format(uuid='uuid_example', risk_characteristic_name='risk_characteristic_name_example'),
            method='PUT',
            data=json.dumps(tapi_topology_risk_characteristic),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_schedule_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_schedule_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/schedule/'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_schedule_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_schedule_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/schedule/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_schedule_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_schedule_post

        
        """
        tapi_common_time_range = TapiCommonTimeRange()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/schedule/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_common_time_range),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_schedule_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_schedule_put

        
        """
        tapi_common_time_range = TapiCommonTimeRange()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/schedule/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(tapi_common_time_range),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_delete(self):
        """Test case for data_context_connectivity_context_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_get(self):
        """Test case for data_context_connectivity_context_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_post(self):
        """Test case for data_context_connectivity_context_post

        
        """
        tapi_connectivity_connectivity_context = TapiConnectivityConnectivityContext()
        response = self.client.open(
            '/data/context/connectivity-context/',
            method='POST',
            data=json.dumps(tapi_connectivity_connectivity_context),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_put(self):
        """Test case for data_context_connectivity_context_put

        
        """
        tapi_connectivity_connectivity_context = TapiConnectivityConnectivityContext()
        response = self.client.open(
            '/data/context/connectivity-context/',
            method='PUT',
            data=json.dumps(tapi_connectivity_connectivity_context),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_aggregated_connection_end_pointtopology_uuidaggregated_connection_end_point_node_uuidnode_edge_point_uuidaggregated_connection_end_point_connection_end_point_uuid_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_aggregated_connection_end_pointtopology_uuidaggregated_connection_end_point_node_uuidnode_edge_point_uuidaggregated_connection_end_point_connection_end_point_uuid_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/aggregated-connection-end-point={topology-uuid},{aggregated-connection-end-point-node-uuid},{node-edge-point-uuid},{aggregated-connection-end-point-connection-end-point-uuid}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example', topology_uuid='topology_uuid_example', aggregated_connection_end_point_node_uuid='aggregated_connection_end_point_node_uuid_example', node_edge_point_uuid='node_edge_point_uuid_example', aggregated_connection_end_point_connection_end_point_uuid='aggregated_connection_end_point_connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_client_node_edge_pointtopology_uuidclient_node_edge_point_node_uuidnode_edge_point_uuid_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_client_node_edge_pointtopology_uuidclient_node_edge_point_node_uuidnode_edge_point_uuid_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/client-node-edge-point={topology-uuid},{client-node-edge-point-node-uuid},{node-edge-point-uuid}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example', topology_uuid='topology_uuid_example', client_node_edge_point_node_uuid='client_node_edge_point_node_uuid_example', node_edge_point_uuid='node_edge_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_namevalue_name_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/name={value-name}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_parent_node_edge_point_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_parent_node_edge_point_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/parent-node-edge-point/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_create_connectivity_service_post(self):
        """Test case for operations_create_connectivity_service_post

        
        """
        inline_object1 = InlineObject1()
        response = self.client.open(
            '/operations/create-connectivity-service/',
            method='POST',
            data=json.dumps(inline_object1),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_delete_connectivity_service_post(self):
        """Test case for operations_delete_connectivity_service_post

        
        """
        inline_object6 = InlineObject6()
        response = self.client.open(
            '/operations/delete-connectivity-service/',
            method='POST',
            data=json.dumps(inline_object6),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_get_connection_details_post(self):
        """Test case for operations_get_connection_details_post

        
        """
        inline_object12 = InlineObject12()
        response = self.client.open(
            '/operations/get-connection-details/',
            method='POST',
            data=json.dumps(inline_object12),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_get_connection_end_point_details_post(self):
        """Test case for operations_get_connection_end_point_details_post

        
        """
        inline_object13 = InlineObject13()
        response = self.client.open(
            '/operations/get-connection-end-point-details/',
            method='POST',
            data=json.dumps(inline_object13),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_get_connectivity_service_details_post(self):
        """Test case for operations_get_connectivity_service_details_post

        
        """
        inline_object14 = InlineObject14()
        response = self.client.open(
            '/operations/get-connectivity-service-details/',
            method='POST',
            data=json.dumps(inline_object14),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_get_connectivity_service_list_post(self):
        """Test case for operations_get_connectivity_service_list_post

        
        """
        response = self.client.open(
            '/operations/get-connectivity-service-list/',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_update_connectivity_service_post(self):
        """Test case for operations_update_connectivity_service_post

        
        """
        inline_object27 = InlineObject27()
        response = self.client.open(
            '/operations/update-connectivity-service/',
            method='POST',
            data=json.dumps(inline_object27),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
