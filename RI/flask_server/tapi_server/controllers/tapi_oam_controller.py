import connexion
import six

from tapi_server.models.inline_object10 import InlineObject10  # noqa: E501
from tapi_server.models.inline_object16 import InlineObject16  # noqa: E501
from tapi_server.models.inline_object21 import InlineObject21  # noqa: E501
from tapi_server.models.inline_object22 import InlineObject22  # noqa: E501
from tapi_server.models.inline_object23 import InlineObject23  # noqa: E501
from tapi_server.models.inline_object29 import InlineObject29  # noqa: E501
from tapi_server.models.inline_object3 import InlineObject3  # noqa: E501
from tapi_server.models.inline_object30 import InlineObject30  # noqa: E501
from tapi_server.models.inline_object31 import InlineObject31  # noqa: E501
from tapi_server.models.inline_object4 import InlineObject4  # noqa: E501
from tapi_server.models.inline_object5 import InlineObject5  # noqa: E501
from tapi_server.models.inline_object8 import InlineObject8  # noqa: E501
from tapi_server.models.inline_object9 import InlineObject9  # noqa: E501
from tapi_server.models.tapi_common_name_and_value import TapiCommonNameAndValue  # noqa: E501
from tapi_server.models.tapi_common_service_interface_point_ref import TapiCommonServiceInterfacePointRef  # noqa: E501
from tapi_server.models.tapi_common_time_interval import TapiCommonTimeInterval  # noqa: E501
from tapi_server.models.tapi_common_time_period import TapiCommonTimePeriod  # noqa: E501
from tapi_server.models.tapi_common_time_range import TapiCommonTimeRange  # noqa: E501
from tapi_server.models.tapi_connectivity_connectivity_service_end_point_ref import TapiConnectivityConnectivityServiceEndPointRef  # noqa: E501
from tapi_server.models.tapi_oam_create_oam_job import TapiOamCreateOamJob  # noqa: E501
from tapi_server.models.tapi_oam_create_oam_service import TapiOamCreateOamService  # noqa: E501
from tapi_server.models.tapi_oam_create_oam_service_end_point import TapiOamCreateOamServiceEndPoint  # noqa: E501
from tapi_server.models.tapi_oam_get_meg import TapiOamGetMeg  # noqa: E501
from tapi_server.models.tapi_oam_get_oam_job import TapiOamGetOamJob  # noqa: E501
from tapi_server.models.tapi_oam_get_oam_service import TapiOamGetOamService  # noqa: E501
from tapi_server.models.tapi_oam_get_oam_service_end_point import TapiOamGetOamServiceEndPoint  # noqa: E501
from tapi_server.models.tapi_oam_get_oam_service_list import TapiOamGetOamServiceList  # noqa: E501
from tapi_server.models.tapi_oam_meg_mep import TapiOamMegMep  # noqa: E501
from tapi_server.models.tapi_oam_meg_mip import TapiOamMegMip  # noqa: E501
from tapi_server.models.tapi_oam_meg_ref import TapiOamMegRef  # noqa: E501
from tapi_server.models.tapi_oam_mep_mip_list import TapiOamMepMipList  # noqa: E501
from tapi_server.models.tapi_oam_mep_ref import TapiOamMepRef  # noqa: E501
from tapi_server.models.tapi_oam_mip_ref import TapiOamMipRef  # noqa: E501
from tapi_server.models.tapi_oam_oam_context import TapiOamOamContext  # noqa: E501
from tapi_server.models.tapi_oam_oam_job import TapiOamOamJob  # noqa: E501
from tapi_server.models.tapi_oam_oam_profile import TapiOamOamProfile  # noqa: E501
from tapi_server.models.tapi_oam_oam_profile_ref import TapiOamOamProfileRef  # noqa: E501
from tapi_server.models.tapi_oam_oam_service import TapiOamOamService  # noqa: E501
from tapi_server.models.tapi_oam_oam_service_end_point import TapiOamOamServiceEndPoint  # noqa: E501
from tapi_server.models.tapi_oam_oam_service_end_point_ref import TapiOamOamServiceEndPointRef  # noqa: E501
from tapi_server.models.tapi_oam_oamcontext_meg import TapiOamOamcontextMeg  # noqa: E501
from tapi_server.models.tapi_oam_pm_bin_data import TapiOamPmBinData  # noqa: E501
from tapi_server.models.tapi_oam_pm_current_data import TapiOamPmCurrentData  # noqa: E501
from tapi_server.models.tapi_oam_pm_history_data import TapiOamPmHistoryData  # noqa: E501
from tapi_server.models.tapi_oam_pm_threshold_data import TapiOamPmThresholdData  # noqa: E501
from tapi_server.models.tapi_oam_update_oam_job import TapiOamUpdateOamJob  # noqa: E501
from tapi_server.models.tapi_oam_update_oam_service import TapiOamUpdateOamService  # noqa: E501
from tapi_server.models.tapi_oam_update_oam_service_end_point import TapiOamUpdateOamServiceEndPoint  # noqa: E501
from tapi_server import util


