import connexion
import six

from tapi_server.models.bandwidth_profile import BandwidthProfile  # noqa: E501
from tapi_server.models.capacity import Capacity  # noqa: E501
from tapi_server.models.capacity_value import CapacityValue  # noqa: E501
from tapi_server.models.connection import Connection  # noqa: E501
from tapi_server.models.connection_end_point import ConnectionEndPoint  # noqa: E501
from tapi_server.models.connectivity_service import ConnectivityService  # noqa: E501
from tapi_server.models.connectivity_service_end_point import ConnectivityServiceEndPoint  # noqa: E501
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
from tapi_server.models.get_link_details_rpc_input_schema import GetLinkDetailsRPCInputSchema  # noqa: E501
from tapi_server.models.get_link_details_rpc_output_schema import GetLinkDetailsRPCOutputSchema  # noqa: E501
from tapi_server.models.get_node_details_rpc_input_schema import GetNodeDetailsRPCInputSchema  # noqa: E501
from tapi_server.models.get_node_details_rpc_output_schema import GetNodeDetailsRPCOutputSchema  # noqa: E501
from tapi_server.models.get_node_edge_point_details_rpc_input_schema import GetNodeEdgePointDetailsRPCInputSchema  # noqa: E501
from tapi_server.models.get_node_edge_point_details_rpc_output_schema import GetNodeEdgePointDetailsRPCOutputSchema  # noqa: E501
from tapi_server.models.get_service_interface_point_details_rpc_input_schema import GetServiceInterfacePointDetailsRPCInputSchema  # noqa: E501
from tapi_server.models.get_service_interface_point_details_rpc_output_schema import GetServiceInterfacePointDetailsRPCOutputSchema  # noqa: E501
from tapi_server.models.get_service_interface_point_list_rpc_output_schema import GetServiceInterfacePointListRPCOutputSchema  # noqa: E501
from tapi_server.models.get_topology_details_rpc_input_schema import GetTopologyDetailsRPCInputSchema  # noqa: E501
from tapi_server.models.get_topology_details_rpc_output_schema import GetTopologyDetailsRPCOutputSchema  # noqa: E501
from tapi_server.models.get_topology_list_rpc_output_schema import GetTopologyListRPCOutputSchema  # noqa: E501
from tapi_server.models.inter_rule_group import InterRuleGroup  # noqa: E501
from tapi_server.models.latency_characteristic import LatencyCharacteristic  # noqa: E501
from tapi_server.models.link import Link  # noqa: E501
from tapi_server.models.name_and_value import NameAndValue  # noqa: E501
from tapi_server.models.network_topology_service import NetworkTopologyService  # noqa: E501
from tapi_server.models.node import Node  # noqa: E501
from tapi_server.models.node_edge_point import NodeEdgePoint  # noqa: E501
from tapi_server.models.node_rule_group import NodeRuleGroup  # noqa: E501
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
from tapi_server.models.tapi_context import TapiContext  # noqa: E501
from tapi_server.models.time_range import TimeRange  # noqa: E501
from tapi_server.models.topology import Topology  # noqa: E501
from tapi_server.models.update_connectivity_service_rpc_input_schema import UpdateConnectivityServiceRPCInputSchema  # noqa: E501
from tapi_server.models.update_connectivity_service_rpc_output_schema import UpdateConnectivityServiceRPCOutputSchema  # noqa: E501
from tapi_server.models.update_service_interface_point_rpc_input_schema import UpdateServiceInterfacePointRPCInputSchema  # noqa: E501
from tapi_server.models.validation_mechanism import ValidationMechanism  # noqa: E501
from tapi_server import util
from tapi_server.database import database


def create_context_by_id(context):  # noqa: E501
    """Create context by ID

    Create operation of resource: context # noqa: E501

    :param context: contextbody object
    :type context: dict | bytes

    :rtype: None
    """
    if database.context.uuid:
        raise Exception ("TAPI Context cannot be created/deleted since it is the root presence-container for all client-server interaction")
    
    logging.info("create_context_by_id %s", context)
    if connexion.request.is_json:
        database.context = TapiContext.from_dict(connexion.request.get_json())  # noqa: E501
    return database.context


