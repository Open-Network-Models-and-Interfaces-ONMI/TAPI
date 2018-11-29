import connexion
import six

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
from tapi_server.models.tapi_topology_gettopologylist_output import TapiTopologyGettopologylistOutput  # noqa: F401,E501
from tapi_server.models.tapi_topology_gettopologydetails_output import TapiTopologyGettopologydetailsOutput  # noqa: F401,E501
from tapi_server.models.tapi_topology_getnodedetails_output import TapiTopologyGetnodedetailsOutput  # noqa: F401,E501
from tapi_server.models.tapi_topology_getlinkdetails_output import TapiTopologyGetlinkdetailsOutput  # noqa: F401,E501
from tapi_server.models.tapi_topology_getnodeedgepointdetails_output import TapiTopologyGetnodeedgepointdetailsOutput  # noqa: F401,E501
from tapi_server.models.tapi_topology_getlinkdetails_output import TapiTopologyGetlinkdetailsOutput  # noqa: F401,E501
from tapi_server import util
from tapi_server import database


def data_context_topology_context_delete():  # noqa: E501
    """data_context_topology_context_delete

    removes tapi.topology.TopologyContext # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def data_context_topology_context_get():  # noqa: E501
    """data_context_topology_context_get

    returns tapi.topology.TopologyContext # noqa: E501


    :rtype: TapiTopologyTopologyContext
    """
    return 'do some magic!'


def data_context_topology_context_nw_topology_service_get():  # noqa: E501
    """data_context_topology_context_nw_topology_service_get

    returns tapi.topology.NetworkTopologyService # noqa: E501


    :rtype: TapiTopologyNetworkTopologyService
    """
    return 'do some magic!'


def data_context_topology_context_nw_topology_service_namevalue_name_get(value_name):  # noqa: E501
    """data_context_topology_context_nw_topology_service_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_topology_context_nw_topology_service_topologytopology_uuid_get(topology_uuid):  # noqa: E501
    """data_context_topology_context_nw_topology_service_topologytopology_uuid_get

    returns tapi.topology.TopologyRef # noqa: E501

    :param topology_uuid: Id of topology
    :type topology_uuid: str

    :rtype: TapiTopologyTopologyRef
    """
    return 'do some magic!'