def data_context_oam_context_delete():  # noqa: E501
    """data_context_oam_context_delete

    removes tapi.oam.OamContext # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def data_context_oam_context_get():  # noqa: E501
    """data_context_oam_context_get

    returns tapi.oam.OamContext # noqa: E501


    :rtype: TapiOamOamContext
    """
    return 'do some magic!'


def data_context_oam_context_meguuid_get(uuid):  # noqa: E501
    """data_context_oam_context_meguuid_get

    returns tapi.oam.oamcontext.Meg # noqa: E501

    :param uuid: Id of meg
    :type uuid: str

    :rtype: TapiOamOamcontextMeg
    """
    return 'do some magic!'


def data_context_oam_context_meguuid_meplocal_id_get(uuid, local_id):  # noqa: E501
    """data_context_oam_context_meguuid_meplocal_id_get

    returns tapi.oam.meg.Mep # noqa: E501

    :param uuid: Id of meg
    :type uuid: str
    :param local_id: Id of mep
    :type local_id: str

    :rtype: TapiOamMegMep
    """
    return 'do some magic!'


def data_context_oam_context_meguuid_meplocal_id_namevalue_name_get(uuid, local_id, value_name):  # noqa: E501
    """data_context_oam_context_meguuid_meplocal_id_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of meg
    :type uuid: str
    :param local_id: Id of mep
    :type local_id: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_oam_context_meguuid_miplocal_id_get(uuid, local_id):  # noqa: E501
    """data_context_oam_context_meguuid_miplocal_id_get

    returns tapi.oam.meg.Mip # noqa: E501

    :param uuid: Id of meg
    :type uuid: str
    :param local_id: Id of mip
    :type local_id: str

    :rtype: TapiOamMegMip
    """
    return 'do some magic!'


def data_context_oam_context_meguuid_miplocal_id_namevalue_name_get(uuid, local_id, value_name):  # noqa: E501
    """data_context_oam_context_meguuid_miplocal_id_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of meg
    :type uuid: str
    :param local_id: Id of mip
    :type local_id: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_oam_context_meguuid_namevalue_name_get(uuid, value_name):  # noqa: E501
    """data_context_oam_context_meguuid_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of meg
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_oam_context_oam_job_post(tapi_oam_oam_job=None):  # noqa: E501
    """data_context_oam_context_oam_job_post

    creates tapi.oam.OamJob # noqa: E501

    :param tapi_oam_oam_job: tapi.oam.OamJob to be added to list
    :type tapi_oam_oam_job: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_oam_oam_job = TapiOamOamJob.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_jobuuid_delete(uuid):  # noqa: E501
    """data_context_oam_context_oam_jobuuid_delete

    removes tapi.oam.OamJob # noqa: E501

    :param uuid: Id of oam-job
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_oam_context_oam_jobuuid_get(uuid):  # noqa: E501
    """data_context_oam_context_oam_jobuuid_get

    returns tapi.oam.OamJob # noqa: E501

    :param uuid: Id of oam-job
    :type uuid: str

    :rtype: TapiOamOamJob
    """
    return 'do some magic!'