def create_context_connectivity_service_connectivity_service_by_id(uuid, connectivity_service):  # noqa: E501
    """Create connectivity-service by ID

    Create operation of resource: connectivity-service # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param connectivity_service: connectivity-servicebody object
    :type connectivity_service: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        connectivity_service = ConnectivityService.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_connectivity_service_cost_characteristic_cost_characteristic_by_id(uuid, cost_name, cost_characteristic):  # noqa: E501
    """Create cost-characteristic by ID

    Create operation of resource: cost-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param cost_name: ID of cost_name
    :type cost_name: str
    :param cost_characteristic: cost-characteristicbody object
    :type cost_characteristic: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        cost_characteristic = CostCharacteristic.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_connectivity_service_end_point_capacity_bandwidth_profile_bandwidth_profile_by_id(uuid, local_id, bandwidth_profile):  # noqa: E501
    """Create bandwidth-profile by ID

    Create operation of resource: bandwidth-profile # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str
    :param bandwidth_profile: bandwidth-profilebody object
    :type bandwidth_profile: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        bandwidth_profile = BandwidthProfile.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_connectivity_service_end_point_capacity_bandwidth_profile_committed_burst_size_committed_burst_size_by_id(uuid, local_id, committed_burst_size):  # noqa: E501
    """Create committed-burst-size by ID

    Create operation of resource: committed-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str
    :param committed_burst_size: committed-burst-sizebody object
    :type committed_burst_size: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        committed_burst_size = CapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_connectivity_service_end_point_capacity_bandwidth_profile_committed_information_rate_committed_information_rate_by_id(uuid, local_id, committed_information_rate):  # noqa: E501
    """Create committed-information-rate by ID

    Create operation of resource: committed-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str
    :param committed_information_rate: committed-information-ratebody object
    :type committed_information_rate: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        committed_information_rate = CapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_connectivity_service_end_point_capacity_bandwidth_profile_peak_burst_size_peak_burst_size_by_id(uuid, local_id, peak_burst_size):  # noqa: E501
    """Create peak-burst-size by ID

    Create operation of resource: peak-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str
    :param peak_burst_size: peak-burst-sizebody object
    :type peak_burst_size: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        peak_burst_size = CapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_connectivity_service_end_point_capacity_bandwidth_profile_peak_information_rate_peak_information_rate_by_id(uuid, local_id, peak_information_rate):  # noqa: E501
    """Create peak-information-rate by ID

    Create operation of resource: peak-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str
    :param peak_information_rate: peak-information-ratebody object
    :type peak_information_rate: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        peak_information_rate = CapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_connectivity_service_end_point_capacity_capacity_by_id(uuid, local_id, capacity):  # noqa: E501
    """Create capacity by ID

    Create operation of resource: capacity # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str
    :param capacity: capacitybody object
    :type capacity: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        capacity = Capacity.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_connectivity_service_end_point_capacity_total_size_total_size_by_id(uuid, local_id, total_size):  # noqa: E501
    """Create total-size by ID

    Create operation of resource: total-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str
    :param total_size: total-sizebody object
    :type total_size: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        total_size = CapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_connectivity_service_end_point_end_point_by_id(uuid, local_id, end_point):  # noqa: E501
    """Create end-point by ID

    Create operation of resource: end-point # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str
    :param end_point: end-pointbody object
    :type end_point: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        end_point = ConnectivityServiceEndPoint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_connectivity_service_end_point_name_name_by_id(uuid, local_id, value_name, name):  # noqa: E501
    """Create name by ID

    Create operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str
    :param value_name: ID of value_name
    :type value_name: str
    :param name: namebody object
    :type name: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        name = NameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_connectivity_service_latency_characteristic_latency_characteristic_by_id(uuid, traffic_property_name, latency_characteristic):  # noqa: E501
    """Create latency-characteristic by ID

    Create operation of resource: latency-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param traffic_property_name: ID of traffic_property_name
    :type traffic_property_name: str
    :param latency_characteristic: latency-characteristicbody object
    :type latency_characteristic: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        latency_characteristic = LatencyCharacteristic.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_connectivity_service_name_name_by_id(uuid, value_name, name):  # noqa: E501
    """Create name by ID

    Create operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param value_name: ID of value_name
    :type value_name: str
    :param name: namebody object
    :type name: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        name = NameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_connectivity_service_requested_capacity_bandwidth_profile_bandwidth_profile_by_id(uuid, bandwidth_profile):  # noqa: E501
    """Create bandwidth-profile by ID

    Create operation of resource: bandwidth-profile # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param bandwidth_profile: bandwidth-profilebody object
    :type bandwidth_profile: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        bandwidth_profile = BandwidthProfile.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_connectivity_service_requested_capacity_bandwidth_profile_committed_burst_size_committed_burst_size_by_id(uuid, committed_burst_size):  # noqa: E501
    """Create committed-burst-size by ID

    Create operation of resource: committed-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param committed_burst_size: committed-burst-sizebody object
    :type committed_burst_size: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        committed_burst_size = CapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_connectivity_service_requested_capacity_bandwidth_profile_committed_information_rate_committed_information_rate_by_id(uuid, committed_information_rate):  # noqa: E501
    """Create committed-information-rate by ID

    Create operation of resource: committed-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param committed_information_rate: committed-information-ratebody object
    :type committed_information_rate: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        committed_information_rate = CapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_connectivity_service_requested_capacity_bandwidth_profile_peak_burst_size_peak_burst_size_by_id(uuid, peak_burst_size):  # noqa: E501
    """Create peak-burst-size by ID

    Create operation of resource: peak-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param peak_burst_size: peak-burst-sizebody object
    :type peak_burst_size: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        peak_burst_size = CapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_connectivity_service_requested_capacity_bandwidth_profile_peak_information_rate_peak_information_rate_by_id(uuid, peak_information_rate):  # noqa: E501
    """Create peak-information-rate by ID

    Create operation of resource: peak-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param peak_information_rate: peak-information-ratebody object
    :type peak_information_rate: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        peak_information_rate = CapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_connectivity_service_requested_capacity_requested_capacity_by_id(uuid, requested_capacity):  # noqa: E501
    """Create requested-capacity by ID

    Create operation of resource: requested-capacity # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param requested_capacity: requested-capacitybody object
    :type requested_capacity: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        requested_capacity = Capacity.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_connectivity_service_requested_capacity_total_size_total_size_by_id(uuid, total_size):  # noqa: E501
    """Create total-size by ID

    Create operation of resource: total-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param total_size: total-sizebody object
    :type total_size: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        total_size = CapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_connectivity_service_resilience_type_resilience_type_by_id(uuid, resilience_type):  # noqa: E501
    """Create resilience-type by ID

    Create operation of resource: resilience-type # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param resilience_type: resilience-typebody object
    :type resilience_type: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        resilience_type = ResilienceType.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_connectivity_service_schedule_schedule_by_id(uuid, schedule):  # noqa: E501
    """Create schedule by ID

    Create operation of resource: schedule # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param schedule: schedulebody object
    :type schedule: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        schedule = TimeRange.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_name_name_by_id(value_name, name):  # noqa: E501
    """Create name by ID

    Create operation of resource: name # noqa: E501

    :param value_name: ID of value_name
    :type value_name: str
    :param name: namebody object
    :type name: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        name = NameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_path_comp_service_end_point_end_point_by_id(uuid, local_id, end_point):  # noqa: E501
    """Create end-point by ID

    Create operation of resource: end-point # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str
    :param end_point: end-pointbody object
    :type end_point: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        end_point = PathServiceEndPoint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_path_comp_service_end_point_name_name_by_id(uuid, local_id, value_name, name):  # noqa: E501
    """Create name by ID

    Create operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str
    :param value_name: ID of value_name
    :type value_name: str
    :param name: namebody object
    :type name: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        name = NameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_path_comp_service_name_name_by_id(uuid, value_name, name):  # noqa: E501
    """Create name by ID

    Create operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param value_name: ID of value_name
    :type value_name: str
    :param name: namebody object
    :type name: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        name = NameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_path_comp_service_objective_function_name_name_by_id(uuid, value_name, name):  # noqa: E501
    """Create name by ID

    Create operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param value_name: ID of value_name
    :type value_name: str
    :param name: namebody object
    :type name: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        name = NameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_path_comp_service_objective_function_objective_function_by_id(uuid, objective_function):  # noqa: E501
    """Create objective-function by ID

    Create operation of resource: objective-function # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param objective_function: objective-functionbody object
    :type objective_function: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        objective_function = PathObjectiveFunction.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_path_comp_service_optimization_constraint_name_name_by_id(uuid, value_name, name):  # noqa: E501
    """Create name by ID

    Create operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param value_name: ID of value_name
    :type value_name: str
    :param name: namebody object
    :type name: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        name = NameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_path_comp_service_optimization_constraint_optimization_constraint_by_id(uuid, optimization_constraint):  # noqa: E501
    """Create optimization-constraint by ID

    Create operation of resource: optimization-constraint # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param optimization_constraint: optimization-constraintbody object
    :type optimization_constraint: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        optimization_constraint = PathOptimizationConstraint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_path_comp_service_path_comp_service_by_id(uuid, path_comp_service):  # noqa: E501
    """Create path-comp-service by ID

    Create operation of resource: path-comp-service # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param path_comp_service: path-comp-servicebody object
    :type path_comp_service: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        path_comp_service = PathComputationService.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_path_comp_service_routing_constraint_name_name_by_id(uuid, value_name, name):  # noqa: E501
    """Create name by ID

    Create operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param value_name: ID of value_name
    :type value_name: str
    :param name: namebody object
    :type name: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        name = NameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_path_comp_service_routing_constraint_routing_constraint_by_id(uuid, routing_constraint):  # noqa: E501
    """Create routing-constraint by ID

    Create operation of resource: routing-constraint # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param routing_constraint: routing-constraintbody object
    :type routing_constraint: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        routing_constraint = RoutingConstraint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_service_interface_point_name_name_by_id(uuid, value_name, name):  # noqa: E501
    """Create name by ID

    Create operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param value_name: ID of value_name
    :type value_name: str
    :param name: namebody object
    :type name: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        name = NameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_context_service_interface_point_service_interface_point_by_id(uuid, service_interface_point):  # noqa: E501
    """Create service-interface-point by ID

    Create operation of resource: service-interface-point # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param service_interface_point: service-interface-pointbody object
    :type service_interface_point: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        service_interface_point = ServiceInterfacePoint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_create_connectivity_service_by_id(create_connectivity_service):  # noqa: E501
    """Create create-connectivity-service by ID

    Create operation of resource: create-connectivity-service # noqa: E501

    :param create_connectivity_service: create-connectivity-servicebody object
    :type create_connectivity_service: dict | bytes

    :rtype: CreateConnectivityServiceRPCOutputSchema
    """
    if connexion.request.is_json:
        create_connectivity_service = CreateConnectivityServiceRPCInputSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_delete_connectivity_service_by_id(delete_connectivity_service):  # noqa: E501
    """Create delete-connectivity-service by ID

    Create operation of resource: delete-connectivity-service # noqa: E501

    :param delete_connectivity_service: delete-connectivity-servicebody object
    :type delete_connectivity_service: dict | bytes

    :rtype: DeleteConnectivityServiceRPCOutputSchema
    """
    if connexion.request.is_json:
        delete_connectivity_service = DeleteConnectivityServiceRPCInputSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_get_connection_details_by_id(get_connection_details):  # noqa: E501
    """Create get-connection-details by ID

    Create operation of resource: get-connection-details # noqa: E501

    :param get_connection_details: get-connection-detailsbody object
    :type get_connection_details: dict | bytes

    :rtype: GetConnectionDetailsRPCOutputSchema
    """
    if connexion.request.is_json:
        get_connection_details = GetConnectionDetailsRPCInputSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_get_connectivity_service_details_by_id(get_connectivity_service_details):  # noqa: E501
    """Create get-connectivity-service-details by ID

    Create operation of resource: get-connectivity-service-details # noqa: E501

    :param get_connectivity_service_details: get-connectivity-service-detailsbody object
    :type get_connectivity_service_details: dict | bytes

    :rtype: GetConnectivityServiceDetailsRPCOutputSchema
    """
    if connexion.request.is_json:
        get_connectivity_service_details = GetConnectivityServiceDetailsRPCInputSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_get_connectivity_service_list_by_id():  # noqa: E501
    """Create get-connectivity-service-list by ID

    Create operation of resource: get-connectivity-service-list # noqa: E501


    :rtype: GetConnectivityServiceListRPCOutputSchema
    """
    return 'do some magic!'


def create_get_link_details_by_id(get_link_details):  # noqa: E501
    """Create get-link-details by ID

    Create operation of resource: get-link-details # noqa: E501

    :param get_link_details: get-link-detailsbody object
    :type get_link_details: dict | bytes

    :rtype: GetLinkDetailsRPCOutputSchema
    """
    if connexion.request.is_json:
        get_link_details = GetLinkDetailsRPCInputSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_get_node_details_by_id(get_node_details):  # noqa: E501
    """Create get-node-details by ID

    Create operation of resource: get-node-details # noqa: E501

    :param get_node_details: get-node-detailsbody object
    :type get_node_details: dict | bytes

    :rtype: GetNodeDetailsRPCOutputSchema
    """
    if connexion.request.is_json:
        get_node_details = GetNodeDetailsRPCInputSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_get_node_edge_point_details_by_id(get_node_edge_point_details):  # noqa: E501
    """Create get-node-edge-point-details by ID

    Create operation of resource: get-node-edge-point-details # noqa: E501

    :param get_node_edge_point_details: get-node-edge-point-detailsbody object
    :type get_node_edge_point_details: dict | bytes

    :rtype: GetNodeEdgePointDetailsRPCOutputSchema
    """
    if connexion.request.is_json:
        get_node_edge_point_details = GetNodeEdgePointDetailsRPCInputSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_get_service_interface_point_details_by_id(get_service_interface_point_details):  # noqa: E501
    """Create get-service-interface-point-details by ID

    Create operation of resource: get-service-interface-point-details # noqa: E501

    :param get_service_interface_point_details: get-service-interface-point-detailsbody object
    :type get_service_interface_point_details: dict | bytes

    :rtype: GetServiceInterfacePointDetailsRPCOutputSchema
    """
    if connexion.request.is_json:
        get_service_interface_point_details = GetServiceInterfacePointDetailsRPCInputSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_get_service_interface_point_list_by_id():  # noqa: E501
    """Create get-service-interface-point-list by ID

    Create operation of resource: get-service-interface-point-list # noqa: E501


    :rtype: GetServiceInterfacePointListRPCOutputSchema
    """
    return 'do some magic!'


def create_get_topology_details_by_id(get_topology_details):  # noqa: E501
    """Create get-topology-details by ID

    Create operation of resource: get-topology-details # noqa: E501

    :param get_topology_details: get-topology-detailsbody object
    :type get_topology_details: dict | bytes

    :rtype: GetTopologyDetailsRPCOutputSchema
    """
    if connexion.request.is_json:
        get_topology_details = GetTopologyDetailsRPCInputSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_get_topology_list_by_id():  # noqa: E501
    """Create get-topology-list by ID

    Create operation of resource: get-topology-list # noqa: E501


    :rtype: GetTopologyListRPCOutputSchema
    """
    return 'do some magic!'


def create_update_connectivity_service_by_id(update_connectivity_service):  # noqa: E501
    """Create update-connectivity-service by ID

    Create operation of resource: update-connectivity-service # noqa: E501

    :param update_connectivity_service: update-connectivity-servicebody object
    :type update_connectivity_service: dict | bytes

    :rtype: UpdateConnectivityServiceRPCOutputSchema
    """
    if connexion.request.is_json:
        update_connectivity_service = UpdateConnectivityServiceRPCInputSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_update_service_interface_point_by_id(update_service_interface_point):  # noqa: E501
    """Create update-service-interface-point by ID

    Create operation of resource: update-service-interface-point # noqa: E501

    :param update_service_interface_point: update-service-interface-pointbody object
    :type update_service_interface_point: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        update_service_interface_point = UpdateServiceInterfacePointRPCInputSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_context_by_id():  # noqa: E501
    """Delete context by ID

    Delete operation of resource: context # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def delete_context_connectivity_service_connectivity_service_by_id(uuid):  # noqa: E501
    """Delete connectivity-service by ID

    Delete operation of resource: connectivity-service # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_connectivity_service_cost_characteristic_cost_characteristic_by_id(uuid, cost_name):  # noqa: E501
    """Delete cost-characteristic by ID

    Delete operation of resource: cost-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param cost_name: ID of cost_name
    :type cost_name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_connectivity_service_end_point_capacity_bandwidth_profile_bandwidth_profile_by_id(uuid, local_id):  # noqa: E501
    """Delete bandwidth-profile by ID

    Delete operation of resource: bandwidth-profile # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_connectivity_service_end_point_capacity_bandwidth_profile_committed_burst_size_committed_burst_size_by_id(uuid, local_id):  # noqa: E501
    """Delete committed-burst-size by ID

    Delete operation of resource: committed-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_connectivity_service_end_point_capacity_bandwidth_profile_committed_information_rate_committed_information_rate_by_id(uuid, local_id):  # noqa: E501
    """Delete committed-information-rate by ID

    Delete operation of resource: committed-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_connectivity_service_end_point_capacity_bandwidth_profile_peak_burst_size_peak_burst_size_by_id(uuid, local_id):  # noqa: E501
    """Delete peak-burst-size by ID

    Delete operation of resource: peak-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_connectivity_service_end_point_capacity_bandwidth_profile_peak_information_rate_peak_information_rate_by_id(uuid, local_id):  # noqa: E501
    """Delete peak-information-rate by ID

    Delete operation of resource: peak-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_connectivity_service_end_point_capacity_capacity_by_id(uuid, local_id):  # noqa: E501
    """Delete capacity by ID

    Delete operation of resource: capacity # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_connectivity_service_end_point_capacity_total_size_total_size_by_id(uuid, local_id):  # noqa: E501
    """Delete total-size by ID

    Delete operation of resource: total-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_connectivity_service_end_point_end_point_by_id(uuid, local_id):  # noqa: E501
    """Delete end-point by ID

    Delete operation of resource: end-point # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_connectivity_service_end_point_name_name_by_id(uuid, local_id, value_name):  # noqa: E501
    """Delete name by ID

    Delete operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_connectivity_service_latency_characteristic_latency_characteristic_by_id(uuid, traffic_property_name):  # noqa: E501
    """Delete latency-characteristic by ID

    Delete operation of resource: latency-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param traffic_property_name: ID of traffic_property_name
    :type traffic_property_name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_connectivity_service_name_name_by_id(uuid, value_name):  # noqa: E501
    """Delete name by ID

    Delete operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_connectivity_service_requested_capacity_bandwidth_profile_bandwidth_profile_by_id(uuid):  # noqa: E501
    """Delete bandwidth-profile by ID

    Delete operation of resource: bandwidth-profile # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_connectivity_service_requested_capacity_bandwidth_profile_committed_burst_size_committed_burst_size_by_id(uuid):  # noqa: E501
    """Delete committed-burst-size by ID

    Delete operation of resource: committed-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_connectivity_service_requested_capacity_bandwidth_profile_committed_information_rate_committed_information_rate_by_id(uuid):  # noqa: E501
    """Delete committed-information-rate by ID

    Delete operation of resource: committed-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_connectivity_service_requested_capacity_bandwidth_profile_peak_burst_size_peak_burst_size_by_id(uuid):  # noqa: E501
    """Delete peak-burst-size by ID

    Delete operation of resource: peak-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_connectivity_service_requested_capacity_bandwidth_profile_peak_information_rate_peak_information_rate_by_id(uuid):  # noqa: E501
    """Delete peak-information-rate by ID

    Delete operation of resource: peak-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_connectivity_service_requested_capacity_requested_capacity_by_id(uuid):  # noqa: E501
    """Delete requested-capacity by ID

    Delete operation of resource: requested-capacity # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_connectivity_service_requested_capacity_total_size_total_size_by_id(uuid):  # noqa: E501
    """Delete total-size by ID

    Delete operation of resource: total-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_connectivity_service_resilience_type_resilience_type_by_id(uuid):  # noqa: E501
    """Delete resilience-type by ID

    Delete operation of resource: resilience-type # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_connectivity_service_schedule_schedule_by_id(uuid):  # noqa: E501
    """Delete schedule by ID

    Delete operation of resource: schedule # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_name_name_by_id(value_name):  # noqa: E501
    """Delete name by ID

    Delete operation of resource: name # noqa: E501

    :param value_name: ID of value_name
    :type value_name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_path_comp_service_end_point_end_point_by_id(uuid, local_id):  # noqa: E501
    """Delete end-point by ID

    Delete operation of resource: end-point # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_path_comp_service_end_point_name_name_by_id(uuid, local_id, value_name):  # noqa: E501
    """Delete name by ID

    Delete operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_path_comp_service_name_name_by_id(uuid, value_name):  # noqa: E501
    """Delete name by ID

    Delete operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_path_comp_service_objective_function_name_name_by_id(uuid, value_name):  # noqa: E501
    """Delete name by ID

    Delete operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_path_comp_service_objective_function_objective_function_by_id(uuid):  # noqa: E501
    """Delete objective-function by ID

    Delete operation of resource: objective-function # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_path_comp_service_optimization_constraint_name_name_by_id(uuid, value_name):  # noqa: E501
    """Delete name by ID

    Delete operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_path_comp_service_optimization_constraint_optimization_constraint_by_id(uuid):  # noqa: E501
    """Delete optimization-constraint by ID

    Delete operation of resource: optimization-constraint # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_path_comp_service_path_comp_service_by_id(uuid):  # noqa: E501
    """Delete path-comp-service by ID

    Delete operation of resource: path-comp-service # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_path_comp_service_routing_constraint_name_name_by_id(uuid, value_name):  # noqa: E501
    """Delete name by ID

    Delete operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_path_comp_service_routing_constraint_routing_constraint_by_id(uuid):  # noqa: E501
    """Delete routing-constraint by ID

    Delete operation of resource: routing-constraint # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_service_interface_point_name_name_by_id(uuid, value_name):  # noqa: E501
    """Delete name by ID

    Delete operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_context_service_interface_point_service_interface_point_by_id(uuid):  # noqa: E501
    """Delete service-interface-point by ID

    Delete operation of resource: service-interface-point # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def retrieve_context():  # noqa: E501
    """Retrieve context

    Retrieve operation of resource: context # noqa: E501


    :rtype: TapiContext
    """
    return database.context


