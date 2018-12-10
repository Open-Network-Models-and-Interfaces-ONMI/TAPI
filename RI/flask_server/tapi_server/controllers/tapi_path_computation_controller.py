import connexion
import six

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
from tapi_server import util


def data_context_path_computation_context_delete():  # noqa: E501
    """data_context_path_computation_context_delete

    removes tapi.path.computation.PathComputationContext # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def data_context_path_computation_context_get():  # noqa: E501
    """data_context_path_computation_context_get

    returns tapi.path.computation.PathComputationContext # noqa: E501


    :rtype: TapiPathComputationPathComputationContext
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_service_post(tapi_path_computation_path_computation_service=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_service_post

    creates tapi.path.computation.PathComputationService # noqa: E501

    :param tapi_path_computation_path_computation_service: tapi.path.computation.PathComputationService to be added to list
    :type tapi_path_computation_path_computation_service: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_path_computation_path_computation_service = TapiPathComputationPathComputationService.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_delete(uuid):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_delete

    removes tapi.path.computation.PathComputationService # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_end_point_post(uuid, tapi_path_computation_path_service_end_point=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_point_post

    creates tapi.path.computation.PathServiceEndPoint # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param tapi_path_computation_path_service_end_point: tapi.path.computation.PathServiceEndPoint to be added to list
    :type tapi_path_computation_path_service_end_point: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_path_computation_path_service_end_point = TapiPathComputationPathServiceEndPoint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_delete(uuid, local_id):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_delete

    removes tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_get(uuid, local_id):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_post(uuid, local_id, tapi_common_capacity_value=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_post

    creates tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of path-comp-service
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


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_put(uuid, local_id, tapi_common_capacity_value=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_burst_size_put

    creates or updates tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of path-comp-service
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


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_delete(uuid, local_id):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_delete

    removes tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_get(uuid, local_id):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_post(uuid, local_id, tapi_common_capacity_value=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_post

    creates tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of path-comp-service
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


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_put(uuid, local_id, tapi_common_capacity_value=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_committed_information_rate_put

    creates or updates tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of path-comp-service
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


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_delete(uuid, local_id):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_delete

    removes tapi.common.BandwidthProfile # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_get(uuid, local_id):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_get

    returns tapi.common.BandwidthProfile # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiCommonBandwidthProfile
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_delete(uuid, local_id):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_delete

    removes tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_get(uuid, local_id):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_post(uuid, local_id, tapi_common_capacity_value=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_post

    creates tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of path-comp-service
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


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_put(uuid, local_id, tapi_common_capacity_value=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_burst_size_put

    creates or updates tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of path-comp-service
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


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_delete(uuid, local_id):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_delete

    removes tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_get(uuid, local_id):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_post(uuid, local_id, tapi_common_capacity_value=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_post

    creates tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of path-comp-service
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


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_put(uuid, local_id, tapi_common_capacity_value=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_peak_information_rate_put

    creates or updates tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of path-comp-service
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


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_post(uuid, local_id, tapi_common_bandwidth_profile=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_post

    creates tapi.common.BandwidthProfile # noqa: E501

    :param uuid: Id of path-comp-service
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


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_put(uuid, local_id, tapi_common_bandwidth_profile=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_bandwidth_profile_put

    creates or updates tapi.common.BandwidthProfile # noqa: E501

    :param uuid: Id of path-comp-service
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


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_delete(uuid, local_id):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_delete

    removes tapi.common.Capacity # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_get(uuid, local_id):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_get

    returns tapi.common.Capacity # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiCommonCapacity
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_post(uuid, local_id, tapi_common_capacity=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_post

    creates tapi.common.Capacity # noqa: E501

    :param uuid: Id of path-comp-service
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


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_put(uuid, local_id, tapi_common_capacity=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_put

    creates or updates tapi.common.Capacity # noqa: E501

    :param uuid: Id of path-comp-service
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


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_total_size_delete(uuid, local_id):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_total_size_delete

    removes tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_total_size_get(uuid, local_id):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_total_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_total_size_post(uuid, local_id, tapi_common_capacity_value=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_total_size_post

    creates tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of path-comp-service
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


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_total_size_put(uuid, local_id, tapi_common_capacity_value=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_capacity_total_size_put

    creates or updates tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of path-comp-service
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


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_delete(uuid, local_id):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_delete

    removes tapi.path.computation.PathServiceEndPoint # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_get(uuid, local_id):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_get

    returns tapi.path.computation.PathServiceEndPoint # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiPathComputationPathServiceEndPoint
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_name_post(uuid, local_id, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of path-comp-service
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


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_namevalue_name_delete(uuid, local_id, value_name):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_namevalue_name_delete

    removes tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_namevalue_name_get(uuid, local_id, value_name):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_namevalue_name_post(uuid, local_id, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_namevalue_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of path-comp-service
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


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_namevalue_name_put(uuid, local_id, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_namevalue_name_put

    creates or updates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of path-comp-service
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


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_post(uuid, local_id, tapi_path_computation_path_service_end_point=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_post

    creates tapi.path.computation.PathServiceEndPoint # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_path_computation_path_service_end_point: tapi.path.computation.PathServiceEndPoint to be added to list
    :type tapi_path_computation_path_service_end_point: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_path_computation_path_service_end_point = TapiPathComputationPathServiceEndPoint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_put(uuid, local_id, tapi_path_computation_path_service_end_point=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_put

    creates or updates tapi.path.computation.PathServiceEndPoint # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_path_computation_path_service_end_point: tapi.path.computation.PathServiceEndPoint to be added or updated
    :type tapi_path_computation_path_service_end_point: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_path_computation_path_service_end_point = TapiPathComputationPathServiceEndPoint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_service_interface_point_get(uuid, local_id):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_end_pointlocal_id_service_interface_point_get

    returns tapi.common.ServiceInterfacePointRef # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiCommonServiceInterfacePointRef
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_get(uuid):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_get

    returns tapi.path.computation.PathComputationService # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str

    :rtype: TapiPathComputationPathComputationService
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_name_post(uuid, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param tapi_common_name_and_value: tapi.common.NameAndValue to be added to list
    :type tapi_common_name_and_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_name_and_value = TapiCommonNameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_namevalue_name_delete(uuid, value_name):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_namevalue_name_delete

    removes tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_namevalue_name_get(uuid, value_name):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_namevalue_name_post(uuid, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_namevalue_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of path-comp-service
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


def data_context_path_computation_context_path_comp_serviceuuid_namevalue_name_put(uuid, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_namevalue_name_put

    creates or updates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of path-comp-service
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


def data_context_path_computation_context_path_comp_serviceuuid_objective_function_delete(uuid):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_objective_function_delete

    removes tapi.path.computation.PathObjectiveFunction # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_objective_function_get(uuid):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_objective_function_get

    returns tapi.path.computation.PathObjectiveFunction # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str

    :rtype: TapiPathComputationPathObjectiveFunction
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_objective_function_name_post(uuid, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_objective_function_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param tapi_common_name_and_value: tapi.common.NameAndValue to be added to list
    :type tapi_common_name_and_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_name_and_value = TapiCommonNameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_objective_function_namevalue_name_delete(uuid, value_name):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_objective_function_namevalue_name_delete

    removes tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_objective_function_namevalue_name_get(uuid, value_name):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_objective_function_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_objective_function_namevalue_name_post(uuid, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_objective_function_namevalue_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of path-comp-service
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


def data_context_path_computation_context_path_comp_serviceuuid_objective_function_namevalue_name_put(uuid, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_objective_function_namevalue_name_put

    creates or updates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of path-comp-service
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


def data_context_path_computation_context_path_comp_serviceuuid_objective_function_post(uuid, tapi_path_computation_path_objective_function=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_objective_function_post

    creates tapi.path.computation.PathObjectiveFunction # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param tapi_path_computation_path_objective_function: tapi.path.computation.PathObjectiveFunction to be added to list
    :type tapi_path_computation_path_objective_function: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_path_computation_path_objective_function = TapiPathComputationPathObjectiveFunction.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_objective_function_put(uuid, tapi_path_computation_path_objective_function=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_objective_function_put

    creates or updates tapi.path.computation.PathObjectiveFunction # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param tapi_path_computation_path_objective_function: tapi.path.computation.PathObjectiveFunction to be added or updated
    :type tapi_path_computation_path_objective_function: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_path_computation_path_objective_function = TapiPathComputationPathObjectiveFunction.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_delete(uuid):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_delete

    removes tapi.path.computation.PathOptimizationConstraint # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_get(uuid):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_get

    returns tapi.path.computation.PathOptimizationConstraint # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str

    :rtype: TapiPathComputationPathOptimizationConstraint
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_name_post(uuid, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param tapi_common_name_and_value: tapi.common.NameAndValue to be added to list
    :type tapi_common_name_and_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_name_and_value = TapiCommonNameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_namevalue_name_delete(uuid, value_name):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_namevalue_name_delete

    removes tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_namevalue_name_get(uuid, value_name):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_namevalue_name_post(uuid, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_namevalue_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of path-comp-service
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


def data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_namevalue_name_put(uuid, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_namevalue_name_put

    creates or updates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of path-comp-service
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


def data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_post(uuid, tapi_path_computation_path_optimization_constraint=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_post

    creates tapi.path.computation.PathOptimizationConstraint # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param tapi_path_computation_path_optimization_constraint: tapi.path.computation.PathOptimizationConstraint to be added to list
    :type tapi_path_computation_path_optimization_constraint: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_path_computation_path_optimization_constraint = TapiPathComputationPathOptimizationConstraint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_put(uuid, tapi_path_computation_path_optimization_constraint=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_optimization_constraint_put

    creates or updates tapi.path.computation.PathOptimizationConstraint # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param tapi_path_computation_path_optimization_constraint: tapi.path.computation.PathOptimizationConstraint to be added or updated
    :type tapi_path_computation_path_optimization_constraint: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_path_computation_path_optimization_constraint = TapiPathComputationPathOptimizationConstraint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_pathpath_uuid_get(uuid, path_uuid):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_pathpath_uuid_get

    returns tapi.path.computation.PathRef # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param path_uuid: Id of path
    :type path_uuid: str

    :rtype: TapiPathComputationPathRef
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_post(uuid, tapi_path_computation_path_computation_service=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_post

    creates tapi.path.computation.PathComputationService # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param tapi_path_computation_path_computation_service: tapi.path.computation.PathComputationService to be added to list
    :type tapi_path_computation_path_computation_service: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_path_computation_path_computation_service = TapiPathComputationPathComputationService.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_put(uuid, tapi_path_computation_path_computation_service=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_put

    creates or updates tapi.path.computation.PathComputationService # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param tapi_path_computation_path_computation_service: tapi.path.computation.PathComputationService to be added or updated
    :type tapi_path_computation_path_computation_service: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_path_computation_path_computation_service = TapiPathComputationPathComputationService.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_cost_characteristic_post(uuid, tapi_topology_cost_characteristic=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_cost_characteristic_post

    creates tapi.topology.CostCharacteristic # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param tapi_topology_cost_characteristic: tapi.topology.CostCharacteristic to be added to list
    :type tapi_topology_cost_characteristic: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_topology_cost_characteristic = TapiTopologyCostCharacteristic.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_cost_characteristiccost_name_delete(uuid, cost_name):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_cost_characteristiccost_name_delete

    removes tapi.topology.CostCharacteristic # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param cost_name: Id of cost-characteristic
    :type cost_name: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_cost_characteristiccost_name_get(uuid, cost_name):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_cost_characteristiccost_name_get

    returns tapi.topology.CostCharacteristic # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param cost_name: Id of cost-characteristic
    :type cost_name: str

    :rtype: TapiTopologyCostCharacteristic
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_cost_characteristiccost_name_post(uuid, cost_name, tapi_topology_cost_characteristic=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_cost_characteristiccost_name_post

    creates tapi.topology.CostCharacteristic # noqa: E501

    :param uuid: Id of path-comp-service
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


def data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_cost_characteristiccost_name_put(uuid, cost_name, tapi_topology_cost_characteristic=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_cost_characteristiccost_name_put

    creates or updates tapi.topology.CostCharacteristic # noqa: E501

    :param uuid: Id of path-comp-service
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


def data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_delete(uuid):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_delete

    removes tapi.path.computation.RoutingConstraint # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_get(uuid):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_get

    returns tapi.path.computation.RoutingConstraint # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str

    :rtype: TapiPathComputationRoutingConstraint
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_latency_characteristic_post(uuid, tapi_topology_latency_characteristic=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_latency_characteristic_post

    creates tapi.topology.LatencyCharacteristic # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param tapi_topology_latency_characteristic: tapi.topology.LatencyCharacteristic to be added to list
    :type tapi_topology_latency_characteristic: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_topology_latency_characteristic = TapiTopologyLatencyCharacteristic.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_latency_characteristictraffic_property_name_delete(uuid, traffic_property_name):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_latency_characteristictraffic_property_name_delete

    removes tapi.topology.LatencyCharacteristic # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param traffic_property_name: Id of latency-characteristic
    :type traffic_property_name: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_latency_characteristictraffic_property_name_get(uuid, traffic_property_name):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_latency_characteristictraffic_property_name_get

    returns tapi.topology.LatencyCharacteristic # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param traffic_property_name: Id of latency-characteristic
    :type traffic_property_name: str

    :rtype: TapiTopologyLatencyCharacteristic
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_latency_characteristictraffic_property_name_post(uuid, traffic_property_name, tapi_topology_latency_characteristic=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_latency_characteristictraffic_property_name_post

    creates tapi.topology.LatencyCharacteristic # noqa: E501

    :param uuid: Id of path-comp-service
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


def data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_latency_characteristictraffic_property_name_put(uuid, traffic_property_name, tapi_topology_latency_characteristic=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_latency_characteristictraffic_property_name_put

    creates or updates tapi.topology.LatencyCharacteristic # noqa: E501

    :param uuid: Id of path-comp-service
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


def data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_post(uuid, tapi_path_computation_routing_constraint=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_post

    creates tapi.path.computation.RoutingConstraint # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param tapi_path_computation_routing_constraint: tapi.path.computation.RoutingConstraint to be added to list
    :type tapi_path_computation_routing_constraint: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_path_computation_routing_constraint = TapiPathComputationRoutingConstraint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_put(uuid, tapi_path_computation_routing_constraint=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_put

    creates or updates tapi.path.computation.RoutingConstraint # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param tapi_path_computation_routing_constraint: tapi.path.computation.RoutingConstraint to be added or updated
    :type tapi_path_computation_routing_constraint: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_path_computation_routing_constraint = TapiPathComputationRoutingConstraint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_risk_diversity_characteristic_post(uuid, tapi_topology_risk_characteristic=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_risk_diversity_characteristic_post

    creates tapi.topology.RiskCharacteristic # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param tapi_topology_risk_characteristic: tapi.topology.RiskCharacteristic to be added to list
    :type tapi_topology_risk_characteristic: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_topology_risk_characteristic = TapiTopologyRiskCharacteristic.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_risk_diversity_characteristicrisk_characteristic_name_delete(uuid, risk_characteristic_name):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_risk_diversity_characteristicrisk_characteristic_name_delete

    removes tapi.topology.RiskCharacteristic # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param risk_characteristic_name: Id of risk-diversity-characteristic
    :type risk_characteristic_name: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_risk_diversity_characteristicrisk_characteristic_name_get(uuid, risk_characteristic_name):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_risk_diversity_characteristicrisk_characteristic_name_get

    returns tapi.topology.RiskCharacteristic # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param risk_characteristic_name: Id of risk-diversity-characteristic
    :type risk_characteristic_name: str

    :rtype: TapiTopologyRiskCharacteristic
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_risk_diversity_characteristicrisk_characteristic_name_post(uuid, risk_characteristic_name, tapi_topology_risk_characteristic=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_risk_diversity_characteristicrisk_characteristic_name_post

    creates tapi.topology.RiskCharacteristic # noqa: E501

    :param uuid: Id of path-comp-service
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


def data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_risk_diversity_characteristicrisk_characteristic_name_put(uuid, risk_characteristic_name, tapi_topology_risk_characteristic=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_routing_constraint_risk_diversity_characteristicrisk_characteristic_name_put

    creates or updates tapi.topology.RiskCharacteristic # noqa: E501

    :param uuid: Id of path-comp-service
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


def data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_avoid_topologytopology_uuid_get(uuid, topology_uuid):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_avoid_topologytopology_uuid_get

    returns tapi.topology.TopologyRef # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param topology_uuid: Id of avoid-topology
    :type topology_uuid: str

    :rtype: TapiTopologyTopologyRef
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_delete(uuid):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_delete

    removes tapi.path.computation.TopologyConstraint # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_exclude_linktopology_uuidlink_uuid_get(uuid, topology_uuid, link_uuid):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_exclude_linktopology_uuidlink_uuid_get

    returns tapi.topology.LinkRef # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param topology_uuid: Id of exclude-link
    :type topology_uuid: str
    :param link_uuid: Id of exclude-link
    :type link_uuid: str

    :rtype: TapiTopologyLinkRef
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_exclude_nodetopology_uuidnode_uuid_get(uuid, topology_uuid, node_uuid):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_exclude_nodetopology_uuidnode_uuid_get

    returns tapi.topology.NodeRef # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param topology_uuid: Id of exclude-node
    :type topology_uuid: str
    :param node_uuid: Id of exclude-node
    :type node_uuid: str

    :rtype: TapiTopologyNodeRef
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_exclude_pathpath_uuid_get(uuid, path_uuid):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_exclude_pathpath_uuid_get

    returns tapi.path.computation.PathRef # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param path_uuid: Id of exclude-path
    :type path_uuid: str

    :rtype: TapiPathComputationPathRef
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_get(uuid):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_get

    returns tapi.path.computation.TopologyConstraint # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str

    :rtype: TapiPathComputationTopologyConstraint
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_include_linktopology_uuidlink_uuid_get(uuid, topology_uuid, link_uuid):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_include_linktopology_uuidlink_uuid_get

    returns tapi.topology.LinkRef # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param topology_uuid: Id of include-link
    :type topology_uuid: str
    :param link_uuid: Id of include-link
    :type link_uuid: str

    :rtype: TapiTopologyLinkRef
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_include_nodetopology_uuidnode_uuid_get(uuid, topology_uuid, node_uuid):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_include_nodetopology_uuidnode_uuid_get

    returns tapi.topology.NodeRef # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param topology_uuid: Id of include-node
    :type topology_uuid: str
    :param node_uuid: Id of include-node
    :type node_uuid: str

    :rtype: TapiTopologyNodeRef
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_include_pathpath_uuid_get(uuid, path_uuid):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_include_pathpath_uuid_get

    returns tapi.path.computation.PathRef # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param path_uuid: Id of include-path
    :type path_uuid: str

    :rtype: TapiPathComputationPathRef
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_include_topologytopology_uuid_get(uuid, topology_uuid):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_include_topologytopology_uuid_get

    returns tapi.topology.TopologyRef # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param topology_uuid: Id of include-topology
    :type topology_uuid: str

    :rtype: TapiTopologyTopologyRef
    """
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_post(uuid, tapi_path_computation_topology_constraint=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_post

    creates tapi.path.computation.TopologyConstraint # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param tapi_path_computation_topology_constraint: tapi.path.computation.TopologyConstraint to be added to list
    :type tapi_path_computation_topology_constraint: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_path_computation_topology_constraint = TapiPathComputationTopologyConstraint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_put(uuid, tapi_path_computation_topology_constraint=None):  # noqa: E501
    """data_context_path_computation_context_path_comp_serviceuuid_topology_constraint_put

    creates or updates tapi.path.computation.TopologyConstraint # noqa: E501

    :param uuid: Id of path-comp-service
    :type uuid: str
    :param tapi_path_computation_topology_constraint: tapi.path.computation.TopologyConstraint to be added or updated
    :type tapi_path_computation_topology_constraint: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_path_computation_topology_constraint = TapiPathComputationTopologyConstraint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_path_computation_context_pathuuid_get(uuid):  # noqa: E501
    """data_context_path_computation_context_pathuuid_get

    returns tapi.path.computation.Path # noqa: E501

    :param uuid: Id of path
    :type uuid: str

    :rtype: TapiPathComputationPath
    """
    return 'do some magic!'


def data_context_path_computation_context_pathuuid_linktopology_uuidlink_uuid_get(uuid, topology_uuid, link_uuid):  # noqa: E501
    """data_context_path_computation_context_pathuuid_linktopology_uuidlink_uuid_get

    returns tapi.topology.LinkRef # noqa: E501

    :param uuid: Id of path
    :type uuid: str
    :param topology_uuid: Id of link
    :type topology_uuid: str
    :param link_uuid: Id of link
    :type link_uuid: str

    :rtype: TapiTopologyLinkRef
    """
    return 'do some magic!'


def data_context_path_computation_context_pathuuid_namevalue_name_get(uuid, value_name):  # noqa: E501
    """data_context_path_computation_context_pathuuid_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of path
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_path_computation_context_pathuuid_routing_constraint_cost_characteristiccost_name_get(uuid, cost_name):  # noqa: E501
    """data_context_path_computation_context_pathuuid_routing_constraint_cost_characteristiccost_name_get

    returns tapi.topology.CostCharacteristic # noqa: E501

    :param uuid: Id of path
    :type uuid: str
    :param cost_name: Id of cost-characteristic
    :type cost_name: str

    :rtype: TapiTopologyCostCharacteristic
    """
    return 'do some magic!'


def data_context_path_computation_context_pathuuid_routing_constraint_get(uuid):  # noqa: E501
    """data_context_path_computation_context_pathuuid_routing_constraint_get

    returns tapi.path.computation.RoutingConstraint # noqa: E501

    :param uuid: Id of path
    :type uuid: str

    :rtype: TapiPathComputationRoutingConstraint
    """
    return 'do some magic!'


def data_context_path_computation_context_pathuuid_routing_constraint_latency_characteristictraffic_property_name_get(uuid, traffic_property_name):  # noqa: E501
    """data_context_path_computation_context_pathuuid_routing_constraint_latency_characteristictraffic_property_name_get

    returns tapi.topology.LatencyCharacteristic # noqa: E501

    :param uuid: Id of path
    :type uuid: str
    :param traffic_property_name: Id of latency-characteristic
    :type traffic_property_name: str

    :rtype: TapiTopologyLatencyCharacteristic
    """
    return 'do some magic!'


def data_context_path_computation_context_pathuuid_routing_constraint_risk_diversity_characteristicrisk_characteristic_name_get(uuid, risk_characteristic_name):  # noqa: E501
    """data_context_path_computation_context_pathuuid_routing_constraint_risk_diversity_characteristicrisk_characteristic_name_get

    returns tapi.topology.RiskCharacteristic # noqa: E501

    :param uuid: Id of path
    :type uuid: str
    :param risk_characteristic_name: Id of risk-diversity-characteristic
    :type risk_characteristic_name: str

    :rtype: TapiTopologyRiskCharacteristic
    """
    return 'do some magic!'


def data_context_path_computation_context_post(tapi_path_computation_path_computation_context=None):  # noqa: E501
    """data_context_path_computation_context_post

    creates tapi.path.computation.PathComputationContext # noqa: E501

    :param tapi_path_computation_path_computation_context: tapi.path.computation.PathComputationContext to be added to list
    :type tapi_path_computation_path_computation_context: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_path_computation_path_computation_context = TapiPathComputationPathComputationContext.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_path_computation_context_put(tapi_path_computation_path_computation_context=None):  # noqa: E501
    """data_context_path_computation_context_put

    creates or updates tapi.path.computation.PathComputationContext # noqa: E501

    :param tapi_path_computation_path_computation_context: tapi.path.computation.PathComputationContext to be added or updated
    :type tapi_path_computation_path_computation_context: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_path_computation_path_computation_context = TapiPathComputationPathComputationContext.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def operations_compute_p_2_p_path_post(inline_object=None):  # noqa: E501
    """operations_compute_p2_p_path_post

     # noqa: E501

    :param inline_object: 
    :type inline_object: dict | bytes

    :rtype: TapiPathComputationComputeP2PPath
    """
    if connexion.request.is_json:
        inline_object = InlineObject.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def operations_delete_p_2_p_path_post(inline_object11=None):  # noqa: E501
    """operations_delete_p2_p_path_post

     # noqa: E501

    :param inline_object11: 
    :type inline_object11: dict | bytes

    :rtype: TapiPathComputationDeleteP2PPath
    """
    if connexion.request.is_json:
        inline_object11 = InlineObject11.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def operations_optimize_p_2_p_path_post(inline_object26=None):  # noqa: E501
    """operations_optimize_p2_p_path_post

     # noqa: E501

    :param inline_object26: 
    :type inline_object26: dict | bytes

    :rtype: TapiPathComputationOptimizeP2PPath
    """
    if connexion.request.is_json:
        inline_object26 = InlineObject26.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
