# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from tapi_server.models.bandwidth_profile import BandwidthProfile  # noqa: E501
from tapi_server.models.capacity import Capacity  # noqa: E501
from tapi_server.models.capacity_pac import CapacityPac  # noqa: E501
from tapi_server.models.capacity_value import CapacityValue  # noqa: E501
from tapi_server.models.connection import Connection  # noqa: E501
from tapi_server.models.connection_end_point import ConnectionEndPoint  # noqa: E501
from tapi_server.models.connectivity_service import ConnectivityService  # noqa: E501
from tapi_server.models.connectivity_service_end_point import ConnectivityServiceEndPoint  # noqa: E501
from tapi_server.models.context_schema import ContextSchema  # noqa: E501
from tapi_server.models.cost_characteristic import CostCharacteristic  # noqa: E501
from tapi_server.models.create_connectivity_service_rpc_input_schema import CreateConnectivityServiceRPCInputSchema  # noqa: E501
from tapi_server.models.create_connectivity_service_rpc_output_schema import CreateConnectivityServiceRPCOutputSchema  # noqa: E501
from tapi_server.models.delete_connectivity_service_rpc_input_schema import DeleteConnectivityServiceRPCInputSchema  # noqa: E501
from tapi_server.models.delete_connectivity_service_rpc_output_schema import DeleteConnectivityServiceRPCOutputSchema  # noqa: E501
from tapi_server.models.get_connection_details_rpc_input_schema import GetConnectionDetailsRPCInputSchema  # noqa: E501
from tapi_server.models.get_connection_details_rpc_output_schema import GetConnectionDetailsRPCOutputSchema  # noqa: E501
from tapi_server.models.get_connectivity_service_details_rpc_input_schema import GetConnectivityServiceDetailsRPCInputSchema  # noqa: E501
from tapi_server.models.get_connectivity_service_details_rpc_output_schema import GetConnectivityServiceDetailsRPCOutputSchema  # noqa: E501
from tapi_server.models.get_connectivity_service_list_rpc_output_schema import GetConnectivityServiceListRPCOutputSchema  # noqa: E501
from tapi_server.models.inter_rule_group import InterRuleGroup  # noqa: E501
from tapi_server.models.latency_characteristic import LatencyCharacteristic  # noqa: E501
from tapi_server.models.link import Link  # noqa: E501
from tapi_server.models.name_and_value import NameAndValue  # noqa: E501
from tapi_server.models.network_topology_service import NetworkTopologyService  # noqa: E501
from tapi_server.models.node import Node  # noqa: E501
from tapi_server.models.node_rule_group import NodeRuleGroup  # noqa: E501
from tapi_server.models.owned_node_edge_point_schema import OwnedNodeEdgePointSchema  # noqa: E501
from tapi_server.models.path import Path  # noqa: E501
from tapi_server.models.path_computation_service import PathComputationService  # noqa: E501
from tapi_server.models.path_objective_function import PathObjectiveFunction  # noqa: E501
from tapi_server.models.path_optimization_constraint import PathOptimizationConstraint  # noqa: E501
from tapi_server.models.path_service_end_point import PathServiceEndPoint  # noqa: E501
from tapi_server.models.resilience_type import ResilienceType  # noqa: E501
from tapi_server.models.risk_characteristic import RiskCharacteristic  # noqa: E501
from tapi_server.models.route import Route  # noqa: E501
from tapi_server.models.routing_constraint import RoutingConstraint  # noqa: E501
from tapi_server.models.rule import Rule  # noqa: E501
from tapi_server.models.service_interface_point import ServiceInterfacePoint  # noqa: E501
from tapi_server.models.switch import Switch  # noqa: E501
from tapi_server.models.switch_control import SwitchControl  # noqa: E501
from tapi_server.models.time_range import TimeRange  # noqa: E501
from tapi_server.models.topology import Topology  # noqa: E501
from tapi_server.models.update_connectivity_service_rpc_input_schema import UpdateConnectivityServiceRPCInputSchema  # noqa: E501
from tapi_server.models.update_connectivity_service_rpc_output_schema import UpdateConnectivityServiceRPCOutputSchema  # noqa: E501
from tapi_server.models.validation_mechanism import ValidationMechanism  # noqa: E501
from tapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_create_context_by_id(self):
        """Test case for create_context_by_id

        Create context by ID
        """
        context = ContextSchema()
        response = self.client.open(
            '/restconf/config/context/',
            method='POST',
            data=json.dumps(context),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_context_connectivity_service_connectivity_service_by_id(self):
        """Test case for create_context_connectivity_service_connectivity_service_by_id

        Create connectivity-service by ID
        """
        connectivity_service = ConnectivityService()
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(connectivity_service),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_context_connectivity_service_end_point_capacity_capacity_by_id(self):
        """Test case for create_context_connectivity_service_end_point_capacity_capacity_by_id

        Create capacity by ID
        """
        capacity = CapacityPac()
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/end-point/{local_id}/capacity/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(capacity),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_context_connectivity_service_end_point_end_point_by_id(self):
        """Test case for create_context_connectivity_service_end_point_end_point_by_id

        Create end-point by ID
        """
        end_point = ConnectivityServiceEndPoint()
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/end-point/{local_id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(end_point),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_context_connectivity_service_end_point_name_name_by_id(self):
        """Test case for create_context_connectivity_service_end_point_name_name_by_id

        Create name by ID
        """
        name = NameAndValue()
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/end-point/{local_id}/name/{value_name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='POST',
            data=json.dumps(name),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_context_connectivity_service_name_name_by_id(self):
        """Test case for create_context_connectivity_service_name_name_by_id

        Create name by ID
        """
        name = NameAndValue()
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/name/{value_name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='POST',
            data=json.dumps(name),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_context_connectivity_service_resilience_type_resilience_type_by_id(self):
        """Test case for create_context_connectivity_service_resilience_type_resilience_type_by_id

        Create resilience-type by ID
        """
        resilience_type = ResilienceType()
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/resilience-type/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(resilience_type),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_context_connectivity_service_schedule_schedule_by_id(self):
        """Test case for create_context_connectivity_service_schedule_schedule_by_id

        Create schedule by ID
        """
        schedule = TimeRange()
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/schedule/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(schedule),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_context_name_name_by_id(self):
        """Test case for create_context_name_name_by_id

        Create name by ID
        """
        name = NameAndValue()
        response = self.client.open(
            '/restconf/config/context/name/{value_name}/'.format(value_name='value_name_example'),
            method='POST',
            data=json.dumps(name),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_context_path_comp_service_end_point_end_point_by_id(self):
        """Test case for create_context_path_comp_service_end_point_end_point_by_id

        Create end-point by ID
        """
        end_point = PathServiceEndPoint()
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/end-point/{local_id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(end_point),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_context_path_comp_service_end_point_name_name_by_id(self):
        """Test case for create_context_path_comp_service_end_point_name_name_by_id

        Create name by ID
        """
        name = NameAndValue()
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/end-point/{local_id}/name/{value_name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='POST',
            data=json.dumps(name),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_context_path_comp_service_name_name_by_id(self):
        """Test case for create_context_path_comp_service_name_name_by_id

        Create name by ID
        """
        name = NameAndValue()
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/name/{value_name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='POST',
            data=json.dumps(name),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_context_path_comp_service_objective_function_name_name_by_id(self):
        """Test case for create_context_path_comp_service_objective_function_name_name_by_id

        Create name by ID
        """
        name = NameAndValue()
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/objective-function/name/{value_name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='POST',
            data=json.dumps(name),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_context_path_comp_service_objective_function_objective_function_by_id(self):
        """Test case for create_context_path_comp_service_objective_function_objective_function_by_id

        Create objective-function by ID
        """
        objective_function = PathObjectiveFunction()
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/objective-function/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(objective_function),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_context_path_comp_service_optimization_constraint_name_name_by_id(self):
        """Test case for create_context_path_comp_service_optimization_constraint_name_name_by_id

        Create name by ID
        """
        name = NameAndValue()
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/optimization-constraint/name/{value_name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='POST',
            data=json.dumps(name),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_context_path_comp_service_optimization_constraint_optimization_constraint_by_id(self):
        """Test case for create_context_path_comp_service_optimization_constraint_optimization_constraint_by_id

        Create optimization-constraint by ID
        """
        optimization_constraint = PathOptimizationConstraint()
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/optimization-constraint/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(optimization_constraint),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_context_path_comp_service_path_comp_service_by_id(self):
        """Test case for create_context_path_comp_service_path_comp_service_by_id

        Create path-comp-service by ID
        """
        path_comp_service = PathComputationService()
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(path_comp_service),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_context_path_comp_service_routing_constraint_name_name_by_id(self):
        """Test case for create_context_path_comp_service_routing_constraint_name_name_by_id

        Create name by ID
        """
        name = NameAndValue()
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/routing-constraint/name/{value_name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='POST',
            data=json.dumps(name),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_context_path_comp_service_routing_constraint_routing_constraint_by_id(self):
        """Test case for create_context_path_comp_service_routing_constraint_routing_constraint_by_id

        Create routing-constraint by ID
        """
        routing_constraint = RoutingConstraint()
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/routing-constraint/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(routing_constraint),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_context_service_interface_point_name_name_by_id(self):
        """Test case for create_context_service_interface_point_name_name_by_id

        Create name by ID
        """
        name = NameAndValue()
        response = self.client.open(
            '/restconf/config/context/service-interface-point/{uuid}/name/{value_name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='POST',
            data=json.dumps(name),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_context_service_interface_point_service_interface_point_by_id(self):
        """Test case for create_context_service_interface_point_service_interface_point_by_id

        Create service-interface-point by ID
        """
        service_interface_point = ServiceInterfacePoint()
        response = self.client.open(
            '/restconf/config/context/service-interface-point/{uuid}/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(service_interface_point),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_create_connectivity_service_by_id(self):
        """Test case for create_create_connectivity_service_by_id

        Create create-connectivity-service by ID
        """
        create_connectivity_service = CreateConnectivityServiceRPCInputSchema()
        response = self.client.open(
            '/restconf/operations/create-connectivity-service/',
            method='POST',
            data=json.dumps(create_connectivity_service),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_delete_connectivity_service_by_id(self):
        """Test case for create_delete_connectivity_service_by_id

        Create delete-connectivity-service by ID
        """
        delete_connectivity_service = DeleteConnectivityServiceRPCInputSchema()
        response = self.client.open(
            '/restconf/operations/delete-connectivity-service/',
            method='POST',
            data=json.dumps(delete_connectivity_service),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_get_connection_details_by_id(self):
        """Test case for create_get_connection_details_by_id

        Create get-connection-details by ID
        """
        get_connection_details = GetConnectionDetailsRPCInputSchema()
        response = self.client.open(
            '/restconf/operations/get-connection-details/',
            method='POST',
            data=json.dumps(get_connection_details),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_get_connectivity_service_details_by_id(self):
        """Test case for create_get_connectivity_service_details_by_id

        Create get-connectivity-service-details by ID
        """
        get_connectivity_service_details = GetConnectivityServiceDetailsRPCInputSchema()
        response = self.client.open(
            '/restconf/operations/get-connectivity-service-details/',
            method='POST',
            data=json.dumps(get_connectivity_service_details),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_get_connectivity_service_list_by_id(self):
        """Test case for create_get_connectivity_service_list_by_id

        Create get-connectivity-service-list by ID
        """
        response = self.client.open(
            '/restconf/operations/get-connectivity-service-list/',
            method='POST',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_update_connectivity_service_by_id(self):
        """Test case for create_update_connectivity_service_by_id

        Create update-connectivity-service by ID
        """
        update_connectivity_service = UpdateConnectivityServiceRPCInputSchema()
        response = self.client.open(
            '/restconf/operations/update-connectivity-service/',
            method='POST',
            data=json.dumps(update_connectivity_service),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_context_by_id(self):
        """Test case for delete_context_by_id

        Delete context by ID
        """
        response = self.client.open(
            '/restconf/config/context/',
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_context_connectivity_service_connectivity_service_by_id(self):
        """Test case for delete_context_connectivity_service_connectivity_service_by_id

        Delete connectivity-service by ID
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/'.format(uuid='uuid_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_context_connectivity_service_end_point_capacity_capacity_by_id(self):
        """Test case for delete_context_connectivity_service_end_point_capacity_capacity_by_id

        Delete capacity by ID
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/end-point/{local_id}/capacity/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_context_connectivity_service_end_point_end_point_by_id(self):
        """Test case for delete_context_connectivity_service_end_point_end_point_by_id

        Delete end-point by ID
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/end-point/{local_id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_context_connectivity_service_end_point_name_name_by_id(self):
        """Test case for delete_context_connectivity_service_end_point_name_name_by_id

        Delete name by ID
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/end-point/{local_id}/name/{value_name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_context_connectivity_service_name_name_by_id(self):
        """Test case for delete_context_connectivity_service_name_name_by_id

        Delete name by ID
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/name/{value_name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_context_connectivity_service_resilience_type_resilience_type_by_id(self):
        """Test case for delete_context_connectivity_service_resilience_type_resilience_type_by_id

        Delete resilience-type by ID
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/resilience-type/'.format(uuid='uuid_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_context_connectivity_service_schedule_schedule_by_id(self):
        """Test case for delete_context_connectivity_service_schedule_schedule_by_id

        Delete schedule by ID
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/schedule/'.format(uuid='uuid_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_context_name_name_by_id(self):
        """Test case for delete_context_name_name_by_id

        Delete name by ID
        """
        response = self.client.open(
            '/restconf/config/context/name/{value_name}/'.format(value_name='value_name_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_context_path_comp_service_end_point_end_point_by_id(self):
        """Test case for delete_context_path_comp_service_end_point_end_point_by_id

        Delete end-point by ID
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/end-point/{local_id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_context_path_comp_service_end_point_name_name_by_id(self):
        """Test case for delete_context_path_comp_service_end_point_name_name_by_id

        Delete name by ID
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/end-point/{local_id}/name/{value_name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_context_path_comp_service_name_name_by_id(self):
        """Test case for delete_context_path_comp_service_name_name_by_id

        Delete name by ID
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/name/{value_name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_context_path_comp_service_objective_function_name_name_by_id(self):
        """Test case for delete_context_path_comp_service_objective_function_name_name_by_id

        Delete name by ID
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/objective-function/name/{value_name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_context_path_comp_service_objective_function_objective_function_by_id(self):
        """Test case for delete_context_path_comp_service_objective_function_objective_function_by_id

        Delete objective-function by ID
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/objective-function/'.format(uuid='uuid_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_context_path_comp_service_optimization_constraint_name_name_by_id(self):
        """Test case for delete_context_path_comp_service_optimization_constraint_name_name_by_id

        Delete name by ID
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/optimization-constraint/name/{value_name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_context_path_comp_service_optimization_constraint_optimization_constraint_by_id(self):
        """Test case for delete_context_path_comp_service_optimization_constraint_optimization_constraint_by_id

        Delete optimization-constraint by ID
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/optimization-constraint/'.format(uuid='uuid_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_context_path_comp_service_path_comp_service_by_id(self):
        """Test case for delete_context_path_comp_service_path_comp_service_by_id

        Delete path-comp-service by ID
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/'.format(uuid='uuid_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_context_path_comp_service_routing_constraint_name_name_by_id(self):
        """Test case for delete_context_path_comp_service_routing_constraint_name_name_by_id

        Delete name by ID
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/routing-constraint/name/{value_name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_context_path_comp_service_routing_constraint_routing_constraint_by_id(self):
        """Test case for delete_context_path_comp_service_routing_constraint_routing_constraint_by_id

        Delete routing-constraint by ID
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/routing-constraint/'.format(uuid='uuid_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_context_service_interface_point_name_name_by_id(self):
        """Test case for delete_context_service_interface_point_name_name_by_id

        Delete name by ID
        """
        response = self.client.open(
            '/restconf/config/context/service-interface-point/{uuid}/name/{value_name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_context_service_interface_point_service_interface_point_by_id(self):
        """Test case for delete_context_service_interface_point_service_interface_point_by_id

        Delete service-interface-point by ID
        """
        response = self.client.open(
            '/restconf/config/context/service-interface-point/{uuid}/'.format(uuid='uuid_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context(self):
        """Test case for retrieve_context

        Retrieve context
        """
        response = self.client.open(
            '/restconf/config/context/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connection_connection(self):
        """Test case for retrieve_context_connection_connection

        Retrieve connection
        """
        response = self.client.open(
            '/restconf/config/context/connection/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connection_connection_by_id(self):
        """Test case for retrieve_context_connection_connection_by_id

        Retrieve connection by ID
        """
        response = self.client.open(
            '/restconf/config/context/connection/{uuid}/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connection_name_name(self):
        """Test case for retrieve_context_connection_name_name

        Retrieve name
        """
        response = self.client.open(
            '/restconf/config/context/connection/{uuid}/name/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connection_name_name_by_id(self):
        """Test case for retrieve_context_connection_name_name_by_id

        Retrieve name by ID
        """
        response = self.client.open(
            '/restconf/config/context/connection/{uuid}/name/{value_name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connection_route_name_name(self):
        """Test case for retrieve_context_connection_route_name_name

        Retrieve name
        """
        response = self.client.open(
            '/restconf/config/context/connection/{uuid}/route/{local_id}/name/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connection_route_name_name_by_id(self):
        """Test case for retrieve_context_connection_route_name_name_by_id

        Retrieve name by ID
        """
        response = self.client.open(
            '/restconf/config/context/connection/{uuid}/route/{local_id}/name/{value_name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connection_route_route(self):
        """Test case for retrieve_context_connection_route_route

        Retrieve route
        """
        response = self.client.open(
            '/restconf/config/context/connection/{uuid}/route/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connection_route_route_by_id(self):
        """Test case for retrieve_context_connection_route_route_by_id

        Retrieve route by ID
        """
        response = self.client.open(
            '/restconf/config/context/connection/{uuid}/route/{local_id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connection_switch_control_name_name(self):
        """Test case for retrieve_context_connection_switch_control_name_name

        Retrieve name
        """
        response = self.client.open(
            '/restconf/config/context/connection/{uuid}/switch-control/{local_id}/name/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connection_switch_control_name_name_by_id(self):
        """Test case for retrieve_context_connection_switch_control_name_name_by_id

        Retrieve name by ID
        """
        response = self.client.open(
            '/restconf/config/context/connection/{uuid}/switch-control/{local_id}/name/{value_name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connection_switch_control_resilience_type_resilience_type(self):
        """Test case for retrieve_context_connection_switch_control_resilience_type_resilience_type

        Retrieve resilience-type
        """
        response = self.client.open(
            '/restconf/config/context/connection/{uuid}/switch-control/{local_id}/resilience-type/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connection_switch_control_switch_control(self):
        """Test case for retrieve_context_connection_switch_control_switch_control

        Retrieve switch-control
        """
        response = self.client.open(
            '/restconf/config/context/connection/{uuid}/switch-control/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connection_switch_control_switch_control_by_id(self):
        """Test case for retrieve_context_connection_switch_control_switch_control_by_id

        Retrieve switch-control by ID
        """
        response = self.client.open(
            '/restconf/config/context/connection/{uuid}/switch-control/{local_id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connection_switch_control_switch_name_name(self):
        """Test case for retrieve_context_connection_switch_control_switch_name_name

        Retrieve name
        """
        response = self.client.open(
            '/restconf/config/context/connection/{uuid}/switch-control/{local_id}/switch/{local2_id}/name/'.format(uuid='uuid_example', local_id='local_id_example', local2_id='local2_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connection_switch_control_switch_name_name_by_id(self):
        """Test case for retrieve_context_connection_switch_control_switch_name_name_by_id

        Retrieve name by ID
        """
        response = self.client.open(
            '/restconf/config/context/connection/{uuid}/switch-control/{local_id}/switch/{local2_id}/name/{value_name}/'.format(uuid='uuid_example', local_id='local_id_example', local2_id='local2_id_example', value_name='value_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connection_switch_control_switch_switch(self):
        """Test case for retrieve_context_connection_switch_control_switch_switch

        Retrieve switch
        """
        response = self.client.open(
            '/restconf/config/context/connection/{uuid}/switch-control/{local_id}/switch/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connection_switch_control_switch_switch_by_id(self):
        """Test case for retrieve_context_connection_switch_control_switch_switch_by_id

        Retrieve switch by ID
        """
        response = self.client.open(
            '/restconf/config/context/connection/{uuid}/switch-control/{local_id}/switch/{local2_id}/'.format(uuid='uuid_example', local_id='local_id_example', local2_id='local2_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_connectivity_service(self):
        """Test case for retrieve_context_connectivity_service_connectivity_service

        Retrieve connectivity-service
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_connectivity_service_by_id(self):
        """Test case for retrieve_context_connectivity_service_connectivity_service_by_id

        Retrieve connectivity-service by ID
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_cost_characteristic_cost_characteristic(self):
        """Test case for retrieve_context_connectivity_service_cost_characteristic_cost_characteristic

        Retrieve cost-characteristic
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/cost-characteristic/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_cost_characteristic_cost_characteristic_by_id(self):
        """Test case for retrieve_context_connectivity_service_cost_characteristic_cost_characteristic_by_id

        Retrieve cost-characteristic by ID
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/cost-characteristic/{cost_name}/'.format(uuid='uuid_example', cost_name='cost_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_end_point_capacity_available_capacity_available_capacity(self):
        """Test case for retrieve_context_connectivity_service_end_point_capacity_available_capacity_available_capacity

        Retrieve available-capacity
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/end-point/{local_id}/capacity/available-capacity/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_end_point_capacity_available_capacity_bandwidth_profile_bandwidth_profile(self):
        """Test case for retrieve_context_connectivity_service_end_point_capacity_available_capacity_bandwidth_profile_bandwidth_profile

        Retrieve bandwidth-profile
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/end-point/{local_id}/capacity/available-capacity/bandwidth-profile/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_end_point_capacity_available_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(self):
        """Test case for retrieve_context_connectivity_service_end_point_capacity_available_capacity_bandwidth_profile_committed_burst_size_committed_burst_size

        Retrieve committed-burst-size
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/end-point/{local_id}/capacity/available-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_end_point_capacity_available_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(self):
        """Test case for retrieve_context_connectivity_service_end_point_capacity_available_capacity_bandwidth_profile_committed_information_rate_committed_information_rate

        Retrieve committed-information-rate
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/end-point/{local_id}/capacity/available-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_end_point_capacity_available_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(self):
        """Test case for retrieve_context_connectivity_service_end_point_capacity_available_capacity_bandwidth_profile_peak_burst_size_peak_burst_size

        Retrieve peak-burst-size
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/end-point/{local_id}/capacity/available-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_end_point_capacity_available_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(self):
        """Test case for retrieve_context_connectivity_service_end_point_capacity_available_capacity_bandwidth_profile_peak_information_rate_peak_information_rate

        Retrieve peak-information-rate
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/end-point/{local_id}/capacity/available-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_end_point_capacity_available_capacity_total_size_total_size(self):
        """Test case for retrieve_context_connectivity_service_end_point_capacity_available_capacity_total_size_total_size

        Retrieve total-size
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/end-point/{local_id}/capacity/available-capacity/total-size/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_end_point_capacity_capacity(self):
        """Test case for retrieve_context_connectivity_service_end_point_capacity_capacity

        Retrieve capacity
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/end-point/{local_id}/capacity/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_end_point_capacity_total_potential_capacity_bandwidth_profile_bandwidth_profile(self):
        """Test case for retrieve_context_connectivity_service_end_point_capacity_total_potential_capacity_bandwidth_profile_bandwidth_profile

        Retrieve bandwidth-profile
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/end-point/{local_id}/capacity/total-potential-capacity/bandwidth-profile/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_end_point_capacity_total_potential_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(self):
        """Test case for retrieve_context_connectivity_service_end_point_capacity_total_potential_capacity_bandwidth_profile_committed_burst_size_committed_burst_size

        Retrieve committed-burst-size
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/end-point/{local_id}/capacity/total-potential-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_end_point_capacity_total_potential_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(self):
        """Test case for retrieve_context_connectivity_service_end_point_capacity_total_potential_capacity_bandwidth_profile_committed_information_rate_committed_information_rate

        Retrieve committed-information-rate
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/end-point/{local_id}/capacity/total-potential-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_end_point_capacity_total_potential_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(self):
        """Test case for retrieve_context_connectivity_service_end_point_capacity_total_potential_capacity_bandwidth_profile_peak_burst_size_peak_burst_size

        Retrieve peak-burst-size
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/end-point/{local_id}/capacity/total-potential-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_end_point_capacity_total_potential_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(self):
        """Test case for retrieve_context_connectivity_service_end_point_capacity_total_potential_capacity_bandwidth_profile_peak_information_rate_peak_information_rate

        Retrieve peak-information-rate
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/end-point/{local_id}/capacity/total-potential-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_end_point_capacity_total_potential_capacity_total_potential_capacity(self):
        """Test case for retrieve_context_connectivity_service_end_point_capacity_total_potential_capacity_total_potential_capacity

        Retrieve total-potential-capacity
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/end-point/{local_id}/capacity/total-potential-capacity/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_end_point_capacity_total_potential_capacity_total_size_total_size(self):
        """Test case for retrieve_context_connectivity_service_end_point_capacity_total_potential_capacity_total_size_total_size

        Retrieve total-size
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/end-point/{local_id}/capacity/total-potential-capacity/total-size/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_end_point_end_point(self):
        """Test case for retrieve_context_connectivity_service_end_point_end_point

        Retrieve end-point
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/end-point/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_end_point_end_point_by_id(self):
        """Test case for retrieve_context_connectivity_service_end_point_end_point_by_id

        Retrieve end-point by ID
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/end-point/{local_id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_end_point_name_name(self):
        """Test case for retrieve_context_connectivity_service_end_point_name_name

        Retrieve name
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/end-point/{local_id}/name/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_end_point_name_name_by_id(self):
        """Test case for retrieve_context_connectivity_service_end_point_name_name_by_id

        Retrieve name by ID
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/end-point/{local_id}/name/{value_name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_latency_characteristic_latency_characteristic(self):
        """Test case for retrieve_context_connectivity_service_latency_characteristic_latency_characteristic

        Retrieve latency-characteristic
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/latency-characteristic/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_latency_characteristic_latency_characteristic_by_id(self):
        """Test case for retrieve_context_connectivity_service_latency_characteristic_latency_characteristic_by_id

        Retrieve latency-characteristic by ID
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/latency-characteristic/{traffic_property_name}/'.format(uuid='uuid_example', traffic_property_name='traffic_property_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_name_name(self):
        """Test case for retrieve_context_connectivity_service_name_name

        Retrieve name
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/name/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_name_name_by_id(self):
        """Test case for retrieve_context_connectivity_service_name_name_by_id

        Retrieve name by ID
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/name/{value_name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_requested_capacity_bandwidth_profile_bandwidth_profile(self):
        """Test case for retrieve_context_connectivity_service_requested_capacity_bandwidth_profile_bandwidth_profile

        Retrieve bandwidth-profile
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/requested-capacity/bandwidth-profile/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_requested_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(self):
        """Test case for retrieve_context_connectivity_service_requested_capacity_bandwidth_profile_committed_burst_size_committed_burst_size

        Retrieve committed-burst-size
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/requested-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_requested_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(self):
        """Test case for retrieve_context_connectivity_service_requested_capacity_bandwidth_profile_committed_information_rate_committed_information_rate

        Retrieve committed-information-rate
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/requested-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_requested_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(self):
        """Test case for retrieve_context_connectivity_service_requested_capacity_bandwidth_profile_peak_burst_size_peak_burst_size

        Retrieve peak-burst-size
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/requested-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_requested_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(self):
        """Test case for retrieve_context_connectivity_service_requested_capacity_bandwidth_profile_peak_information_rate_peak_information_rate

        Retrieve peak-information-rate
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/requested-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_requested_capacity_requested_capacity(self):
        """Test case for retrieve_context_connectivity_service_requested_capacity_requested_capacity

        Retrieve requested-capacity
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/requested-capacity/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_requested_capacity_total_size_total_size(self):
        """Test case for retrieve_context_connectivity_service_requested_capacity_total_size_total_size

        Retrieve total-size
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/requested-capacity/total-size/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_resilience_type_resilience_type(self):
        """Test case for retrieve_context_connectivity_service_resilience_type_resilience_type

        Retrieve resilience-type
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/resilience-type/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_connectivity_service_schedule_schedule(self):
        """Test case for retrieve_context_connectivity_service_schedule_schedule

        Retrieve schedule
        """
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/schedule/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_name_name(self):
        """Test case for retrieve_context_name_name

        Retrieve name
        """
        response = self.client.open(
            '/restconf/config/context/name/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_name_name_by_id(self):
        """Test case for retrieve_context_name_name_by_id

        Retrieve name by ID
        """
        response = self.client.open(
            '/restconf/config/context/name/{value_name}/'.format(value_name='value_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_nw_topology_service_name_name(self):
        """Test case for retrieve_context_nw_topology_service_name_name

        Retrieve name
        """
        response = self.client.open(
            '/restconf/config/context/nw-topology-service/name/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_nw_topology_service_name_name_by_id(self):
        """Test case for retrieve_context_nw_topology_service_name_name_by_id

        Retrieve name by ID
        """
        response = self.client.open(
            '/restconf/config/context/nw-topology-service/name/{value_name}/'.format(value_name='value_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_nw_topology_service_nw_topology_service(self):
        """Test case for retrieve_context_nw_topology_service_nw_topology_service

        Retrieve nw-topology-service
        """
        response = self.client.open(
            '/restconf/config/context/nw-topology-service/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_comp_service_end_point_end_point(self):
        """Test case for retrieve_context_path_comp_service_end_point_end_point

        Retrieve end-point
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/end-point/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_comp_service_end_point_end_point_by_id(self):
        """Test case for retrieve_context_path_comp_service_end_point_end_point_by_id

        Retrieve end-point by ID
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/end-point/{local_id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_comp_service_end_point_name_name(self):
        """Test case for retrieve_context_path_comp_service_end_point_name_name

        Retrieve name
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/end-point/{local_id}/name/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_comp_service_end_point_name_name_by_id(self):
        """Test case for retrieve_context_path_comp_service_end_point_name_name_by_id

        Retrieve name by ID
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/end-point/{local_id}/name/{value_name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_comp_service_name_name(self):
        """Test case for retrieve_context_path_comp_service_name_name

        Retrieve name
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/name/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_comp_service_name_name_by_id(self):
        """Test case for retrieve_context_path_comp_service_name_name_by_id

        Retrieve name by ID
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/name/{value_name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_comp_service_objective_function_name_name(self):
        """Test case for retrieve_context_path_comp_service_objective_function_name_name

        Retrieve name
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/objective-function/name/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_comp_service_objective_function_name_name_by_id(self):
        """Test case for retrieve_context_path_comp_service_objective_function_name_name_by_id

        Retrieve name by ID
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/objective-function/name/{value_name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_comp_service_objective_function_objective_function(self):
        """Test case for retrieve_context_path_comp_service_objective_function_objective_function

        Retrieve objective-function
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/objective-function/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_comp_service_optimization_constraint_name_name(self):
        """Test case for retrieve_context_path_comp_service_optimization_constraint_name_name

        Retrieve name
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/optimization-constraint/name/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_comp_service_optimization_constraint_name_name_by_id(self):
        """Test case for retrieve_context_path_comp_service_optimization_constraint_name_name_by_id

        Retrieve name by ID
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/optimization-constraint/name/{value_name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_comp_service_optimization_constraint_optimization_constraint(self):
        """Test case for retrieve_context_path_comp_service_optimization_constraint_optimization_constraint

        Retrieve optimization-constraint
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/optimization-constraint/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_comp_service_path_comp_service(self):
        """Test case for retrieve_context_path_comp_service_path_comp_service

        Retrieve path-comp-service
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_comp_service_path_comp_service_by_id(self):
        """Test case for retrieve_context_path_comp_service_path_comp_service_by_id

        Retrieve path-comp-service by ID
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_comp_service_routing_constraint_cost_characteristic_cost_characteristic(self):
        """Test case for retrieve_context_path_comp_service_routing_constraint_cost_characteristic_cost_characteristic

        Retrieve cost-characteristic
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/routing-constraint/cost-characteristic/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_comp_service_routing_constraint_cost_characteristic_cost_characteristic_by_id(self):
        """Test case for retrieve_context_path_comp_service_routing_constraint_cost_characteristic_cost_characteristic_by_id

        Retrieve cost-characteristic by ID
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/routing-constraint/cost-characteristic/{cost_name}/'.format(uuid='uuid_example', cost_name='cost_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_comp_service_routing_constraint_latency_characteristic_latency_characteristic(self):
        """Test case for retrieve_context_path_comp_service_routing_constraint_latency_characteristic_latency_characteristic

        Retrieve latency-characteristic
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/routing-constraint/latency-characteristic/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_comp_service_routing_constraint_latency_characteristic_latency_characteristic_by_id(self):
        """Test case for retrieve_context_path_comp_service_routing_constraint_latency_characteristic_latency_characteristic_by_id

        Retrieve latency-characteristic by ID
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/routing-constraint/latency-characteristic/{traffic_property_name}/'.format(uuid='uuid_example', traffic_property_name='traffic_property_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_comp_service_routing_constraint_name_name(self):
        """Test case for retrieve_context_path_comp_service_routing_constraint_name_name

        Retrieve name
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/routing-constraint/name/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_comp_service_routing_constraint_name_name_by_id(self):
        """Test case for retrieve_context_path_comp_service_routing_constraint_name_name_by_id

        Retrieve name by ID
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/routing-constraint/name/{value_name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_comp_service_routing_constraint_requested_capacity_bandwidth_profile_bandwidth_profile(self):
        """Test case for retrieve_context_path_comp_service_routing_constraint_requested_capacity_bandwidth_profile_bandwidth_profile

        Retrieve bandwidth-profile
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/routing-constraint/requested-capacity/bandwidth-profile/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_comp_service_routing_constraint_requested_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(self):
        """Test case for retrieve_context_path_comp_service_routing_constraint_requested_capacity_bandwidth_profile_committed_burst_size_committed_burst_size

        Retrieve committed-burst-size
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/routing-constraint/requested-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_comp_service_routing_constraint_requested_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(self):
        """Test case for retrieve_context_path_comp_service_routing_constraint_requested_capacity_bandwidth_profile_committed_information_rate_committed_information_rate

        Retrieve committed-information-rate
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/routing-constraint/requested-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_comp_service_routing_constraint_requested_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(self):
        """Test case for retrieve_context_path_comp_service_routing_constraint_requested_capacity_bandwidth_profile_peak_burst_size_peak_burst_size

        Retrieve peak-burst-size
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/routing-constraint/requested-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_comp_service_routing_constraint_requested_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(self):
        """Test case for retrieve_context_path_comp_service_routing_constraint_requested_capacity_bandwidth_profile_peak_information_rate_peak_information_rate

        Retrieve peak-information-rate
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/routing-constraint/requested-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_comp_service_routing_constraint_requested_capacity_requested_capacity(self):
        """Test case for retrieve_context_path_comp_service_routing_constraint_requested_capacity_requested_capacity

        Retrieve requested-capacity
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/routing-constraint/requested-capacity/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_comp_service_routing_constraint_requested_capacity_total_size_total_size(self):
        """Test case for retrieve_context_path_comp_service_routing_constraint_requested_capacity_total_size_total_size

        Retrieve total-size
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/routing-constraint/requested-capacity/total-size/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_comp_service_routing_constraint_routing_constraint(self):
        """Test case for retrieve_context_path_comp_service_routing_constraint_routing_constraint

        Retrieve routing-constraint
        """
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/routing-constraint/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_name_name(self):
        """Test case for retrieve_context_path_name_name

        Retrieve name
        """
        response = self.client.open(
            '/restconf/config/context/path/{uuid}/name/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_name_name_by_id(self):
        """Test case for retrieve_context_path_name_name_by_id

        Retrieve name by ID
        """
        response = self.client.open(
            '/restconf/config/context/path/{uuid}/name/{value_name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_path(self):
        """Test case for retrieve_context_path_path

        Retrieve path
        """
        response = self.client.open(
            '/restconf/config/context/path/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_path_by_id(self):
        """Test case for retrieve_context_path_path_by_id

        Retrieve path by ID
        """
        response = self.client.open(
            '/restconf/config/context/path/{uuid}/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_routing_constraint_cost_characteristic_cost_characteristic(self):
        """Test case for retrieve_context_path_routing_constraint_cost_characteristic_cost_characteristic

        Retrieve cost-characteristic
        """
        response = self.client.open(
            '/restconf/config/context/path/{uuid}/routing-constraint/cost-characteristic/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_routing_constraint_cost_characteristic_cost_characteristic_by_id(self):
        """Test case for retrieve_context_path_routing_constraint_cost_characteristic_cost_characteristic_by_id

        Retrieve cost-characteristic by ID
        """
        response = self.client.open(
            '/restconf/config/context/path/{uuid}/routing-constraint/cost-characteristic/{cost_name}/'.format(uuid='uuid_example', cost_name='cost_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_routing_constraint_latency_characteristic_latency_characteristic(self):
        """Test case for retrieve_context_path_routing_constraint_latency_characteristic_latency_characteristic

        Retrieve latency-characteristic
        """
        response = self.client.open(
            '/restconf/config/context/path/{uuid}/routing-constraint/latency-characteristic/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_routing_constraint_latency_characteristic_latency_characteristic_by_id(self):
        """Test case for retrieve_context_path_routing_constraint_latency_characteristic_latency_characteristic_by_id

        Retrieve latency-characteristic by ID
        """
        response = self.client.open(
            '/restconf/config/context/path/{uuid}/routing-constraint/latency-characteristic/{traffic_property_name}/'.format(uuid='uuid_example', traffic_property_name='traffic_property_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_routing_constraint_name_name(self):
        """Test case for retrieve_context_path_routing_constraint_name_name

        Retrieve name
        """
        response = self.client.open(
            '/restconf/config/context/path/{uuid}/routing-constraint/name/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_routing_constraint_name_name_by_id(self):
        """Test case for retrieve_context_path_routing_constraint_name_name_by_id

        Retrieve name by ID
        """
        response = self.client.open(
            '/restconf/config/context/path/{uuid}/routing-constraint/name/{value_name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_routing_constraint_requested_capacity_bandwidth_profile_bandwidth_profile(self):
        """Test case for retrieve_context_path_routing_constraint_requested_capacity_bandwidth_profile_bandwidth_profile

        Retrieve bandwidth-profile
        """
        response = self.client.open(
            '/restconf/config/context/path/{uuid}/routing-constraint/requested-capacity/bandwidth-profile/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_routing_constraint_requested_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(self):
        """Test case for retrieve_context_path_routing_constraint_requested_capacity_bandwidth_profile_committed_burst_size_committed_burst_size

        Retrieve committed-burst-size
        """
        response = self.client.open(
            '/restconf/config/context/path/{uuid}/routing-constraint/requested-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_routing_constraint_requested_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(self):
        """Test case for retrieve_context_path_routing_constraint_requested_capacity_bandwidth_profile_committed_information_rate_committed_information_rate

        Retrieve committed-information-rate
        """
        response = self.client.open(
            '/restconf/config/context/path/{uuid}/routing-constraint/requested-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_routing_constraint_requested_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(self):
        """Test case for retrieve_context_path_routing_constraint_requested_capacity_bandwidth_profile_peak_burst_size_peak_burst_size

        Retrieve peak-burst-size
        """
        response = self.client.open(
            '/restconf/config/context/path/{uuid}/routing-constraint/requested-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_routing_constraint_requested_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(self):
        """Test case for retrieve_context_path_routing_constraint_requested_capacity_bandwidth_profile_peak_information_rate_peak_information_rate

        Retrieve peak-information-rate
        """
        response = self.client.open(
            '/restconf/config/context/path/{uuid}/routing-constraint/requested-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_routing_constraint_requested_capacity_requested_capacity(self):
        """Test case for retrieve_context_path_routing_constraint_requested_capacity_requested_capacity

        Retrieve requested-capacity
        """
        response = self.client.open(
            '/restconf/config/context/path/{uuid}/routing-constraint/requested-capacity/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_routing_constraint_requested_capacity_total_size_total_size(self):
        """Test case for retrieve_context_path_routing_constraint_requested_capacity_total_size_total_size

        Retrieve total-size
        """
        response = self.client.open(
            '/restconf/config/context/path/{uuid}/routing-constraint/requested-capacity/total-size/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_path_routing_constraint_routing_constraint(self):
        """Test case for retrieve_context_path_routing_constraint_routing_constraint

        Retrieve routing-constraint
        """
        response = self.client.open(
            '/restconf/config/context/path/{uuid}/routing-constraint/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_service_interface_point_available_capacity_available_capacity(self):
        """Test case for retrieve_context_service_interface_point_available_capacity_available_capacity

        Retrieve available-capacity
        """
        response = self.client.open(
            '/restconf/config/context/service-interface-point/{uuid}/available-capacity/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_service_interface_point_available_capacity_bandwidth_profile_bandwidth_profile(self):
        """Test case for retrieve_context_service_interface_point_available_capacity_bandwidth_profile_bandwidth_profile

        Retrieve bandwidth-profile
        """
        response = self.client.open(
            '/restconf/config/context/service-interface-point/{uuid}/available-capacity/bandwidth-profile/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_service_interface_point_available_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(self):
        """Test case for retrieve_context_service_interface_point_available_capacity_bandwidth_profile_committed_burst_size_committed_burst_size

        Retrieve committed-burst-size
        """
        response = self.client.open(
            '/restconf/config/context/service-interface-point/{uuid}/available-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_service_interface_point_available_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(self):
        """Test case for retrieve_context_service_interface_point_available_capacity_bandwidth_profile_committed_information_rate_committed_information_rate

        Retrieve committed-information-rate
        """
        response = self.client.open(
            '/restconf/config/context/service-interface-point/{uuid}/available-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_service_interface_point_available_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(self):
        """Test case for retrieve_context_service_interface_point_available_capacity_bandwidth_profile_peak_burst_size_peak_burst_size

        Retrieve peak-burst-size
        """
        response = self.client.open(
            '/restconf/config/context/service-interface-point/{uuid}/available-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_service_interface_point_available_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(self):
        """Test case for retrieve_context_service_interface_point_available_capacity_bandwidth_profile_peak_information_rate_peak_information_rate

        Retrieve peak-information-rate
        """
        response = self.client.open(
            '/restconf/config/context/service-interface-point/{uuid}/available-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_service_interface_point_available_capacity_total_size_total_size(self):
        """Test case for retrieve_context_service_interface_point_available_capacity_total_size_total_size

        Retrieve total-size
        """
        response = self.client.open(
            '/restconf/config/context/service-interface-point/{uuid}/available-capacity/total-size/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_service_interface_point_name_name(self):
        """Test case for retrieve_context_service_interface_point_name_name

        Retrieve name
        """
        response = self.client.open(
            '/restconf/config/context/service-interface-point/{uuid}/name/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_service_interface_point_name_name_by_id(self):
        """Test case for retrieve_context_service_interface_point_name_name_by_id

        Retrieve name by ID
        """
        response = self.client.open(
            '/restconf/config/context/service-interface-point/{uuid}/name/{value_name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_service_interface_point_service_interface_point(self):
        """Test case for retrieve_context_service_interface_point_service_interface_point

        Retrieve service-interface-point
        """
        response = self.client.open(
            '/restconf/config/context/service-interface-point/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_service_interface_point_service_interface_point_by_id(self):
        """Test case for retrieve_context_service_interface_point_service_interface_point_by_id

        Retrieve service-interface-point by ID
        """
        response = self.client.open(
            '/restconf/config/context/service-interface-point/{uuid}/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_service_interface_point_total_potential_capacity_bandwidth_profile_bandwidth_profile(self):
        """Test case for retrieve_context_service_interface_point_total_potential_capacity_bandwidth_profile_bandwidth_profile

        Retrieve bandwidth-profile
        """
        response = self.client.open(
            '/restconf/config/context/service-interface-point/{uuid}/total-potential-capacity/bandwidth-profile/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_service_interface_point_total_potential_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(self):
        """Test case for retrieve_context_service_interface_point_total_potential_capacity_bandwidth_profile_committed_burst_size_committed_burst_size

        Retrieve committed-burst-size
        """
        response = self.client.open(
            '/restconf/config/context/service-interface-point/{uuid}/total-potential-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_service_interface_point_total_potential_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(self):
        """Test case for retrieve_context_service_interface_point_total_potential_capacity_bandwidth_profile_committed_information_rate_committed_information_rate

        Retrieve committed-information-rate
        """
        response = self.client.open(
            '/restconf/config/context/service-interface-point/{uuid}/total-potential-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_service_interface_point_total_potential_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(self):
        """Test case for retrieve_context_service_interface_point_total_potential_capacity_bandwidth_profile_peak_burst_size_peak_burst_size

        Retrieve peak-burst-size
        """
        response = self.client.open(
            '/restconf/config/context/service-interface-point/{uuid}/total-potential-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_service_interface_point_total_potential_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(self):
        """Test case for retrieve_context_service_interface_point_total_potential_capacity_bandwidth_profile_peak_information_rate_peak_information_rate

        Retrieve peak-information-rate
        """
        response = self.client.open(
            '/restconf/config/context/service-interface-point/{uuid}/total-potential-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_service_interface_point_total_potential_capacity_total_potential_capacity(self):
        """Test case for retrieve_context_service_interface_point_total_potential_capacity_total_potential_capacity

        Retrieve total-potential-capacity
        """
        response = self.client.open(
            '/restconf/config/context/service-interface-point/{uuid}/total-potential-capacity/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_service_interface_point_total_potential_capacity_total_size_total_size(self):
        """Test case for retrieve_context_service_interface_point_total_potential_capacity_total_size_total_size

        Retrieve total-size
        """
        response = self.client.open(
            '/restconf/config/context/service-interface-point/{uuid}/total-potential-capacity/total-size/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_link_available_capacity_available_capacity(self):
        """Test case for retrieve_context_topology_link_available_capacity_available_capacity

        Retrieve available-capacity
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/link/{link_uuid}/available-capacity/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_link_available_capacity_bandwidth_profile_bandwidth_profile(self):
        """Test case for retrieve_context_topology_link_available_capacity_bandwidth_profile_bandwidth_profile

        Retrieve bandwidth-profile
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/link/{link_uuid}/available-capacity/bandwidth-profile/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_link_available_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(self):
        """Test case for retrieve_context_topology_link_available_capacity_bandwidth_profile_committed_burst_size_committed_burst_size

        Retrieve committed-burst-size
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/link/{link_uuid}/available-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_link_available_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(self):
        """Test case for retrieve_context_topology_link_available_capacity_bandwidth_profile_committed_information_rate_committed_information_rate

        Retrieve committed-information-rate
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/link/{link_uuid}/available-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_link_available_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(self):
        """Test case for retrieve_context_topology_link_available_capacity_bandwidth_profile_peak_burst_size_peak_burst_size

        Retrieve peak-burst-size
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/link/{link_uuid}/available-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_link_available_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(self):
        """Test case for retrieve_context_topology_link_available_capacity_bandwidth_profile_peak_information_rate_peak_information_rate

        Retrieve peak-information-rate
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/link/{link_uuid}/available-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_link_available_capacity_total_size_total_size(self):
        """Test case for retrieve_context_topology_link_available_capacity_total_size_total_size

        Retrieve total-size
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/link/{link_uuid}/available-capacity/total-size/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_link_cost_characteristic_cost_characteristic(self):
        """Test case for retrieve_context_topology_link_cost_characteristic_cost_characteristic

        Retrieve cost-characteristic
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/link/{link_uuid}/cost-characteristic/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_link_cost_characteristic_cost_characteristic_by_id(self):
        """Test case for retrieve_context_topology_link_cost_characteristic_cost_characteristic_by_id

        Retrieve cost-characteristic by ID
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/link/{link_uuid}/cost-characteristic/{cost_name}/'.format(uuid='uuid_example', link_uuid='link_uuid_example', cost_name='cost_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_link_latency_characteristic_latency_characteristic(self):
        """Test case for retrieve_context_topology_link_latency_characteristic_latency_characteristic

        Retrieve latency-characteristic
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/link/{link_uuid}/latency-characteristic/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_link_latency_characteristic_latency_characteristic_by_id(self):
        """Test case for retrieve_context_topology_link_latency_characteristic_latency_characteristic_by_id

        Retrieve latency-characteristic by ID
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/link/{link_uuid}/latency-characteristic/{traffic_property_name}/'.format(uuid='uuid_example', link_uuid='link_uuid_example', traffic_property_name='traffic_property_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_link_link(self):
        """Test case for retrieve_context_topology_link_link

        Retrieve link
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/link/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_link_link_by_id(self):
        """Test case for retrieve_context_topology_link_link_by_id

        Retrieve link by ID
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/link/{link_uuid}/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_link_name_name(self):
        """Test case for retrieve_context_topology_link_name_name

        Retrieve name
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/link/{link_uuid}/name/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_link_name_name_by_id(self):
        """Test case for retrieve_context_topology_link_name_name_by_id

        Retrieve name by ID
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/link/{link_uuid}/name/{value_name}/'.format(uuid='uuid_example', link_uuid='link_uuid_example', value_name='value_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_link_resilience_type_resilience_type(self):
        """Test case for retrieve_context_topology_link_resilience_type_resilience_type

        Retrieve resilience-type
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/link/{link_uuid}/resilience-type/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_link_risk_characteristic_risk_characteristic(self):
        """Test case for retrieve_context_topology_link_risk_characteristic_risk_characteristic

        Retrieve risk-characteristic
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/link/{link_uuid}/risk-characteristic/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_link_risk_characteristic_risk_characteristic_by_id(self):
        """Test case for retrieve_context_topology_link_risk_characteristic_risk_characteristic_by_id

        Retrieve risk-characteristic by ID
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/link/{link_uuid}/risk-characteristic/{risk_characteristic_name}/'.format(uuid='uuid_example', link_uuid='link_uuid_example', risk_characteristic_name='risk_characteristic_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_link_total_potential_capacity_bandwidth_profile_bandwidth_profile(self):
        """Test case for retrieve_context_topology_link_total_potential_capacity_bandwidth_profile_bandwidth_profile

        Retrieve bandwidth-profile
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/link/{link_uuid}/total-potential-capacity/bandwidth-profile/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_link_total_potential_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(self):
        """Test case for retrieve_context_topology_link_total_potential_capacity_bandwidth_profile_committed_burst_size_committed_burst_size

        Retrieve committed-burst-size
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/link/{link_uuid}/total-potential-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_link_total_potential_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(self):
        """Test case for retrieve_context_topology_link_total_potential_capacity_bandwidth_profile_committed_information_rate_committed_information_rate

        Retrieve committed-information-rate
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/link/{link_uuid}/total-potential-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_link_total_potential_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(self):
        """Test case for retrieve_context_topology_link_total_potential_capacity_bandwidth_profile_peak_burst_size_peak_burst_size

        Retrieve peak-burst-size
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/link/{link_uuid}/total-potential-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_link_total_potential_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(self):
        """Test case for retrieve_context_topology_link_total_potential_capacity_bandwidth_profile_peak_information_rate_peak_information_rate

        Retrieve peak-information-rate
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/link/{link_uuid}/total-potential-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_link_total_potential_capacity_total_potential_capacity(self):
        """Test case for retrieve_context_topology_link_total_potential_capacity_total_potential_capacity

        Retrieve total-potential-capacity
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/link/{link_uuid}/total-potential-capacity/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_link_total_potential_capacity_total_size_total_size(self):
        """Test case for retrieve_context_topology_link_total_potential_capacity_total_size_total_size

        Retrieve total-size
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/link/{link_uuid}/total-potential-capacity/total-size/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_link_validation_mechanism_validation_mechanism(self):
        """Test case for retrieve_context_topology_link_validation_mechanism_validation_mechanism

        Retrieve validation-mechanism
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/link/{link_uuid}/validation-mechanism/'.format(uuid='uuid_example', link_uuid='link_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_link_validation_mechanism_validation_mechanism_by_id(self):
        """Test case for retrieve_context_topology_link_validation_mechanism_validation_mechanism_by_id

        Retrieve validation-mechanism by ID
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/link/{link_uuid}/validation-mechanism/{validation_mechanism}/'.format(uuid='uuid_example', link_uuid='link_uuid_example', validation_mechanism='validation_mechanism_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_name_name(self):
        """Test case for retrieve_context_topology_name_name

        Retrieve name
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/name/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_name_name_by_id(self):
        """Test case for retrieve_context_topology_name_name_by_id

        Retrieve name by ID
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/name/{value_name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_available_capacity_available_capacity(self):
        """Test case for retrieve_context_topology_node_available_capacity_available_capacity

        Retrieve available-capacity
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/available-capacity/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_available_capacity_bandwidth_profile_bandwidth_profile(self):
        """Test case for retrieve_context_topology_node_available_capacity_bandwidth_profile_bandwidth_profile

        Retrieve bandwidth-profile
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/available-capacity/bandwidth-profile/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_available_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(self):
        """Test case for retrieve_context_topology_node_available_capacity_bandwidth_profile_committed_burst_size_committed_burst_size

        Retrieve committed-burst-size
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/available-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_available_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(self):
        """Test case for retrieve_context_topology_node_available_capacity_bandwidth_profile_committed_information_rate_committed_information_rate

        Retrieve committed-information-rate
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/available-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_available_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(self):
        """Test case for retrieve_context_topology_node_available_capacity_bandwidth_profile_peak_burst_size_peak_burst_size

        Retrieve peak-burst-size
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/available-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_available_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(self):
        """Test case for retrieve_context_topology_node_available_capacity_bandwidth_profile_peak_information_rate_peak_information_rate

        Retrieve peak-information-rate
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/available-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_available_capacity_total_size_total_size(self):
        """Test case for retrieve_context_topology_node_available_capacity_total_size_total_size

        Retrieve total-size
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/available-capacity/total-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_cost_characteristic_cost_characteristic(self):
        """Test case for retrieve_context_topology_node_cost_characteristic_cost_characteristic

        Retrieve cost-characteristic
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/cost-characteristic/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_cost_characteristic_cost_characteristic_by_id(self):
        """Test case for retrieve_context_topology_node_cost_characteristic_cost_characteristic_by_id

        Retrieve cost-characteristic by ID
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/cost-characteristic/{cost_name}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', cost_name='cost_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_latency_characteristic_latency_characteristic(self):
        """Test case for retrieve_context_topology_node_latency_characteristic_latency_characteristic

        Retrieve latency-characteristic
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/latency-characteristic/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_latency_characteristic_latency_characteristic_by_id(self):
        """Test case for retrieve_context_topology_node_latency_characteristic_latency_characteristic_by_id

        Retrieve latency-characteristic by ID
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/latency-characteristic/{traffic_property_name}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', traffic_property_name='traffic_property_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_name_name(self):
        """Test case for retrieve_context_topology_node_name_name

        Retrieve name
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/name/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_name_name_by_id(self):
        """Test case for retrieve_context_topology_node_name_name_by_id

        Retrieve name by ID
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/name/{value_name}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', value_name='value_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node(self):
        """Test case for retrieve_context_topology_node_node

        Retrieve node
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_by_id(self):
        """Test case for retrieve_context_topology_node_node_by_id

        Retrieve node by ID
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_available_capacity_available_capacity(self):
        """Test case for retrieve_context_topology_node_node_rule_group_available_capacity_available_capacity

        Retrieve available-capacity
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/available-capacity/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_available_capacity_bandwidth_profile_bandwidth_profile(self):
        """Test case for retrieve_context_topology_node_node_rule_group_available_capacity_bandwidth_profile_bandwidth_profile

        Retrieve bandwidth-profile
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/available-capacity/bandwidth-profile/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_available_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(self):
        """Test case for retrieve_context_topology_node_node_rule_group_available_capacity_bandwidth_profile_committed_burst_size_committed_burst_size

        Retrieve committed-burst-size
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/available-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_available_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(self):
        """Test case for retrieve_context_topology_node_node_rule_group_available_capacity_bandwidth_profile_committed_information_rate_committed_information_rate

        Retrieve committed-information-rate
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/available-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_available_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(self):
        """Test case for retrieve_context_topology_node_node_rule_group_available_capacity_bandwidth_profile_peak_burst_size_peak_burst_size

        Retrieve peak-burst-size
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/available-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_available_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(self):
        """Test case for retrieve_context_topology_node_node_rule_group_available_capacity_bandwidth_profile_peak_information_rate_peak_information_rate

        Retrieve peak-information-rate
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/available-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_available_capacity_total_size_total_size(self):
        """Test case for retrieve_context_topology_node_node_rule_group_available_capacity_total_size_total_size

        Retrieve total-size
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/available-capacity/total-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_cost_characteristic_cost_characteristic(self):
        """Test case for retrieve_context_topology_node_node_rule_group_cost_characteristic_cost_characteristic

        Retrieve cost-characteristic
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/cost-characteristic/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_cost_characteristic_cost_characteristic_by_id(self):
        """Test case for retrieve_context_topology_node_node_rule_group_cost_characteristic_cost_characteristic_by_id

        Retrieve cost-characteristic by ID
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/cost-characteristic/{cost_name}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', cost_name='cost_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_inter_rule_group_available_capacity_available_capacity(self):
        """Test case for retrieve_context_topology_node_node_rule_group_inter_rule_group_available_capacity_available_capacity

        Retrieve available-capacity
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/inter-rule-group/{inter_rule_group_uuid}/available-capacity/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_inter_rule_group_available_capacity_bandwidth_profile_bandwidth_profile(self):
        """Test case for retrieve_context_topology_node_node_rule_group_inter_rule_group_available_capacity_bandwidth_profile_bandwidth_profile

        Retrieve bandwidth-profile
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/inter-rule-group/{inter_rule_group_uuid}/available-capacity/bandwidth-profile/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_inter_rule_group_available_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(self):
        """Test case for retrieve_context_topology_node_node_rule_group_inter_rule_group_available_capacity_bandwidth_profile_committed_burst_size_committed_burst_size

        Retrieve committed-burst-size
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/inter-rule-group/{inter_rule_group_uuid}/available-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_inter_rule_group_available_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(self):
        """Test case for retrieve_context_topology_node_node_rule_group_inter_rule_group_available_capacity_bandwidth_profile_committed_information_rate_committed_information_rate

        Retrieve committed-information-rate
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/inter-rule-group/{inter_rule_group_uuid}/available-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_inter_rule_group_available_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(self):
        """Test case for retrieve_context_topology_node_node_rule_group_inter_rule_group_available_capacity_bandwidth_profile_peak_burst_size_peak_burst_size

        Retrieve peak-burst-size
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/inter-rule-group/{inter_rule_group_uuid}/available-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_inter_rule_group_available_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(self):
        """Test case for retrieve_context_topology_node_node_rule_group_inter_rule_group_available_capacity_bandwidth_profile_peak_information_rate_peak_information_rate

        Retrieve peak-information-rate
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/inter-rule-group/{inter_rule_group_uuid}/available-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_inter_rule_group_available_capacity_total_size_total_size(self):
        """Test case for retrieve_context_topology_node_node_rule_group_inter_rule_group_available_capacity_total_size_total_size

        Retrieve total-size
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/inter-rule-group/{inter_rule_group_uuid}/available-capacity/total-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_inter_rule_group_cost_characteristic_cost_characteristic(self):
        """Test case for retrieve_context_topology_node_node_rule_group_inter_rule_group_cost_characteristic_cost_characteristic

        Retrieve cost-characteristic
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/inter-rule-group/{inter_rule_group_uuid}/cost-characteristic/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_inter_rule_group_cost_characteristic_cost_characteristic_by_id(self):
        """Test case for retrieve_context_topology_node_node_rule_group_inter_rule_group_cost_characteristic_cost_characteristic_by_id

        Retrieve cost-characteristic by ID
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/inter-rule-group/{inter_rule_group_uuid}/cost-characteristic/{cost_name}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example', cost_name='cost_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_inter_rule_group_inter_rule_group(self):
        """Test case for retrieve_context_topology_node_node_rule_group_inter_rule_group_inter_rule_group

        Retrieve inter-rule-group
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/inter-rule-group/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_inter_rule_group_inter_rule_group_by_id(self):
        """Test case for retrieve_context_topology_node_node_rule_group_inter_rule_group_inter_rule_group_by_id

        Retrieve inter-rule-group by ID
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/inter-rule-group/{inter_rule_group_uuid}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_inter_rule_group_latency_characteristic_latency_characteristic(self):
        """Test case for retrieve_context_topology_node_node_rule_group_inter_rule_group_latency_characteristic_latency_characteristic

        Retrieve latency-characteristic
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/inter-rule-group/{inter_rule_group_uuid}/latency-characteristic/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_inter_rule_group_latency_characteristic_latency_characteristic_by_id(self):
        """Test case for retrieve_context_topology_node_node_rule_group_inter_rule_group_latency_characteristic_latency_characteristic_by_id

        Retrieve latency-characteristic by ID
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/inter-rule-group/{inter_rule_group_uuid}/latency-characteristic/{traffic_property_name}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example', traffic_property_name='traffic_property_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_inter_rule_group_name_name(self):
        """Test case for retrieve_context_topology_node_node_rule_group_inter_rule_group_name_name

        Retrieve name
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/inter-rule-group/{inter_rule_group_uuid}/name/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_inter_rule_group_name_name_by_id(self):
        """Test case for retrieve_context_topology_node_node_rule_group_inter_rule_group_name_name_by_id

        Retrieve name by ID
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/inter-rule-group/{inter_rule_group_uuid}/name/{value_name}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example', value_name='value_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_inter_rule_group_risk_characteristic_risk_characteristic(self):
        """Test case for retrieve_context_topology_node_node_rule_group_inter_rule_group_risk_characteristic_risk_characteristic

        Retrieve risk-characteristic
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/inter-rule-group/{inter_rule_group_uuid}/risk-characteristic/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_inter_rule_group_risk_characteristic_risk_characteristic_by_id(self):
        """Test case for retrieve_context_topology_node_node_rule_group_inter_rule_group_risk_characteristic_risk_characteristic_by_id

        Retrieve risk-characteristic by ID
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/inter-rule-group/{inter_rule_group_uuid}/risk-characteristic/{risk_characteristic_name}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example', risk_characteristic_name='risk_characteristic_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_inter_rule_group_rule_name_name(self):
        """Test case for retrieve_context_topology_node_node_rule_group_inter_rule_group_rule_name_name

        Retrieve name
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/inter-rule-group/{inter_rule_group_uuid}/rule/{local_id}/name/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example', local_id='local_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_inter_rule_group_rule_name_name_by_id(self):
        """Test case for retrieve_context_topology_node_node_rule_group_inter_rule_group_rule_name_name_by_id

        Retrieve name by ID
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/inter-rule-group/{inter_rule_group_uuid}/rule/{local_id}/name/{value_name}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_inter_rule_group_rule_rule(self):
        """Test case for retrieve_context_topology_node_node_rule_group_inter_rule_group_rule_rule

        Retrieve rule
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/inter-rule-group/{inter_rule_group_uuid}/rule/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_inter_rule_group_rule_rule_by_id(self):
        """Test case for retrieve_context_topology_node_node_rule_group_inter_rule_group_rule_rule_by_id

        Retrieve rule by ID
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/inter-rule-group/{inter_rule_group_uuid}/rule/{local_id}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example', local_id='local_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_inter_rule_group_total_potential_capacity_bandwidth_profile_bandwidth_profile(self):
        """Test case for retrieve_context_topology_node_node_rule_group_inter_rule_group_total_potential_capacity_bandwidth_profile_bandwidth_profile

        Retrieve bandwidth-profile
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/inter-rule-group/{inter_rule_group_uuid}/total-potential-capacity/bandwidth-profile/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_inter_rule_group_total_potential_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(self):
        """Test case for retrieve_context_topology_node_node_rule_group_inter_rule_group_total_potential_capacity_bandwidth_profile_committed_burst_size_committed_burst_size

        Retrieve committed-burst-size
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/inter-rule-group/{inter_rule_group_uuid}/total-potential-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_inter_rule_group_total_potential_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(self):
        """Test case for retrieve_context_topology_node_node_rule_group_inter_rule_group_total_potential_capacity_bandwidth_profile_committed_information_rate_committed_information_rate

        Retrieve committed-information-rate
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/inter-rule-group/{inter_rule_group_uuid}/total-potential-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_inter_rule_group_total_potential_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(self):
        """Test case for retrieve_context_topology_node_node_rule_group_inter_rule_group_total_potential_capacity_bandwidth_profile_peak_burst_size_peak_burst_size

        Retrieve peak-burst-size
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/inter-rule-group/{inter_rule_group_uuid}/total-potential-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_inter_rule_group_total_potential_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(self):
        """Test case for retrieve_context_topology_node_node_rule_group_inter_rule_group_total_potential_capacity_bandwidth_profile_peak_information_rate_peak_information_rate

        Retrieve peak-information-rate
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/inter-rule-group/{inter_rule_group_uuid}/total-potential-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_inter_rule_group_total_potential_capacity_total_potential_capacity(self):
        """Test case for retrieve_context_topology_node_node_rule_group_inter_rule_group_total_potential_capacity_total_potential_capacity

        Retrieve total-potential-capacity
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/inter-rule-group/{inter_rule_group_uuid}/total-potential-capacity/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_inter_rule_group_total_potential_capacity_total_size_total_size(self):
        """Test case for retrieve_context_topology_node_node_rule_group_inter_rule_group_total_potential_capacity_total_size_total_size

        Retrieve total-size
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/inter-rule-group/{inter_rule_group_uuid}/total-potential-capacity/total-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', inter_rule_group_uuid='inter_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_latency_characteristic_latency_characteristic(self):
        """Test case for retrieve_context_topology_node_node_rule_group_latency_characteristic_latency_characteristic

        Retrieve latency-characteristic
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/latency-characteristic/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_latency_characteristic_latency_characteristic_by_id(self):
        """Test case for retrieve_context_topology_node_node_rule_group_latency_characteristic_latency_characteristic_by_id

        Retrieve latency-characteristic by ID
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/latency-characteristic/{traffic_property_name}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', traffic_property_name='traffic_property_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_name_name(self):
        """Test case for retrieve_context_topology_node_node_rule_group_name_name

        Retrieve name
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/name/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_name_name_by_id(self):
        """Test case for retrieve_context_topology_node_node_rule_group_name_name_by_id

        Retrieve name by ID
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/name/{value_name}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', value_name='value_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_node_rule_group(self):
        """Test case for retrieve_context_topology_node_node_rule_group_node_rule_group

        Retrieve node-rule-group
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_node_rule_group_by_id(self):
        """Test case for retrieve_context_topology_node_node_rule_group_node_rule_group_by_id

        Retrieve node-rule-group by ID
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_risk_characteristic_risk_characteristic(self):
        """Test case for retrieve_context_topology_node_node_rule_group_risk_characteristic_risk_characteristic

        Retrieve risk-characteristic
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/risk-characteristic/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_risk_characteristic_risk_characteristic_by_id(self):
        """Test case for retrieve_context_topology_node_node_rule_group_risk_characteristic_risk_characteristic_by_id

        Retrieve risk-characteristic by ID
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/risk-characteristic/{risk_characteristic_name}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', risk_characteristic_name='risk_characteristic_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_rule_name_name(self):
        """Test case for retrieve_context_topology_node_node_rule_group_rule_name_name

        Retrieve name
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/rule/{local_id}/name/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', local_id='local_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_rule_name_name_by_id(self):
        """Test case for retrieve_context_topology_node_node_rule_group_rule_name_name_by_id

        Retrieve name by ID
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/rule/{local_id}/name/{value_name}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_rule_rule(self):
        """Test case for retrieve_context_topology_node_node_rule_group_rule_rule

        Retrieve rule
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/rule/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_rule_rule_by_id(self):
        """Test case for retrieve_context_topology_node_node_rule_group_rule_rule_by_id

        Retrieve rule by ID
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/rule/{local_id}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example', local_id='local_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_total_potential_capacity_bandwidth_profile_bandwidth_profile(self):
        """Test case for retrieve_context_topology_node_node_rule_group_total_potential_capacity_bandwidth_profile_bandwidth_profile

        Retrieve bandwidth-profile
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/total-potential-capacity/bandwidth-profile/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_total_potential_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(self):
        """Test case for retrieve_context_topology_node_node_rule_group_total_potential_capacity_bandwidth_profile_committed_burst_size_committed_burst_size

        Retrieve committed-burst-size
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/total-potential-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_total_potential_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(self):
        """Test case for retrieve_context_topology_node_node_rule_group_total_potential_capacity_bandwidth_profile_committed_information_rate_committed_information_rate

        Retrieve committed-information-rate
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/total-potential-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_total_potential_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(self):
        """Test case for retrieve_context_topology_node_node_rule_group_total_potential_capacity_bandwidth_profile_peak_burst_size_peak_burst_size

        Retrieve peak-burst-size
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/total-potential-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_total_potential_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(self):
        """Test case for retrieve_context_topology_node_node_rule_group_total_potential_capacity_bandwidth_profile_peak_information_rate_peak_information_rate

        Retrieve peak-information-rate
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/total-potential-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_total_potential_capacity_total_potential_capacity(self):
        """Test case for retrieve_context_topology_node_node_rule_group_total_potential_capacity_total_potential_capacity

        Retrieve total-potential-capacity
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/total-potential-capacity/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_node_rule_group_total_potential_capacity_total_size_total_size(self):
        """Test case for retrieve_context_topology_node_node_rule_group_total_potential_capacity_total_size_total_size

        Retrieve total-size
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/node-rule-group/{node_rule_group_uuid}/total-potential-capacity/total-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example', node_rule_group_uuid='node_rule_group_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_owned_node_edge_point_connection_end_point_connection_end_point(self):
        """Test case for retrieve_context_topology_node_owned_node_edge_point_connection_end_point_connection_end_point

        Retrieve connection-end-point
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/owned-node-edge-point/{owned_node_edge_point_uuid}/connection-end-point/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_owned_node_edge_point_connection_end_point_connection_end_point_by_id(self):
        """Test case for retrieve_context_topology_node_owned_node_edge_point_connection_end_point_connection_end_point_by_id

        Retrieve connection-end-point by ID
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/owned-node-edge-point/{owned_node_edge_point_uuid}/connection-end-point/{connection_end_point_uuid}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_owned_node_edge_point_connection_end_point_name_name(self):
        """Test case for retrieve_context_topology_node_owned_node_edge_point_connection_end_point_name_name

        Retrieve name
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/owned-node-edge-point/{owned_node_edge_point_uuid}/connection-end-point/{connection_end_point_uuid}/name/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_owned_node_edge_point_connection_end_point_name_name_by_id(self):
        """Test case for retrieve_context_topology_node_owned_node_edge_point_connection_end_point_name_name_by_id

        Retrieve name by ID
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/owned-node-edge-point/{owned_node_edge_point_uuid}/connection-end-point/{connection_end_point_uuid}/name/{value_name}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example', value_name='value_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_owned_node_edge_point_name_name(self):
        """Test case for retrieve_context_topology_node_owned_node_edge_point_name_name

        Retrieve name
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/owned-node-edge-point/{owned_node_edge_point_uuid}/name/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_owned_node_edge_point_name_name_by_id(self):
        """Test case for retrieve_context_topology_node_owned_node_edge_point_name_name_by_id

        Retrieve name by ID
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/owned-node-edge-point/{owned_node_edge_point_uuid}/name/{value_name}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', value_name='value_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_owned_node_edge_point_owned_node_edge_point(self):
        """Test case for retrieve_context_topology_node_owned_node_edge_point_owned_node_edge_point

        Retrieve owned-node-edge-point
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/owned-node-edge-point/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_owned_node_edge_point_owned_node_edge_point_by_id(self):
        """Test case for retrieve_context_topology_node_owned_node_edge_point_owned_node_edge_point_by_id

        Retrieve owned-node-edge-point by ID
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/owned-node-edge-point/{owned_node_edge_point_uuid}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_total_potential_capacity_bandwidth_profile_bandwidth_profile(self):
        """Test case for retrieve_context_topology_node_total_potential_capacity_bandwidth_profile_bandwidth_profile

        Retrieve bandwidth-profile
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/total-potential-capacity/bandwidth-profile/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_total_potential_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(self):
        """Test case for retrieve_context_topology_node_total_potential_capacity_bandwidth_profile_committed_burst_size_committed_burst_size

        Retrieve committed-burst-size
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/total-potential-capacity/bandwidth-profile/committed-burst-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_total_potential_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(self):
        """Test case for retrieve_context_topology_node_total_potential_capacity_bandwidth_profile_committed_information_rate_committed_information_rate

        Retrieve committed-information-rate
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/total-potential-capacity/bandwidth-profile/committed-information-rate/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_total_potential_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(self):
        """Test case for retrieve_context_topology_node_total_potential_capacity_bandwidth_profile_peak_burst_size_peak_burst_size

        Retrieve peak-burst-size
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/total-potential-capacity/bandwidth-profile/peak-burst-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_total_potential_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(self):
        """Test case for retrieve_context_topology_node_total_potential_capacity_bandwidth_profile_peak_information_rate_peak_information_rate

        Retrieve peak-information-rate
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/total-potential-capacity/bandwidth-profile/peak-information-rate/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_total_potential_capacity_total_potential_capacity(self):
        """Test case for retrieve_context_topology_node_total_potential_capacity_total_potential_capacity

        Retrieve total-potential-capacity
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/total-potential-capacity/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_node_total_potential_capacity_total_size_total_size(self):
        """Test case for retrieve_context_topology_node_total_potential_capacity_total_size_total_size

        Retrieve total-size
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/node/{node_uuid}/total-potential-capacity/total-size/'.format(uuid='uuid_example', node_uuid='node_uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_topology(self):
        """Test case for retrieve_context_topology_topology

        Retrieve topology
        """
        response = self.client.open(
            '/restconf/config/context/topology/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_context_topology_topology_by_id(self):
        """Test case for retrieve_context_topology_topology_by_id

        Retrieve topology by ID
        """
        response = self.client.open(
            '/restconf/config/context/topology/{uuid}/'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_context_by_id(self):
        """Test case for update_context_by_id

        Update context by ID
        """
        context = ContextSchema()
        response = self.client.open(
            '/restconf/config/context/',
            method='PUT',
            data=json.dumps(context),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_context_connectivity_service_connectivity_service_by_id(self):
        """Test case for update_context_connectivity_service_connectivity_service_by_id

        Update connectivity-service by ID
        """
        connectivity_service = ConnectivityService()
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(connectivity_service),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_context_connectivity_service_end_point_capacity_capacity_by_id(self):
        """Test case for update_context_connectivity_service_end_point_capacity_capacity_by_id

        Update capacity by ID
        """
        capacity = CapacityPac()
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/end-point/{local_id}/capacity/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(capacity),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_context_connectivity_service_end_point_end_point_by_id(self):
        """Test case for update_context_connectivity_service_end_point_end_point_by_id

        Update end-point by ID
        """
        end_point = ConnectivityServiceEndPoint()
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/end-point/{local_id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(end_point),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_context_connectivity_service_end_point_name_name_by_id(self):
        """Test case for update_context_connectivity_service_end_point_name_name_by_id

        Update name by ID
        """
        name = NameAndValue()
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/end-point/{local_id}/name/{value_name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='PUT',
            data=json.dumps(name),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_context_connectivity_service_name_name_by_id(self):
        """Test case for update_context_connectivity_service_name_name_by_id

        Update name by ID
        """
        name = NameAndValue()
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/name/{value_name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='PUT',
            data=json.dumps(name),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_context_connectivity_service_resilience_type_resilience_type_by_id(self):
        """Test case for update_context_connectivity_service_resilience_type_resilience_type_by_id

        Update resilience-type by ID
        """
        resilience_type = ResilienceType()
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/resilience-type/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(resilience_type),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_context_connectivity_service_schedule_schedule_by_id(self):
        """Test case for update_context_connectivity_service_schedule_schedule_by_id

        Update schedule by ID
        """
        schedule = TimeRange()
        response = self.client.open(
            '/restconf/config/context/connectivity-service/{uuid}/schedule/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(schedule),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_context_name_name_by_id(self):
        """Test case for update_context_name_name_by_id

        Update name by ID
        """
        name = NameAndValue()
        response = self.client.open(
            '/restconf/config/context/name/{value_name}/'.format(value_name='value_name_example'),
            method='PUT',
            data=json.dumps(name),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_context_path_comp_service_end_point_end_point_by_id(self):
        """Test case for update_context_path_comp_service_end_point_end_point_by_id

        Update end-point by ID
        """
        end_point = PathServiceEndPoint()
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/end-point/{local_id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(end_point),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_context_path_comp_service_end_point_name_name_by_id(self):
        """Test case for update_context_path_comp_service_end_point_name_name_by_id

        Update name by ID
        """
        name = NameAndValue()
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/end-point/{local_id}/name/{value_name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='PUT',
            data=json.dumps(name),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_context_path_comp_service_name_name_by_id(self):
        """Test case for update_context_path_comp_service_name_name_by_id

        Update name by ID
        """
        name = NameAndValue()
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/name/{value_name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='PUT',
            data=json.dumps(name),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_context_path_comp_service_objective_function_name_name_by_id(self):
        """Test case for update_context_path_comp_service_objective_function_name_name_by_id

        Update name by ID
        """
        name = NameAndValue()
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/objective-function/name/{value_name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='PUT',
            data=json.dumps(name),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_context_path_comp_service_objective_function_objective_function_by_id(self):
        """Test case for update_context_path_comp_service_objective_function_objective_function_by_id

        Update objective-function by ID
        """
        objective_function = PathObjectiveFunction()
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/objective-function/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(objective_function),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_context_path_comp_service_optimization_constraint_name_name_by_id(self):
        """Test case for update_context_path_comp_service_optimization_constraint_name_name_by_id

        Update name by ID
        """
        name = NameAndValue()
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/optimization-constraint/name/{value_name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='PUT',
            data=json.dumps(name),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_context_path_comp_service_optimization_constraint_optimization_constraint_by_id(self):
        """Test case for update_context_path_comp_service_optimization_constraint_optimization_constraint_by_id

        Update optimization-constraint by ID
        """
        optimization_constraint = PathOptimizationConstraint()
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/optimization-constraint/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(optimization_constraint),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_context_path_comp_service_path_comp_service_by_id(self):
        """Test case for update_context_path_comp_service_path_comp_service_by_id

        Update path-comp-service by ID
        """
        path_comp_service = PathComputationService()
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(path_comp_service),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_context_path_comp_service_routing_constraint_name_name_by_id(self):
        """Test case for update_context_path_comp_service_routing_constraint_name_name_by_id

        Update name by ID
        """
        name = NameAndValue()
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/routing-constraint/name/{value_name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='PUT',
            data=json.dumps(name),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_context_path_comp_service_routing_constraint_routing_constraint_by_id(self):
        """Test case for update_context_path_comp_service_routing_constraint_routing_constraint_by_id

        Update routing-constraint by ID
        """
        routing_constraint = RoutingConstraint()
        response = self.client.open(
            '/restconf/config/context/path-comp-service/{uuid}/routing-constraint/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(routing_constraint),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_context_service_interface_point_name_name_by_id(self):
        """Test case for update_context_service_interface_point_name_name_by_id

        Update name by ID
        """
        name = NameAndValue()
        response = self.client.open(
            '/restconf/config/context/service-interface-point/{uuid}/name/{value_name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='PUT',
            data=json.dumps(name),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_context_service_interface_point_service_interface_point_by_id(self):
        """Test case for update_context_service_interface_point_service_interface_point_by_id

        Update service-interface-point by ID
        """
        service_interface_point = ServiceInterfacePoint()
        response = self.client.open(
            '/restconf/config/context/service-interface-point/{uuid}/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(service_interface_point),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