def retrieve_context_connection_connection():  # noqa: E501
    """Retrieve connection

    Retrieve operation of resource: connection # noqa: E501


    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_connection_connection_by_id(uuid):  # noqa: E501
    """Retrieve connection by ID

    Retrieve operation of resource: connection # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: Connection
    """
    return 'do some magic!'


def retrieve_context_connection_name_name(uuid):  # noqa: E501
    """Retrieve name

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_connection_name_name_by_id(uuid, value_name):  # noqa: E501
    """Retrieve name by ID

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: NameAndValue
    """
    return 'do some magic!'


def retrieve_context_connection_route_name_name(uuid, local_id):  # noqa: E501
    """Retrieve name

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_connection_route_name_name_by_id(uuid, local_id, value_name):  # noqa: E501
    """Retrieve name by ID

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: NameAndValue
    """
    return 'do some magic!'


def retrieve_context_connection_route_route(uuid):  # noqa: E501
    """Retrieve route

    Retrieve operation of resource: route # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_connection_route_route_by_id(uuid, local_id):  # noqa: E501
    """Retrieve route by ID

    Retrieve operation of resource: route # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str

    :rtype: Route
    """
    return 'do some magic!'


def retrieve_context_connection_switch_control_name_name(uuid, switch_control_uuid):  # noqa: E501
    """Retrieve name

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param switch_control_uuid: ID of switch_control_uuid
    :type switch_control_uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_connection_switch_control_name_name_by_id(uuid, switch_control_uuid, value_name):  # noqa: E501
    """Retrieve name by ID

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param switch_control_uuid: ID of switch_control_uuid
    :type switch_control_uuid: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: NameAndValue
    """
    return 'do some magic!'


def retrieve_context_connection_switch_control_resilience_type_resilience_type(uuid, switch_control_uuid):  # noqa: E501
    """Retrieve resilience-type

    Retrieve operation of resource: resilience-type # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param switch_control_uuid: ID of switch_control_uuid
    :type switch_control_uuid: str

    :rtype: ResilienceType
    """
    return 'do some magic!'


def retrieve_context_connection_switch_control_switch_control(uuid):  # noqa: E501
    """Retrieve switch-control

    Retrieve operation of resource: switch-control # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_connection_switch_control_switch_control_by_id(uuid, switch_control_uuid):  # noqa: E501
    """Retrieve switch-control by ID

    Retrieve operation of resource: switch-control # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param switch_control_uuid: ID of switch_control_uuid
    :type switch_control_uuid: str

    :rtype: SwitchControl
    """
    return 'do some magic!'


def retrieve_context_connection_switch_control_switch_name_name(uuid, switch_control_uuid, local_id):  # noqa: E501
    """Retrieve name

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param switch_control_uuid: ID of switch_control_uuid
    :type switch_control_uuid: str
    :param local_id: ID of local_id
    :type local_id: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_connection_switch_control_switch_name_name_by_id(uuid, switch_control_uuid, local_id, value_name):  # noqa: E501
    """Retrieve name by ID

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param switch_control_uuid: ID of switch_control_uuid
    :type switch_control_uuid: str
    :param local_id: ID of local_id
    :type local_id: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: NameAndValue
    """
    return 'do some magic!'


def retrieve_context_connection_switch_control_switch_switch(uuid, switch_control_uuid):  # noqa: E501
    """Retrieve switch

    Retrieve operation of resource: switch # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param switch_control_uuid: ID of switch_control_uuid
    :type switch_control_uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_connection_switch_control_switch_switch_by_id(uuid, switch_control_uuid, local_id):  # noqa: E501
    """Retrieve switch by ID

    Retrieve operation of resource: switch # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param switch_control_uuid: ID of switch_control_uuid
    :type switch_control_uuid: str
    :param local_id: ID of local_id
    :type local_id: str

    :rtype: Switch
    """
    return 'do some magic!'


def retrieve_context_connectivity_service_connectivity_service():  # noqa: E501
    """Retrieve connectivity-service

    Retrieve operation of resource: connectivity-service # noqa: E501


    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_connectivity_service_connectivity_service_by_id(uuid):  # noqa: E501
    """Retrieve connectivity-service by ID

    Retrieve operation of resource: connectivity-service # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: ConnectivityService
    """
    return 'do some magic!'


def retrieve_context_connectivity_service_cost_characteristic_cost_characteristic(uuid):  # noqa: E501
    """Retrieve cost-characteristic

    Retrieve operation of resource: cost-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_connectivity_service_cost_characteristic_cost_characteristic_by_id(uuid, cost_name):  # noqa: E501
    """Retrieve cost-characteristic by ID

    Retrieve operation of resource: cost-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param cost_name: ID of cost_name
    :type cost_name: str

    :rtype: CostCharacteristic
    """
    return 'do some magic!'


def retrieve_context_connectivity_service_end_point_capacity_bandwidth_profile_bandwidth_profile(uuid, local_id):  # noqa: E501
    """Retrieve bandwidth-profile

    Retrieve operation of resource: bandwidth-profile # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str

    :rtype: BandwidthProfile
    """
    return 'do some magic!'


def retrieve_context_connectivity_service_end_point_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(uuid, local_id):  # noqa: E501
    """Retrieve committed-burst-size

    Retrieve operation of resource: committed-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_connectivity_service_end_point_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(uuid, local_id):  # noqa: E501
    """Retrieve committed-information-rate

    Retrieve operation of resource: committed-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_connectivity_service_end_point_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(uuid, local_id):  # noqa: E501
    """Retrieve peak-burst-size

    Retrieve operation of resource: peak-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_connectivity_service_end_point_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(uuid, local_id):  # noqa: E501
    """Retrieve peak-information-rate

    Retrieve operation of resource: peak-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_connectivity_service_end_point_capacity_capacity(uuid, local_id):  # noqa: E501
    """Retrieve capacity

    Retrieve operation of resource: capacity # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str

    :rtype: Capacity
    """
    return 'do some magic!'


def retrieve_context_connectivity_service_end_point_capacity_total_size_total_size(uuid, local_id):  # noqa: E501
    """Retrieve total-size

    Retrieve operation of resource: total-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_connectivity_service_end_point_end_point(uuid):  # noqa: E501
    """Retrieve end-point

    Retrieve operation of resource: end-point # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_connectivity_service_end_point_end_point_by_id(uuid, local_id):  # noqa: E501
    """Retrieve end-point by ID

    Retrieve operation of resource: end-point # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str

    :rtype: ConnectivityServiceEndPoint
    """
    return 'do some magic!'


def retrieve_context_connectivity_service_end_point_name_name(uuid, local_id):  # noqa: E501
    """Retrieve name

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_connectivity_service_end_point_name_name_by_id(uuid, local_id, value_name):  # noqa: E501
    """Retrieve name by ID

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: NameAndValue
    """
    return 'do some magic!'


def retrieve_context_connectivity_service_latency_characteristic_latency_characteristic(uuid):  # noqa: E501
    """Retrieve latency-characteristic

    Retrieve operation of resource: latency-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_connectivity_service_latency_characteristic_latency_characteristic_by_id(uuid, traffic_property_name):  # noqa: E501
    """Retrieve latency-characteristic by ID

    Retrieve operation of resource: latency-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param traffic_property_name: ID of traffic_property_name
    :type traffic_property_name: str

    :rtype: LatencyCharacteristic
    """
    return 'do some magic!'


