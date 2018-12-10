import connexion
import six

from tapi_server.models.tapi_photonic_media_application_identifier import TapiPhotonicMediaApplicationIdentifier  # noqa: E501
from tapi_server.models.tapi_photonic_media_central_frequency import TapiPhotonicMediaCentralFrequency  # noqa: E501
from tapi_server.models.tapi_photonic_media_fec_properties_pac import TapiPhotonicMediaFecPropertiesPac  # noqa: E501
from tapi_server.models.tapi_photonic_media_frequency_constraint import TapiPhotonicMediaFrequencyConstraint  # noqa: E501
from tapi_server.models.tapi_photonic_media_laser_properties_pac import TapiPhotonicMediaLaserPropertiesPac  # noqa: E501
from tapi_server.models.tapi_photonic_media_media_channel_assembly_spec import TapiPhotonicMediaMediaChannelAssemblySpec  # noqa: E501
from tapi_server.models.tapi_photonic_media_media_channel_connection_end_point_spec import TapiPhotonicMediaMediaChannelConnectionEndPointSpec  # noqa: E501
from tapi_server.models.tapi_photonic_media_media_channel_node_edge_point_spec import TapiPhotonicMediaMediaChannelNodeEdgePointSpec  # noqa: E501
from tapi_server.models.tapi_photonic_media_media_channel_pool_capability_pac import TapiPhotonicMediaMediaChannelPoolCapabilityPac  # noqa: E501
from tapi_server.models.tapi_photonic_media_media_channel_properties_pac import TapiPhotonicMediaMediaChannelPropertiesPac  # noqa: E501
from tapi_server.models.tapi_photonic_media_media_channel_service_interface_point_spec import TapiPhotonicMediaMediaChannelServiceInterfacePointSpec  # noqa: E501
from tapi_server.models.tapi_photonic_media_ots_connection_end_point_spec import TapiPhotonicMediaOtsConnectionEndPointSpec  # noqa: E501
from tapi_server.models.tapi_photonic_media_otsi_assembly_connection_end_point_spec import TapiPhotonicMediaOtsiAssemblyConnectionEndPointSpec  # noqa: E501
from tapi_server.models.tapi_photonic_media_otsi_capability_pac import TapiPhotonicMediaOtsiCapabilityPac  # noqa: E501
from tapi_server.models.tapi_photonic_media_otsi_connection_end_point_spec import TapiPhotonicMediaOtsiConnectionEndPointSpec  # noqa: E501
from tapi_server.models.tapi_photonic_media_otsi_connectivity_service_end_point_spec import TapiPhotonicMediaOtsiConnectivityServiceEndPointSpec  # noqa: E501
from tapi_server.models.tapi_photonic_media_otsi_gserver_adaptation_pac import TapiPhotonicMediaOtsiGserverAdaptationPac  # noqa: E501
from tapi_server.models.tapi_photonic_media_otsi_service_interface_point_spec import TapiPhotonicMediaOtsiServiceInterfacePointSpec  # noqa: E501
from tapi_server.models.tapi_photonic_media_otsi_termination_config_pac import TapiPhotonicMediaOtsiTerminationConfigPac  # noqa: E501
from tapi_server.models.tapi_photonic_media_otsi_termination_pac import TapiPhotonicMediaOtsiTerminationPac  # noqa: E501
from tapi_server.models.tapi_photonic_media_power_properties_pac import TapiPhotonicMediaPowerPropertiesPac  # noqa: E501
from tapi_server.models.tapi_photonic_media_spectrum_band import TapiPhotonicMediaSpectrumBand  # noqa: E501
from tapi_server.models.tapi_photonic_media_total_power_threshold_pac import TapiPhotonicMediaTotalPowerThresholdPac  # noqa: E501
from tapi_server import util


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_delete(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_delete

    removes tapi.photonic.media.MediaChannelServiceInterfacePointSpec # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_get(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_get

    returns tapi.photonic.media.MediaChannelServiceInterfacePointSpec # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiPhotonicMediaMediaChannelServiceInterfacePointSpec
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_mc_pool_available_spectrumupper_frequencylower_frequency_frequency_constraint_get(uuid, local_id, upper_frequency, lower_frequency):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_mc_pool_available_spectrumupper_frequencylower_frequency_frequency_constraint_get

    returns tapi.photonic.media.FrequencyConstraint # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param upper_frequency: Id of available-spectrum
    :type upper_frequency: int
    :param lower_frequency: Id of available-spectrum
    :type lower_frequency: int

    :rtype: TapiPhotonicMediaFrequencyConstraint
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_mc_pool_available_spectrumupper_frequencylower_frequency_get(uuid, local_id, upper_frequency, lower_frequency):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_mc_pool_available_spectrumupper_frequencylower_frequency_get

    returns tapi.photonic.media.SpectrumBand # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param upper_frequency: Id of available-spectrum
    :type upper_frequency: int
    :param lower_frequency: Id of available-spectrum
    :type lower_frequency: int

    :rtype: TapiPhotonicMediaSpectrumBand
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_mc_pool_get(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_mc_pool_get

    returns tapi.photonic.media.MediaChannelPoolCapabilityPac # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiPhotonicMediaMediaChannelPoolCapabilityPac
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_mc_pool_occupied_spectrumupper_frequencylower_frequency_frequency_constraint_get(uuid, local_id, upper_frequency, lower_frequency):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_mc_pool_occupied_spectrumupper_frequencylower_frequency_frequency_constraint_get

    returns tapi.photonic.media.FrequencyConstraint # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param upper_frequency: Id of occupied-spectrum
    :type upper_frequency: int
    :param lower_frequency: Id of occupied-spectrum
    :type lower_frequency: int

    :rtype: TapiPhotonicMediaFrequencyConstraint
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_mc_pool_occupied_spectrumupper_frequencylower_frequency_get(uuid, local_id, upper_frequency, lower_frequency):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_mc_pool_occupied_spectrumupper_frequencylower_frequency_get

    returns tapi.photonic.media.SpectrumBand # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param upper_frequency: Id of occupied-spectrum
    :type upper_frequency: int
    :param lower_frequency: Id of occupied-spectrum
    :type lower_frequency: int

    :rtype: TapiPhotonicMediaSpectrumBand
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_mc_pool_supportable_spectrumupper_frequencylower_frequency_frequency_constraint_get(uuid, local_id, upper_frequency, lower_frequency):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_mc_pool_supportable_spectrumupper_frequencylower_frequency_frequency_constraint_get

    returns tapi.photonic.media.FrequencyConstraint # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param upper_frequency: Id of supportable-spectrum
    :type upper_frequency: int
    :param lower_frequency: Id of supportable-spectrum
    :type lower_frequency: int

    :rtype: TapiPhotonicMediaFrequencyConstraint
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_mc_pool_supportable_spectrumupper_frequencylower_frequency_get(uuid, local_id, upper_frequency, lower_frequency):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_mc_pool_supportable_spectrumupper_frequencylower_frequency_get

    returns tapi.photonic.media.SpectrumBand # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param upper_frequency: Id of supportable-spectrum
    :type upper_frequency: int
    :param lower_frequency: Id of supportable-spectrum
    :type lower_frequency: int

    :rtype: TapiPhotonicMediaSpectrumBand
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_post(uuid, local_id, tapi_photonic_media_media_channel_service_interface_point_spec=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_post

    creates tapi.photonic.media.MediaChannelServiceInterfacePointSpec # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_photonic_media_media_channel_service_interface_point_spec: tapi.photonic.media.MediaChannelServiceInterfacePointSpec to be added to list
    :type tapi_photonic_media_media_channel_service_interface_point_spec: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_photonic_media_media_channel_service_interface_point_spec = TapiPhotonicMediaMediaChannelServiceInterfacePointSpec.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_put(uuid, local_id, tapi_photonic_media_media_channel_service_interface_point_spec=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_put

    creates or updates tapi.photonic.media.MediaChannelServiceInterfacePointSpec # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_photonic_media_media_channel_service_interface_point_spec: tapi.photonic.media.MediaChannelServiceInterfacePointSpec to be added or updated
    :type tapi_photonic_media_media_channel_service_interface_point_spec: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_photonic_media_media_channel_service_interface_point_spec = TapiPhotonicMediaMediaChannelServiceInterfacePointSpec.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_delete(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_delete

    removes tapi.photonic.media.OtsiConnectivityServiceEndPointSpec # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_get(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_get

    returns tapi.photonic.media.OtsiConnectivityServiceEndPointSpec # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiPhotonicMediaOtsiConnectivityServiceEndPointSpec
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_application_identifier_delete(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_application_identifier_delete

    removes tapi.photonic.media.ApplicationIdentifier # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_application_identifier_get(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_application_identifier_get

    returns tapi.photonic.media.ApplicationIdentifier # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiPhotonicMediaApplicationIdentifier
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_application_identifier_post(uuid, local_id, tapi_photonic_media_application_identifier=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_application_identifier_post

    creates tapi.photonic.media.ApplicationIdentifier # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_photonic_media_application_identifier: tapi.photonic.media.ApplicationIdentifier to be added to list
    :type tapi_photonic_media_application_identifier: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_photonic_media_application_identifier = TapiPhotonicMediaApplicationIdentifier.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_application_identifier_put(uuid, local_id, tapi_photonic_media_application_identifier=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_application_identifier_put

    creates or updates tapi.photonic.media.ApplicationIdentifier # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_photonic_media_application_identifier: tapi.photonic.media.ApplicationIdentifier to be added or updated
    :type tapi_photonic_media_application_identifier: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_photonic_media_application_identifier = TapiPhotonicMediaApplicationIdentifier.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_delete(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_delete

    removes tapi.photonic.media.CentralFrequency # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_frequency_constraint_delete(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_frequency_constraint_delete

    removes tapi.photonic.media.FrequencyConstraint # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_frequency_constraint_get(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_frequency_constraint_get

    returns tapi.photonic.media.FrequencyConstraint # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiPhotonicMediaFrequencyConstraint
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_frequency_constraint_post(uuid, local_id, tapi_photonic_media_frequency_constraint=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_frequency_constraint_post

    creates tapi.photonic.media.FrequencyConstraint # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_photonic_media_frequency_constraint: tapi.photonic.media.FrequencyConstraint to be added to list
    :type tapi_photonic_media_frequency_constraint: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_photonic_media_frequency_constraint = TapiPhotonicMediaFrequencyConstraint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_frequency_constraint_put(uuid, local_id, tapi_photonic_media_frequency_constraint=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_frequency_constraint_put

    creates or updates tapi.photonic.media.FrequencyConstraint # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_photonic_media_frequency_constraint: tapi.photonic.media.FrequencyConstraint to be added or updated
    :type tapi_photonic_media_frequency_constraint: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_photonic_media_frequency_constraint = TapiPhotonicMediaFrequencyConstraint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_get(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_get

    returns tapi.photonic.media.CentralFrequency # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiPhotonicMediaCentralFrequency
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_post(uuid, local_id, tapi_photonic_media_central_frequency=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_post

    creates tapi.photonic.media.CentralFrequency # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_photonic_media_central_frequency: tapi.photonic.media.CentralFrequency to be added to list
    :type tapi_photonic_media_central_frequency: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_photonic_media_central_frequency = TapiPhotonicMediaCentralFrequency.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_put(uuid, local_id, tapi_photonic_media_central_frequency=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_put

    creates or updates tapi.photonic.media.CentralFrequency # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_photonic_media_central_frequency: tapi.photonic.media.CentralFrequency to be added or updated
    :type tapi_photonic_media_central_frequency: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_photonic_media_central_frequency = TapiPhotonicMediaCentralFrequency.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_delete(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_delete

    removes tapi.photonic.media.OtsiTerminationConfigPac # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_get(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_get

    returns tapi.photonic.media.OtsiTerminationConfigPac # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiPhotonicMediaOtsiTerminationConfigPac
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_post(uuid, local_id, tapi_photonic_media_otsi_termination_config_pac=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_post

    creates tapi.photonic.media.OtsiTerminationConfigPac # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_photonic_media_otsi_termination_config_pac: tapi.photonic.media.OtsiTerminationConfigPac to be added to list
    :type tapi_photonic_media_otsi_termination_config_pac: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_photonic_media_otsi_termination_config_pac = TapiPhotonicMediaOtsiTerminationConfigPac.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_put(uuid, local_id, tapi_photonic_media_otsi_termination_config_pac=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_put

    creates or updates tapi.photonic.media.OtsiTerminationConfigPac # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_photonic_media_otsi_termination_config_pac: tapi.photonic.media.OtsiTerminationConfigPac to be added or updated
    :type tapi_photonic_media_otsi_termination_config_pac: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_photonic_media_otsi_termination_config_pac = TapiPhotonicMediaOtsiTerminationConfigPac.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_delete(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_delete

    removes tapi.photonic.media.SpectrumBand # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_frequency_constraint_delete(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_frequency_constraint_delete

    removes tapi.photonic.media.FrequencyConstraint # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_frequency_constraint_get(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_frequency_constraint_get

    returns tapi.photonic.media.FrequencyConstraint # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiPhotonicMediaFrequencyConstraint
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_frequency_constraint_post(uuid, local_id, tapi_photonic_media_frequency_constraint=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_frequency_constraint_post

    creates tapi.photonic.media.FrequencyConstraint # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_photonic_media_frequency_constraint: tapi.photonic.media.FrequencyConstraint to be added to list
    :type tapi_photonic_media_frequency_constraint: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_photonic_media_frequency_constraint = TapiPhotonicMediaFrequencyConstraint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_frequency_constraint_put(uuid, local_id, tapi_photonic_media_frequency_constraint=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_frequency_constraint_put

    creates or updates tapi.photonic.media.FrequencyConstraint # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_photonic_media_frequency_constraint: tapi.photonic.media.FrequencyConstraint to be added or updated
    :type tapi_photonic_media_frequency_constraint: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_photonic_media_frequency_constraint = TapiPhotonicMediaFrequencyConstraint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_get(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_get

    returns tapi.photonic.media.SpectrumBand # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiPhotonicMediaSpectrumBand
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_post(uuid, local_id, tapi_photonic_media_spectrum_band=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_post

    creates tapi.photonic.media.SpectrumBand # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_photonic_media_spectrum_band: tapi.photonic.media.SpectrumBand to be added to list
    :type tapi_photonic_media_spectrum_band: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_photonic_media_spectrum_band = TapiPhotonicMediaSpectrumBand.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_put(uuid, local_id, tapi_photonic_media_spectrum_band=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_put

    creates or updates tapi.photonic.media.SpectrumBand # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_photonic_media_spectrum_band: tapi.photonic.media.SpectrumBand to be added or updated
    :type tapi_photonic_media_spectrum_band: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_photonic_media_spectrum_band = TapiPhotonicMediaSpectrumBand.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_transmit_power_delete(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_transmit_power_delete

    removes tapi.photonic.media.PowerPropertiesPac # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_transmit_power_get(uuid, local_id):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_transmit_power_get

    returns tapi.photonic.media.PowerPropertiesPac # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiPhotonicMediaPowerPropertiesPac
    """
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_transmit_power_post(uuid, local_id, tapi_photonic_media_power_properties_pac=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_transmit_power_post

    creates tapi.photonic.media.PowerPropertiesPac # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_photonic_media_power_properties_pac: tapi.photonic.media.PowerPropertiesPac to be added to list
    :type tapi_photonic_media_power_properties_pac: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_photonic_media_power_properties_pac = TapiPhotonicMediaPowerPropertiesPac.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_transmit_power_put(uuid, local_id, tapi_photonic_media_power_properties_pac=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_transmit_power_put

    creates or updates tapi.photonic.media.PowerPropertiesPac # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_photonic_media_power_properties_pac: tapi.photonic.media.PowerPropertiesPac to be added or updated
    :type tapi_photonic_media_power_properties_pac: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_photonic_media_power_properties_pac = TapiPhotonicMediaPowerPropertiesPac.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_post(uuid, local_id, tapi_photonic_media_otsi_connectivity_service_end_point_spec=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_post

    creates tapi.photonic.media.OtsiConnectivityServiceEndPointSpec # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_photonic_media_otsi_connectivity_service_end_point_spec: tapi.photonic.media.OtsiConnectivityServiceEndPointSpec to be added to list
    :type tapi_photonic_media_otsi_connectivity_service_end_point_spec: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_photonic_media_otsi_connectivity_service_end_point_spec = TapiPhotonicMediaOtsiConnectivityServiceEndPointSpec.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_put(uuid, local_id, tapi_photonic_media_otsi_connectivity_service_end_point_spec=None):  # noqa: E501
    """data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_put

    creates or updates tapi.photonic.media.OtsiConnectivityServiceEndPointSpec # noqa: E501

    :param uuid: Id of connectivity-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_photonic_media_otsi_connectivity_service_end_point_spec: tapi.photonic.media.OtsiConnectivityServiceEndPointSpec to be added or updated
    :type tapi_photonic_media_otsi_connectivity_service_end_point_spec: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_photonic_media_otsi_connectivity_service_end_point_spec = TapiPhotonicMediaOtsiConnectivityServiceEndPointSpec.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_delete(uuid):  # noqa: E501
    """data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_delete

    removes tapi.photonic.media.MediaChannelServiceInterfacePointSpec # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_get(uuid):  # noqa: E501
    """data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_get

    returns tapi.photonic.media.MediaChannelServiceInterfacePointSpec # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str

    :rtype: TapiPhotonicMediaMediaChannelServiceInterfacePointSpec
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_mc_pool_available_spectrumupper_frequencylower_frequency_frequency_constraint_get(uuid, upper_frequency, lower_frequency):  # noqa: E501
    """data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_mc_pool_available_spectrumupper_frequencylower_frequency_frequency_constraint_get

    returns tapi.photonic.media.FrequencyConstraint # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str
    :param upper_frequency: Id of available-spectrum
    :type upper_frequency: int
    :param lower_frequency: Id of available-spectrum
    :type lower_frequency: int

    :rtype: TapiPhotonicMediaFrequencyConstraint
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_mc_pool_available_spectrumupper_frequencylower_frequency_get(uuid, upper_frequency, lower_frequency):  # noqa: E501
    """data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_mc_pool_available_spectrumupper_frequencylower_frequency_get

    returns tapi.photonic.media.SpectrumBand # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str
    :param upper_frequency: Id of available-spectrum
    :type upper_frequency: int
    :param lower_frequency: Id of available-spectrum
    :type lower_frequency: int

    :rtype: TapiPhotonicMediaSpectrumBand
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_mc_pool_get(uuid):  # noqa: E501
    """data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_mc_pool_get

    returns tapi.photonic.media.MediaChannelPoolCapabilityPac # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str

    :rtype: TapiPhotonicMediaMediaChannelPoolCapabilityPac
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_mc_pool_occupied_spectrumupper_frequencylower_frequency_frequency_constraint_get(uuid, upper_frequency, lower_frequency):  # noqa: E501
    """data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_mc_pool_occupied_spectrumupper_frequencylower_frequency_frequency_constraint_get

    returns tapi.photonic.media.FrequencyConstraint # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str
    :param upper_frequency: Id of occupied-spectrum
    :type upper_frequency: int
    :param lower_frequency: Id of occupied-spectrum
    :type lower_frequency: int

    :rtype: TapiPhotonicMediaFrequencyConstraint
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_mc_pool_occupied_spectrumupper_frequencylower_frequency_get(uuid, upper_frequency, lower_frequency):  # noqa: E501
    """data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_mc_pool_occupied_spectrumupper_frequencylower_frequency_get

    returns tapi.photonic.media.SpectrumBand # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str
    :param upper_frequency: Id of occupied-spectrum
    :type upper_frequency: int
    :param lower_frequency: Id of occupied-spectrum
    :type lower_frequency: int

    :rtype: TapiPhotonicMediaSpectrumBand
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_mc_pool_supportable_spectrumupper_frequencylower_frequency_frequency_constraint_get(uuid, upper_frequency, lower_frequency):  # noqa: E501
    """data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_mc_pool_supportable_spectrumupper_frequencylower_frequency_frequency_constraint_get

    returns tapi.photonic.media.FrequencyConstraint # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str
    :param upper_frequency: Id of supportable-spectrum
    :type upper_frequency: int
    :param lower_frequency: Id of supportable-spectrum
    :type lower_frequency: int

    :rtype: TapiPhotonicMediaFrequencyConstraint
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_mc_pool_supportable_spectrumupper_frequencylower_frequency_get(uuid, upper_frequency, lower_frequency):  # noqa: E501
    """data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_mc_pool_supportable_spectrumupper_frequencylower_frequency_get

    returns tapi.photonic.media.SpectrumBand # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str
    :param upper_frequency: Id of supportable-spectrum
    :type upper_frequency: int
    :param lower_frequency: Id of supportable-spectrum
    :type lower_frequency: int

    :rtype: TapiPhotonicMediaSpectrumBand
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_post(uuid, tapi_photonic_media_media_channel_service_interface_point_spec=None):  # noqa: E501
    """data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_post

    creates tapi.photonic.media.MediaChannelServiceInterfacePointSpec # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str
    :param tapi_photonic_media_media_channel_service_interface_point_spec: tapi.photonic.media.MediaChannelServiceInterfacePointSpec to be added to list
    :type tapi_photonic_media_media_channel_service_interface_point_spec: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_photonic_media_media_channel_service_interface_point_spec = TapiPhotonicMediaMediaChannelServiceInterfacePointSpec.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_put(uuid, tapi_photonic_media_media_channel_service_interface_point_spec=None):  # noqa: E501
    """data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_put

    creates or updates tapi.photonic.media.MediaChannelServiceInterfacePointSpec # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str
    :param tapi_photonic_media_media_channel_service_interface_point_spec: tapi.photonic.media.MediaChannelServiceInterfacePointSpec to be added or updated
    :type tapi_photonic_media_media_channel_service_interface_point_spec: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_photonic_media_media_channel_service_interface_point_spec = TapiPhotonicMediaMediaChannelServiceInterfacePointSpec.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_service_interface_pointuuid_otsi_service_interface_point_spec_delete(uuid):  # noqa: E501
    """data_context_service_interface_pointuuid_otsi_service_interface_point_spec_delete

    removes tapi.photonic.media.OtsiServiceInterfacePointSpec # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_otsi_service_interface_point_spec_get(uuid):  # noqa: E501
    """data_context_service_interface_pointuuid_otsi_service_interface_point_spec_get

    returns tapi.photonic.media.OtsiServiceInterfacePointSpec # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str

    :rtype: TapiPhotonicMediaOtsiServiceInterfacePointSpec
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_otsi_service_interface_point_spec_otsi_capability_get(uuid):  # noqa: E501
    """data_context_service_interface_pointuuid_otsi_service_interface_point_spec_otsi_capability_get

    returns tapi.photonic.media.OtsiCapabilityPac # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str

    :rtype: TapiPhotonicMediaOtsiCapabilityPac
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_otsi_service_interface_point_spec_otsi_capability_supportable_application_identifierapplication_code_get(uuid, application_code):  # noqa: E501
    """data_context_service_interface_pointuuid_otsi_service_interface_point_spec_otsi_capability_supportable_application_identifierapplication_code_get

    returns tapi.photonic.media.ApplicationIdentifier # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str
    :param application_code: Id of supportable-application-identifier
    :type application_code: str

    :rtype: TapiPhotonicMediaApplicationIdentifier
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_otsi_service_interface_point_spec_otsi_capability_supportable_lower_central_frequencycentral_frequency_frequency_constraint_get(uuid, central_frequency):  # noqa: E501
    """data_context_service_interface_pointuuid_otsi_service_interface_point_spec_otsi_capability_supportable_lower_central_frequencycentral_frequency_frequency_constraint_get

    returns tapi.photonic.media.FrequencyConstraint # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str
    :param central_frequency: Id of supportable-lower-central-frequency
    :type central_frequency: int

    :rtype: TapiPhotonicMediaFrequencyConstraint
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_otsi_service_interface_point_spec_otsi_capability_supportable_lower_central_frequencycentral_frequency_get(uuid, central_frequency):  # noqa: E501
    """data_context_service_interface_pointuuid_otsi_service_interface_point_spec_otsi_capability_supportable_lower_central_frequencycentral_frequency_get

    returns tapi.photonic.media.CentralFrequency # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str
    :param central_frequency: Id of supportable-lower-central-frequency
    :type central_frequency: int

    :rtype: TapiPhotonicMediaCentralFrequency
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_otsi_service_interface_point_spec_otsi_capability_supportable_upper_central_frequencycentral_frequency_frequency_constraint_get(uuid, central_frequency):  # noqa: E501
    """data_context_service_interface_pointuuid_otsi_service_interface_point_spec_otsi_capability_supportable_upper_central_frequencycentral_frequency_frequency_constraint_get

    returns tapi.photonic.media.FrequencyConstraint # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str
    :param central_frequency: Id of supportable-upper-central-frequency
    :type central_frequency: int

    :rtype: TapiPhotonicMediaFrequencyConstraint
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_otsi_service_interface_point_spec_otsi_capability_supportable_upper_central_frequencycentral_frequency_get(uuid, central_frequency):  # noqa: E501
    """data_context_service_interface_pointuuid_otsi_service_interface_point_spec_otsi_capability_supportable_upper_central_frequencycentral_frequency_get

    returns tapi.photonic.media.CentralFrequency # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str
    :param central_frequency: Id of supportable-upper-central-frequency
    :type central_frequency: int

    :rtype: TapiPhotonicMediaCentralFrequency
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_otsi_service_interface_point_spec_otsi_capability_total_power_warn_threshold_get(uuid):  # noqa: E501
    """data_context_service_interface_pointuuid_otsi_service_interface_point_spec_otsi_capability_total_power_warn_threshold_get

    returns tapi.photonic.media.TotalPowerThresholdPac # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str

    :rtype: TapiPhotonicMediaTotalPowerThresholdPac
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_otsi_service_interface_point_spec_post(uuid, tapi_photonic_media_otsi_service_interface_point_spec=None):  # noqa: E501
    """data_context_service_interface_pointuuid_otsi_service_interface_point_spec_post

    creates tapi.photonic.media.OtsiServiceInterfacePointSpec # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str
    :param tapi_photonic_media_otsi_service_interface_point_spec: tapi.photonic.media.OtsiServiceInterfacePointSpec to be added to list
    :type tapi_photonic_media_otsi_service_interface_point_spec: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_photonic_media_otsi_service_interface_point_spec = TapiPhotonicMediaOtsiServiceInterfacePointSpec.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_service_interface_pointuuid_otsi_service_interface_point_spec_put(uuid, tapi_photonic_media_otsi_service_interface_point_spec=None):  # noqa: E501
    """data_context_service_interface_pointuuid_otsi_service_interface_point_spec_put

    creates or updates tapi.photonic.media.OtsiServiceInterfacePointSpec # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str
    :param tapi_photonic_media_otsi_service_interface_point_spec: tapi.photonic.media.OtsiServiceInterfacePointSpec to be added or updated
    :type tapi_photonic_media_otsi_service_interface_point_spec: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_photonic_media_otsi_service_interface_point_spec = TapiPhotonicMediaOtsiServiceInterfacePointSpec.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_media_channel_assembly_spec_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_media_channel_assembly_spec_get

    returns tapi.photonic.media.MediaChannelAssemblySpec # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiPhotonicMediaMediaChannelAssemblySpec
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_media_channel_connection_end_point_spec_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_media_channel_connection_end_point_spec_get

    returns tapi.photonic.media.MediaChannelConnectionEndPointSpec # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiPhotonicMediaMediaChannelConnectionEndPointSpec
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_media_channel_connection_end_point_spec_media_channel_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_media_channel_connection_end_point_spec_media_channel_get

    returns tapi.photonic.media.MediaChannelPropertiesPac # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiPhotonicMediaMediaChannelPropertiesPac
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_media_channel_connection_end_point_spec_media_channel_measured_power_egress_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_media_channel_connection_end_point_spec_media_channel_measured_power_egress_get

    returns tapi.photonic.media.PowerPropertiesPac # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiPhotonicMediaPowerPropertiesPac
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_media_channel_connection_end_point_spec_media_channel_measured_power_ingress_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_media_channel_connection_end_point_spec_media_channel_measured_power_ingress_get

    returns tapi.photonic.media.PowerPropertiesPac # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiPhotonicMediaPowerPropertiesPac
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_media_channel_connection_end_point_spec_media_channel_occupied_spectrum_frequency_constraint_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_media_channel_connection_end_point_spec_media_channel_occupied_spectrum_frequency_constraint_get

    returns tapi.photonic.media.FrequencyConstraint # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiPhotonicMediaFrequencyConstraint
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_media_channel_connection_end_point_spec_media_channel_occupied_spectrum_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_media_channel_connection_end_point_spec_media_channel_occupied_spectrum_get

    returns tapi.photonic.media.SpectrumBand # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiPhotonicMediaSpectrumBand
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_ots_connection_end_point_spec_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_ots_connection_end_point_spec_get

    returns tapi.photonic.media.OtsConnectionEndPointSpec # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiPhotonicMediaOtsConnectionEndPointSpec
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_ots_connection_end_point_spec_ots_media_channel_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_ots_connection_end_point_spec_ots_media_channel_get

    returns tapi.photonic.media.MediaChannelPropertiesPac # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiPhotonicMediaMediaChannelPropertiesPac
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_ots_connection_end_point_spec_ots_media_channel_measured_power_egress_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_ots_connection_end_point_spec_ots_media_channel_measured_power_egress_get

    returns tapi.photonic.media.PowerPropertiesPac # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiPhotonicMediaPowerPropertiesPac
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_ots_connection_end_point_spec_ots_media_channel_measured_power_ingress_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_ots_connection_end_point_spec_ots_media_channel_measured_power_ingress_get

    returns tapi.photonic.media.PowerPropertiesPac # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiPhotonicMediaPowerPropertiesPac
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_ots_connection_end_point_spec_ots_media_channel_occupied_spectrum_frequency_constraint_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_ots_connection_end_point_spec_ots_media_channel_occupied_spectrum_frequency_constraint_get

    returns tapi.photonic.media.FrequencyConstraint # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiPhotonicMediaFrequencyConstraint
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_ots_connection_end_point_spec_ots_media_channel_occupied_spectrum_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_ots_connection_end_point_spec_ots_media_channel_occupied_spectrum_get

    returns tapi.photonic.media.SpectrumBand # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiPhotonicMediaSpectrumBand
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_assembly_connection_end_point_spec_fec_parameters_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_assembly_connection_end_point_spec_fec_parameters_get

    returns tapi.photonic.media.FecPropertiesPac # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiPhotonicMediaFecPropertiesPac
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_assembly_connection_end_point_spec_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_assembly_connection_end_point_spec_get

    returns tapi.photonic.media.OtsiAssemblyConnectionEndPointSpec # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiPhotonicMediaOtsiAssemblyConnectionEndPointSpec
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_assembly_connection_end_point_spec_otsi_adapter_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_assembly_connection_end_point_spec_otsi_adapter_get

    returns tapi.photonic.media.OtsiGserverAdaptationPac # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiPhotonicMediaOtsiGserverAdaptationPac
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_get

    returns tapi.photonic.media.OtsiConnectionEndPointSpec # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiPhotonicMediaOtsiConnectionEndPointSpec
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_get

    returns tapi.photonic.media.OtsiTerminationPac # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiPhotonicMediaOtsiTerminationPac
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_laser_properties_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_laser_properties_get

    returns tapi.photonic.media.LaserPropertiesPac # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiPhotonicMediaLaserPropertiesPac
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_received_power_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_received_power_get

    returns tapi.photonic.media.PowerPropertiesPac # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiPhotonicMediaPowerPropertiesPac
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_selected_application_identifier_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_selected_application_identifier_get

    returns tapi.photonic.media.ApplicationIdentifier # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiPhotonicMediaApplicationIdentifier
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_selected_central_frequency_frequency_constraint_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_selected_central_frequency_frequency_constraint_get

    returns tapi.photonic.media.FrequencyConstraint # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiPhotonicMediaFrequencyConstraint
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_selected_central_frequency_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_selected_central_frequency_get

    returns tapi.photonic.media.CentralFrequency # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiPhotonicMediaCentralFrequency
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_selected_spectrum_frequency_constraint_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_selected_spectrum_frequency_constraint_get

    returns tapi.photonic.media.FrequencyConstraint # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiPhotonicMediaFrequencyConstraint
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_selected_spectrum_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_selected_spectrum_get

    returns tapi.photonic.media.SpectrumBand # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiPhotonicMediaSpectrumBand
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_transmited_power_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_transmited_power_get

    returns tapi.photonic.media.PowerPropertiesPac # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiPhotonicMediaPowerPropertiesPac
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_get(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_get

    returns tapi.photonic.media.MediaChannelNodeEdgePointSpec # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str

    :rtype: TapiPhotonicMediaMediaChannelNodeEdgePointSpec
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_mc_pool_available_spectrumupper_frequencylower_frequency_frequency_constraint_get(uuid, node_uuid, owned_node_edge_point_uuid, upper_frequency, lower_frequency):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_mc_pool_available_spectrumupper_frequencylower_frequency_frequency_constraint_get

    returns tapi.photonic.media.FrequencyConstraint # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param upper_frequency: Id of available-spectrum
    :type upper_frequency: int
    :param lower_frequency: Id of available-spectrum
    :type lower_frequency: int

    :rtype: TapiPhotonicMediaFrequencyConstraint
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_mc_pool_available_spectrumupper_frequencylower_frequency_get(uuid, node_uuid, owned_node_edge_point_uuid, upper_frequency, lower_frequency):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_mc_pool_available_spectrumupper_frequencylower_frequency_get

    returns tapi.photonic.media.SpectrumBand # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param upper_frequency: Id of available-spectrum
    :type upper_frequency: int
    :param lower_frequency: Id of available-spectrum
    :type lower_frequency: int

    :rtype: TapiPhotonicMediaSpectrumBand
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_mc_pool_get(uuid, node_uuid, owned_node_edge_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_mc_pool_get

    returns tapi.photonic.media.MediaChannelPoolCapabilityPac # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str

    :rtype: TapiPhotonicMediaMediaChannelPoolCapabilityPac
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_mc_pool_occupied_spectrumupper_frequencylower_frequency_frequency_constraint_get(uuid, node_uuid, owned_node_edge_point_uuid, upper_frequency, lower_frequency):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_mc_pool_occupied_spectrumupper_frequencylower_frequency_frequency_constraint_get

    returns tapi.photonic.media.FrequencyConstraint # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param upper_frequency: Id of occupied-spectrum
    :type upper_frequency: int
    :param lower_frequency: Id of occupied-spectrum
    :type lower_frequency: int

    :rtype: TapiPhotonicMediaFrequencyConstraint
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_mc_pool_occupied_spectrumupper_frequencylower_frequency_get(uuid, node_uuid, owned_node_edge_point_uuid, upper_frequency, lower_frequency):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_mc_pool_occupied_spectrumupper_frequencylower_frequency_get

    returns tapi.photonic.media.SpectrumBand # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param upper_frequency: Id of occupied-spectrum
    :type upper_frequency: int
    :param lower_frequency: Id of occupied-spectrum
    :type lower_frequency: int

    :rtype: TapiPhotonicMediaSpectrumBand
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_mc_pool_supportable_spectrumupper_frequencylower_frequency_frequency_constraint_get(uuid, node_uuid, owned_node_edge_point_uuid, upper_frequency, lower_frequency):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_mc_pool_supportable_spectrumupper_frequencylower_frequency_frequency_constraint_get

    returns tapi.photonic.media.FrequencyConstraint # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param upper_frequency: Id of supportable-spectrum
    :type upper_frequency: int
    :param lower_frequency: Id of supportable-spectrum
    :type lower_frequency: int

    :rtype: TapiPhotonicMediaFrequencyConstraint
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_mc_pool_supportable_spectrumupper_frequencylower_frequency_get(uuid, node_uuid, owned_node_edge_point_uuid, upper_frequency, lower_frequency):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_mc_pool_supportable_spectrumupper_frequencylower_frequency_get

    returns tapi.photonic.media.SpectrumBand # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param upper_frequency: Id of supportable-spectrum
    :type upper_frequency: int
    :param lower_frequency: Id of supportable-spectrum
    :type lower_frequency: int

    :rtype: TapiPhotonicMediaSpectrumBand
    """
    return 'do some magic!'
