import connexion
import six

from tapi_server.models.tapi_odu_deg_thr import TapiOduDegThr  # noqa: E501
from tapi_server.models.tapi_odu_odu_common_pac import TapiOduOduCommonPac  # noqa: E501
from tapi_server.models.tapi_odu_odu_connection_end_point_spec import TapiOduOduConnectionEndPointSpec  # noqa: E501
from tapi_server.models.tapi_odu_odu_ctp_pac import TapiOduOduCtpPac  # noqa: E501
from tapi_server.models.tapi_odu_odu_defect_pac import TapiOduOduDefectPac  # noqa: E501
from tapi_server.models.tapi_odu_odu_mip_pac import TapiOduOduMipPac  # noqa: E501
from tapi_server.models.tapi_odu_odu_mip_spec import TapiOduOduMipSpec  # noqa: E501
from tapi_server.models.tapi_odu_odu_ncm_pac import TapiOduOduNcmPac  # noqa: E501
from tapi_server.models.tapi_odu_odu_node_edge_point_spec import TapiOduOduNodeEdgePointSpec  # noqa: E501
from tapi_server.models.tapi_odu_odu_payload_type import TapiOduOduPayloadType  # noqa: E501
from tapi_server.models.tapi_odu_odu_pm_pac import TapiOduOduPmPac  # noqa: E501
from tapi_server.models.tapi_odu_odu_pool_pac import TapiOduOduPoolPac  # noqa: E501
from tapi_server.models.tapi_odu_odu_protection_pac import TapiOduOduProtectionPac  # noqa: E501
from tapi_server.models.tapi_odu_odu_tcm_mip_pac import TapiOduOduTcmMipPac  # noqa: E501
from tapi_server.models.tapi_odu_odu_termination_and_client_adaptation_pac import TapiOduOduTerminationAndClientAdaptationPac  # noqa: E501
from tapi_server.models.tapi_odu_uas_choice import TapiOduUasChoice  # noqa: E501
from tapi_server import util


def data_context_oam_context_meguuid_meplocal_id_odu_connection_end_point_spec_get(uuid, local_id):  # noqa: E501
    """data_context_oam_context_meguuid_meplocal_id_odu_connection_end_point_spec_get

    returns tapi.odu.OduConnectionEndPointSpec # noqa: E501

    :param uuid: Id of meg
    :type uuid: str
    :param local_id: Id of mep
    :type local_id: str

    :rtype: TapiOduOduConnectionEndPointSpec
    """
    return 'do some magic!'


def data_context_oam_context_meguuid_meplocal_id_odu_connection_end_point_spec_odu_common_get(uuid, local_id):  # noqa: E501
    """data_context_oam_context_meguuid_meplocal_id_odu_connection_end_point_spec_odu_common_get

    returns tapi.odu.OduCommonPac # noqa: E501

    :param uuid: Id of meg
    :type uuid: str
    :param local_id: Id of mep
    :type local_id: str

    :rtype: TapiOduOduCommonPac
    """
    return 'do some magic!'


def data_context_oam_context_meguuid_meplocal_id_odu_connection_end_point_spec_odu_ctp_get(uuid, local_id):  # noqa: E501
    """data_context_oam_context_meguuid_meplocal_id_odu_connection_end_point_spec_odu_ctp_get

    returns tapi.odu.OduCtpPac # noqa: E501

    :param uuid: Id of meg
    :type uuid: str
    :param local_id: Id of mep
    :type local_id: str

    :rtype: TapiOduOduCtpPac
    """
    return 'do some magic!'


def data_context_oam_context_meguuid_meplocal_id_odu_connection_end_point_spec_odu_protection_get(uuid, local_id):  # noqa: E501
    """data_context_oam_context_meguuid_meplocal_id_odu_connection_end_point_spec_odu_protection_get

    returns tapi.odu.OduProtectionPac # noqa: E501

    :param uuid: Id of meg
    :type uuid: str
    :param local_id: Id of mep
    :type local_id: str

    :rtype: TapiOduOduProtectionPac
    """
    return 'do some magic!'


def data_context_oam_context_meguuid_meplocal_id_odu_connection_end_point_spec_odu_term_and_adapter_accepted_payload_type_get(uuid, local_id):  # noqa: E501
    """data_context_oam_context_meguuid_meplocal_id_odu_connection_end_point_spec_odu_term_and_adapter_accepted_payload_type_get

    returns tapi.odu.OduPayloadType # noqa: E501

    :param uuid: Id of meg
    :type uuid: str
    :param local_id: Id of mep
    :type local_id: str

    :rtype: TapiOduOduPayloadType
    """
    return 'do some magic!'