def retrieve_context_connectivity_service_name_name(uuid):  # noqa: E501
    """Retrieve name

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_connectivity_service_name_name_by_id(uuid, value_name):  # noqa: E501
    """Retrieve name by ID

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: NameAndValue
    """
    return 'do some magic!'


def retrieve_context_connectivity_service_requested_capacity_bandwidth_profile_bandwidth_profile(uuid):  # noqa: E501
    """Retrieve bandwidth-profile

    Retrieve operation of resource: bandwidth-profile # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: BandwidthProfile
    """
    return 'do some magic!'


def retrieve_context_connectivity_service_requested_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(uuid):  # noqa: E501
    """Retrieve committed-burst-size

    Retrieve operation of resource: committed-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_connectivity_service_requested_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(uuid):  # noqa: E501
    """Retrieve committed-information-rate

    Retrieve operation of resource: committed-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_connectivity_service_requested_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(uuid):  # noqa: E501
    """Retrieve peak-burst-size

    Retrieve operation of resource: peak-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_connectivity_service_requested_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(uuid):  # noqa: E501
    """Retrieve peak-information-rate

    Retrieve operation of resource: peak-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_connectivity_service_requested_capacity_requested_capacity(uuid):  # noqa: E501
    """Retrieve requested-capacity

    Retrieve operation of resource: requested-capacity # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: Capacity
    """
    return 'do some magic!'


def retrieve_context_connectivity_service_requested_capacity_total_size_total_size(uuid):  # noqa: E501
    """Retrieve total-size

    Retrieve operation of resource: total-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_connectivity_service_resilience_type_resilience_type(uuid):  # noqa: E501
    """Retrieve resilience-type

    Retrieve operation of resource: resilience-type # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: ResilienceType
    """
    return 'do some magic!'


def retrieve_context_connectivity_service_schedule_schedule(uuid):  # noqa: E501
    """Retrieve schedule

    Retrieve operation of resource: schedule # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: TimeRange
    """
    return 'do some magic!'


def retrieve_context_name_name():  # noqa: E501
    """Retrieve name

    Retrieve operation of resource: name # noqa: E501


    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_name_name_by_id(value_name):  # noqa: E501
    """Retrieve name by ID

    Retrieve operation of resource: name # noqa: E501

    :param value_name: ID of value_name
    :type value_name: str

    :rtype: NameAndValue
    """
    return 'do some magic!'


def retrieve_context_nw_topology_service_name_name():  # noqa: E501
    """Retrieve name

    Retrieve operation of resource: name # noqa: E501


    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_nw_topology_service_name_name_by_id(value_name):  # noqa: E501
    """Retrieve name by ID

    Retrieve operation of resource: name # noqa: E501

    :param value_name: ID of value_name
    :type value_name: str

    :rtype: NameAndValue
    """
    return 'do some magic!'


def retrieve_context_nw_topology_service_nw_topology_service():  # noqa: E501
    """Retrieve nw-topology-service

    Retrieve operation of resource: nw-topology-service # noqa: E501


    :rtype: NetworkTopologyService
    """
    return 'do some magic!'


def retrieve_context_path_comp_service_end_point_end_point(uuid):  # noqa: E501
    """Retrieve end-point

    Retrieve operation of resource: end-point # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_path_comp_service_end_point_end_point_by_id(uuid, local_id):  # noqa: E501
    """Retrieve end-point by ID

    Retrieve operation of resource: end-point # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str

    :rtype: PathServiceEndPoint
    """
    return 'do some magic!'


def retrieve_context_path_comp_service_end_point_name_name(uuid, local_id):  # noqa: E501
    """Retrieve name

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_path_comp_service_end_point_name_name_by_id(uuid, local_id, value_name):  # noqa: E501
    """Retrieve name by ID

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: NameAndValue
    """
    return 'do some magic!'


def retrieve_context_path_comp_service_name_name(uuid):  # noqa: E501
    """Retrieve name

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_path_comp_service_name_name_by_id(uuid, value_name):  # noqa: E501
    """Retrieve name by ID

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: NameAndValue
    """
    return 'do some magic!'


def retrieve_context_path_comp_service_objective_function_name_name(uuid):  # noqa: E501
    """Retrieve name

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_path_comp_service_objective_function_name_name_by_id(uuid, value_name):  # noqa: E501
    """Retrieve name by ID

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: NameAndValue
    """
    return 'do some magic!'


def retrieve_context_path_comp_service_objective_function_objective_function(uuid):  # noqa: E501
    """Retrieve objective-function

    Retrieve operation of resource: objective-function # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: PathObjectiveFunction
    """
    return 'do some magic!'


def retrieve_context_path_comp_service_optimization_constraint_name_name(uuid):  # noqa: E501
    """Retrieve name

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_path_comp_service_optimization_constraint_name_name_by_id(uuid, value_name):  # noqa: E501
    """Retrieve name by ID

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: NameAndValue
    """
    return 'do some magic!'


def retrieve_context_path_comp_service_optimization_constraint_optimization_constraint(uuid):  # noqa: E501
    """Retrieve optimization-constraint

    Retrieve operation of resource: optimization-constraint # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: PathOptimizationConstraint
    """
    return 'do some magic!'


def retrieve_context_path_comp_service_path_comp_service():  # noqa: E501
    """Retrieve path-comp-service

    Retrieve operation of resource: path-comp-service # noqa: E501


    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_path_comp_service_path_comp_service_by_id(uuid):  # noqa: E501
    """Retrieve path-comp-service by ID

    Retrieve operation of resource: path-comp-service # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: PathComputationService
    """
    return 'do some magic!'


def retrieve_context_path_comp_service_routing_constraint_cost_characteristic_cost_characteristic(uuid):  # noqa: E501
    """Retrieve cost-characteristic

    Retrieve operation of resource: cost-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_path_comp_service_routing_constraint_cost_characteristic_cost_characteristic_by_id(uuid, cost_name):  # noqa: E501
    """Retrieve cost-characteristic by ID

    Retrieve operation of resource: cost-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param cost_name: ID of cost_name
    :type cost_name: str

    :rtype: CostCharacteristic
    """
    return 'do some magic!'


def retrieve_context_path_comp_service_routing_constraint_latency_characteristic_latency_characteristic(uuid):  # noqa: E501
    """Retrieve latency-characteristic

    Retrieve operation of resource: latency-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_path_comp_service_routing_constraint_latency_characteristic_latency_characteristic_by_id(uuid, traffic_property_name):  # noqa: E501
    """Retrieve latency-characteristic by ID

    Retrieve operation of resource: latency-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param traffic_property_name: ID of traffic_property_name
    :type traffic_property_name: str

    :rtype: LatencyCharacteristic
    """
    return 'do some magic!'


def retrieve_context_path_comp_service_routing_constraint_name_name(uuid):  # noqa: E501
    """Retrieve name

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_path_comp_service_routing_constraint_name_name_by_id(uuid, value_name):  # noqa: E501
    """Retrieve name by ID

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: NameAndValue
    """
    return 'do some magic!'


def retrieve_context_path_comp_service_routing_constraint_requested_capacity_bandwidth_profile_bandwidth_profile(uuid):  # noqa: E501
    """Retrieve bandwidth-profile

    Retrieve operation of resource: bandwidth-profile # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: BandwidthProfile
    """
    return 'do some magic!'


def retrieve_context_path_comp_service_routing_constraint_requested_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(uuid):  # noqa: E501
    """Retrieve committed-burst-size

    Retrieve operation of resource: committed-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_path_comp_service_routing_constraint_requested_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(uuid):  # noqa: E501
    """Retrieve committed-information-rate

    Retrieve operation of resource: committed-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_path_comp_service_routing_constraint_requested_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(uuid):  # noqa: E501
    """Retrieve peak-burst-size

    Retrieve operation of resource: peak-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_path_comp_service_routing_constraint_requested_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(uuid):  # noqa: E501
    """Retrieve peak-information-rate

    Retrieve operation of resource: peak-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_path_comp_service_routing_constraint_requested_capacity_requested_capacity(uuid):  # noqa: E501
    """Retrieve requested-capacity

    Retrieve operation of resource: requested-capacity # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: Capacity
    """
    return 'do some magic!'


def retrieve_context_path_comp_service_routing_constraint_requested_capacity_total_size_total_size(uuid):  # noqa: E501
    """Retrieve total-size

    Retrieve operation of resource: total-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_path_comp_service_routing_constraint_routing_constraint(uuid):  # noqa: E501
    """Retrieve routing-constraint

    Retrieve operation of resource: routing-constraint # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: RoutingConstraint
    """
    return 'do some magic!'


def retrieve_context_path_name_name(uuid):  # noqa: E501
    """Retrieve name

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_path_name_name_by_id(uuid, value_name):  # noqa: E501
    """Retrieve name by ID

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: NameAndValue
    """
    return 'do some magic!'


def retrieve_context_path_path():  # noqa: E501
    """Retrieve path

    Retrieve operation of resource: path # noqa: E501


    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_path_path_by_id(uuid):  # noqa: E501
    """Retrieve path by ID

    Retrieve operation of resource: path # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: Path
    """
    return 'do some magic!'


def retrieve_context_path_routing_constraint_cost_characteristic_cost_characteristic(uuid):  # noqa: E501
    """Retrieve cost-characteristic

    Retrieve operation of resource: cost-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_path_routing_constraint_cost_characteristic_cost_characteristic_by_id(uuid, cost_name):  # noqa: E501
    """Retrieve cost-characteristic by ID

    Retrieve operation of resource: cost-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param cost_name: ID of cost_name
    :type cost_name: str

    :rtype: CostCharacteristic
    """
    return 'do some magic!'


def retrieve_context_path_routing_constraint_latency_characteristic_latency_characteristic(uuid):  # noqa: E501
    """Retrieve latency-characteristic

    Retrieve operation of resource: latency-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_path_routing_constraint_latency_characteristic_latency_characteristic_by_id(uuid, traffic_property_name):  # noqa: E501
    """Retrieve latency-characteristic by ID

    Retrieve operation of resource: latency-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param traffic_property_name: ID of traffic_property_name
    :type traffic_property_name: str

    :rtype: LatencyCharacteristic
    """
    return 'do some magic!'


def retrieve_context_path_routing_constraint_name_name(uuid):  # noqa: E501
    """Retrieve name

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_path_routing_constraint_name_name_by_id(uuid, value_name):  # noqa: E501
    """Retrieve name by ID

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: NameAndValue
    """
    return 'do some magic!'


def retrieve_context_path_routing_constraint_requested_capacity_bandwidth_profile_bandwidth_profile(uuid):  # noqa: E501
    """Retrieve bandwidth-profile

    Retrieve operation of resource: bandwidth-profile # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: BandwidthProfile
    """
    return 'do some magic!'


def retrieve_context_path_routing_constraint_requested_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(uuid):  # noqa: E501
    """Retrieve committed-burst-size

    Retrieve operation of resource: committed-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_path_routing_constraint_requested_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(uuid):  # noqa: E501
    """Retrieve committed-information-rate

    Retrieve operation of resource: committed-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_path_routing_constraint_requested_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(uuid):  # noqa: E501
    """Retrieve peak-burst-size

    Retrieve operation of resource: peak-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_path_routing_constraint_requested_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(uuid):  # noqa: E501
    """Retrieve peak-information-rate

    Retrieve operation of resource: peak-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_path_routing_constraint_requested_capacity_requested_capacity(uuid):  # noqa: E501
    """Retrieve requested-capacity

    Retrieve operation of resource: requested-capacity # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: Capacity
    """
    return 'do some magic!'


def retrieve_context_path_routing_constraint_requested_capacity_total_size_total_size(uuid):  # noqa: E501
    """Retrieve total-size

    Retrieve operation of resource: total-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_path_routing_constraint_routing_constraint(uuid):  # noqa: E501
    """Retrieve routing-constraint

    Retrieve operation of resource: routing-constraint # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: RoutingConstraint
    """
    return 'do some magic!'