def data_context_topology_context_post(tapi_topology_topology_context=None):  # noqa: E501
    """data_context_topology_context_post

    creates tapi.topology.TopologyContext # noqa: E501

    :param tapi_topology_topology_context: tapi.topology.TopologyContext to be added to list
    :type tapi_topology_topology_context: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_topology_topology_context = TapiTopologyTopologyContext.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_topology_context_put(tapi_topology_topology_context=None):  # noqa: E501
    """data_context_topology_context_put

    creates or updates tapi.topology.TopologyContext # noqa: E501

    :param tapi_topology_topology_context: tapi.topology.TopologyContext to be added or updated
    :type tapi_topology_topology_context: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_topology_topology_context = TapiTopologyTopologyContext.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_topology_context_topologyuuid_get(uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_get

    returns tapi.topology.Topology # noqa: E501

    :param uuid: Id of topology
    :type uuid: str

    :rtype: TapiTopologyTopology
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_linklink_uuid_available_capacity_bandwidth_profile_committed_burst_size_get(uuid, link_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_linklink_uuid_available_capacity_bandwidth_profile_committed_burst_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param link_uuid: Id of link
    :type link_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_linklink_uuid_available_capacity_bandwidth_profile_committed_information_rate_get(uuid, link_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_linklink_uuid_available_capacity_bandwidth_profile_committed_information_rate_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param link_uuid: Id of link
    :type link_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_linklink_uuid_available_capacity_bandwidth_profile_get(uuid, link_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_linklink_uuid_available_capacity_bandwidth_profile_get

    returns tapi.common.BandwidthProfile # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param link_uuid: Id of link
    :type link_uuid: str

    :rtype: TapiCommonBandwidthProfile
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_linklink_uuid_available_capacity_bandwidth_profile_peak_burst_size_get(uuid, link_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_linklink_uuid_available_capacity_bandwidth_profile_peak_burst_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param link_uuid: Id of link
    :type link_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_linklink_uuid_available_capacity_bandwidth_profile_peak_information_rate_get(uuid, link_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_linklink_uuid_available_capacity_bandwidth_profile_peak_information_rate_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param link_uuid: Id of link
    :type link_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_linklink_uuid_available_capacity_get(uuid, link_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_linklink_uuid_available_capacity_get

    returns tapi.common.Capacity # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param link_uuid: Id of link
    :type link_uuid: str

    :rtype: TapiCommonCapacity
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_linklink_uuid_available_capacity_total_size_get(uuid, link_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_linklink_uuid_available_capacity_total_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param link_uuid: Id of link
    :type link_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_linklink_uuid_cost_characteristiccost_name_get(uuid, link_uuid, cost_name):  # noqa: E501
    """data_context_topology_context_topologyuuid_linklink_uuid_cost_characteristiccost_name_get

    returns tapi.topology.CostCharacteristic # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param link_uuid: Id of link
    :type link_uuid: str
    :param cost_name: Id of cost-characteristic
    :type cost_name: str

    :rtype: TapiTopologyCostCharacteristic
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_linklink_uuid_get(uuid, link_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_linklink_uuid_get

    returns tapi.topology.Link # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param link_uuid: Id of link
    :type link_uuid: str

    :rtype: TapiTopologyLink
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_linklink_uuid_latency_characteristictraffic_property_name_get(uuid, link_uuid, traffic_property_name):  # noqa: E501
    """data_context_topology_context_topologyuuid_linklink_uuid_latency_characteristictraffic_property_name_get

    returns tapi.topology.LatencyCharacteristic # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param link_uuid: Id of link
    :type link_uuid: str
    :param traffic_property_name: Id of latency-characteristic
    :type traffic_property_name: str

    :rtype: TapiTopologyLatencyCharacteristic
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_linklink_uuid_namevalue_name_get(uuid, link_uuid, value_name):  # noqa: E501
    """data_context_topology_context_topologyuuid_linklink_uuid_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param link_uuid: Id of link
    :type link_uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_linklink_uuid_node_edge_pointtopology_uuidnode_uuidnode_edge_point_uuid_get(uuid, link_uuid, topology_uuid, node_uuid, node_edge_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_linklink_uuid_node_edge_pointtopology_uuidnode_uuidnode_edge_point_uuid_get

    returns tapi.topology.NodeEdgePointRef # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param link_uuid: Id of link
    :type link_uuid: str
    :param topology_uuid: Id of node-edge-point
    :type topology_uuid: str
    :param node_uuid: Id of node-edge-point
    :type node_uuid: str
    :param node_edge_point_uuid: Id of node-edge-point
    :type node_edge_point_uuid: str

    :rtype: TapiTopologyNodeEdgePointRef
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_linklink_uuid_resilience_type_get(uuid, link_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_linklink_uuid_resilience_type_get

    returns tapi.topology.ResilienceType # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param link_uuid: Id of link
    :type link_uuid: str

    :rtype: TapiTopologyResilienceType
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_linklink_uuid_risk_characteristicrisk_characteristic_name_get(uuid, link_uuid, risk_characteristic_name):  # noqa: E501
    """data_context_topology_context_topologyuuid_linklink_uuid_risk_characteristicrisk_characteristic_name_get

    returns tapi.topology.RiskCharacteristic # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param link_uuid: Id of link
    :type link_uuid: str
    :param risk_characteristic_name: Id of risk-characteristic
    :type risk_characteristic_name: str

    :rtype: TapiTopologyRiskCharacteristic
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_linklink_uuid_total_potential_capacity_bandwidth_profile_committed_burst_size_get(uuid, link_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_linklink_uuid_total_potential_capacity_bandwidth_profile_committed_burst_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param link_uuid: Id of link
    :type link_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_linklink_uuid_total_potential_capacity_bandwidth_profile_committed_information_rate_get(uuid, link_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_linklink_uuid_total_potential_capacity_bandwidth_profile_committed_information_rate_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param link_uuid: Id of link
    :type link_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_linklink_uuid_total_potential_capacity_bandwidth_profile_get(uuid, link_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_linklink_uuid_total_potential_capacity_bandwidth_profile_get

    returns tapi.common.BandwidthProfile # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param link_uuid: Id of link
    :type link_uuid: str

    :rtype: TapiCommonBandwidthProfile
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_linklink_uuid_total_potential_capacity_bandwidth_profile_peak_burst_size_get(uuid, link_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_linklink_uuid_total_potential_capacity_bandwidth_profile_peak_burst_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param link_uuid: Id of link
    :type link_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_linklink_uuid_total_potential_capacity_bandwidth_profile_peak_information_rate_get(uuid, link_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_linklink_uuid_total_potential_capacity_bandwidth_profile_peak_information_rate_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param link_uuid: Id of link
    :type link_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_linklink_uuid_total_potential_capacity_get(uuid, link_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_linklink_uuid_total_potential_capacity_get

    returns tapi.common.Capacity # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param link_uuid: Id of link
    :type link_uuid: str

    :rtype: TapiCommonCapacity
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_linklink_uuid_total_potential_capacity_total_size_get(uuid, link_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_linklink_uuid_total_potential_capacity_total_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param link_uuid: Id of link
    :type link_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_linklink_uuid_validation_mechanismvalidation_mechanism_get(uuid, link_uuid, validation_mechanism):  # noqa: E501
    """data_context_topology_context_topologyuuid_linklink_uuid_validation_mechanismvalidation_mechanism_get

    returns tapi.topology.ValidationMechanism # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param link_uuid: Id of link
    :type link_uuid: str
    :param validation_mechanism: Id of validation-mechanism
    :type validation_mechanism: str

    :rtype: TapiTopologyValidationMechanism
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_namevalue_name_get(uuid, value_name):  # noqa: E501
    """data_context_topology_context_topologyuuid_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_aggregated_node_edge_pointtopology_uuidaggregated_node_edge_point_node_uuidnode_edge_point_uuid_get(uuid, node_uuid, topology_uuid, aggregated_node_edge_point_node_uuid, node_edge_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_aggregated_node_edge_pointtopology_uuidaggregated_node_edge_point_node_uuidnode_edge_point_uuid_get

    returns tapi.topology.NodeEdgePointRef # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param topology_uuid: Id of aggregated-node-edge-point
    :type topology_uuid: str
    :param aggregated_node_edge_point_node_uuid: Id of aggregated-node-edge-point
    :type aggregated_node_edge_point_node_uuid: str
    :param node_edge_point_uuid: Id of aggregated-node-edge-point
    :type node_edge_point_uuid: str

    :rtype: TapiTopologyNodeEdgePointRef
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_available_capacity_bandwidth_profile_committed_burst_size_get(uuid, node_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_available_capacity_bandwidth_profile_committed_burst_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_available_capacity_bandwidth_profile_committed_information_rate_get(uuid, node_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_available_capacity_bandwidth_profile_committed_information_rate_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_available_capacity_bandwidth_profile_get(uuid, node_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_available_capacity_bandwidth_profile_get

    returns tapi.common.BandwidthProfile # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str

    :rtype: TapiCommonBandwidthProfile
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_available_capacity_bandwidth_profile_peak_burst_size_get(uuid, node_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_available_capacity_bandwidth_profile_peak_burst_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_available_capacity_bandwidth_profile_peak_information_rate_get(uuid, node_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_available_capacity_bandwidth_profile_peak_information_rate_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_available_capacity_get(uuid, node_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_available_capacity_get

    returns tapi.common.Capacity # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str

    :rtype: TapiCommonCapacity
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_available_capacity_total_size_get(uuid, node_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_available_capacity_total_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_cost_characteristiccost_name_get(uuid, node_uuid, cost_name):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_cost_characteristiccost_name_get

    returns tapi.topology.CostCharacteristic # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param cost_name: Id of cost-characteristic
    :type cost_name: str

    :rtype: TapiTopologyCostCharacteristic
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_encap_topology_get(uuid, node_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_encap_topology_get

    returns tapi.topology.TopologyRef # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str

    :rtype: TapiTopologyTopologyRef
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_get(uuid, node_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_get

    returns tapi.topology.topology.Node # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str

    :rtype: TapiTopologyTopologyNode
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_latency_characteristictraffic_property_name_get(uuid, node_uuid, traffic_property_name):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_latency_characteristictraffic_property_name_get

    returns tapi.topology.LatencyCharacteristic # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param traffic_property_name: Id of latency-characteristic
    :type traffic_property_name: str

    :rtype: TapiTopologyLatencyCharacteristic
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_namevalue_name_get(uuid, node_uuid, value_name):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_available_capacity_bandwidth_profile_committed_burst_size_get(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_available_capacity_bandwidth_profile_committed_burst_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_available_capacity_bandwidth_profile_committed_information_rate_get(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_available_capacity_bandwidth_profile_committed_information_rate_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_available_capacity_bandwidth_profile_get(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_available_capacity_bandwidth_profile_get

    returns tapi.common.BandwidthProfile # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str

    :rtype: TapiCommonBandwidthProfile
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_available_capacity_bandwidth_profile_peak_burst_size_get(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_available_capacity_bandwidth_profile_peak_burst_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_available_capacity_bandwidth_profile_peak_information_rate_get(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_available_capacity_bandwidth_profile_peak_information_rate_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_available_capacity_get(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_available_capacity_get

    returns tapi.common.Capacity # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str

    :rtype: TapiCommonCapacity
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_available_capacity_total_size_get(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_available_capacity_total_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_composed_rule_grouptopology_uuidcomposed_rule_group_node_uuidcomposed_rule_group_node_rule_group_uuid_get(uuid, node_uuid, node_rule_group_uuid, topology_uuid, composed_rule_group_node_uuid, composed_rule_group_node_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_composed_rule_grouptopology_uuidcomposed_rule_group_node_uuidcomposed_rule_group_node_rule_group_uuid_get

    returns tapi.topology.NodeRuleGroupRef # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str
    :param topology_uuid: Id of composed-rule-group
    :type topology_uuid: str
    :param composed_rule_group_node_uuid: Id of composed-rule-group
    :type composed_rule_group_node_uuid: str
    :param composed_rule_group_node_rule_group_uuid: Id of composed-rule-group
    :type composed_rule_group_node_rule_group_uuid: str

    :rtype: TapiTopologyNodeRuleGroupRef
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_cost_characteristiccost_name_get(uuid, node_uuid, node_rule_group_uuid, cost_name):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_cost_characteristiccost_name_get

    returns tapi.topology.CostCharacteristic # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str
    :param cost_name: Id of cost-characteristic
    :type cost_name: str

    :rtype: TapiTopologyCostCharacteristic
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_get(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_get

    returns tapi.topology.NodeRuleGroup # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str

    :rtype: TapiTopologyNodeRuleGroup
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_associated_node_rule_grouptopology_uuidassociated_node_rule_group_node_uuidassociated_node_rule_group_node_rule_group_uuid_get(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid, topology_uuid, associated_node_rule_group_node_uuid, associated_node_rule_group_node_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_associated_node_rule_grouptopology_uuidassociated_node_rule_group_node_uuidassociated_node_rule_group_node_rule_group_uuid_get

    returns tapi.topology.NodeRuleGroupRef # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: Id of inter-rule-group
    :type inter_rule_group_uuid: str
    :param topology_uuid: Id of associated-node-rule-group
    :type topology_uuid: str
    :param associated_node_rule_group_node_uuid: Id of associated-node-rule-group
    :type associated_node_rule_group_node_uuid: str
    :param associated_node_rule_group_node_rule_group_uuid: Id of associated-node-rule-group
    :type associated_node_rule_group_node_rule_group_uuid: str

    :rtype: TapiTopologyNodeRuleGroupRef
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_available_capacity_bandwidth_profile_committed_burst_size_get(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_available_capacity_bandwidth_profile_committed_burst_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: Id of inter-rule-group
    :type inter_rule_group_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_available_capacity_bandwidth_profile_committed_information_rate_get(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_available_capacity_bandwidth_profile_committed_information_rate_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: Id of inter-rule-group
    :type inter_rule_group_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_available_capacity_bandwidth_profile_get(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_available_capacity_bandwidth_profile_get

    returns tapi.common.BandwidthProfile # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: Id of inter-rule-group
    :type inter_rule_group_uuid: str

    :rtype: TapiCommonBandwidthProfile
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_available_capacity_bandwidth_profile_peak_burst_size_get(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_available_capacity_bandwidth_profile_peak_burst_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: Id of inter-rule-group
    :type inter_rule_group_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_available_capacity_bandwidth_profile_peak_information_rate_get(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_available_capacity_bandwidth_profile_peak_information_rate_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: Id of inter-rule-group
    :type inter_rule_group_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_available_capacity_get(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_available_capacity_get

    returns tapi.common.Capacity # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: Id of inter-rule-group
    :type inter_rule_group_uuid: str

    :rtype: TapiCommonCapacity
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_available_capacity_total_size_get(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_available_capacity_total_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: Id of inter-rule-group
    :type inter_rule_group_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_cost_characteristiccost_name_get(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid, cost_name):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_cost_characteristiccost_name_get

    returns tapi.topology.CostCharacteristic # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: Id of inter-rule-group
    :type inter_rule_group_uuid: str
    :param cost_name: Id of cost-characteristic
    :type cost_name: str

    :rtype: TapiTopologyCostCharacteristic
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_get(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_get

    returns tapi.topology.InterRuleGroup # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: Id of inter-rule-group
    :type inter_rule_group_uuid: str

    :rtype: TapiTopologyInterRuleGroup
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_latency_characteristictraffic_property_name_get(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid, traffic_property_name):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_latency_characteristictraffic_property_name_get

    returns tapi.topology.LatencyCharacteristic # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: Id of inter-rule-group
    :type inter_rule_group_uuid: str
    :param traffic_property_name: Id of latency-characteristic
    :type traffic_property_name: str

    :rtype: TapiTopologyLatencyCharacteristic
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_namevalue_name_get(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid, value_name):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: Id of inter-rule-group
    :type inter_rule_group_uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_risk_characteristicrisk_characteristic_name_get(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid, risk_characteristic_name):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_risk_characteristicrisk_characteristic_name_get

    returns tapi.topology.RiskCharacteristic # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: Id of inter-rule-group
    :type inter_rule_group_uuid: str
    :param risk_characteristic_name: Id of risk-characteristic
    :type risk_characteristic_name: str

    :rtype: TapiTopologyRiskCharacteristic
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_rulelocal_id_get(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid, local_id):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_rulelocal_id_get

    returns tapi.topology.Rule # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: Id of inter-rule-group
    :type inter_rule_group_uuid: str
    :param local_id: Id of rule
    :type local_id: str

    :rtype: TapiTopologyRule
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_rulelocal_id_namevalue_name_get(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid, local_id, value_name):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_rulelocal_id_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: Id of inter-rule-group
    :type inter_rule_group_uuid: str
    :param local_id: Id of rule
    :type local_id: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_total_potential_capacity_bandwidth_profile_committed_burst_size_get(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_total_potential_capacity_bandwidth_profile_committed_burst_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: Id of inter-rule-group
    :type inter_rule_group_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_total_potential_capacity_bandwidth_profile_committed_information_rate_get(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_total_potential_capacity_bandwidth_profile_committed_information_rate_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: Id of inter-rule-group
    :type inter_rule_group_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_total_potential_capacity_bandwidth_profile_get(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_total_potential_capacity_bandwidth_profile_get

    returns tapi.common.BandwidthProfile # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: Id of inter-rule-group
    :type inter_rule_group_uuid: str

    :rtype: TapiCommonBandwidthProfile
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_total_potential_capacity_bandwidth_profile_peak_burst_size_get(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_total_potential_capacity_bandwidth_profile_peak_burst_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: Id of inter-rule-group
    :type inter_rule_group_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_total_potential_capacity_bandwidth_profile_peak_information_rate_get(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_total_potential_capacity_bandwidth_profile_peak_information_rate_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: Id of inter-rule-group
    :type inter_rule_group_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_total_potential_capacity_get(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_total_potential_capacity_get

    returns tapi.common.Capacity # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: Id of inter-rule-group
    :type inter_rule_group_uuid: str

    :rtype: TapiCommonCapacity
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_total_potential_capacity_total_size_get(uuid, node_uuid, node_rule_group_uuid, inter_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_inter_rule_groupinter_rule_group_uuid_total_potential_capacity_total_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str
    :param inter_rule_group_uuid: Id of inter-rule-group
    :type inter_rule_group_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_latency_characteristictraffic_property_name_get(uuid, node_uuid, node_rule_group_uuid, traffic_property_name):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_latency_characteristictraffic_property_name_get

    returns tapi.topology.LatencyCharacteristic # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str
    :param traffic_property_name: Id of latency-characteristic
    :type traffic_property_name: str

    :rtype: TapiTopologyLatencyCharacteristic
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_namevalue_name_get(uuid, node_uuid, node_rule_group_uuid, value_name):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_node_edge_pointtopology_uuidnode_edge_point_node_uuidnode_edge_point_uuid_get(uuid, node_uuid, node_rule_group_uuid, topology_uuid, node_edge_point_node_uuid, node_edge_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_node_edge_pointtopology_uuidnode_edge_point_node_uuidnode_edge_point_uuid_get

    returns tapi.topology.NodeEdgePointRef # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str
    :param topology_uuid: Id of node-edge-point
    :type topology_uuid: str
    :param node_edge_point_node_uuid: Id of node-edge-point
    :type node_edge_point_node_uuid: str
    :param node_edge_point_uuid: Id of node-edge-point
    :type node_edge_point_uuid: str

    :rtype: TapiTopologyNodeEdgePointRef
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_risk_characteristicrisk_characteristic_name_get(uuid, node_uuid, node_rule_group_uuid, risk_characteristic_name):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_risk_characteristicrisk_characteristic_name_get

    returns tapi.topology.RiskCharacteristic # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str
    :param risk_characteristic_name: Id of risk-characteristic
    :type risk_characteristic_name: str

    :rtype: TapiTopologyRiskCharacteristic
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_rulelocal_id_get(uuid, node_uuid, node_rule_group_uuid, local_id):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_rulelocal_id_get

    returns tapi.topology.Rule # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str
    :param local_id: Id of rule
    :type local_id: str

    :rtype: TapiTopologyRule
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_rulelocal_id_namevalue_name_get(uuid, node_uuid, node_rule_group_uuid, local_id, value_name):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_rulelocal_id_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str
    :param local_id: Id of rule
    :type local_id: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_total_potential_capacity_bandwidth_profile_committed_burst_size_get(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_total_potential_capacity_bandwidth_profile_committed_burst_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_total_potential_capacity_bandwidth_profile_committed_information_rate_get(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_total_potential_capacity_bandwidth_profile_committed_information_rate_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_total_potential_capacity_bandwidth_profile_get(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_total_potential_capacity_bandwidth_profile_get

    returns tapi.common.BandwidthProfile # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str

    :rtype: TapiCommonBandwidthProfile
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_total_potential_capacity_bandwidth_profile_peak_burst_size_get(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_total_potential_capacity_bandwidth_profile_peak_burst_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_total_potential_capacity_bandwidth_profile_peak_information_rate_get(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_total_potential_capacity_bandwidth_profile_peak_information_rate_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_total_potential_capacity_get(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_total_potential_capacity_get

    returns tapi.common.Capacity # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str

    :rtype: TapiCommonCapacity
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_total_potential_capacity_total_size_get(uuid, node_uuid, node_rule_group_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_node_rule_groupnode_rule_group_uuid_total_potential_capacity_total_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param node_rule_group_uuid: Id of node-rule-group
    :type node_rule_group_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_aggregated_node_edge_pointtopology_uuidaggregated_node_edge_point_node_uuidnode_edge_point_uuid_get(uuid, node_uuid, owned_node_edge_point_uuid, topology_uuid, aggregated_node_edge_point_node_uuid, node_edge_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_aggregated_node_edge_pointtopology_uuidaggregated_node_edge_point_node_uuidnode_edge_point_uuid_get

    returns tapi.topology.NodeEdgePointRef # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param topology_uuid: Id of aggregated-node-edge-point
    :type topology_uuid: str
    :param aggregated_node_edge_point_node_uuid: Id of aggregated-node-edge-point
    :type aggregated_node_edge_point_node_uuid: str
    :param node_edge_point_uuid: Id of aggregated-node-edge-point
    :type node_edge_point_uuid: str

    :rtype: TapiTopologyNodeEdgePointRef
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_available_capacity_bandwidth_profile_committed_burst_size_get(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_available_capacity_bandwidth_profile_committed_burst_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_available_capacity_bandwidth_profile_committed_information_rate_get(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_available_capacity_bandwidth_profile_committed_information_rate_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_available_capacity_bandwidth_profile_get(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_available_capacity_bandwidth_profile_get

    returns tapi.common.BandwidthProfile # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str

    :rtype: TapiCommonBandwidthProfile
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_available_capacity_bandwidth_profile_peak_burst_size_get(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_available_capacity_bandwidth_profile_peak_burst_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_available_capacity_bandwidth_profile_peak_information_rate_get(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_available_capacity_bandwidth_profile_peak_information_rate_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_available_capacity_get(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_available_capacity_get

    returns tapi.common.Capacity # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str

    :rtype: TapiCommonCapacity
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_available_capacity_total_size_get(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_available_capacity_total_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_get(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_get

    returns tapi.topology.node.OwnedNodeEdgePoint # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str

    :rtype: TapiTopologyNodeOwnedNodeEdgePoint
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_mapped_service_interface_pointservice_interface_point_uuid_get(uuid, node_uuid, owned_node_edge_point_uuid, service_interface_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_mapped_service_interface_pointservice_interface_point_uuid_get

    returns tapi.common.ServiceInterfacePointRef # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param service_interface_point_uuid: Id of mapped-service-interface-point
    :type service_interface_point_uuid: str

    :rtype: TapiCommonServiceInterfacePointRef
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_namevalue_name_get(uuid, node_uuid, owned_node_edge_point_uuid, value_name):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_total_potential_capacity_bandwidth_profile_committed_burst_size_get(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_total_potential_capacity_bandwidth_profile_committed_burst_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_total_potential_capacity_bandwidth_profile_committed_information_rate_get(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_total_potential_capacity_bandwidth_profile_committed_information_rate_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_total_potential_capacity_bandwidth_profile_get(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_total_potential_capacity_bandwidth_profile_get

    returns tapi.common.BandwidthProfile # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str

    :rtype: TapiCommonBandwidthProfile
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_total_potential_capacity_bandwidth_profile_peak_burst_size_get(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_total_potential_capacity_bandwidth_profile_peak_burst_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_total_potential_capacity_bandwidth_profile_peak_information_rate_get(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_total_potential_capacity_bandwidth_profile_peak_information_rate_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_total_potential_capacity_get(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_total_potential_capacity_get

    returns tapi.common.Capacity # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str

    :rtype: TapiCommonCapacity
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_total_potential_capacity_total_size_get(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_total_potential_capacity_total_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_total_potential_capacity_bandwidth_profile_committed_burst_size_get(uuid, node_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_total_potential_capacity_bandwidth_profile_committed_burst_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_total_potential_capacity_bandwidth_profile_committed_information_rate_get(uuid, node_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_total_potential_capacity_bandwidth_profile_committed_information_rate_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_total_potential_capacity_bandwidth_profile_get(uuid, node_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_total_potential_capacity_bandwidth_profile_get

    returns tapi.common.BandwidthProfile # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str

    :rtype: TapiCommonBandwidthProfile
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_total_potential_capacity_bandwidth_profile_peak_burst_size_get(uuid, node_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_total_potential_capacity_bandwidth_profile_peak_burst_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_total_potential_capacity_bandwidth_profile_peak_information_rate_get(uuid, node_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_total_potential_capacity_bandwidth_profile_peak_information_rate_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_total_potential_capacity_get(uuid, node_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_total_potential_capacity_get

    returns tapi.common.Capacity # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str

    :rtype: TapiCommonCapacity
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_total_potential_capacity_total_size_get(uuid, node_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_total_potential_capacity_total_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def operations_get_link_details_post(inline_object15=None):  # noqa: E501
    """operations_get_link_details_post

     # noqa: E501

    :param inline_object15: 
    :type inline_object15: dict | bytes

    :rtype: TapiTopologyGetLinkDetails
    """
    if connexion.request.is_json:
        inline_object15 = InlineObject15.from_dict(connexion.request.get_json())  # noqa: E501
    
    return TapiTopologyGetLinkDetails(TapiTopologyGetlinkdetailsOutput(
        database.link(inline_object15.input.topology_id_or_name, 
                      inline_object15.input.link_id_or_name)))


def operations_get_node_details_post(inline_object17=None):  # noqa: E501
    """operations_get_node_details_post

     # noqa: E501

    :param inline_object17: 
    :type inline_object17: dict | bytes

    :rtype: TapiTopologyGetNodeDetails
    """
    if connexion.request.is_json:
        inline_object17 = InlineObject17.from_dict(connexion.request.get_json())  # noqa: E501
    
    return TapiTopologyGetNodeDetails(TapiTopologyGetnodedetailsOutput(
        database.node(InlineObject17.input.topology_id_or_name,
                      InlineObject17.input.node_id_or_name)))


def operations_get_node_edge_point_details_post(inline_object18=None):  # noqa: E501
    """operations_get_node_edge_point_details_post

     # noqa: E501

    :param inline_object18: 
    :type inline_object18: dict | bytes

    :rtype: TapiTopologyGetNodeEdgePointDetails
    """
    if connexion.request.is_json:
        inline_object18 = InlineObject18.from_dict(connexion.request.get_json())  # noqa: E501
    
    return TapiTopologyGetNodeEdgePointDetails(TapiTopologyGetnodeedgepointdetailsOutput(
        database.node_edge_point(inline_object18.input.topology_id_or_name,
                                 inline_object18.input.node_id_or_name,
                                 inline_object18.input.nep_id_or_name)))


def operations_get_topology_details_post(inline_object25=None):  # noqa: E501
    """operations_get_topology_details_post

     # noqa: E501

    :param inline_object25: 
    :type inline_object25: dict | bytes

    :rtype: TapiTopologyGetTopologyDetails
    """
    if connexion.request.is_json:
        inline_object25 = InlineObject25.from_dict(connexion.request.get_json())  # noqa: E501
        
    return TapiTopologyGetTopologyDetails(TapiTopologyGettopologydetailsOutput(
        database.topology(inline_object25.input.topology_id_or_name)))


def operations_get_topology_list_post():  # noqa: E501
    """operations_get_topology_list_post

     # noqa: E501


    :rtype: TapiTopologyGetTopologyList
    """
    return TapiTopologyGetTopologyList(TapiTopologyGettopologylistOutput(
        database.topology_list()))
    
    
