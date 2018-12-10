import connexion
import six

from tapi_server.models.inline_object24 import InlineObject24  # noqa: E501
from tapi_server.models.inline_object32 import InlineObject32  # noqa: E501
from tapi_server.models.tapi_common_bandwidth_profile import TapiCommonBandwidthProfile  # noqa: E501
from tapi_server.models.tapi_common_capacity import TapiCommonCapacity  # noqa: E501
from tapi_server.models.tapi_common_capacity_value import TapiCommonCapacityValue  # noqa: E501
from tapi_server.models.tapi_common_context import TapiCommonContext  # noqa: E501
from tapi_server.models.tapi_common_context_service_interface_point import TapiCommonContextServiceInterfacePoint  # noqa: E501
from tapi_server.models.tapi_common_get_service_interface_point_details import TapiCommonGetServiceInterfacePointDetails  # noqa: E501
from tapi_server.models.tapi_common_get_service_interface_point_list import TapiCommonGetServiceInterfacePointList  # noqa: E501
from tapi_server.models.tapi_common_getserviceinterfacepointdetails_output import TapiCommonGetserviceinterfacepointdetailsOutput  # noqa: F401,E501
from tapi_server.models.tapi_common_getserviceinterfacepointlist_output import TapiCommonGetserviceinterfacepointlistOutput  # noqa: F401,E501
from tapi_server.models.tapi_common_name_and_value import TapiCommonNameAndValue  # noqa: E501
from tapi_server import util
from tapi_server import database