def retrieve_context_service_interface_point_available_capacity_available_capacity(uuid):  # noqa: E501
    """Retrieve available-capacity

    Retrieve operation of resource: available-capacity # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: Capacity
    """
    return 'do some magic!'


def retrieve_context_service_interface_point_available_capacity_bandwidth_profile_bandwidth_profile(uuid):  # noqa: E501
    """Retrieve bandwidth-profile

    Retrieve operation of resource: bandwidth-profile # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: BandwidthProfile
    """
    return 'do some magic!'


def retrieve_context_service_interface_point_available_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(uuid):  # noqa: E501
    """Retrieve committed-burst-size

    Retrieve operation of resource: committed-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_service_interface_point_available_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(uuid):  # noqa: E501
    """Retrieve committed-information-rate

    Retrieve operation of resource: committed-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_service_interface_point_available_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(uuid):  # noqa: E501
    """Retrieve peak-burst-size

    Retrieve operation of resource: peak-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_service_interface_point_available_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(uuid):  # noqa: E501
    """Retrieve peak-information-rate

    Retrieve operation of resource: peak-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_service_interface_point_available_capacity_total_size_total_size(uuid):  # noqa: E501
    """Retrieve total-size

    Retrieve operation of resource: total-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_service_interface_point_name_name(uuid):  # noqa: E501
    """Retrieve name

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_service_interface_point_name_name_by_id(uuid, value_name):  # noqa: E501
    """Retrieve name by ID

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: NameAndValue
    """
    return 'do some magic!'


def retrieve_context_service_interface_point_service_interface_point():  # noqa: E501
    """Retrieve service-interface-point

    Retrieve operation of resource: service-interface-point # noqa: E501


    :rtype: List[str]
    """
    uri_list = []
    for sip in database.context.service_interface_point:
        uri="/restconf/config/context/service-interface-point/"+sip.uuid
        uri_list.append(uri)
    return uri_list


def retrieve_context_service_interface_point_service_interface_point_by_id(uuid):  # noqa: E501
    """Retrieve service-interface-point by ID

    Retrieve operation of resource: service-interface-point # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: ServiceInterfacePoint
    """
    for sip in database.context.service_interface_point:
        if sip.uuid == uuid:
           return sip


def retrieve_context_service_interface_point_total_potential_capacity_bandwidth_profile_bandwidth_profile(uuid):  # noqa: E501
    """Retrieve bandwidth-profile

    Retrieve operation of resource: bandwidth-profile # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: BandwidthProfile
    """
    return 'do some magic!'


def retrieve_context_service_interface_point_total_potential_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(uuid):  # noqa: E501
    """Retrieve committed-burst-size

    Retrieve operation of resource: committed-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_service_interface_point_total_potential_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(uuid):  # noqa: E501
    """Retrieve committed-information-rate

    Retrieve operation of resource: committed-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_service_interface_point_total_potential_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(uuid):  # noqa: E501
    """Retrieve peak-burst-size

    Retrieve operation of resource: peak-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_service_interface_point_total_potential_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(uuid):  # noqa: E501
    """Retrieve peak-information-rate

    Retrieve operation of resource: peak-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_service_interface_point_total_potential_capacity_total_potential_capacity(uuid):  # noqa: E501
    """Retrieve total-potential-capacity

    Retrieve operation of resource: total-potential-capacity # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: Capacity
    """
    return 'do some magic!'


def retrieve_context_service_interface_point_total_potential_capacity_total_size_total_size(uuid):  # noqa: E501
    """Retrieve total-size

    Retrieve operation of resource: total-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_link_available_capacity_available_capacity(uuid, link_uuid):  # noqa: E501
    """Retrieve available-capacity

    Retrieve operation of resource: available-capacity # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param link_uuid: ID of link_uuid
    :type link_uuid: str

    :rtype: Capacity
    """
    return 'do some magic!'


def retrieve_context_topology_link_available_capacity_bandwidth_profile_bandwidth_profile(uuid, link_uuid):  # noqa: E501
    """Retrieve bandwidth-profile

    Retrieve operation of resource: bandwidth-profile # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param link_uuid: ID of link_uuid
    :type link_uuid: str

    :rtype: BandwidthProfile
    """
    return 'do some magic!'


def retrieve_context_topology_link_available_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(uuid, link_uuid):  # noqa: E501
    """Retrieve committed-burst-size

    Retrieve operation of resource: committed-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param link_uuid: ID of link_uuid
    :type link_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_link_available_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(uuid, link_uuid):  # noqa: E501
    """Retrieve committed-information-rate

    Retrieve operation of resource: committed-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param link_uuid: ID of link_uuid
    :type link_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_link_available_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(uuid, link_uuid):  # noqa: E501
    """Retrieve peak-burst-size

    Retrieve operation of resource: peak-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param link_uuid: ID of link_uuid
    :type link_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_link_available_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(uuid, link_uuid):  # noqa: E501
    """Retrieve peak-information-rate

    Retrieve operation of resource: peak-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param link_uuid: ID of link_uuid
    :type link_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_link_available_capacity_total_size_total_size(uuid, link_uuid):  # noqa: E501
    """Retrieve total-size

    Retrieve operation of resource: total-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param link_uuid: ID of link_uuid
    :type link_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_link_cost_characteristic_cost_characteristic(uuid, link_uuid):  # noqa: E501
    """Retrieve cost-characteristic

    Retrieve operation of resource: cost-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param link_uuid: ID of link_uuid
    :type link_uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_topology_link_cost_characteristic_cost_characteristic_by_id(uuid, link_uuid, cost_name):  # noqa: E501
    """Retrieve cost-characteristic by ID

    Retrieve operation of resource: cost-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param link_uuid: ID of link_uuid
    :type link_uuid: str
    :param cost_name: ID of cost_name
    :type cost_name: str

    :rtype: CostCharacteristic
    """
    return 'do some magic!'


def retrieve_context_topology_link_latency_characteristic_latency_characteristic(uuid, link_uuid):  # noqa: E501
    """Retrieve latency-characteristic

    Retrieve operation of resource: latency-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param link_uuid: ID of link_uuid
    :type link_uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_topology_link_latency_characteristic_latency_characteristic_by_id(uuid, link_uuid, traffic_property_name):  # noqa: E501
    """Retrieve latency-characteristic by ID

    Retrieve operation of resource: latency-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param link_uuid: ID of link_uuid
    :type link_uuid: str
    :param traffic_property_name: ID of traffic_property_name
    :type traffic_property_name: str

    :rtype: LatencyCharacteristic
    """
    return 'do some magic!'


def retrieve_context_topology_link_link(uuid):  # noqa: E501
    """Retrieve link

    Retrieve operation of resource: link # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: List[str]
    """
    uri_list = []
    for topo in database.context.topology:
        if topo.uuid == uuid:
            for link in topo.link:
                uri="/restconf/config/context/topology/"+uuid+"/node/"+link.uuid
                uri_list.append(uri)
            return uri_list


def retrieve_context_topology_link_link_by_id(uuid, link_uuid):  # noqa: E501
    """Retrieve link by ID

    Retrieve operation of resource: link # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param link_uuid: ID of link_uuid
    :type link_uuid: str

    :rtype: Link
    """
    for topo in database.context.topology:
        if topo.uuid == uuid:
            for link in topo.link:
                if link.uuid == link_uuid:
                    return link


def retrieve_context_topology_link_name_name(uuid, link_uuid):  # noqa: E501
    """Retrieve name

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param link_uuid: ID of link_uuid
    :type link_uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_topology_link_name_name_by_id(uuid, link_uuid, value_name):  # noqa: E501
    """Retrieve name by ID

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param link_uuid: ID of link_uuid
    :type link_uuid: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: NameAndValue
    """
    return 'do some magic!'


def retrieve_context_topology_link_resilience_type_resilience_type(uuid, link_uuid):  # noqa: E501
    """Retrieve resilience-type

    Retrieve operation of resource: resilience-type # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param link_uuid: ID of link_uuid
    :type link_uuid: str

    :rtype: ResilienceType
    """
    return 'do some magic!'


def retrieve_context_topology_link_risk_characteristic_risk_characteristic(uuid, link_uuid):  # noqa: E501
    """Retrieve risk-characteristic

    Retrieve operation of resource: risk-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param link_uuid: ID of link_uuid
    :type link_uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_topology_link_risk_characteristic_risk_characteristic_by_id(uuid, link_uuid, risk_characteristic_name):  # noqa: E501
    """Retrieve risk-characteristic by ID

    Retrieve operation of resource: risk-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param link_uuid: ID of link_uuid
    :type link_uuid: str
    :param risk_characteristic_name: ID of risk_characteristic_name
    :type risk_characteristic_name: str

    :rtype: RiskCharacteristic
    """
    return 'do some magic!'


def retrieve_context_topology_link_total_potential_capacity_bandwidth_profile_bandwidth_profile(uuid, link_uuid):  # noqa: E501
    """Retrieve bandwidth-profile

    Retrieve operation of resource: bandwidth-profile # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param link_uuid: ID of link_uuid
    :type link_uuid: str

    :rtype: BandwidthProfile
    """
    return 'do some magic!'


def retrieve_context_topology_link_total_potential_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(uuid, link_uuid):  # noqa: E501
    """Retrieve committed-burst-size

    Retrieve operation of resource: committed-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param link_uuid: ID of link_uuid
    :type link_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_link_total_potential_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(uuid, link_uuid):  # noqa: E501
    """Retrieve committed-information-rate

    Retrieve operation of resource: committed-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param link_uuid: ID of link_uuid
    :type link_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_link_total_potential_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(uuid, link_uuid):  # noqa: E501
    """Retrieve peak-burst-size

    Retrieve operation of resource: peak-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param link_uuid: ID of link_uuid
    :type link_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_link_total_potential_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(uuid, link_uuid):  # noqa: E501
    """Retrieve peak-information-rate

    Retrieve operation of resource: peak-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param link_uuid: ID of link_uuid
    :type link_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_link_total_potential_capacity_total_potential_capacity(uuid, link_uuid):  # noqa: E501
    """Retrieve total-potential-capacity

    Retrieve operation of resource: total-potential-capacity # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param link_uuid: ID of link_uuid
    :type link_uuid: str

    :rtype: Capacity
    """
    return 'do some magic!'


def retrieve_context_topology_link_total_potential_capacity_total_size_total_size(uuid, link_uuid):  # noqa: E501
    """Retrieve total-size

    Retrieve operation of resource: total-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param link_uuid: ID of link_uuid
    :type link_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_link_validation_mechanism_validation_mechanism(uuid, link_uuid):  # noqa: E501
    """Retrieve validation-mechanism

    Retrieve operation of resource: validation-mechanism # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param link_uuid: ID of link_uuid
    :type link_uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_topology_link_validation_mechanism_validation_mechanism_by_id(uuid, link_uuid, validation_mechanism):  # noqa: E501
    """Retrieve validation-mechanism by ID

    Retrieve operation of resource: validation-mechanism # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param link_uuid: ID of link_uuid
    :type link_uuid: str
    :param validation_mechanism: ID of validation_mechanism
    :type validation_mechanism: str

    :rtype: ValidationMechanism
    """
    return 'do some magic!'


def retrieve_context_topology_name_name(uuid):  # noqa: E501
    """Retrieve name

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_topology_name_name_by_id(uuid, value_name):  # noqa: E501
    """Retrieve name by ID

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: NameAndValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_available_capacity_available_capacity(uuid, node_uuid):  # noqa: E501
    """Retrieve available-capacity

    Retrieve operation of resource: available-capacity # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str

    :rtype: Capacity
    """
    return 'do some magic!'