def data_context_oam_context_meguuid_meplocal_id_odu_connection_end_point_spec_odu_term_and_adapter_get(uuid, local_id):  # noqa: E501
    """data_context_oam_context_meguuid_meplocal_id_odu_connection_end_point_spec_odu_term_and_adapter_get

    returns tapi.odu.OduTerminationAndClientAdaptationPac # noqa: E501

    :param uuid: Id of meg
    :type uuid: str
    :param local_id: Id of mep
    :type local_id: str

    :rtype: TapiOduOduTerminationAndClientAdaptationPac
    """
    return 'do some magic!'


def data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_get(uuid, local_id):  # noqa: E501
    """data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_get

    returns tapi.odu.OduMipSpec # noqa: E501

    :param uuid: Id of meg
    :type uuid: str
    :param local_id: Id of mip
    :type local_id: str

    :rtype: TapiOduOduMipSpec
    """
    return 'do some magic!'


def data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_odu_defect_get(uuid, local_id):  # noqa: E501
    """data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_odu_defect_get

    returns tapi.odu.OduDefectPac # noqa: E501

    :param uuid: Id of meg
    :type uuid: str
    :param local_id: Id of mip
    :type local_id: str

    :rtype: TapiOduOduDefectPac
    """
    return 'do some magic!'


def data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_odu_mip_deg_thr_get(uuid, local_id):  # noqa: E501
    """data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_odu_mip_deg_thr_get

    returns tapi.odu.DegThr # noqa: E501

    :param uuid: Id of meg
    :type uuid: str
    :param local_id: Id of mip
    :type local_id: str

    :rtype: TapiOduDegThr
    """
    return 'do some magic!'


def data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_odu_mip_get(uuid, local_id):  # noqa: E501
    """data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_odu_mip_get

    returns tapi.odu.OduMipPac # noqa: E501

    :param uuid: Id of meg
    :type uuid: str
    :param local_id: Id of mip
    :type local_id: str

    :rtype: TapiOduOduMipPac
    """
    return 'do some magic!'


def data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_odu_ncm_get(uuid, local_id):  # noqa: E501
    """data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_odu_ncm_get

    returns tapi.odu.OduNcmPac # noqa: E501

    :param uuid: Id of meg
    :type uuid: str
    :param local_id: Id of mip
    :type local_id: str

    :rtype: TapiOduOduNcmPac
    """
    return 'do some magic!'


def data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_odu_pm_get(uuid, local_id):  # noqa: E501
    """data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_odu_pm_get

    returns tapi.odu.OduPmPac # noqa: E501

    :param uuid: Id of meg
    :type uuid: str
    :param local_id: Id of mip
    :type local_id: str

    :rtype: TapiOduOduPmPac
    """
    return 'do some magic!'


def data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_odu_pm_uas_get(uuid, local_id):  # noqa: E501
    """data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_odu_pm_uas_get

    returns tapi.odu.UasChoice # noqa: E501

    :param uuid: Id of meg
    :type uuid: str
    :param local_id: Id of mip
    :type local_id: str

    :rtype: TapiOduUasChoice
    """
    return 'do some magic!'


def data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_odu_tcm_get(uuid, local_id):  # noqa: E501
    """data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_odu_tcm_get

    returns tapi.odu.OduTcmMipPac # noqa: E501

    :param uuid: Id of meg
    :type uuid: str
    :param local_id: Id of mip
    :type local_id: str

    :rtype: TapiOduOduTcmMipPac
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_odu_connection_end_point_spec_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_odu_connection_end_point_spec_get

    returns tapi.odu.OduConnectionEndPointSpec # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiOduOduConnectionEndPointSpec
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_odu_connection_end_point_spec_odu_common_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_odu_connection_end_point_spec_odu_common_get

    returns tapi.odu.OduCommonPac # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiOduOduCommonPac
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_odu_connection_end_point_spec_odu_ctp_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_odu_connection_end_point_spec_odu_ctp_get

    returns tapi.odu.OduCtpPac # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiOduOduCtpPac
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_odu_connection_end_point_spec_odu_protection_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_odu_connection_end_point_spec_odu_protection_get

    returns tapi.odu.OduProtectionPac # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiOduOduProtectionPac
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_odu_connection_end_point_spec_odu_term_and_adapter_accepted_payload_type_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_odu_connection_end_point_spec_odu_term_and_adapter_accepted_payload_type_get

    returns tapi.odu.OduPayloadType # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiOduOduPayloadType
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_odu_connection_end_point_spec_odu_term_and_adapter_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_odu_connection_end_point_spec_odu_term_and_adapter_get

    returns tapi.odu.OduTerminationAndClientAdaptationPac # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiOduOduTerminationAndClientAdaptationPac
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_odu_node_edge_point_spec_get(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_odu_node_edge_point_spec_get

    returns tapi.odu.OduNodeEdgePointSpec # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str

    :rtype: TapiOduOduNodeEdgePointSpec
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_odu_node_edge_point_spec_odu_pool_get(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_odu_node_edge_point_spec_odu_pool_get

    returns tapi.odu.OduPoolPac # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str

    :rtype: TapiOduOduPoolPac
    """
    return 'do some magic!'