def data_context_delete():  # noqa: E501
    """data_context_delete

    removes tapi.common.Context # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def data_context_get():  # noqa: E501
    """data_context_get

    returns tapi.common.Context # noqa: E501


    :rtype: TapiCommonContext
    """
    return database.context;


def data_context_name_post(tapi_common_name_and_value=None):  # noqa: E501
    """data_context_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param tapi_common_name_and_value: tapi.common.NameAndValue to be added to list
    :type tapi_common_name_and_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_name_and_value = TapiCommonNameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_namevalue_name_delete(value_name):  # noqa: E501
    """data_context_namevalue_name_delete

    removes tapi.common.NameAndValue # noqa: E501

    :param value_name: Id of name
    :type value_name: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_namevalue_name_get(value_name):  # noqa: E501
    """data_context_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_namevalue_name_post(value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_namevalue_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param value_name: Id of name
    :type value_name: str
    :param tapi_common_name_and_value: tapi.common.NameAndValue to be added to list
    :type tapi_common_name_and_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_name_and_value = TapiCommonNameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_namevalue_name_put(value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_namevalue_name_put

    creates or updates tapi.common.NameAndValue # noqa: E501

    :param value_name: Id of name
    :type value_name: str
    :param tapi_common_name_and_value: tapi.common.NameAndValue to be added or updated
    :type tapi_common_name_and_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_name_and_value = TapiCommonNameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_post(tapi_common_context=None):  # noqa: E501
    """data_context_post

    creates tapi.common.Context # noqa: E501

    :param tapi_common_context: tapi.common.Context to be added to list
    :type tapi_common_context: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_context = TapiCommonContext.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_put(tapi_common_context=None):  # noqa: E501
    """data_context_put

    creates or updates tapi.common.Context # noqa: E501

    :param tapi_common_context: tapi.common.Context to be added or updated
    :type tapi_common_context: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_context = TapiCommonContext.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_service_interface_point_post(tapi_common_context_service_interface_point=None):  # noqa: E501
    """data_context_service_interface_point_post

    creates tapi.common.context.ServiceInterfacePoint # noqa: E501

    :param tapi_common_context_service_interface_point: tapi.common.context.ServiceInterfacePoint to be added to list
    :type tapi_common_context_service_interface_point: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_context_service_interface_point = TapiCommonContextServiceInterfacePoint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_service_interface_pointuuid_available_capacity_bandwidth_profile_committed_burst_size_get(uuid):  # noqa: E501
    """data_context_service_interface_pointuuid_available_capacity_bandwidth_profile_committed_burst_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_available_capacity_bandwidth_profile_committed_information_rate_get(uuid):  # noqa: E501
    """data_context_service_interface_pointuuid_available_capacity_bandwidth_profile_committed_information_rate_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_available_capacity_bandwidth_profile_get(uuid):  # noqa: E501
    """data_context_service_interface_pointuuid_available_capacity_bandwidth_profile_get

    returns tapi.common.BandwidthProfile # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str

    :rtype: TapiCommonBandwidthProfile
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_available_capacity_bandwidth_profile_peak_burst_size_get(uuid):  # noqa: E501
    """data_context_service_interface_pointuuid_available_capacity_bandwidth_profile_peak_burst_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_available_capacity_bandwidth_profile_peak_information_rate_get(uuid):  # noqa: E501
    """data_context_service_interface_pointuuid_available_capacity_bandwidth_profile_peak_information_rate_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_available_capacity_get(uuid):  # noqa: E501
    """data_context_service_interface_pointuuid_available_capacity_get

    returns tapi.common.Capacity # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str

    :rtype: TapiCommonCapacity
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_available_capacity_total_size_get(uuid):  # noqa: E501
    """data_context_service_interface_pointuuid_available_capacity_total_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_delete(uuid):  # noqa: E501
    """data_context_service_interface_pointuuid_delete

    removes tapi.common.context.ServiceInterfacePoint # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_get(uuid):  # noqa: E501
    """data_context_service_interface_pointuuid_get

    returns tapi.common.context.ServiceInterfacePoint # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str

    :rtype: TapiCommonContextServiceInterfacePoint
    """
    return database.service_interface_point(uuid);


def data_context_service_interface_pointuuid_name_post(uuid, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_service_interface_pointuuid_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str
    :param tapi_common_name_and_value: tapi.common.NameAndValue to be added to list
    :type tapi_common_name_and_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_name_and_value = TapiCommonNameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_service_interface_pointuuid_namevalue_name_delete(uuid, value_name):  # noqa: E501
    """data_context_service_interface_pointuuid_namevalue_name_delete

    removes tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_namevalue_name_get(uuid, value_name):  # noqa: E501
    """data_context_service_interface_pointuuid_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_namevalue_name_post(uuid, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_service_interface_pointuuid_namevalue_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of service-interface-point
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


def data_context_service_interface_pointuuid_namevalue_name_put(uuid, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_service_interface_pointuuid_namevalue_name_put

    creates or updates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of service-interface-point
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


def data_context_service_interface_pointuuid_post(uuid, tapi_common_context_service_interface_point=None):  # noqa: E501
    """data_context_service_interface_pointuuid_post

    creates tapi.common.context.ServiceInterfacePoint # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str
    :param tapi_common_context_service_interface_point: tapi.common.context.ServiceInterfacePoint to be added to list
    :type tapi_common_context_service_interface_point: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_context_service_interface_point = TapiCommonContextServiceInterfacePoint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_service_interface_pointuuid_put(uuid, tapi_common_context_service_interface_point=None):  # noqa: E501
    """data_context_service_interface_pointuuid_put

    creates or updates tapi.common.context.ServiceInterfacePoint # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str
    :param tapi_common_context_service_interface_point: tapi.common.context.ServiceInterfacePoint to be added or updated
    :type tapi_common_context_service_interface_point: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_context_service_interface_point = TapiCommonContextServiceInterfacePoint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_service_interface_pointuuid_total_potential_capacity_bandwidth_profile_committed_burst_size_get(uuid):  # noqa: E501
    """data_context_service_interface_pointuuid_total_potential_capacity_bandwidth_profile_committed_burst_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_total_potential_capacity_bandwidth_profile_committed_information_rate_get(uuid):  # noqa: E501
    """data_context_service_interface_pointuuid_total_potential_capacity_bandwidth_profile_committed_information_rate_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_total_potential_capacity_bandwidth_profile_get(uuid):  # noqa: E501
    """data_context_service_interface_pointuuid_total_potential_capacity_bandwidth_profile_get

    returns tapi.common.BandwidthProfile # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str

    :rtype: TapiCommonBandwidthProfile
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_total_potential_capacity_bandwidth_profile_peak_burst_size_get(uuid):  # noqa: E501
    """data_context_service_interface_pointuuid_total_potential_capacity_bandwidth_profile_peak_burst_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_total_potential_capacity_bandwidth_profile_peak_information_rate_get(uuid):  # noqa: E501
    """data_context_service_interface_pointuuid_total_potential_capacity_bandwidth_profile_peak_information_rate_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_total_potential_capacity_get(uuid):  # noqa: E501
    """data_context_service_interface_pointuuid_total_potential_capacity_get

    returns tapi.common.Capacity # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str

    :rtype: TapiCommonCapacity
    """
    return 'do some magic!'


def data_context_service_interface_pointuuid_total_potential_capacity_total_size_get(uuid):  # noqa: E501
    """data_context_service_interface_pointuuid_total_potential_capacity_total_size_get

    returns tapi.common.CapacityValue # noqa: E501

    :param uuid: Id of service-interface-point
    :type uuid: str

    :rtype: TapiCommonCapacityValue
    """
    return 'do some magic!'


def operations_get_service_interface_point_details_post(inline_object24=None):  # noqa: E501
    """operations_get_service_interface_point_details_post

     # noqa: E501

    :param inline_object24: 
    :type inline_object24: dict | bytes

    :rtype: TapiCommonGetServiceInterfacePointDetails
    """
    if connexion.request.is_json:
        inline_object24 = InlineObject24.from_dict(connexion.request.get_json())  # noqa: E501
    
    return TapiCommonGetServiceInterfacePointDetails(TapiCommonGetserviceinterfacepointdetailsOutput(
        database.service_interface_point(inline_object24.input.sip_id_or_name)));


def operations_get_service_interface_point_list_post():  # noqa: E501
    """operations_get_service_interface_point_list_post

     # noqa: E501


    :rtype: TapiCommonGetServiceInterfacePointList
    """
    return TapiCommonGetServiceInterfacePointList(TapiCommonGetserviceinterfacepointlistOutput(
        database.service_interface_point_list()));


def operations_update_service_interface_point_post(inline_object32=None):  # noqa: E501
    """operations_update_service_interface_point_post

     # noqa: E501

    :param inline_object32: 
    :type inline_object32: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        inline_object32 = InlineObject32.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