def retrieve_context_topology_node_available_capacity_bandwidth_profile_bandwidth_profile(uuid, node_uuid):  # noqa: E501
    """Retrieve bandwidth-profile

    Retrieve operation of resource: bandwidth-profile # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str

    :rtype: BandwidthProfile
    """
    return 'do some magic!'


def retrieve_context_topology_node_available_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(uuid, node_uuid):  # noqa: E501
    """Retrieve committed-burst-size

    Retrieve operation of resource: committed-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_available_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(uuid, node_uuid):  # noqa: E501
    """Retrieve committed-information-rate

    Retrieve operation of resource: committed-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_available_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(uuid, node_uuid):  # noqa: E501
    """Retrieve peak-burst-size

    Retrieve operation of resource: peak-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_available_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(uuid, node_uuid):  # noqa: E501
    """Retrieve peak-information-rate

    Retrieve operation of resource: peak-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_available_capacity_total_size_total_size(uuid, node_uuid):  # noqa: E501
    """Retrieve total-size

    Retrieve operation of resource: total-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_cost_characteristic_cost_characteristic(uuid, node_uuid):  # noqa: E501
    """Retrieve cost-characteristic

    Retrieve operation of resource: cost-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_topology_node_cost_characteristic_cost_characteristic_by_id(uuid, node_uuid, cost_name):  # noqa: E501
    """Retrieve cost-characteristic by ID

    Retrieve operation of resource: cost-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param cost_name: ID of cost_name
    :type cost_name: str

    :rtype: CostCharacteristic
    """
    return 'do some magic!'