def data_context_oam_context_oam_jobuuid_name_post(uuid, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_oam_context_oam_jobuuid_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-job
    :type uuid: str
    :param tapi_common_name_and_value: tapi.common.NameAndValue to be added to list
    :type tapi_common_name_and_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_name_and_value = TapiCommonNameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_jobuuid_namevalue_name_delete(uuid, value_name):  # noqa: E501
    """data_context_oam_context_oam_jobuuid_namevalue_name_delete

    removes tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-job
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_oam_context_oam_jobuuid_namevalue_name_get(uuid, value_name):  # noqa: E501
    """data_context_oam_context_oam_jobuuid_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-job
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_oam_context_oam_jobuuid_namevalue_name_post(uuid, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_oam_context_oam_jobuuid_namevalue_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-job
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


def data_context_oam_context_oam_jobuuid_namevalue_name_put(uuid, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_oam_context_oam_jobuuid_namevalue_name_put

    creates or updates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-job
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


def data_context_oam_context_oam_jobuuid_oam_profile_delete(uuid):  # noqa: E501
    """data_context_oam_context_oam_jobuuid_oam_profile_delete

    removes tapi.oam.OamProfileRef # noqa: E501

    :param uuid: Id of oam-job
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_oam_context_oam_jobuuid_oam_profile_get(uuid):  # noqa: E501
    """data_context_oam_context_oam_jobuuid_oam_profile_get

    returns tapi.oam.OamProfileRef # noqa: E501

    :param uuid: Id of oam-job
    :type uuid: str

    :rtype: TapiOamOamProfileRef
    """
    return 'do some magic!'


def data_context_oam_context_oam_jobuuid_oam_profile_post(uuid, tapi_oam_oam_profile_ref=None):  # noqa: E501
    """data_context_oam_context_oam_jobuuid_oam_profile_post

    creates tapi.oam.OamProfileRef # noqa: E501

    :param uuid: Id of oam-job
    :type uuid: str
    :param tapi_oam_oam_profile_ref: tapi.oam.OamProfileRef to be added to list
    :type tapi_oam_oam_profile_ref: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_oam_oam_profile_ref = TapiOamOamProfileRef.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_jobuuid_oam_profile_put(uuid, tapi_oam_oam_profile_ref=None):  # noqa: E501
    """data_context_oam_context_oam_jobuuid_oam_profile_put

    creates or updates tapi.oam.OamProfileRef # noqa: E501

    :param uuid: Id of oam-job
    :type uuid: str
    :param tapi_oam_oam_profile_ref: tapi.oam.OamProfileRef to be added or updated
    :type tapi_oam_oam_profile_ref: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_oam_oam_profile_ref = TapiOamOamProfileRef.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_jobuuid_oam_service_end_point_post(uuid, tapi_oam_oam_service_end_point_ref=None):  # noqa: E501
    """data_context_oam_context_oam_jobuuid_oam_service_end_point_post

    creates tapi.oam.OamServiceEndPointRef # noqa: E501

    :param uuid: Id of oam-job
    :type uuid: str
    :param tapi_oam_oam_service_end_point_ref: tapi.oam.OamServiceEndPointRef to be added to list
    :type tapi_oam_oam_service_end_point_ref: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_oam_oam_service_end_point_ref = TapiOamOamServiceEndPointRef.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_jobuuid_oam_service_end_pointoam_service_uuidoam_service_end_point_local_id_delete(uuid, oam_service_uuid, oam_service_end_point_local_id):  # noqa: E501
    """data_context_oam_context_oam_jobuuid_oam_service_end_pointoam_service_uuidoam_service_end_point_local_id_delete

    removes tapi.oam.OamServiceEndPointRef # noqa: E501

    :param uuid: Id of oam-job
    :type uuid: str
    :param oam_service_uuid: Id of oam-service-end-point
    :type oam_service_uuid: str
    :param oam_service_end_point_local_id: Id of oam-service-end-point
    :type oam_service_end_point_local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_oam_context_oam_jobuuid_oam_service_end_pointoam_service_uuidoam_service_end_point_local_id_get(uuid, oam_service_uuid, oam_service_end_point_local_id):  # noqa: E501
    """data_context_oam_context_oam_jobuuid_oam_service_end_pointoam_service_uuidoam_service_end_point_local_id_get

    returns tapi.oam.OamServiceEndPointRef # noqa: E501

    :param uuid: Id of oam-job
    :type uuid: str
    :param oam_service_uuid: Id of oam-service-end-point
    :type oam_service_uuid: str
    :param oam_service_end_point_local_id: Id of oam-service-end-point
    :type oam_service_end_point_local_id: str

    :rtype: TapiOamOamServiceEndPointRef
    """
    return 'do some magic!'


def data_context_oam_context_oam_jobuuid_oam_service_end_pointoam_service_uuidoam_service_end_point_local_id_post(uuid, oam_service_uuid, oam_service_end_point_local_id, tapi_oam_oam_service_end_point_ref=None):  # noqa: E501
    """data_context_oam_context_oam_jobuuid_oam_service_end_pointoam_service_uuidoam_service_end_point_local_id_post

    creates tapi.oam.OamServiceEndPointRef # noqa: E501

    :param uuid: Id of oam-job
    :type uuid: str
    :param oam_service_uuid: Id of oam-service-end-point
    :type oam_service_uuid: str
    :param oam_service_end_point_local_id: Id of oam-service-end-point
    :type oam_service_end_point_local_id: str
    :param tapi_oam_oam_service_end_point_ref: tapi.oam.OamServiceEndPointRef to be added to list
    :type tapi_oam_oam_service_end_point_ref: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_oam_oam_service_end_point_ref = TapiOamOamServiceEndPointRef.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_jobuuid_oam_service_end_pointoam_service_uuidoam_service_end_point_local_id_put(uuid, oam_service_uuid, oam_service_end_point_local_id, tapi_oam_oam_service_end_point_ref=None):  # noqa: E501
    """data_context_oam_context_oam_jobuuid_oam_service_end_pointoam_service_uuidoam_service_end_point_local_id_put

    creates or updates tapi.oam.OamServiceEndPointRef # noqa: E501

    :param uuid: Id of oam-job
    :type uuid: str
    :param oam_service_uuid: Id of oam-service-end-point
    :type oam_service_uuid: str
    :param oam_service_end_point_local_id: Id of oam-service-end-point
    :type oam_service_end_point_local_id: str
    :param tapi_oam_oam_service_end_point_ref: tapi.oam.OamServiceEndPointRef to be added or updated
    :type tapi_oam_oam_service_end_point_ref: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_oam_oam_service_end_point_ref = TapiOamOamServiceEndPointRef.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_elapsed_time_get(uuid, local_id):  # noqa: E501
    """data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_elapsed_time_get

    returns tapi.common.TimeInterval # noqa: E501

    :param uuid: Id of oam-job
    :type uuid: str
    :param local_id: Id of pm-current-data
    :type local_id: str

    :rtype: TapiCommonTimeInterval
    """
    return 'do some magic!'


def data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_elapsed_time_periodunit_get(uuid, local_id, unit):  # noqa: E501
    """data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_elapsed_time_periodunit_get

    returns tapi.common.TimePeriod # noqa: E501

    :param uuid: Id of oam-job
    :type uuid: str
    :param local_id: Id of pm-current-data
    :type local_id: str
    :param unit: Id of period
    :type unit: str

    :rtype: TapiCommonTimePeriod
    """
    return 'do some magic!'


def data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_get(uuid, local_id):  # noqa: E501
    """data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_get

    returns tapi.oam.PmCurrentData # noqa: E501

    :param uuid: Id of oam-job
    :type uuid: str
    :param local_id: Id of pm-current-data
    :type local_id: str

    :rtype: TapiOamPmCurrentData
    """
    return 'do some magic!'


def data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_granularity_period_get(uuid, local_id):  # noqa: E501
    """data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_granularity_period_get

    returns tapi.common.TimePeriod # noqa: E501

    :param uuid: Id of oam-job
    :type uuid: str
    :param local_id: Id of pm-current-data
    :type local_id: str

    :rtype: TapiCommonTimePeriod
    """
    return 'do some magic!'


def data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_namevalue_name_get(uuid, local_id, value_name):  # noqa: E501
    """data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-job
    :type uuid: str
    :param local_id: Id of pm-current-data
    :type local_id: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_pm_history_datapm_history_data_local_id_get(uuid, local_id, pm_history_data_local_id):  # noqa: E501
    """data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_pm_history_datapm_history_data_local_id_get

    returns tapi.oam.PmHistoryData # noqa: E501

    :param uuid: Id of oam-job
    :type uuid: str
    :param local_id: Id of pm-current-data
    :type local_id: str
    :param pm_history_data_local_id: Id of pm-history-data
    :type pm_history_data_local_id: str

    :rtype: TapiOamPmHistoryData
    """
    return 'do some magic!'


def data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_pm_history_datapm_history_data_local_id_granularity_period_get(uuid, local_id, pm_history_data_local_id):  # noqa: E501
    """data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_pm_history_datapm_history_data_local_id_granularity_period_get

    returns tapi.common.TimePeriod # noqa: E501

    :param uuid: Id of oam-job
    :type uuid: str
    :param local_id: Id of pm-current-data
    :type local_id: str
    :param pm_history_data_local_id: Id of pm-history-data
    :type pm_history_data_local_id: str

    :rtype: TapiCommonTimePeriod
    """
    return 'do some magic!'


def data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_pm_history_datapm_history_data_local_id_namevalue_name_get(uuid, local_id, pm_history_data_local_id, value_name):  # noqa: E501
    """data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_pm_history_datapm_history_data_local_id_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-job
    :type uuid: str
    :param local_id: Id of pm-current-data
    :type local_id: str
    :param pm_history_data_local_id: Id of pm-history-data
    :type pm_history_data_local_id: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_oam_context_oam_jobuuid_post(uuid, tapi_oam_oam_job=None):  # noqa: E501
    """data_context_oam_context_oam_jobuuid_post

    creates tapi.oam.OamJob # noqa: E501

    :param uuid: Id of oam-job
    :type uuid: str
    :param tapi_oam_oam_job: tapi.oam.OamJob to be added to list
    :type tapi_oam_oam_job: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_oam_oam_job = TapiOamOamJob.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_jobuuid_put(uuid, tapi_oam_oam_job=None):  # noqa: E501
    """data_context_oam_context_oam_jobuuid_put

    creates or updates tapi.oam.OamJob # noqa: E501

    :param uuid: Id of oam-job
    :type uuid: str
    :param tapi_oam_oam_job: tapi.oam.OamJob to be added or updated
    :type tapi_oam_oam_job: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_oam_oam_job = TapiOamOamJob.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_jobuuid_schedule_delete(uuid):  # noqa: E501
    """data_context_oam_context_oam_jobuuid_schedule_delete

    removes tapi.common.TimeRange # noqa: E501

    :param uuid: Id of oam-job
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_oam_context_oam_jobuuid_schedule_get(uuid):  # noqa: E501
    """data_context_oam_context_oam_jobuuid_schedule_get

    returns tapi.common.TimeRange # noqa: E501

    :param uuid: Id of oam-job
    :type uuid: str

    :rtype: TapiCommonTimeRange
    """
    return 'do some magic!'


def data_context_oam_context_oam_jobuuid_schedule_post(uuid, tapi_common_time_range=None):  # noqa: E501
    """data_context_oam_context_oam_jobuuid_schedule_post

    creates tapi.common.TimeRange # noqa: E501

    :param uuid: Id of oam-job
    :type uuid: str
    :param tapi_common_time_range: tapi.common.TimeRange to be added to list
    :type tapi_common_time_range: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_time_range = TapiCommonTimeRange.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_jobuuid_schedule_put(uuid, tapi_common_time_range=None):  # noqa: E501
    """data_context_oam_context_oam_jobuuid_schedule_put

    creates or updates tapi.common.TimeRange # noqa: E501

    :param uuid: Id of oam-job
    :type uuid: str
    :param tapi_common_time_range: tapi.common.TimeRange to be added or updated
    :type tapi_common_time_range: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_time_range = TapiCommonTimeRange.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_profile_post(tapi_oam_oam_profile=None):  # noqa: E501
    """data_context_oam_context_oam_profile_post

    creates tapi.oam.OamProfile # noqa: E501

    :param tapi_oam_oam_profile: tapi.oam.OamProfile to be added to list
    :type tapi_oam_oam_profile: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_oam_oam_profile = TapiOamOamProfile.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_delete(uuid):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_delete

    removes tapi.oam.OamProfile # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_get(uuid):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_get

    returns tapi.oam.OamProfile # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str

    :rtype: TapiOamOamProfile
    """
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_name_post(uuid, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param tapi_common_name_and_value: tapi.common.NameAndValue to be added to list
    :type tapi_common_name_and_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_name_and_value = TapiCommonNameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_namevalue_name_delete(uuid, value_name):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_namevalue_name_delete

    removes tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_namevalue_name_get(uuid, value_name):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_namevalue_name_post(uuid, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_namevalue_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-profile
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


def data_context_oam_context_oam_profileuuid_namevalue_name_put(uuid, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_namevalue_name_put

    creates or updates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-profile
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


def data_context_oam_context_oam_profileuuid_pm_bin_data_post(uuid, tapi_oam_pm_bin_data=None):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_pm_bin_data_post

    creates tapi.oam.PmBinData # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param tapi_oam_pm_bin_data: tapi.oam.PmBinData to be added to list
    :type tapi_oam_pm_bin_data: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_oam_pm_bin_data = TapiOamPmBinData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_delete(uuid, local_id):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_delete

    removes tapi.oam.PmBinData # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param local_id: Id of pm-bin-data
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_get(uuid, local_id):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_get

    returns tapi.oam.PmBinData # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param local_id: Id of pm-bin-data
    :type local_id: str

    :rtype: TapiOamPmBinData
    """
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_granularity_period_delete(uuid, local_id):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_granularity_period_delete

    removes tapi.common.TimePeriod # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param local_id: Id of pm-bin-data
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_granularity_period_get(uuid, local_id):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_granularity_period_get

    returns tapi.common.TimePeriod # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param local_id: Id of pm-bin-data
    :type local_id: str

    :rtype: TapiCommonTimePeriod
    """
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_granularity_period_post(uuid, local_id, tapi_common_time_period=None):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_granularity_period_post

    creates tapi.common.TimePeriod # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param local_id: Id of pm-bin-data
    :type local_id: str
    :param tapi_common_time_period: tapi.common.TimePeriod to be added to list
    :type tapi_common_time_period: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_time_period = TapiCommonTimePeriod.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_granularity_period_put(uuid, local_id, tapi_common_time_period=None):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_granularity_period_put

    creates or updates tapi.common.TimePeriod # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param local_id: Id of pm-bin-data
    :type local_id: str
    :param tapi_common_time_period: tapi.common.TimePeriod to be added or updated
    :type tapi_common_time_period: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_time_period = TapiCommonTimePeriod.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_name_post(uuid, local_id, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param local_id: Id of pm-bin-data
    :type local_id: str
    :param tapi_common_name_and_value: tapi.common.NameAndValue to be added to list
    :type tapi_common_name_and_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_name_and_value = TapiCommonNameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_namevalue_name_delete(uuid, local_id, value_name):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_namevalue_name_delete

    removes tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param local_id: Id of pm-bin-data
    :type local_id: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_namevalue_name_get(uuid, local_id, value_name):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param local_id: Id of pm-bin-data
    :type local_id: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_namevalue_name_post(uuid, local_id, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_namevalue_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param local_id: Id of pm-bin-data
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


def data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_namevalue_name_put(uuid, local_id, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_namevalue_name_put

    creates or updates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param local_id: Id of pm-bin-data
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


def data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_post(uuid, local_id, tapi_oam_pm_bin_data=None):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_post

    creates tapi.oam.PmBinData # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param local_id: Id of pm-bin-data
    :type local_id: str
    :param tapi_oam_pm_bin_data: tapi.oam.PmBinData to be added to list
    :type tapi_oam_pm_bin_data: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_oam_pm_bin_data = TapiOamPmBinData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_put(uuid, local_id, tapi_oam_pm_bin_data=None):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_put

    creates or updates tapi.oam.PmBinData # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param local_id: Id of pm-bin-data
    :type local_id: str
    :param tapi_oam_pm_bin_data: tapi.oam.PmBinData to be added or updated
    :type tapi_oam_pm_bin_data: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_oam_pm_bin_data = TapiOamPmBinData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_pm_threshold_data_post(uuid, tapi_oam_pm_threshold_data=None):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_pm_threshold_data_post

    creates tapi.oam.PmThresholdData # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param tapi_oam_pm_threshold_data: tapi.oam.PmThresholdData to be added to list
    :type tapi_oam_pm_threshold_data: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_oam_pm_threshold_data = TapiOamPmThresholdData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_delete(uuid, local_id):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_delete

    removes tapi.oam.PmThresholdData # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param local_id: Id of pm-threshold-data
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_get(uuid, local_id):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_get

    returns tapi.oam.PmThresholdData # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param local_id: Id of pm-threshold-data
    :type local_id: str

    :rtype: TapiOamPmThresholdData
    """
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_granularity_period_delete(uuid, local_id):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_granularity_period_delete

    removes tapi.common.TimePeriod # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param local_id: Id of pm-threshold-data
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_granularity_period_get(uuid, local_id):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_granularity_period_get

    returns tapi.common.TimePeriod # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param local_id: Id of pm-threshold-data
    :type local_id: str

    :rtype: TapiCommonTimePeriod
    """
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_granularity_period_post(uuid, local_id, tapi_common_time_period=None):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_granularity_period_post

    creates tapi.common.TimePeriod # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param local_id: Id of pm-threshold-data
    :type local_id: str
    :param tapi_common_time_period: tapi.common.TimePeriod to be added to list
    :type tapi_common_time_period: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_time_period = TapiCommonTimePeriod.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_granularity_period_put(uuid, local_id, tapi_common_time_period=None):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_granularity_period_put

    creates or updates tapi.common.TimePeriod # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param local_id: Id of pm-threshold-data
    :type local_id: str
    :param tapi_common_time_period: tapi.common.TimePeriod to be added or updated
    :type tapi_common_time_period: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_time_period = TapiCommonTimePeriod.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_name_post(uuid, local_id, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param local_id: Id of pm-threshold-data
    :type local_id: str
    :param tapi_common_name_and_value: tapi.common.NameAndValue to be added to list
    :type tapi_common_name_and_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_name_and_value = TapiCommonNameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_namevalue_name_delete(uuid, local_id, value_name):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_namevalue_name_delete

    removes tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param local_id: Id of pm-threshold-data
    :type local_id: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_namevalue_name_get(uuid, local_id, value_name):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param local_id: Id of pm-threshold-data
    :type local_id: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_namevalue_name_post(uuid, local_id, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_namevalue_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param local_id: Id of pm-threshold-data
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


def data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_namevalue_name_put(uuid, local_id, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_namevalue_name_put

    creates or updates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param local_id: Id of pm-threshold-data
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


def data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_post(uuid, local_id, tapi_oam_pm_threshold_data=None):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_post

    creates tapi.oam.PmThresholdData # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param local_id: Id of pm-threshold-data
    :type local_id: str
    :param tapi_oam_pm_threshold_data: tapi.oam.PmThresholdData to be added to list
    :type tapi_oam_pm_threshold_data: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_oam_pm_threshold_data = TapiOamPmThresholdData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_put(uuid, local_id, tapi_oam_pm_threshold_data=None):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_put

    creates or updates tapi.oam.PmThresholdData # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param local_id: Id of pm-threshold-data
    :type local_id: str
    :param tapi_oam_pm_threshold_data: tapi.oam.PmThresholdData to be added or updated
    :type tapi_oam_pm_threshold_data: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_oam_pm_threshold_data = TapiOamPmThresholdData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_post(uuid, tapi_oam_oam_profile=None):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_post

    creates tapi.oam.OamProfile # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param tapi_oam_oam_profile: tapi.oam.OamProfile to be added to list
    :type tapi_oam_oam_profile: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_oam_oam_profile = TapiOamOamProfile.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_profileuuid_put(uuid, tapi_oam_oam_profile=None):  # noqa: E501
    """data_context_oam_context_oam_profileuuid_put

    creates or updates tapi.oam.OamProfile # noqa: E501

    :param uuid: Id of oam-profile
    :type uuid: str
    :param tapi_oam_oam_profile: tapi.oam.OamProfile to be added or updated
    :type tapi_oam_oam_profile: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_oam_oam_profile = TapiOamOamProfile.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_service_post(tapi_oam_oam_service=None):  # noqa: E501
    """data_context_oam_context_oam_service_post

    creates tapi.oam.OamService # noqa: E501

    :param tapi_oam_oam_service: tapi.oam.OamService to be added to list
    :type tapi_oam_oam_service: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_oam_oam_service = TapiOamOamService.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_serviceuuid_delete(uuid):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_delete

    removes tapi.oam.OamService # noqa: E501

    :param uuid: Id of oam-service
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_oam_context_oam_serviceuuid_end_point_post(uuid, tapi_oam_oam_service_end_point=None):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_end_point_post

    creates tapi.oam.OamServiceEndPoint # noqa: E501

    :param uuid: Id of oam-service
    :type uuid: str
    :param tapi_oam_oam_service_end_point: tapi.oam.OamServiceEndPoint to be added to list
    :type tapi_oam_oam_service_end_point: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_oam_oam_service_end_point = TapiOamOamServiceEndPoint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_serviceuuid_end_pointlocal_id_connectivity_service_end_point_delete(uuid, local_id):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_end_pointlocal_id_connectivity_service_end_point_delete

    removes tapi.connectivity.ConnectivityServiceEndPointRef # noqa: E501

    :param uuid: Id of oam-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_oam_context_oam_serviceuuid_end_pointlocal_id_connectivity_service_end_point_get(uuid, local_id):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_end_pointlocal_id_connectivity_service_end_point_get

    returns tapi.connectivity.ConnectivityServiceEndPointRef # noqa: E501

    :param uuid: Id of oam-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiConnectivityConnectivityServiceEndPointRef
    """
    return 'do some magic!'


def data_context_oam_context_oam_serviceuuid_end_pointlocal_id_connectivity_service_end_point_post(uuid, local_id, tapi_connectivity_connectivity_service_end_point_ref=None):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_end_pointlocal_id_connectivity_service_end_point_post

    creates tapi.connectivity.ConnectivityServiceEndPointRef # noqa: E501

    :param uuid: Id of oam-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_connectivity_connectivity_service_end_point_ref: tapi.connectivity.ConnectivityServiceEndPointRef to be added to list
    :type tapi_connectivity_connectivity_service_end_point_ref: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_connectivity_connectivity_service_end_point_ref = TapiConnectivityConnectivityServiceEndPointRef.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_serviceuuid_end_pointlocal_id_connectivity_service_end_point_put(uuid, local_id, tapi_connectivity_connectivity_service_end_point_ref=None):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_end_pointlocal_id_connectivity_service_end_point_put

    creates or updates tapi.connectivity.ConnectivityServiceEndPointRef # noqa: E501

    :param uuid: Id of oam-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_connectivity_connectivity_service_end_point_ref: tapi.connectivity.ConnectivityServiceEndPointRef to be added or updated
    :type tapi_connectivity_connectivity_service_end_point_ref: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_connectivity_connectivity_service_end_point_ref = TapiConnectivityConnectivityServiceEndPointRef.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_serviceuuid_end_pointlocal_id_delete(uuid, local_id):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_end_pointlocal_id_delete

    removes tapi.oam.OamServiceEndPoint # noqa: E501

    :param uuid: Id of oam-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_oam_context_oam_serviceuuid_end_pointlocal_id_get(uuid, local_id):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_end_pointlocal_id_get

    returns tapi.oam.OamServiceEndPoint # noqa: E501

    :param uuid: Id of oam-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiOamOamServiceEndPoint
    """
    return 'do some magic!'


def data_context_oam_context_oam_serviceuuid_end_pointlocal_id_mep_get(uuid, local_id):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_end_pointlocal_id_mep_get

    returns tapi.oam.MepRef # noqa: E501

    :param uuid: Id of oam-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiOamMepRef
    """
    return 'do some magic!'


def data_context_oam_context_oam_serviceuuid_end_pointlocal_id_mip_get(uuid, local_id):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_end_pointlocal_id_mip_get

    returns tapi.oam.MipRef # noqa: E501

    :param uuid: Id of oam-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiOamMipRef
    """
    return 'do some magic!'


def data_context_oam_context_oam_serviceuuid_end_pointlocal_id_name_post(uuid, local_id, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_end_pointlocal_id_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-service
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


def data_context_oam_context_oam_serviceuuid_end_pointlocal_id_namevalue_name_delete(uuid, local_id, value_name):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_end_pointlocal_id_namevalue_name_delete

    removes tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_oam_context_oam_serviceuuid_end_pointlocal_id_namevalue_name_get(uuid, local_id, value_name):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_end_pointlocal_id_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_oam_context_oam_serviceuuid_end_pointlocal_id_namevalue_name_post(uuid, local_id, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_end_pointlocal_id_namevalue_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-service
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


def data_context_oam_context_oam_serviceuuid_end_pointlocal_id_namevalue_name_put(uuid, local_id, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_end_pointlocal_id_namevalue_name_put

    creates or updates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-service
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


def data_context_oam_context_oam_serviceuuid_end_pointlocal_id_post(uuid, local_id, tapi_oam_oam_service_end_point=None):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_end_pointlocal_id_post

    creates tapi.oam.OamServiceEndPoint # noqa: E501

    :param uuid: Id of oam-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_oam_oam_service_end_point: tapi.oam.OamServiceEndPoint to be added to list
    :type tapi_oam_oam_service_end_point: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_oam_oam_service_end_point = TapiOamOamServiceEndPoint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_serviceuuid_end_pointlocal_id_put(uuid, local_id, tapi_oam_oam_service_end_point=None):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_end_pointlocal_id_put

    creates or updates tapi.oam.OamServiceEndPoint # noqa: E501

    :param uuid: Id of oam-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str
    :param tapi_oam_oam_service_end_point: tapi.oam.OamServiceEndPoint to be added or updated
    :type tapi_oam_oam_service_end_point: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_oam_oam_service_end_point = TapiOamOamServiceEndPoint.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_serviceuuid_end_pointlocal_id_service_interface_point_delete(uuid, local_id):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_end_pointlocal_id_service_interface_point_delete

    removes tapi.common.ServiceInterfacePointRef # noqa: E501

    :param uuid: Id of oam-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_oam_context_oam_serviceuuid_end_pointlocal_id_service_interface_point_get(uuid, local_id):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_end_pointlocal_id_service_interface_point_get

    returns tapi.common.ServiceInterfacePointRef # noqa: E501

    :param uuid: Id of oam-service
    :type uuid: str
    :param local_id: Id of end-point
    :type local_id: str

    :rtype: TapiCommonServiceInterfacePointRef
    """
    return 'do some magic!'


def data_context_oam_context_oam_serviceuuid_end_pointlocal_id_service_interface_point_post(uuid, local_id, tapi_common_service_interface_point_ref=None):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_end_pointlocal_id_service_interface_point_post

    creates tapi.common.ServiceInterfacePointRef # noqa: E501

    :param uuid: Id of oam-service
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


def data_context_oam_context_oam_serviceuuid_end_pointlocal_id_service_interface_point_put(uuid, local_id, tapi_common_service_interface_point_ref=None):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_end_pointlocal_id_service_interface_point_put

    creates or updates tapi.common.ServiceInterfacePointRef # noqa: E501

    :param uuid: Id of oam-service
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


def data_context_oam_context_oam_serviceuuid_get(uuid):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_get

    returns tapi.oam.OamService # noqa: E501

    :param uuid: Id of oam-service
    :type uuid: str

    :rtype: TapiOamOamService
    """
    return 'do some magic!'


def data_context_oam_context_oam_serviceuuid_meg_get(uuid):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_meg_get

    returns tapi.oam.MegRef # noqa: E501

    :param uuid: Id of oam-service
    :type uuid: str

    :rtype: TapiOamMegRef
    """
    return 'do some magic!'


def data_context_oam_context_oam_serviceuuid_name_post(uuid, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-service
    :type uuid: str
    :param tapi_common_name_and_value: tapi.common.NameAndValue to be added to list
    :type tapi_common_name_and_value: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_common_name_and_value = TapiCommonNameAndValue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_serviceuuid_namevalue_name_delete(uuid, value_name):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_namevalue_name_delete

    removes tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-service
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_oam_context_oam_serviceuuid_namevalue_name_get(uuid, value_name):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_namevalue_name_get

    returns tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-service
    :type uuid: str
    :param value_name: Id of name
    :type value_name: str

    :rtype: TapiCommonNameAndValue
    """
    return 'do some magic!'


def data_context_oam_context_oam_serviceuuid_namevalue_name_post(uuid, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_namevalue_name_post

    creates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-service
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


def data_context_oam_context_oam_serviceuuid_namevalue_name_put(uuid, value_name, tapi_common_name_and_value=None):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_namevalue_name_put

    creates or updates tapi.common.NameAndValue # noqa: E501

    :param uuid: Id of oam-service
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


def data_context_oam_context_oam_serviceuuid_oam_profile_delete(uuid):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_oam_profile_delete

    removes tapi.oam.OamProfileRef # noqa: E501

    :param uuid: Id of oam-service
    :type uuid: str

    :rtype: None
    """
    return 'do some magic!'


def data_context_oam_context_oam_serviceuuid_oam_profile_get(uuid):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_oam_profile_get

    returns tapi.oam.OamProfileRef # noqa: E501

    :param uuid: Id of oam-service
    :type uuid: str

    :rtype: TapiOamOamProfileRef
    """
    return 'do some magic!'


def data_context_oam_context_oam_serviceuuid_oam_profile_post(uuid, tapi_oam_oam_profile_ref=None):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_oam_profile_post

    creates tapi.oam.OamProfileRef # noqa: E501

    :param uuid: Id of oam-service
    :type uuid: str
    :param tapi_oam_oam_profile_ref: tapi.oam.OamProfileRef to be added to list
    :type tapi_oam_oam_profile_ref: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_oam_oam_profile_ref = TapiOamOamProfileRef.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_serviceuuid_oam_profile_put(uuid, tapi_oam_oam_profile_ref=None):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_oam_profile_put

    creates or updates tapi.oam.OamProfileRef # noqa: E501

    :param uuid: Id of oam-service
    :type uuid: str
    :param tapi_oam_oam_profile_ref: tapi.oam.OamProfileRef to be added or updated
    :type tapi_oam_oam_profile_ref: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_oam_oam_profile_ref = TapiOamOamProfileRef.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_serviceuuid_post(uuid, tapi_oam_oam_service=None):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_post

    creates tapi.oam.OamService # noqa: E501

    :param uuid: Id of oam-service
    :type uuid: str
    :param tapi_oam_oam_service: tapi.oam.OamService to be added to list
    :type tapi_oam_oam_service: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_oam_oam_service = TapiOamOamService.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_oam_serviceuuid_put(uuid, tapi_oam_oam_service=None):  # noqa: E501
    """data_context_oam_context_oam_serviceuuid_put

    creates or updates tapi.oam.OamService # noqa: E501

    :param uuid: Id of oam-service
    :type uuid: str
    :param tapi_oam_oam_service: tapi.oam.OamService to be added or updated
    :type tapi_oam_oam_service: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_oam_oam_service = TapiOamOamService.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_post(tapi_oam_oam_context=None):  # noqa: E501
    """data_context_oam_context_post

    creates tapi.oam.OamContext # noqa: E501

    :param tapi_oam_oam_context: tapi.oam.OamContext to be added to list
    :type tapi_oam_oam_context: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_oam_oam_context = TapiOamOamContext.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_oam_context_put(tapi_oam_oam_context=None):  # noqa: E501
    """data_context_oam_context_put

    creates or updates tapi.oam.OamContext # noqa: E501

    :param tapi_oam_oam_context: tapi.oam.OamContext to be added or updated
    :type tapi_oam_oam_context: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tapi_oam_oam_context = TapiOamOamContext.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_mep_mip_list_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_mep_mip_list_get

    returns tapi.oam.MepMipList # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str

    :rtype: TapiOamMepMipList
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_mep_mip_list_mepmeg_uuidmep_local_id_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid, meg_uuid, mep_local_id):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_mep_mip_list_mepmeg_uuidmep_local_id_get

    returns tapi.oam.MepRef # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str
    :param meg_uuid: Id of mep
    :type meg_uuid: str
    :param mep_local_id: Id of mep
    :type mep_local_id: str

    :rtype: TapiOamMepRef
    """
    return 'do some magic!'


def data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_mep_mip_list_mipmeg_uuidmip_local_id_get(uuid, node_uuid, owned_node_edge_point_uuid, connection_end_point_uuid, meg_uuid, mip_local_id):  # noqa: E501
    """data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_mep_mip_list_mipmeg_uuidmip_local_id_get

    returns tapi.oam.MipRef # noqa: E501

    :param uuid: Id of topology
    :type uuid: str
    :param node_uuid: Id of node
    :type node_uuid: str
    :param owned_node_edge_point_uuid: Id of owned-node-edge-point
    :type owned_node_edge_point_uuid: str
    :param connection_end_point_uuid: Id of connection-end-point
    :type connection_end_point_uuid: str
    :param meg_uuid: Id of mip
    :type meg_uuid: str
    :param mip_local_id: Id of mip
    :type mip_local_id: str

    :rtype: TapiOamMipRef
    """
    return 'do some magic!'


def operations_create_oam_job_post(inline_object3=None):  # noqa: E501
    """operations_create_oam_job_post

     # noqa: E501

    :param inline_object3: 
    :type inline_object3: dict | bytes

    :rtype: TapiOamCreateOamJob
    """
    if connexion.request.is_json:
        inline_object3 = InlineObject3.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def operations_create_oam_service_end_point_post(inline_object4=None):  # noqa: E501
    """operations_create_oam_service_end_point_post

     # noqa: E501

    :param inline_object4: 
    :type inline_object4: dict | bytes

    :rtype: TapiOamCreateOamServiceEndPoint
    """
    if connexion.request.is_json:
        inline_object4 = InlineObject4.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def operations_create_oam_service_post(inline_object5=None):  # noqa: E501
    """operations_create_oam_service_post

     # noqa: E501

    :param inline_object5: 
    :type inline_object5: dict | bytes

    :rtype: TapiOamCreateOamService
    """
    if connexion.request.is_json:
        inline_object5 = InlineObject5.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def operations_delete_oam_job_post(inline_object8=None):  # noqa: E501
    """operations_delete_oam_job_post

     # noqa: E501

    :param inline_object8: 
    :type inline_object8: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        inline_object8 = InlineObject8.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def operations_delete_oam_service_end_point_post(inline_object9=None):  # noqa: E501
    """operations_delete_oam_service_end_point_post

     # noqa: E501

    :param inline_object9: 
    :type inline_object9: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        inline_object9 = InlineObject9.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def operations_delete_oam_service_post(inline_object10=None):  # noqa: E501
    """operations_delete_oam_service_post

     # noqa: E501

    :param inline_object10: 
    :type inline_object10: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        inline_object10 = InlineObject10.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def operations_get_meg_post(inline_object16=None):  # noqa: E501
    """operations_get_meg_post

     # noqa: E501

    :param inline_object16: 
    :type inline_object16: dict | bytes

    :rtype: TapiOamGetMeg
    """
    if connexion.request.is_json:
        inline_object16 = InlineObject16.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def operations_get_oam_job_post(inline_object21=None):  # noqa: E501
    """operations_get_oam_job_post

     # noqa: E501

    :param inline_object21: 
    :type inline_object21: dict | bytes

    :rtype: TapiOamGetOamJob
    """
    if connexion.request.is_json:
        inline_object21 = InlineObject21.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def operations_get_oam_service_end_point_post(inline_object22=None):  # noqa: E501
    """operations_get_oam_service_end_point_post

     # noqa: E501

    :param inline_object22: 
    :type inline_object22: dict | bytes

    :rtype: TapiOamGetOamServiceEndPoint
    """
    if connexion.request.is_json:
        inline_object22 = InlineObject22.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def operations_get_oam_service_list_post():  # noqa: E501
    """operations_get_oam_service_list_post

     # noqa: E501


    :rtype: TapiOamGetOamServiceList
    """
    return 'do some magic!'


def operations_get_oam_service_post(inline_object23=None):  # noqa: E501
    """operations_get_oam_service_post

     # noqa: E501

    :param inline_object23: 
    :type inline_object23: dict | bytes

    :rtype: TapiOamGetOamService
    """
    if connexion.request.is_json:
        inline_object23 = InlineObject23.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def operations_update_oam_job_post(inline_object29=None):  # noqa: E501
    """operations_update_oam_job_post

     # noqa: E501

    :param inline_object29: 
    :type inline_object29: dict | bytes

    :rtype: TapiOamUpdateOamJob
    """
    if connexion.request.is_json:
        inline_object29 = InlineObject29.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def operations_update_oam_service_end_point_post(inline_object30=None):  # noqa: E501
    """operations_update_oam_service_end_point_post

     # noqa: E501

    :param inline_object30: 
    :type inline_object30: dict | bytes

    :rtype: TapiOamUpdateOamServiceEndPoint
    """
    if connexion.request.is_json:
        inline_object30 = InlineObject30.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def operations_update_oam_service_post(inline_object31=None):  # noqa: E501
    """operations_update_oam_service_post

     # noqa: E501

    :param inline_object31: 
    :type inline_object31: dict | bytes

    :rtype: TapiOamUpdateOamService
    """
    if connexion.request.is_json:
        inline_object31 = InlineObject31.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
