import connexion
import six

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
from tapi_server.models.tapi_connectivity_getconnectivityservicelist_output import TapiConnectivityGetconnectivityservicelistOutput  # noqa: F401,E501
from tapi_server.models.tapi_connectivity_getconnectivityservicedetails_output import TapiConnectivityGetconnectivityservicedetailsOutput  # noqa: F401,E501
from tapi_server.models.tapi_connectivity_getconnectiondetails_output import TapiConnectivityGetconnectiondetailsOutput  # noqa: F401,E501
from tapi_server.models.tapi_connectivity_getconnectionendpointdetails_output import TapiConnectivityGetconnectionendpointdetailsOutput  # noqa: F401,E501
from tapi_server import util
from tapi_server import database


def data_context_connectivity_context_connectionuuid_connection_end_pointtopology_uuidnode_uuidnode_edge_point_uuidconnection_end_point_uuid_get(uuid, topology_uuid, node_uuid, node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_connectivity_context_connectionuuid_connection_end_pointtopology_uuidnode_uuidnode_edge_point_uuidconnection_end_point_uuid_get

    returns tapi.connectivity.ConnectionEndPointRef # noqa: E501

    :param uuid: Id of connection
    :type uuid: str
    :param topology_uuid: Id of connection-end-point
    :type topology_uuid: str
    :param node_uuid: Id of connection-end-point
    :type node_uuid: str
    :param node_edge_point_uuid: Id of connection-end-point
    :type node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiConnectivityConnectionEndPointRef
    """
    return 'do some magic!'


def data_context_connectivity_context_connectionuuid_get(uuid):  # noqa: E501
    """data_context_connectivity_context_connectionuuid_get

    returns tapi.connectivity.Connection # noqa: E501

    :param uuid: Id of connection
    :type uuid: str

    :rtype: TapiConnectivityConnection
    """
    return 'do some magic!'


def data_context_connectivity_context_connectionuuid_lower_connectionconnection_uuid_get(uuid, connection_uuid):  # noqa: E501
    """data_context_connectivity_context_connectionuuid_lower_connectionconnection_uuid_get

    returns tapi.connectivity.ConnectionRef # noqa: E501

    :param uuid: Id of connection
    :type uuid: str
    :param connection_uuid: Id of lower-connection
    :type connection_uuid: str

    :rtype: TapiConnectivityConnectionRef
    """
    return 'do some magic!'


def data_context_connectivity_context_connectionuuid_namevalue_name_get(uuid, value_name):  # noqa: E501
    """data_context_connectivity_context_connectionuuid_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of connection
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_connectivity_context_connectionuuid_routelocal_id_connection_end_pointtopology_uuidnode_uuidnode_edge_point_uuidconnection_end_point_uuid_get(uuid, local_id, topology_uuid, node_uuid, node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_connectivity_context_connectionuuid_routelocal_id_connection_end_pointtopology_uuidnode_uuidnode_edge_point_uuidconnection_end_point_uuid_get

    returns tapi.connectivity.ConnectionEndPointRef # noqa: E501

    :param uuid: Id of connection
    :type uuid: str
    :param local_id: Id of route
    :type local_id: str
    :param topology_uuid: Id of connection-end-point
    :type topology_uuid: str
    :param node_uuid: Id of connection-end-point
    :type node_uuid: str
    :param node_edge_point_uuid: Id of connection-end-point
    :type node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiConnectivityConnectionEndPointRef
    """
    return 'do some magic!'


def data_context_connectivity_context_connectionuuid_routelocal_id_get(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectionuuid_routelocal_id_get

    returns tapi.connectivity.Route # noqa: E501

    :param uuid: Id of connection
    :type uuid: str
    :param local_id: Id of route
    :type local_id: str

    :rtype: TapiConnectivityRoute
    """
    return 'do some magic!'


def data_context_connectivity_context_connectionuuid_routelocal_id_namevalue_name_get(uuid, local_id, value_name):  # noqa: E501
    """data_context_connectivity_context_connectionuuid_routelocal_id_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of connection
    :type uuid: str
    :param local_id: Id of route
    :type local_id: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_connectivity_context_connectionuuid_supported_client_linktopology_uuidlink_uuid_get(uuid, topology_uuid, link_uuid):  # noqa: E501
    """data_context_connectivity_context_connectionuuid_supported_client_linktopology_uuidlink_uuid_get

    returns tapi.topology.LinkRef # noqa: E501

    :param uuid: Id of connection
    :type uuid: str
    :param topology_uuid: Id of supported-client-link
    :type topology_uuid: str
    :param link_uuid: Id of supported-client-link
    :type link_uuid: str

    :rtype: TapiTopologyLinkRef
    """
    return 'do some magic!'


def data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_get(uuid, switch_control_uuid):  # noqa: E501
    """data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_get

    returns tapi.connectivity.SwitchControl # noqa: E501

    :param uuid: Id of connection
    :type uuid: str
    :param switch_control_uuid: Id of switch-control
    :type switch_control_uuid: str

    :rtype: TapiConnectivitySwitchControl
    """
    return 'do some magic!'


def data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_namevalue_name_get(uuid, switch_control_uuid, value_name):  # noqa: E501
    """data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of connection
    :type uuid: str
    :param switch_control_uuid: Id of switch-control
    :type switch_control_uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_resilience_type_get(uuid, switch_control_uuid):  # noqa: E501
    """data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_resilience_type_get

    returns tapi.topology.ResilienceType # noqa: E501

    :param uuid: Id of connection
    :type uuid: str
    :param switch_control_uuid: Id of switch-control
    :type switch_control_uuid: str

    :rtype: TapiTopologyResilienceType
    """
    return 'do some magic!'


def data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_sub_switch_controlconnection_uuidsub_switch_control_switch_control_uuid_get(uuid, switch_control_uuid, connection_uuid, sub_switch_control_switch_control_uuid):  # noqa: E501
    """data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_sub_switch_controlconnection_uuidsub_switch_control_switch_control_uuid_get

    returns tapi.connectivity.SwitchControlRef # noqa: E501

    :param uuid: Id of connection
    :type uuid: str
    :param switch_control_uuid: Id of switch-control
    :type switch_control_uuid: str
    :param connection_uuid: Id of sub-switch-control
    :type connection_uuid: str
    :param sub_switch_control_switch_control_uuid: Id of sub-switch-control
    :type sub_switch_control_switch_control_uuid: str

    :rtype: TapiConnectivitySwitchControlRef
    """
    return 'do some magic!'


def data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_switchlocal_id_get(uuid, switch_control_uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_switchlocal_id_get

    returns tapi.connectivity.Switch # noqa: E501

    :param uuid: Id of connection
    :type uuid: str
    :param switch_control_uuid: Id of switch-control
    :type switch_control_uuid: str
    :param local_id: Id of switch
    :type local_id: str

    :rtype: TapiConnectivitySwitch
    """
    return 'do some magic!'


def data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_switchlocal_id_namevalue_name_get(uuid, switch_control_uuid, local_id, value_name):  # noqa: E501
    """data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_switchlocal_id_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of connection
    :type uuid: str
    :param switch_control_uuid: Id of switch-control
    :type switch_control_uuid: str
    :param local_id: Id of switch
    :type local_id: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_switchlocal_id_selected_connection_end_pointtopology_uuidnode_uuidnode_edge_point_uuidconnection_end_point_uuid_get(uuid, switch_control_uuid, local_id, topology_uuid, node_uuid, node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_switchlocal_id_selected_connection_end_pointtopology_uuidnode_uuidnode_edge_point_uuidconnection_end_point_uuid_get

    returns tapi.connectivity.ConnectionEndPointRef # noqa: E501

    :param uuid: Id of connection
    :type uuid: str
    :param switch_control_uuid: Id of switch-control
    :type switch_control_uuid: str
    :param local_id: Id of switch
    :type local_id: str
    :param topology_uuid: Id of selected-connection-end-point
    :type topology_uuid: str
    :param node_uuid: Id of selected-connection-end-point
    :type node_uuid: str
    :param node_edge_point_uuid: Id of selected-connection-end-point
    :type node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of selected-connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiConnectivityConnectionEndPointRef
    """
    return 'do some magic!'


def data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_switchlocal_id_selected_routeconnection_uuidroute_local_id_get(uuid, switch_control_uuid, local_id, connection_uuid, route_local_id):  # noqa: E501
    """data_context_connectivity_context_connectionuuid_switch_controlswitch_control_uuid_switchlocal_id_selected_routeconnection_uuidroute_local_id_get

    returns tapi.connectivity.RouteRef # noqa: E501

    :param uuid: Id of connection
    :type uuid: str
    :param switch_control_uuid: Id of switch-control
    :type switch_control_uuid: str
    :param local_id: Id of switch
    :type local_id: str
    :param connection_uuid: Id of selected-route
    :type connection_uuid: str
    :param route_local_id: Id of selected-route
    :type route_local_id: str

    :rtype: TapiConnectivityRouteRef
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_service_post(tapi_connectivity_connectivitycontext_connectivity_service=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_service_post

    creates tapi.connectivity.connectivitycontext.ConnectivityService # noqa: E501

    :param tapi_connectivity_connectivitycontext_connectivity_service: tapi.connectivity.connectivitycontext.ConnectivityService to be added to list
    :type tapi_connectivity_connectivitycontext_connectivity_service: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_connectivity_connectivitycontext_connectivity_service = TapiConnectivityConnectivitycontextConnectivityService.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_avoid_topologytopology_uuid_get(uuid, topology_uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_avoid_topologytopology_uuid_get

    returns tapi.topology.TopologyRef # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param topology_uuid: Id of avoid-topology
    :type topology_uuid: str

    :rtype: TapiTopologyTopologyRef
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_connectionconnection_uuid_get(uuid, connection_uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_connectionconnection_uuid_get

    returns tapi.connectivity.ConnectionRef # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param connection_uuid: Id of connection
    :type connection_uuid: str

    :rtype: TapiConnectivityConnectionRef
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_coroute_inclusion_delete(uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_coroute_inclusion_delete

    removes tapi.connectivity.ConnectivityServiceRef # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_coroute_inclusion_get(uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_coroute_inclusion_get

    returns tapi.connectivity.ConnectivityServiceRef # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str

    :rtype: TapiConnectivityConnectivityServiceRef
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_coroute_inclusion_post(uuid, tapi_connectivity_connectivity_service_ref=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_coroute_inclusion_post

    creates tapi.connectivity.ConnectivityServiceRef # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param tapi_connectivity_connectivity_service_ref: tapi.connectivity.ConnectivityServiceRef to be added to list
    :type tapi_connectivity_connectivity_service_ref: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_connectivity_connectivity_service_ref = TapiConnectivityConnectivityServiceRef.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_coroute_inclusion_put(uuid, tapi_connectivity_connectivity_service_ref=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_coroute_inclusion_put

    creates or updates tapi.connectivity.ConnectivityServiceRef # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param tapi_connectivity_connectivity_service_ref: tapi.connectivity.ConnectivityServiceRef to be added or updated
    :type tapi_connectivity_connectivity_service_ref: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_connectivity_connectivity_service_ref = TapiConnectivityConnectivityServiceRef.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_cost_characteristic_post(uuid, tapi_topology_cost_characteristic=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_cost_characteristic_post

    creates tapi.topology.CostCharacteristic # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param tapi_topology_cost_characteristic: tapi.topology.CostCharacteristic to be added to list
    :type tapi_topology_cost_characteristic: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_topology_cost_characteristic = TapiTopologyCostCharacteristic.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_cost_characteristiccost_name_delete(uuid, cost_name):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_cost_characteristiccost_name_delete

    removes tapi.topology.CostCharacteristic # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param cost_name: Id of cost-characteristic
    :type cost_name: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_cost_characteristiccost_name_get(uuid, cost_name):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_cost_characteristiccost_name_get

    returns tapi.topology.CostCharacteristic # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param cost_name: Id of cost-characteristic
    :type cost_name: str

    :rtype: TapiTopologyCostCharacteristic
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_cost_characteristiccost_name_post(uuid, cost_name, tapi_topology_cost_characteristic=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_cost_characteristiccost_name_post

    creates tapi.topology.CostCharacteristic # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param cost_name: Id of cost-characteristic
    :type cost_name: str
    :param tapi_topology_cost_characteristic: tapi.topology.CostCharacteristic to be added to list
    :type tapi_topology_cost_characteristic: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_topology_cost_characteristic = TapiTopologyCostCharacteristic.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_cost_characteristiccost_name_put(uuid, cost_name, tapi_topology_cost_characteristic=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_cost_characteristiccost_name_put

    creates or updates tapi.topology.CostCharacteristic # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param cost_name: Id of cost-characteristic
    :type cost_name: str
    :param tapi_topology_cost_characteristic: tapi.topology.CostCharacteristic to be added or updated
    :type tapi_topology_cost_characteristic: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_topology_cost_characteristic = TapiTopologyCostCharacteristic.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_delete(uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_delete

    removes tapi.connectivity.connectivitycontext.ConnectivityService # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_diversity_exclusion_post(uuid, tapi_connectivity_connectivity_service_ref=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_diversity_exclusion_post

    creates tapi.connectivity.ConnectivityServiceRef # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param tapi_connectivity_connectivity_service_ref: tapi.connectivity.ConnectivityServiceRef to be added to list
    :type tapi_connectivity_connectivity_service_ref: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_connectivity_connectivity_service_ref = TapiConnectivityConnectivityServiceRef.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_diversity_exclusionconnectivity_service_uuid_delete(uuid, connectivity_service_uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_diversity_exclusionconnectivity_service_uuid_delete

    removes tapi.connectivity.ConnectivityServiceRef # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param connectivity_service_uuid: Id of diversity-exclusion
    :type connectivity_service_uuid: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_diversity_exclusionconnectivity_service_uuid_get(uuid, connectivity_service_uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_diversity_exclusionconnectivity_service_uuid_get

    returns tapi.connectivity.ConnectivityServiceRef # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param connectivity_service_uuid: Id of diversity-exclusion
    :type connectivity_service_uuid: str

    :rtype: TapiConnectivityConnectivityServiceRef
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_diversity_exclusionconnectivity_service_uuid_post(uuid, connectivity_service_uuid, tapi_connectivity_connectivity_service_ref=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_diversity_exclusionconnectivity_service_uuid_post

    creates tapi.connectivity.ConnectivityServiceRef # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param connectivity_service_uuid: Id of diversity-exclusion
    :type connectivity_service_uuid: str
    :param tapi_connectivity_connectivity_service_ref: tapi.connectivity.ConnectivityServiceRef to be added to list
    :type tapi_connectivity_connectivity_service_ref: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_connectivity_connectivity_service_ref = TapiConnectivityConnectivityServiceRef.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_diversity_exclusionconnectivity_service_uuid_put(uuid, connectivity_service_uuid, tapi_connectivity_connectivity_service_ref=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_diversity_exclusionconnectivity_service_uuid_put

    creates or updates tapi.connectivity.ConnectivityServiceRef # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param connectivity_service_uuid: Id of diversity-exclusion
    :type connectivity_service_uuid: str
    :param tapi_connectivity_connectivity_service_ref: tapi.connectivity.ConnectivityServiceRef to be added or updated
    :type tapi_connectivity_connectivity_service_ref: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_connectivity_connectivity_service_ref = TapiConnectivityConnectivityServiceRef.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_point_post(uuid, tapi_connectivity_connectivityservice_end_point=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_point_post

    creates tapi.connectivity.connectivityservice.EndPoint # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param tapi_connectivity_connectivityservice_end_point: tapi.connectivity.connectivityservice.EndPoint to be added to list
    :type tapi_connectivity_connectivityservice_end_point: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_connectivity_connectivityservice_end_point = TapiConnectivityConnectivityserviceEndPoint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_delete(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_delete

    removes tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_get(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_post(uuid, local_id, tapi_common_capacity_value=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_post

    creates tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_common_capacity_value: tapi.common.CapacityValue to be added to list
    :type tapi_common_capacity_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_capacity_value = TapiCommonCapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_put(uuid, local_id, tapi_common_capacity_value=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_put

    creates or updates tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_common_capacity_value: tapi.common.CapacityValue to be added or updated
    :type tapi_common_capacity_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_capacity_value = TapiCommonCapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_delete(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_delete

    removes tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_get(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_post(uuid, local_id, tapi_common_capacity_value=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_post

    creates tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_common_capacity_value: tapi.common.CapacityValue to be added to list
    :type tapi_common_capacity_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_capacity_value = TapiCommonCapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_put(uuid, local_id, tapi_common_capacity_value=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_put

    creates or updates tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_common_capacity_value: tapi.common.CapacityValue to be added or updated
    :type tapi_common_capacity_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_capacity_value = TapiCommonCapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_delete(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_delete

    removes tapi.common.BandwidthProfile # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_get(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_get

    returns tapi.common.BandwidthProfile # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiCommonBandwidthProfile
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_delete(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_delete

    removes tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_get(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_post(uuid, local_id, tapi_common_capacity_value=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_post

    creates tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_common_capacity_value: tapi.common.CapacityValue to be added to list
    :type tapi_common_capacity_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_capacity_value = TapiCommonCapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_put(uuid, local_id, tapi_common_capacity_value=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_put

    creates or updates tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_common_capacity_value: tapi.common.CapacityValue to be added or updated
    :type tapi_common_capacity_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_capacity_value = TapiCommonCapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_delete(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_delete

    removes tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_get(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_post(uuid, local_id, tapi_common_capacity_value=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_post

    creates tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_common_capacity_value: tapi.common.CapacityValue to be added to list
    :type tapi_common_capacity_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_capacity_value = TapiCommonCapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_put(uuid, local_id, tapi_common_capacity_value=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_put

    creates or updates tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_common_capacity_value: tapi.common.CapacityValue to be added or updated
    :type tapi_common_capacity_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_capacity_value = TapiCommonCapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_post(uuid, local_id, tapi_common_bandwidth_profile=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_post

    creates tapi.common.BandwidthProfile # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_common_bandwidth_profile: tapi.common.BandwidthProfile to be added to list
    :type tapi_common_bandwidth_profile: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_bandwidth_profile = TapiCommonBandwidthProfile.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_put(uuid, local_id, tapi_common_bandwidth_profile=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_put

    creates or updates tapi.common.BandwidthProfile # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_common_bandwidth_profile: tapi.common.BandwidthProfile to be added or updated
    :type tapi_common_bandwidth_profile: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_bandwidth_profile = TapiCommonBandwidthProfile.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_delete(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_delete

    removes tapi.common.Capacity # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_get(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_get

    returns tapi.common.Capacity # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiCommonCapacity
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_post(uuid, local_id, tapi_common_capacity=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_post

    creates tapi.common.Capacity # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_common_capacity: tapi.common.Capacity to be added to list
    :type tapi_common_capacity: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_capacity = TapiCommonCapacity.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_put(uuid, local_id, tapi_common_capacity=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_put

    creates or updates tapi.common.Capacity # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_common_capacity: tapi.common.Capacity to be added or updated
    :type tapi_common_capacity: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_capacity = TapiCommonCapacity.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_total_size_delete(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_total_size_delete

    removes tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_total_size_get(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_total_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_total_size_post(uuid, local_id, tapi_common_capacity_value=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_total_size_post

    creates tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_common_capacity_value: tapi.common.CapacityValue to be added to list
    :type tapi_common_capacity_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_capacity_value = TapiCommonCapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_total_size_put(uuid, local_id, tapi_common_capacity_value=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_capacity_total_size_put

    creates or updates tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_common_capacity_value: tapi.common.CapacityValue to be added or updated
    :type tapi_common_capacity_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_capacity_value = TapiCommonCapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_connection_end_pointtopology_uuidnode_uuidnode_edge_point_uuidconnection_end_point_uuid_get(uuid, local_id, topology_uuid, node_uuid, node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_connection_end_pointtopology_uuidnode_uuidnode_edge_point_uuidconnection_end_point_uuid_get

    returns tapi.connectivity.ConnectionEndPointRef # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param topology_uuid: Id of connection-end-point
    :type topology_uuid: str
    :param node_uuid: Id of connection-end-point
    :type node_uuid: str
    :param node_edge_point_uuid: Id of connection-end-point
    :type node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiConnectivityConnectionEndPointRef
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_delete(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_delete

    removes tapi.connectivity.connectivityservice.EndPoint # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_get(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_get

    returns tapi.connectivity.connectivityservice.EndPoint # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiConnectivityConnectivityserviceEndPoint
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_name_post(uuid, local_id, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_common_name_and_value: tapi.common.NameAndValue to be added to list
    :type tapi_common_name_and_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_name_and_value = TapiCommonNameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_namevalue_name_delete(uuid, local_id, value_name):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_namevalue_name_delete

    removes tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_namevalue_name_get(uuid, local_id, value_name):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_namevalue_name_post(uuid, local_id, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_namevalue_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param value_name: Id of name
    :type value_name: str
    :param tapi_common_name_and_value: tapi.common.NameAndValue to be added to list
    :type tapi_common_name_and_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_name_and_value = TapiCommonNameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_namevalue_name_put(uuid, local_id, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_namevalue_name_put

    creates or updates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param value_name: Id of name
    :type value_name: str
    :param tapi_common_name_and_value: tapi.common.NameAndValue to be added or updated
    :type tapi_common_name_and_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_name_and_value = TapiCommonNameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_post(uuid, local_id, tapi_connectivity_connectivityservice_end_point=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_post

    creates tapi.connectivity.connectivityservice.EndPoint # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_connectivity_connectivityservice_end_point: tapi.connectivity.connectivityservice.EndPoint to be added to list
    :type tapi_connectivity_connectivityservice_end_point: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_connectivity_connectivityservice_end_point = TapiConnectivityConnectivityserviceEndPoint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_put(uuid, local_id, tapi_connectivity_connectivityservice_end_point=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_put

    creates or updates tapi.connectivity.connectivityservice.EndPoint # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_connectivity_connectivityservice_end_point: tapi.connectivity.connectivityservice.EndPoint to be added or updated
    :type tapi_connectivity_connectivityservice_end_point: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_connectivity_connectivityservice_end_point = TapiConnectivityConnectivityserviceEndPoint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_service_interface_point_delete(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_service_interface_point_delete

    removes tapi.common.ServiceInterfacePointRef # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_service_interface_point_get(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_service_interface_point_get

    returns tapi.common.ServiceInterfacePointRef # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiCommonServiceInterfacePointRef
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_service_interface_point_post(uuid, local_id, tapi_common_service_interface_point_ref=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_service_interface_point_post

    creates tapi.common.ServiceInterfacePointRef # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_common_service_interface_point_ref: tapi.common.ServiceInterfacePointRef to be added to list
    :type tapi_common_service_interface_point_ref: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_service_interface_point_ref = TapiCommonServiceInterfacePointRef.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_service_interface_point_put(uuid, local_id, tapi_common_service_interface_point_ref=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_service_interface_point_put

    creates or updates tapi.common.ServiceInterfacePointRef # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_common_service_interface_point_ref: tapi.common.ServiceInterfacePointRef to be added or updated
    :type tapi_common_service_interface_point_ref: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_service_interface_point_ref = TapiCommonServiceInterfacePointRef.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_exclude_linktopology_uuidlink_uuid_get(uuid, topology_uuid, link_uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_exclude_linktopology_uuidlink_uuid_get

    returns tapi.topology.LinkRef # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param topology_uuid: Id of exclude-link
    :type topology_uuid: str
    :param link_uuid: Id of exclude-link
    :type link_uuid: str

    :rtype: TapiTopologyLinkRef
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_exclude_nodetopology_uuidnode_uuid_get(uuid, topology_uuid, node_uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_exclude_nodetopology_uuidnode_uuid_get

    returns tapi.topology.NodeRef # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param topology_uuid: Id of exclude-node
    :type topology_uuid: str
    :param node_uuid: Id of exclude-node
    :type node_uuid: str

    :rtype: TapiTopologyNodeRef
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_exclude_pathpath_uuid_get(uuid, path_uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_exclude_pathpath_uuid_get

    returns tapi.path.computation.PathRef # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param path_uuid: Id of exclude-path
    :type path_uuid: str

    :rtype: TapiPathComputationPathRef
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_get(uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_get

    returns tapi.connectivity.connectivitycontext.ConnectivityService # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str

    :rtype: TapiConnectivityConnectivitycontextConnectivityService
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_include_linktopology_uuidlink_uuid_get(uuid, topology_uuid, link_uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_include_linktopology_uuidlink_uuid_get

    returns tapi.topology.LinkRef # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param topology_uuid: Id of include-link
    :type topology_uuid: str
    :param link_uuid: Id of include-link
    :type link_uuid: str

    :rtype: TapiTopologyLinkRef
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_include_nodetopology_uuidnode_uuid_get(uuid, topology_uuid, node_uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_include_nodetopology_uuidnode_uuid_get

    returns tapi.topology.NodeRef # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param topology_uuid: Id of include-node
    :type topology_uuid: str
    :param node_uuid: Id of include-node
    :type node_uuid: str

    :rtype: TapiTopologyNodeRef
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_include_pathpath_uuid_get(uuid, path_uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_include_pathpath_uuid_get

    returns tapi.path.computation.PathRef # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param path_uuid: Id of include-path
    :type path_uuid: str

    :rtype: TapiPathComputationPathRef
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_include_topologytopology_uuid_get(uuid, topology_uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_include_topologytopology_uuid_get

    returns tapi.topology.TopologyRef # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param topology_uuid: Id of include-topology
    :type topology_uuid: str

    :rtype: TapiTopologyTopologyRef
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_latency_characteristic_post(uuid, tapi_topology_latency_characteristic=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_latency_characteristic_post

    creates tapi.topology.LatencyCharacteristic # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param tapi_topology_latency_characteristic: tapi.topology.LatencyCharacteristic to be added to list
    :type tapi_topology_latency_characteristic: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_topology_latency_characteristic = TapiTopologyLatencyCharacteristic.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_latency_characteristictraffic_property_name_delete(uuid, traffic_property_name):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_latency_characteristictraffic_property_name_delete

    removes tapi.topology.LatencyCharacteristic # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param traffic_property_name: Id of latency-characteristic
    :type traffic_property_name: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_latency_characteristictraffic_property_name_get(uuid, traffic_property_name):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_latency_characteristictraffic_property_name_get

    returns tapi.topology.LatencyCharacteristic # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param traffic_property_name: Id of latency-characteristic
    :type traffic_property_name: str

    :rtype: TapiTopologyLatencyCharacteristic
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_latency_characteristictraffic_property_name_post(uuid, traffic_property_name, tapi_topology_latency_characteristic=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_latency_characteristictraffic_property_name_post

    creates tapi.topology.LatencyCharacteristic # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param traffic_property_name: Id of latency-characteristic
    :type traffic_property_name: str
    :param tapi_topology_latency_characteristic: tapi.topology.LatencyCharacteristic to be added to list
    :type tapi_topology_latency_characteristic: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_topology_latency_characteristic = TapiTopologyLatencyCharacteristic.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_latency_characteristictraffic_property_name_put(uuid, traffic_property_name, tapi_topology_latency_characteristic=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_latency_characteristictraffic_property_name_put

    creates or updates tapi.topology.LatencyCharacteristic # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param traffic_property_name: Id of latency-characteristic
    :type traffic_property_name: str
    :param tapi_topology_latency_characteristic: tapi.topology.LatencyCharacteristic to be added or updated
    :type tapi_topology_latency_characteristic: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_topology_latency_characteristic = TapiTopologyLatencyCharacteristic.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_name_post(uuid, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param tapi_common_name_and_value: tapi.common.NameAndValue to be added to list
    :type tapi_common_name_and_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_name_and_value = TapiCommonNameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_namevalue_name_delete(uuid, value_name):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_namevalue_name_delete

    removes tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_namevalue_name_get(uuid, value_name):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_namevalue_name_post(uuid, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_namevalue_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of connectivity-service
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


def data_context_connectivity_context_connectivity_serviceuuid_namevalue_name_put(uuid, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_namevalue_name_put

    creates or updates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of connectivity-service
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


def data_context_connectivity_context_connectivity_serviceuuid_post(uuid, tapi_connectivity_connectivitycontext_connectivity_service=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_post

    creates tapi.connectivity.connectivitycontext.ConnectivityService # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param tapi_connectivity_connectivitycontext_connectivity_service: tapi.connectivity.connectivitycontext.ConnectivityService to be added to list
    :type tapi_connectivity_connectivitycontext_connectivity_service: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_connectivity_connectivitycontext_connectivity_service = TapiConnectivityConnectivitycontextConnectivityService.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_put(uuid, tapi_connectivity_connectivitycontext_connectivity_service=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_put

    creates or updates tapi.connectivity.connectivitycontext.ConnectivityService # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param tapi_connectivity_connectivitycontext_connectivity_service: tapi.connectivity.connectivitycontext.ConnectivityService to be added or updated
    :type tapi_connectivity_connectivitycontext_connectivity_service: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_connectivity_connectivitycontext_connectivity_service = TapiConnectivityConnectivitycontextConnectivityService.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_burst_size_delete(uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_burst_size_delete

    removes tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_burst_size_get(uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_burst_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_burst_size_post(uuid, tapi_common_capacity_value=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_burst_size_post

    creates tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param tapi_common_capacity_value: tapi.common.CapacityValue to be added to list
    :type tapi_common_capacity_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_capacity_value = TapiCommonCapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_burst_size_put(uuid, tapi_common_capacity_value=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_burst_size_put

    creates or updates tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param tapi_common_capacity_value: tapi.common.CapacityValue to be added or updated
    :type tapi_common_capacity_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_capacity_value = TapiCommonCapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_information_rate_delete(uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_information_rate_delete

    removes tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_information_rate_get(uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_information_rate_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_information_rate_post(uuid, tapi_common_capacity_value=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_information_rate_post

    creates tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param tapi_common_capacity_value: tapi.common.CapacityValue to be added to list
    :type tapi_common_capacity_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_capacity_value = TapiCommonCapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_information_rate_put(uuid, tapi_common_capacity_value=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_committed_information_rate_put

    creates or updates tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param tapi_common_capacity_value: tapi.common.CapacityValue to be added or updated
    :type tapi_common_capacity_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_capacity_value = TapiCommonCapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_delete(uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_delete

    removes tapi.common.BandwidthProfile # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_get(uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_get

    returns tapi.common.BandwidthProfile # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str

    :rtype: TapiCommonBandwidthProfile
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_burst_size_delete(uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_burst_size_delete

    removes tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_burst_size_get(uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_burst_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_burst_size_post(uuid, tapi_common_capacity_value=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_burst_size_post

    creates tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param tapi_common_capacity_value: tapi.common.CapacityValue to be added to list
    :type tapi_common_capacity_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_capacity_value = TapiCommonCapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_burst_size_put(uuid, tapi_common_capacity_value=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_burst_size_put

    creates or updates tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param tapi_common_capacity_value: tapi.common.CapacityValue to be added or updated
    :type tapi_common_capacity_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_capacity_value = TapiCommonCapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_information_rate_delete(uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_information_rate_delete

    removes tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_information_rate_get(uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_information_rate_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_information_rate_post(uuid, tapi_common_capacity_value=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_information_rate_post

    creates tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param tapi_common_capacity_value: tapi.common.CapacityValue to be added to list
    :type tapi_common_capacity_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_capacity_value = TapiCommonCapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_information_rate_put(uuid, tapi_common_capacity_value=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_peak_information_rate_put

    creates or updates tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param tapi_common_capacity_value: tapi.common.CapacityValue to be added or updated
    :type tapi_common_capacity_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_capacity_value = TapiCommonCapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_post(uuid, tapi_common_bandwidth_profile=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_post

    creates tapi.common.BandwidthProfile # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param tapi_common_bandwidth_profile: tapi.common.BandwidthProfile to be added to list
    :type tapi_common_bandwidth_profile: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_bandwidth_profile = TapiCommonBandwidthProfile.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_put(uuid, tapi_common_bandwidth_profile=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_bandwidth_profile_put

    creates or updates tapi.common.BandwidthProfile # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param tapi_common_bandwidth_profile: tapi.common.BandwidthProfile to be added or updated
    :type tapi_common_bandwidth_profile: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_bandwidth_profile = TapiCommonBandwidthProfile.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_delete(uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_delete

    removes tapi.common.Capacity # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_get(uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_get

    returns tapi.common.Capacity # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str

    :rtype: TapiCommonCapacity
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_post(uuid, tapi_common_capacity=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_post

    creates tapi.common.Capacity # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param tapi_common_capacity: tapi.common.Capacity to be added to list
    :type tapi_common_capacity: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_capacity = TapiCommonCapacity.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_put(uuid, tapi_common_capacity=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_put

    creates or updates tapi.common.Capacity # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param tapi_common_capacity: tapi.common.Capacity to be added or updated
    :type tapi_common_capacity: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_capacity = TapiCommonCapacity.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_total_size_delete(uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_total_size_delete

    removes tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_total_size_get(uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_total_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_total_size_post(uuid, tapi_common_capacity_value=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_total_size_post

    creates tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param tapi_common_capacity_value: tapi.common.CapacityValue to be added to list
    :type tapi_common_capacity_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_capacity_value = TapiCommonCapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_total_size_put(uuid, tapi_common_capacity_value=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_requested_capacity_total_size_put

    creates or updates tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param tapi_common_capacity_value: tapi.common.CapacityValue to be added or updated
    :type tapi_common_capacity_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_capacity_value = TapiCommonCapacityValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_resilience_type_delete(uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_resilience_type_delete

    removes tapi.topology.ResilienceType # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_resilience_type_get(uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_resilience_type_get

    returns tapi.topology.ResilienceType # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str

    :rtype: TapiTopologyResilienceType
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_resilience_type_post(uuid, tapi_topology_resilience_type=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_resilience_type_post

    creates tapi.topology.ResilienceType # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param tapi_topology_resilience_type: tapi.topology.ResilienceType to be added to list
    :type tapi_topology_resilience_type: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_topology_resilience_type = TapiTopologyResilienceType.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_resilience_type_put(uuid, tapi_topology_resilience_type=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_resilience_type_put

    creates or updates tapi.topology.ResilienceType # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param tapi_topology_resilience_type: tapi.topology.ResilienceType to be added or updated
    :type tapi_topology_resilience_type: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_topology_resilience_type = TapiTopologyResilienceType.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_risk_diversity_characteristic_post(uuid, tapi_topology_risk_characteristic=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_risk_diversity_characteristic_post

    creates tapi.topology.RiskCharacteristic # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param tapi_topology_risk_characteristic: tapi.topology.RiskCharacteristic to be added to list
    :type tapi_topology_risk_characteristic: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_topology_risk_characteristic = TapiTopologyRiskCharacteristic.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_risk_diversity_characteristicrisk_characteristic_name_delete(uuid, risk_characteristic_name):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_risk_diversity_characteristicrisk_characteristic_name_delete

    removes tapi.topology.RiskCharacteristic # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param risk_characteristic_name: Id of risk-diversity-characteristic
    :type risk_characteristic_name: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_risk_diversity_characteristicrisk_characteristic_name_get(uuid, risk_characteristic_name):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_risk_diversity_characteristicrisk_characteristic_name_get

    returns tapi.topology.RiskCharacteristic # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param risk_characteristic_name: Id of risk-diversity-characteristic
    :type risk_characteristic_name: str

    :rtype: TapiTopologyRiskCharacteristic
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_risk_diversity_characteristicrisk_characteristic_name_post(uuid, risk_characteristic_name, tapi_topology_risk_characteristic=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_risk_diversity_characteristicrisk_characteristic_name_post

    creates tapi.topology.RiskCharacteristic # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param risk_characteristic_name: Id of risk-diversity-characteristic
    :type risk_characteristic_name: str
    :param tapi_topology_risk_characteristic: tapi.topology.RiskCharacteristic to be added to list
    :type tapi_topology_risk_characteristic: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_topology_risk_characteristic = TapiTopologyRiskCharacteristic.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_risk_diversity_characteristicrisk_characteristic_name_put(uuid, risk_characteristic_name, tapi_topology_risk_characteristic=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_risk_diversity_characteristicrisk_characteristic_name_put

    creates or updates tapi.topology.RiskCharacteristic # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param risk_characteristic_name: Id of risk-diversity-characteristic
    :type risk_characteristic_name: str
    :param tapi_topology_risk_characteristic: tapi.topology.RiskCharacteristic to be added or updated
    :type tapi_topology_risk_characteristic: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_topology_risk_characteristic = TapiTopologyRiskCharacteristic.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_schedule_delete(uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_schedule_delete

    removes tapi.common.TimeRange # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_schedule_get(uuid):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_schedule_get

    returns tapi.common.TimeRange # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str

    :rtype: TapiCommonTimeRange
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_schedule_post(uuid, tapi_common_time_range=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_schedule_post

    creates tapi.common.TimeRange # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param tapi_common_time_range: tapi.common.TimeRange to be added to list
    :type tapi_common_time_range: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_time_range = TapiCommonTimeRange.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_schedule_put(uuid, tapi_common_time_range=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_schedule_put

    creates or updates tapi.common.TimeRange # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param tapi_common_time_range: tapi.common.TimeRange to be added or updated
    :type tapi_common_time_range: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_time_range = TapiCommonTimeRange.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_delete():  # noqa: E501
    """data_context_connectivity_context_delete

    removes tapi.connectivity.ConnectivityContext # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_get():  # noqa: E501
    """data_context_connectivity_context_get

    returns tapi.connectivity.ConnectivityContext # noqa: E501


    :rtype: TapiConnectivityConnectivityContext
    """
    return 'do some magic!'


def data_context_connectivity_context_post(tapi_connectivity_connectivity_context=None):  # noqa: E501
    """data_context_connectivity_context_post

    creates tapi.connectivity.ConnectivityContext # noqa: E501

    :param tapi_connectivity_connectivity_context: tapi.connectivity.ConnectivityContext to be added to list
    :type tapi_connectivity_connectivity_context: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_connectivity_connectivity_context = TapiConnectivityConnectivityContext.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_put(tapi_connectivity_connectivity_context=None):  # noqa: E501
    """data_context_connectivity_context_put

    creates or updates tapi.connectivity.ConnectivityContext # noqa: E501

    :param tapi_connectivity_connectivity_context: tapi.connectivity.ConnectivityContext to be added or updated
    :type tapi_connectivity_connectivity_context: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_connectivity_connectivity_context = TapiConnectivityConnectivityContext.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_aggregated_connection_end_pointtopology_uuidaggregated_connection_end_point_node_uuidnode_edge_point_uuidaggregated_connection_end_point_connection_end_point_uuid_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid, topology_uuid, aggregated_connection_end_point_node_uuid, node_edge_point_uuid, aggregated_connection_end_point_connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_aggregated_connection_end_pointtopology_uuidaggregated_connection_end_point_node_uuidnode_edge_point_uuidaggregated_connection_end_point_connection_end_point_uuid_get

    returns tapi.connectivity.ConnectionEndPointRef # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str
    :param topology_uuid: Id of aggregated-connection-end-point
    :type topology_uuid: str
    :param aggregated_connection_end_point_node_uuid: Id of aggregated-connection-end-point
    :type aggregated_connection_end_point_node_uuid: str
    :param node_edge_point_uuid: Id of aggregated-connection-end-point
    :type node_edge_point_uuid: str
    :param aggregated_connection_end_point_connection_end_point_uuid: Id of aggregated-connection-end-point
    :type aggregated_connection_end_point_connection_end_point_uuid: str

    :rtype: TapiConnectivityConnectionEndPointRef
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_client_node_edge_pointtopology_uuidclient_node_edge_point_node_uuidnode_edge_point_uuid_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid, topology_uuid, client_node_edge_point_node_uuid, node_edge_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_client_node_edge_pointtopology_uuidclient_node_edge_point_node_uuidnode_edge_point_uuid_get

    returns tapi.topology.NodeEdgePointRef # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str
    :param topology_uuid: Id of client-node-edge-point
    :type topology_uuid: str
    :param client_node_edge_point_node_uuid: Id of client-node-edge-point
    :type client_node_edge_point_node_uuid: str
    :param node_edge_point_uuid: Id of client-node-edge-point
    :type node_edge_point_uuid: str

    :rtype: TapiTopologyNodeEdgePointRef
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_get

    returns tapi.connectivity.ceplist.ConnectionEndPoint # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiConnectivityCeplistConnectionEndPoint
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_namevalue_name_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid, value_name):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_parent_node_edge_point_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_parent_node_edge_point_get

    returns tapi.topology.NodeEdgePointRef # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiTopologyNodeEdgePointRef
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_get(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_get

    returns tapi.connectivity.context.topologycontext.topology.node.ownednodeedgepoint.CepList # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str

    :rtype: TapiConnectivityContextTopologycontextTopologyNodeOwnednodeedgepointCepList
    """
    return 'do some magic!'


def operations_create_connectivity_service_post(inline_object1=None):  # noqa: E501
    """operations_create_connectivity_service_post

     # noqa: E501

    :param inline_object1: 
    :type inline_object1: dict | bytes

    :rtype: TapiConnectivityCreateConnectivityService
    """
    if connexion.request.is_json:
        inline_object1 = InlineObject1.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def operations_delete_connectivity_service_post(inline_object6=None):  # noqa: E501
    """operations_delete_connectivity_service_post

     # noqa: E501

    :param inline_object6: 
    :type inline_object6: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        inline_object6 = InlineObject6.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def operations_get_connection_details_post(inline_object12=None):  # noqa: E501
    """operations_get_connection_details_post

     # noqa: E501

    :param inline_object12: 
    :type inline_object12: dict | bytes

    :rtype: TapiConnectivityGetConnectionDetails
    """
    if connexion.request.is_json:
        inline_object12 = InlineObject12.from_dict(connexion.request.get_json())  # noqa: E501
    
    return TapiConnectivityGetConnectionDetails(TapiConnectivityGetconnectiondetailsOutput(
        database.connection(inline_object12.input.connection_id_or_name)))


def operations_get_connection_end_point_details_post(inline_object13=None):  # noqa: E501
    """operations_get_connection_end_point_details_post

     # noqa: E501

    :param inline_object13: 
    :type inline_object13: dict | bytes

    :rtype: TapiConnectivityGetConnectionEndPointDetails
    """
    if connexion.request.is_json:
        inline_object13 = InlineObject13.from_dict(connexion.request.get_json())  # noqa: E501
    
    return TapiConnectivityGetConnectionEndPointDetails(TapiConnectivityGetconnectionendpointdetailsOutput(
        database.connection_end_point(inline_object13.input.topology_id_or_name, 
                                      inline_object13.input.node_id_or_name,
                                      inline_object13.input.nep_id_or_name,
                                      inline_object13.input.cep_id_or_name)))


def operations_get_connectivity_service_details_post(inline_object14=None):  # noqa: E501
    """operations_get_connectivity_service_details_post

     # noqa: E501

    :param inline_object14: 
    :type inline_object14: dict | bytes

    :rtype: TapiConnectivityGetConnectivityServiceDetails
    """
    if connexion.request.is_json:
        inline_object14 = InlineObject14.from_dict(connexion.request.get_json())  # noqa: E501
    
    return TapiConnectivityGetConnectivityServiceDetails(TapiConnectivityGetconnectivityservicedetailsOutput(
        database.connectivity_service(inline_object14.input.service_id_or_name)))


def operations_get_connectivity_service_list_post():  # noqa: E501
    """operations_get_connectivity_service_list_post

     # noqa: E501


    :rtype: TapiConnectivityGetConnectivityServiceList
    """
    return TapiConnectivityGetConnectivityServiceList(TapiConnectivityGetconnectivityservicelistOutput(
        database.connectivity_service_list()))


def operations_update_connectivity_service_post(inline_object27=None):  # noqa: E501
    """operations_update_connectivity_service_post

     # noqa: E501

    :param inline_object27: 
    :type inline_object27: dict | bytes

    :rtype: TapiConnectivityUpdateConnectivityService
    """
    if connexion.request.is_json:
        inline_object27 = InlineObject27.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