def retrieve_context_topology_node_latency_characteristic_latency_characteristic(uuid, node_uuid):  # noqa: E501
    """Retrieve latency-characteristic

    Retrieve operation of resource: latency-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_topology_node_latency_characteristic_latency_characteristic_by_id(uuid, node_uuid, traffic_property_name):  # noqa: E501
    """Retrieve latency-characteristic by ID

    Retrieve operation of resource: latency-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param traffic_property_name: ID of traffic_property_name
    :type traffic_property_name: str

    :rtype: LatencyCharacteristic
    """
    return 'do some magic!'


def retrieve_context_topology_node_name_name(uuid, node_uuid):  # noqa: E501
    """Retrieve name

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_topology_node_name_name_by_id(uuid, node_uuid, value_name):  # noqa: E501
    """Retrieve name by ID

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: NameAndValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_node(uuid):  # noqa: E501
    """Retrieve node

    Retrieve operation of resource: node # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: List[str]
    """
    uri_list = []
    for topo in database.context.topology:
        if topo.uuid == uuid:
            for node in topo.node:
                uri="/restconf/config/context/topology/"+uuid+"/node/"+node.uuid
                uri_list.append(uri)
            return uri_list


def retrieve_context_topology_node_node_by_id(uuid, node_uuid):  # noqa: E501
    """Retrieve node by ID

    Retrieve operation of resource: node # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str

    :rtype: Node
    """
    for topo in database.context.topology:
        if topo.uuid == uuid:
            for node in topo.node:
                if node.uuid == node_uuid:
                    return node


def retrieve_context_topology_node_node_rule_group_available_capacity_available_capacity(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """Retrieve available-capacity

    Retrieve operation of resource: available-capacity # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str

    :rtype: Capacity
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_available_capacity_bandwidth_profile_bandwidth_profile(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """Retrieve bandwidth-profile

    Retrieve operation of resource: bandwidth-profile # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str

    :rtype: BandwidthProfile
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_available_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """Retrieve committed-burst-size

    Retrieve operation of resource: committed-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_available_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """Retrieve committed-information-rate

    Retrieve operation of resource: committed-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_available_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """Retrieve peak-burst-size

    Retrieve operation of resource: peak-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_available_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """Retrieve peak-information-rate

    Retrieve operation of resource: peak-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_available_capacity_total_size_total_size(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """Retrieve total-size

    Retrieve operation of resource: total-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_cost_characteristic_cost_characteristic(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """Retrieve cost-characteristic

    Retrieve operation of resource: cost-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_cost_characteristic_cost_characteristic_by_id(uuid, node_uuid, node_rule_group_uuid, cost_name):  # noqa: E501
    """Retrieve cost-characteristic by ID

    Retrieve operation of resource: cost-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param cost_name: ID of cost_name
    :type cost_name: str

    :rtype: CostCharacteristic
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_inter_rule_group_available_capacity_available_capacity(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """Retrieve available-capacity

    Retrieve operation of resource: available-capacity # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: ID of inter_rule_group_uuid
    :type inter_rule_group_uuid: str

    :rtype: Capacity
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_inter_rule_group_available_capacity_bandwidth_profile_bandwidth_profile(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """Retrieve bandwidth-profile

    Retrieve operation of resource: bandwidth-profile # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: ID of inter_rule_group_uuid
    :type inter_rule_group_uuid: str

    :rtype: BandwidthProfile
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_inter_rule_group_available_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """Retrieve committed-burst-size

    Retrieve operation of resource: committed-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: ID of inter_rule_group_uuid
    :type inter_rule_group_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_inter_rule_group_available_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """Retrieve committed-information-rate

    Retrieve operation of resource: committed-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: ID of inter_rule_group_uuid
    :type inter_rule_group_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_inter_rule_group_available_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """Retrieve peak-burst-size

    Retrieve operation of resource: peak-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: ID of inter_rule_group_uuid
    :type inter_rule_group_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_inter_rule_group_available_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """Retrieve peak-information-rate

    Retrieve operation of resource: peak-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: ID of inter_rule_group_uuid
    :type inter_rule_group_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_inter_rule_group_available_capacity_total_size_total_size(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """Retrieve total-size

    Retrieve operation of resource: total-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: ID of inter_rule_group_uuid
    :type inter_rule_group_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_inter_rule_group_cost_characteristic_cost_characteristic(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """Retrieve cost-characteristic

    Retrieve operation of resource: cost-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: ID of inter_rule_group_uuid
    :type inter_rule_group_uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_inter_rule_group_cost_characteristic_cost_characteristic_by_id(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid, cost_name):  # noqa: E501
    """Retrieve cost-characteristic by ID

    Retrieve operation of resource: cost-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: ID of inter_rule_group_uuid
    :type inter_rule_group_uuid: str
    :param cost_name: ID of cost_name
    :type cost_name: str

    :rtype: CostCharacteristic
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_inter_rule_group_inter_rule_group(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """Retrieve inter-rule-group

    Retrieve operation of resource: inter-rule-group # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_inter_rule_group_inter_rule_group_by_id(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """Retrieve inter-rule-group by ID

    Retrieve operation of resource: inter-rule-group # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: ID of inter_rule_group_uuid
    :type inter_rule_group_uuid: str

    :rtype: InterRuleGroup
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_inter_rule_group_latency_characteristic_latency_characteristic(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """Retrieve latency-characteristic

    Retrieve operation of resource: latency-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: ID of inter_rule_group_uuid
    :type inter_rule_group_uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_inter_rule_group_latency_characteristic_latency_characteristic_by_id(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid, traffic_property_name):  # noqa: E501
    """Retrieve latency-characteristic by ID

    Retrieve operation of resource: latency-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: ID of inter_rule_group_uuid
    :type inter_rule_group_uuid: str
    :param traffic_property_name: ID of traffic_property_name
    :type traffic_property_name: str

    :rtype: LatencyCharacteristic
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_inter_rule_group_name_name(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """Retrieve name

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: ID of inter_rule_group_uuid
    :type inter_rule_group_uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_inter_rule_group_name_name_by_id(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid, value_name):  # noqa: E501
    """Retrieve name by ID

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: ID of inter_rule_group_uuid
    :type inter_rule_group_uuid: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: NameAndValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_inter_rule_group_risk_characteristic_risk_characteristic(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """Retrieve risk-characteristic

    Retrieve operation of resource: risk-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: ID of inter_rule_group_uuid
    :type inter_rule_group_uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_inter_rule_group_risk_characteristic_risk_characteristic_by_id(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid, risk_characteristic_name):  # noqa: E501
    """Retrieve risk-characteristic by ID

    Retrieve operation of resource: risk-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: ID of inter_rule_group_uuid
    :type inter_rule_group_uuid: str
    :param risk_characteristic_name: ID of risk_characteristic_name
    :type risk_characteristic_name: str

    :rtype: RiskCharacteristic
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_inter_rule_group_rule_name_name(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid, local_id):  # noqa: E501
    """Retrieve name

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: ID of inter_rule_group_uuid
    :type inter_rule_group_uuid: str
    :param local_id: ID of local_id
    :type local_id: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_inter_rule_group_rule_name_name_by_id(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid, local_id, value_name):  # noqa: E501
    """Retrieve name by ID

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: ID of inter_rule_group_uuid
    :type inter_rule_group_uuid: str
    :param local_id: ID of local_id
    :type local_id: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: NameAndValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_inter_rule_group_rule_rule(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """Retrieve rule

    Retrieve operation of resource: rule # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: ID of inter_rule_group_uuid
    :type inter_rule_group_uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_inter_rule_group_rule_rule_by_id(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid, local_id):  # noqa: E501
    """Retrieve rule by ID

    Retrieve operation of resource: rule # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: ID of inter_rule_group_uuid
    :type inter_rule_group_uuid: str
    :param local_id: ID of local_id
    :type local_id: str

    :rtype: Rule
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_inter_rule_group_total_potential_capacity_bandwidth_profile_bandwidth_profile(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """Retrieve bandwidth-profile

    Retrieve operation of resource: bandwidth-profile # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: ID of inter_rule_group_uuid
    :type inter_rule_group_uuid: str

    :rtype: BandwidthProfile
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_inter_rule_group_total_potential_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """Retrieve committed-burst-size

    Retrieve operation of resource: committed-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: ID of inter_rule_group_uuid
    :type inter_rule_group_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_inter_rule_group_total_potential_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """Retrieve committed-information-rate

    Retrieve operation of resource: committed-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: ID of inter_rule_group_uuid
    :type inter_rule_group_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_inter_rule_group_total_potential_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """Retrieve peak-burst-size

    Retrieve operation of resource: peak-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: ID of inter_rule_group_uuid
    :type inter_rule_group_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_inter_rule_group_total_potential_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """Retrieve peak-information-rate

    Retrieve operation of resource: peak-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: ID of inter_rule_group_uuid
    :type inter_rule_group_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_inter_rule_group_total_potential_capacity_total_potential_capacity(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """Retrieve total-potential-capacity

    Retrieve operation of resource: total-potential-capacity # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: ID of inter_rule_group_uuid
    :type inter_rule_group_uuid: str

    :rtype: Capacity
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_inter_rule_group_total_potential_capacity_total_size_total_size(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """Retrieve total-size

    Retrieve operation of resource: total-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: ID of inter_rule_group_uuid
    :type inter_rule_group_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_latency_characteristic_latency_characteristic(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """Retrieve latency-characteristic

    Retrieve operation of resource: latency-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_latency_characteristic_latency_characteristic_by_id(uuid, node_uuid, node_rule_group_uuid, traffic_property_name):  # noqa: E501
    """Retrieve latency-characteristic by ID

    Retrieve operation of resource: latency-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param traffic_property_name: ID of traffic_property_name
    :type traffic_property_name: str

    :rtype: LatencyCharacteristic
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_name_name(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """Retrieve name

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_name_name_by_id(uuid, node_uuid, node_rule_group_uuid, value_name):  # noqa: E501
    """Retrieve name by ID

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: NameAndValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_node_rule_group(uuid, node_uuid):  # noqa: E501
    """Retrieve node-rule-group

    Retrieve operation of resource: node-rule-group # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_node_rule_group_by_id(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """Retrieve node-rule-group by ID

    Retrieve operation of resource: node-rule-group # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str

    :rtype: NodeRuleGroup
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_risk_characteristic_risk_characteristic(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """Retrieve risk-characteristic

    Retrieve operation of resource: risk-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_risk_characteristic_risk_characteristic_by_id(uuid, node_uuid, node_rule_group_uuid, risk_characteristic_name):  # noqa: E501
    """Retrieve risk-characteristic by ID

    Retrieve operation of resource: risk-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param risk_characteristic_name: ID of risk_characteristic_name
    :type risk_characteristic_name: str

    :rtype: RiskCharacteristic
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_rule_name_name(uuid, node_uuid, node_rule_group_uuid, local_id):  # noqa: E501
    """Retrieve name

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param local_id: ID of local_id
    :type local_id: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_rule_name_name_by_id(uuid, node_uuid, node_rule_group_uuid, local_id, value_name):  # noqa: E501
    """Retrieve name by ID

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param local_id: ID of local_id
    :type local_id: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: NameAndValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_rule_rule(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """Retrieve rule

    Retrieve operation of resource: rule # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_rule_rule_by_id(uuid, node_uuid, node_rule_group_uuid, local_id):  # noqa: E501
    """Retrieve rule by ID

    Retrieve operation of resource: rule # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str
    :param local_id: ID of local_id
    :type local_id: str

    :rtype: Rule
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_total_potential_capacity_bandwidth_profile_bandwidth_profile(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """Retrieve bandwidth-profile

    Retrieve operation of resource: bandwidth-profile # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str

    :rtype: BandwidthProfile
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_total_potential_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """Retrieve committed-burst-size

    Retrieve operation of resource: committed-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_total_potential_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """Retrieve committed-information-rate

    Retrieve operation of resource: committed-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_total_potential_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """Retrieve peak-burst-size

    Retrieve operation of resource: peak-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_total_potential_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """Retrieve peak-information-rate

    Retrieve operation of resource: peak-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_total_potential_capacity_total_potential_capacity(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """Retrieve total-potential-capacity

    Retrieve operation of resource: total-potential-capacity # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str

    :rtype: Capacity
    """
    return 'do some magic!'


def retrieve_context_topology_node_node_rule_group_total_potential_capacity_total_size_total_size(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """Retrieve total-size

    Retrieve operation of resource: total-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param node_rule_group_uuid: ID of node_rule_group_uuid
    :type node_rule_group_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_owned_node_edge_point_available_capacity_available_capacity(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """Retrieve available-capacity

    Retrieve operation of resource: available-capacity # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param owned_node_edge_point_uuid: ID of owned_node_edge_point_uuid
    :type owned_node_edge_point_uuid: str

    :rtype: Capacity
    """
    return 'do some magic!'


def retrieve_context_topology_node_owned_node_edge_point_available_capacity_bandwidth_profile_bandwidth_profile(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """Retrieve bandwidth-profile

    Retrieve operation of resource: bandwidth-profile # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param owned_node_edge_point_uuid: ID of owned_node_edge_point_uuid
    :type owned_node_edge_point_uuid: str

    :rtype: BandwidthProfile
    """
    return 'do some magic!'


def retrieve_context_topology_node_owned_node_edge_point_available_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """Retrieve committed-burst-size

    Retrieve operation of resource: committed-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param owned_node_edge_point_uuid: ID of owned_node_edge_point_uuid
    :type owned_node_edge_point_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_owned_node_edge_point_available_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """Retrieve committed-information-rate

    Retrieve operation of resource: committed-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param owned_node_edge_point_uuid: ID of owned_node_edge_point_uuid
    :type owned_node_edge_point_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_owned_node_edge_point_available_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """Retrieve peak-burst-size

    Retrieve operation of resource: peak-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param owned_node_edge_point_uuid: ID of owned_node_edge_point_uuid
    :type owned_node_edge_point_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_owned_node_edge_point_available_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """Retrieve peak-information-rate

    Retrieve operation of resource: peak-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param owned_node_edge_point_uuid: ID of owned_node_edge_point_uuid
    :type owned_node_edge_point_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_owned_node_edge_point_available_capacity_total_size_total_size(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """Retrieve total-size

    Retrieve operation of resource: total-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param owned_node_edge_point_uuid: ID of owned_node_edge_point_uuid
    :type owned_node_edge_point_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_owned_node_edge_point_connection_end_point_connection_end_point(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """Retrieve connection-end-point

    Retrieve operation of resource: connection-end-point # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param owned_node_edge_point_uuid: ID of owned_node_edge_point_uuid
    :type owned_node_edge_point_uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_topology_node_owned_node_edge_point_connection_end_point_connection_end_point_by_id(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """Retrieve connection-end-point by ID

    Retrieve operation of resource: connection-end-point # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param owned_node_edge_point_uuid: ID of owned_node_edge_point_uuid
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: ID of connection_end_point_uuid
    :type connection_end_point_uuid: str

    :rtype: ConnectionEndPoint
    """
    return 'do some magic!'


def retrieve_context_topology_node_owned_node_edge_point_connection_end_point_name_name(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """Retrieve name

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param owned_node_edge_point_uuid: ID of owned_node_edge_point_uuid
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: ID of connection_end_point_uuid
    :type connection_end_point_uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_topology_node_owned_node_edge_point_connection_end_point_name_name_by_id(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid, value_name):  # noqa: E501
    """Retrieve name by ID

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param owned_node_edge_point_uuid: ID of owned_node_edge_point_uuid
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: ID of connection_end_point_uuid
    :type connection_end_point_uuid: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: NameAndValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_owned_node_edge_point_name_name(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """Retrieve name

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param owned_node_edge_point_uuid: ID of owned_node_edge_point_uuid
    :type owned_node_edge_point_uuid: str

    :rtype: List[str]
    """
    return 'do some magic!'


def retrieve_context_topology_node_owned_node_edge_point_name_name_by_id(uuid, node_uuid, owned_node_edge_point_uuid, value_name):  # noqa: E501
    """Retrieve name by ID

    Retrieve operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param owned_node_edge_point_uuid: ID of owned_node_edge_point_uuid
    :type owned_node_edge_point_uuid: str
    :param value_name: ID of value_name
    :type value_name: str

    :rtype: NameAndValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_owned_node_edge_point_owned_node_edge_point(uuid, node_uuid):  # noqa: E501
    """Retrieve owned-node-edge-point

    Retrieve operation of resource: owned-node-edge-point # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str

    :rtype: List[str]
    """
    uri_list = []
    for topo in database.context.topology:
        if topo.uuid == uuid:
            for node in topo.node:
                if node.uuid == node_uuid:
                    for nep in node.owned_node_edge_point:
                        uri="/restconf/config/context/topology/"+uuid+"/node/"+node_uuid+"/owned-node-edge-point/"+nep.uuid
                        uri_list.append(uri)
                    return uri_list


def retrieve_context_topology_node_owned_node_edge_point_owned_node_edge_point_by_id(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """Retrieve owned-node-edge-point by ID

    Retrieve operation of resource: owned-node-edge-point # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param owned_node_edge_point_uuid: ID of owned_node_edge_point_uuid
    :type owned_node_edge_point_uuid: str

    :rtype: NodeEdgePoint
    """
    for topo in database.context.topology:
        if topo.uuid == uuid:
            for node in topo.node:
                if node.uuid == node_uuid:
                    for nep in node.owned_node_edge_point:
                        if nep.uuid == owned_node_edge_point_uuid:
                            return nep


def retrieve_context_topology_node_owned_node_edge_point_total_potential_capacity_bandwidth_profile_bandwidth_profile(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """Retrieve bandwidth-profile

    Retrieve operation of resource: bandwidth-profile # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param owned_node_edge_point_uuid: ID of owned_node_edge_point_uuid
    :type owned_node_edge_point_uuid: str

    :rtype: BandwidthProfile
    """
    return 'do some magic!'


def retrieve_context_topology_node_owned_node_edge_point_total_potential_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """Retrieve committed-burst-size

    Retrieve operation of resource: committed-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param owned_node_edge_point_uuid: ID of owned_node_edge_point_uuid
    :type owned_node_edge_point_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_owned_node_edge_point_total_potential_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """Retrieve committed-information-rate

    Retrieve operation of resource: committed-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param owned_node_edge_point_uuid: ID of owned_node_edge_point_uuid
    :type owned_node_edge_point_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_owned_node_edge_point_total_potential_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """Retrieve peak-burst-size

    Retrieve operation of resource: peak-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param owned_node_edge_point_uuid: ID of owned_node_edge_point_uuid
    :type owned_node_edge_point_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_owned_node_edge_point_total_potential_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """Retrieve peak-information-rate

    Retrieve operation of resource: peak-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param owned_node_edge_point_uuid: ID of owned_node_edge_point_uuid
    :type owned_node_edge_point_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_owned_node_edge_point_total_potential_capacity_total_potential_capacity(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """Retrieve total-potential-capacity

    Retrieve operation of resource: total-potential-capacity # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param owned_node_edge_point_uuid: ID of owned_node_edge_point_uuid
    :type owned_node_edge_point_uuid: str

    :rtype: Capacity
    """
    return 'do some magic!'


def retrieve_context_topology_node_owned_node_edge_point_total_potential_capacity_total_size_total_size(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """Retrieve total-size

    Retrieve operation of resource: total-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str
    :param owned_node_edge_point_uuid: ID of owned_node_edge_point_uuid
    :type owned_node_edge_point_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_total_potential_capacity_bandwidth_profile_bandwidth_profile(uuid, node_uuid):  # noqa: E501
    """Retrieve bandwidth-profile

    Retrieve operation of resource: bandwidth-profile # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str

    :rtype: BandwidthProfile
    """
    return 'do some magic!'


def retrieve_context_topology_node_total_potential_capacity_bandwidth_profile_committed_burst_size_committed_burst_size(uuid, node_uuid):  # noqa: E501
    """Retrieve committed-burst-size

    Retrieve operation of resource: committed-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_total_potential_capacity_bandwidth_profile_committed_information_rate_committed_information_rate(uuid, node_uuid):  # noqa: E501
    """Retrieve committed-information-rate

    Retrieve operation of resource: committed-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_total_potential_capacity_bandwidth_profile_peak_burst_size_peak_burst_size(uuid, node_uuid):  # noqa: E501
    """Retrieve peak-burst-size

    Retrieve operation of resource: peak-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_total_potential_capacity_bandwidth_profile_peak_information_rate_peak_information_rate(uuid, node_uuid):  # noqa: E501
    """Retrieve peak-information-rate

    Retrieve operation of resource: peak-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_node_total_potential_capacity_total_potential_capacity(uuid, node_uuid):  # noqa: E501
    """Retrieve total-potential-capacity

    Retrieve operation of resource: total-potential-capacity # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str

    :rtype: Capacity
    """
    return 'do some magic!'


def retrieve_context_topology_node_total_potential_capacity_total_size_total_size(uuid, node_uuid):  # noqa: E501
    """Retrieve total-size

    Retrieve operation of resource: total-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param node_uuid: ID of node_uuid
    :type node_uuid: str

    :rtype: CapacityValue
    """
    return 'do some magic!'


def retrieve_context_topology_topology():  # noqa: E501
    """Retrieve topology

    Retrieve operation of resource: topology # noqa: E501


    :rtype: List[str]
    """
    uri_list = []
    for topo in database.context.topology:
        uri="/restconf/config/context/topology/"+topo.uuid
        uri_list.append(uri)
    return uri_list


def retrieve_context_topology_topology_by_id(uuid):  # noqa: E501
    """Retrieve topology by ID

    Retrieve operation of resource: topology # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str

    :rtype: Topology
    """
    for topo in database.context.topology:
        if topo.uuid == uuid:
           return topo


def update_context_by_id(context):  # noqa: E501
    """Update context by ID

    Update operation of resource: context # noqa: E501

    :param context: contextbody object
    :type context: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        context = TapiContext.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_connectivity_service_connectivity_service_by_id(uuid, connectivity_service):  # noqa: E501
    """Update connectivity-service by ID

    Update operation of resource: connectivity-service # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param connectivity_service: connectivity-servicebody object
    :type connectivity_service: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        connectivity_service = ConnectivityService.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_connectivity_service_cost_characteristic_cost_characteristic_by_id(uuid, cost_name, cost_characteristic):  # noqa: E501
    """Update cost-characteristic by ID

    Update operation of resource: cost-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param cost_name: ID of cost_name
    :type cost_name: str
    :param cost_characteristic: cost-characteristicbody object
    :type cost_characteristic: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        cost_characteristic = CostCharacteristic.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_connectivity_service_end_point_capacity_bandwidth_profile_bandwidth_profile_by_id(uuid, local_id, bandwidth_profile):  # noqa: E501
    """Update bandwidth-profile by ID

    Update operation of resource: bandwidth-profile # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str
    :param bandwidth_profile: bandwidth-profilebody object
    :type bandwidth_profile: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        bandwidth_profile = BandwidthProfile.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_connectivity_service_end_point_capacity_bandwidth_profile_committed_burst_size_committed_burst_size_by_id(uuid, local_id, committed_burst_size):  # noqa: E501
    """Update committed-burst-size by ID

    Update operation of resource: committed-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str
    :param committed_burst_size: committed-burst-sizebody object
    :type committed_burst_size: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        committed_burst_size = CapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_connectivity_service_end_point_capacity_bandwidth_profile_committed_information_rate_committed_information_rate_by_id(uuid, local_id, committed_information_rate):  # noqa: E501
    """Update committed-information-rate by ID

    Update operation of resource: committed-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str
    :param committed_information_rate: committed-information-ratebody object
    :type committed_information_rate: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        committed_information_rate = CapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_connectivity_service_end_point_capacity_bandwidth_profile_peak_burst_size_peak_burst_size_by_id(uuid, local_id, peak_burst_size):  # noqa: E501
    """Update peak-burst-size by ID

    Update operation of resource: peak-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str
    :param peak_burst_size: peak-burst-sizebody object
    :type peak_burst_size: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        peak_burst_size = CapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_connectivity_service_end_point_capacity_bandwidth_profile_peak_information_rate_peak_information_rate_by_id(uuid, local_id, peak_information_rate):  # noqa: E501
    """Update peak-information-rate by ID

    Update operation of resource: peak-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str
    :param peak_information_rate: peak-information-ratebody object
    :type peak_information_rate: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        peak_information_rate = CapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_connectivity_service_end_point_capacity_capacity_by_id(uuid, local_id, capacity):  # noqa: E501
    """Update capacity by ID

    Update operation of resource: capacity # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str
    :param capacity: capacitybody object
    :type capacity: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        capacity = Capacity.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_connectivity_service_end_point_capacity_total_size_total_size_by_id(uuid, local_id, total_size):  # noqa: E501
    """Update total-size by ID

    Update operation of resource: total-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str
    :param total_size: total-sizebody object
    :type total_size: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        total_size = CapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_connectivity_service_end_point_end_point_by_id(uuid, local_id, end_point):  # noqa: E501
    """Update end-point by ID

    Update operation of resource: end-point # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str
    :param end_point: end-pointbody object
    :type end_point: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        end_point = ConnectivityServiceEndPoint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_connectivity_service_end_point_name_name_by_id(uuid, local_id, value_name, name):  # noqa: E501
    """Update name by ID

    Update operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str
    :param value_name: ID of value_name
    :type value_name: str
    :param name: namebody object
    :type name: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        name = NameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_connectivity_service_latency_characteristic_latency_characteristic_by_id(uuid, traffic_property_name, latency_characteristic):  # noqa: E501
    """Update latency-characteristic by ID

    Update operation of resource: latency-characteristic # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param traffic_property_name: ID of traffic_property_name
    :type traffic_property_name: str
    :param latency_characteristic: latency-characteristicbody object
    :type latency_characteristic: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        latency_characteristic = LatencyCharacteristic.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_connectivity_service_name_name_by_id(uuid, value_name, name):  # noqa: E501
    """Update name by ID

    Update operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param value_name: ID of value_name
    :type value_name: str
    :param name: namebody object
    :type name: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        name = NameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_connectivity_service_requested_capacity_bandwidth_profile_bandwidth_profile_by_id(uuid, bandwidth_profile):  # noqa: E501
    """Update bandwidth-profile by ID

    Update operation of resource: bandwidth-profile # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param bandwidth_profile: bandwidth-profilebody object
    :type bandwidth_profile: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        bandwidth_profile = BandwidthProfile.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_connectivity_service_requested_capacity_bandwidth_profile_committed_burst_size_committed_burst_size_by_id(uuid, committed_burst_size):  # noqa: E501
    """Update committed-burst-size by ID

    Update operation of resource: committed-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param committed_burst_size: committed-burst-sizebody object
    :type committed_burst_size: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        committed_burst_size = CapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_connectivity_service_requested_capacity_bandwidth_profile_committed_information_rate_committed_information_rate_by_id(uuid, committed_information_rate):  # noqa: E501
    """Update committed-information-rate by ID

    Update operation of resource: committed-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param committed_information_rate: committed-information-ratebody object
    :type committed_information_rate: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        committed_information_rate = CapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_connectivity_service_requested_capacity_bandwidth_profile_peak_burst_size_peak_burst_size_by_id(uuid, peak_burst_size):  # noqa: E501
    """Update peak-burst-size by ID

    Update operation of resource: peak-burst-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param peak_burst_size: peak-burst-sizebody object
    :type peak_burst_size: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        peak_burst_size = CapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_connectivity_service_requested_capacity_bandwidth_profile_peak_information_rate_peak_information_rate_by_id(uuid, peak_information_rate):  # noqa: E501
    """Update peak-information-rate by ID

    Update operation of resource: peak-information-rate # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param peak_information_rate: peak-information-ratebody object
    :type peak_information_rate: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        peak_information_rate = CapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_connectivity_service_requested_capacity_requested_capacity_by_id(uuid, requested_capacity):  # noqa: E501
    """Update requested-capacity by ID

    Update operation of resource: requested-capacity # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param requested_capacity: requested-capacitybody object
    :type requested_capacity: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        requested_capacity = Capacity.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_connectivity_service_requested_capacity_total_size_total_size_by_id(uuid, total_size):  # noqa: E501
    """Update total-size by ID

    Update operation of resource: total-size # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param total_size: total-sizebody object
    :type total_size: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        total_size = CapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_connectivity_service_resilience_type_resilience_type_by_id(uuid, resilience_type):  # noqa: E501
    """Update resilience-type by ID

    Update operation of resource: resilience-type # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param resilience_type: resilience-typebody object
    :type resilience_type: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        resilience_type = ResilienceType.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_connectivity_service_schedule_schedule_by_id(uuid, schedule):  # noqa: E501
    """Update schedule by ID

    Update operation of resource: schedule # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param schedule: schedulebody object
    :type schedule: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        schedule = TimeRange.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_name_name_by_id(value_name, name):  # noqa: E501
    """Update name by ID

    Update operation of resource: name # noqa: E501

    :param value_name: ID of value_name
    :type value_name: str
    :param name: namebody object
    :type name: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        name = NameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_path_comp_service_end_point_end_point_by_id(uuid, local_id, end_point):  # noqa: E501
    """Update end-point by ID

    Update operation of resource: end-point # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str
    :param end_point: end-pointbody object
    :type end_point: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        end_point = PathServiceEndPoint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_path_comp_service_end_point_name_name_by_id(uuid, local_id, value_name, name):  # noqa: E501
    """Update name by ID

    Update operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param local_id: ID of local_id
    :type local_id: str
    :param value_name: ID of value_name
    :type value_name: str
    :param name: namebody object
    :type name: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        name = NameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_path_comp_service_name_name_by_id(uuid, value_name, name):  # noqa: E501
    """Update name by ID

    Update operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param value_name: ID of value_name
    :type value_name: str
    :param name: namebody object
    :type name: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        name = NameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_path_comp_service_objective_function_name_name_by_id(uuid, value_name, name):  # noqa: E501
    """Update name by ID

    Update operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param value_name: ID of value_name
    :type value_name: str
    :param name: namebody object
    :type name: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        name = NameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_path_comp_service_objective_function_objective_function_by_id(uuid, objective_function):  # noqa: E501
    """Update objective-function by ID

    Update operation of resource: objective-function # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param objective_function: objective-functionbody object
    :type objective_function: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        objective_function = PathObjectiveFunction.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_path_comp_service_optimization_constraint_name_name_by_id(uuid, value_name, name):  # noqa: E501
    """Update name by ID

    Update operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param value_name: ID of value_name
    :type value_name: str
    :param name: namebody object
    :type name: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        name = NameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_path_comp_service_optimization_constraint_optimization_constraint_by_id(uuid, optimization_constraint):  # noqa: E501
    """Update optimization-constraint by ID

    Update operation of resource: optimization-constraint # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param optimization_constraint: optimization-constraintbody object
    :type optimization_constraint: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        optimization_constraint = PathOptimizationConstraint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_path_comp_service_path_comp_service_by_id(uuid, path_comp_service):  # noqa: E501
    """Update path-comp-service by ID

    Update operation of resource: path-comp-service # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param path_comp_service: path-comp-servicebody object
    :type path_comp_service: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        path_comp_service = PathComputationService.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_path_comp_service_routing_constraint_name_name_by_id(uuid, value_name, name):  # noqa: E501
    """Update name by ID

    Update operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param value_name: ID of value_name
    :type value_name: str
    :param name: namebody object
    :type name: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        name = NameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_path_comp_service_routing_constraint_routing_constraint_by_id(uuid, routing_constraint):  # noqa: E501
    """Update routing-constraint by ID

    Update operation of resource: routing-constraint # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param routing_constraint: routing-constraintbody object
    :type routing_constraint: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        routing_constraint = RoutingConstraint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_service_interface_point_name_name_by_id(uuid, value_name, name):  # noqa: E501
    """Update name by ID

    Update operation of resource: name # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param value_name: ID of value_name
    :type value_name: str
    :param name: namebody object
    :type name: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        name = NameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_context_service_interface_point_service_interface_point_by_id(uuid, service_interface_point):  # noqa: E501
    """Update service-interface-point by ID

    Update operation of resource: service-interface-point # noqa: E501

    :param uuid: ID of uuid
    :type uuid: str
    :param service_interface_point: service-interface-pointbody object
    :type service_interface_point: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        service_interface_point = ServiceInterfacePoint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
