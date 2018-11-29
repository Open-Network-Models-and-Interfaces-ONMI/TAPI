# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

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
from tapi_server.test import BaseTestCase


class TestTapiOamController(BaseTestCase):
    """TapiOamController integration test stubs"""

    def test_data_context_oam_context_delete(self):
        """Test case for data_context_oam_context_delete

        
        """
        response = self.client.open(
            '/data/context/oam-context/',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_get(self):
        """Test case for data_context_oam_context_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_meguuid_get(self):
        """Test case for data_context_oam_context_meguuid_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/meg={uuid}/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_meguuid_meplocal_id_get(self):
        """Test case for data_context_oam_context_meguuid_meplocal_id_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/meg={uuid}/mep={local-id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_meguuid_meplocal_id_namevalue_name_get(self):
        """Test case for data_context_oam_context_meguuid_meplocal_id_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/meg={uuid}/mep={local-id}/name={value-name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_meguuid_miplocal_id_get(self):
        """Test case for data_context_oam_context_meguuid_miplocal_id_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/meg={uuid}/mip={local-id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_meguuid_miplocal_id_namevalue_name_get(self):
        """Test case for data_context_oam_context_meguuid_miplocal_id_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/meg={uuid}/mip={local-id}/name={value-name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_meguuid_namevalue_name_get(self):
        """Test case for data_context_oam_context_meguuid_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/meg={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_job_post(self):
        """Test case for data_context_oam_context_oam_job_post

        
        """
        tapi_oam_oam_job = TapiOamOamJob()
        response = self.client.open(
            '/data/context/oam-context/oam-job/',
            method='POST',
            data=json.dumps(tapi_oam_oam_job),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_jobuuid_delete(self):
        """Test case for data_context_oam_context_oam_jobuuid_delete

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-job={uuid}/'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_jobuuid_get(self):
        """Test case for data_context_oam_context_oam_jobuuid_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-job={uuid}/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_jobuuid_name_post(self):
        """Test case for data_context_oam_context_oam_jobuuid_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/oam-context/oam-job={uuid}/name/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_jobuuid_namevalue_name_delete(self):
        """Test case for data_context_oam_context_oam_jobuuid_namevalue_name_delete

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-job={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_jobuuid_namevalue_name_get(self):
        """Test case for data_context_oam_context_oam_jobuuid_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-job={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_jobuuid_namevalue_name_post(self):
        """Test case for data_context_oam_context_oam_jobuuid_namevalue_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/oam-context/oam-job={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_jobuuid_namevalue_name_put(self):
        """Test case for data_context_oam_context_oam_jobuuid_namevalue_name_put

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/oam-context/oam-job={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='PUT',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_jobuuid_oam_profile_delete(self):
        """Test case for data_context_oam_context_oam_jobuuid_oam_profile_delete

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-job={uuid}/oam-profile/'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_jobuuid_oam_profile_get(self):
        """Test case for data_context_oam_context_oam_jobuuid_oam_profile_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-job={uuid}/oam-profile/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_jobuuid_oam_profile_post(self):
        """Test case for data_context_oam_context_oam_jobuuid_oam_profile_post

        
        """
        tapi_oam_oam_profile_ref = TapiOamOamProfileRef()
        response = self.client.open(
            '/data/context/oam-context/oam-job={uuid}/oam-profile/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_oam_oam_profile_ref),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_jobuuid_oam_profile_put(self):
        """Test case for data_context_oam_context_oam_jobuuid_oam_profile_put

        
        """
        tapi_oam_oam_profile_ref = TapiOamOamProfileRef()
        response = self.client.open(
            '/data/context/oam-context/oam-job={uuid}/oam-profile/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(tapi_oam_oam_profile_ref),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_jobuuid_oam_service_end_point_post(self):
        """Test case for data_context_oam_context_oam_jobuuid_oam_service_end_point_post

        
        """
        tapi_oam_oam_service_end_point_ref = TapiOamOamServiceEndPointRef()
        response = self.client.open(
            '/data/context/oam-context/oam-job={uuid}/oam-service-end-point/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_oam_oam_service_end_point_ref),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_jobuuid_oam_service_end_pointoam_service_uuidoam_service_end_point_local_id_delete(self):
        """Test case for data_context_oam_context_oam_jobuuid_oam_service_end_pointoam_service_uuidoam_service_end_point_local_id_delete

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-job={uuid}/oam-service-end-point={oam-service-uuid},{oam-service-end-point-local-id}/'.format(uuid='uuid_example', oam_service_uuid='oam_service_uuid_example', oam_service_end_point_local_id='oam_service_end_point_local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_jobuuid_oam_service_end_pointoam_service_uuidoam_service_end_point_local_id_get(self):
        """Test case for data_context_oam_context_oam_jobuuid_oam_service_end_pointoam_service_uuidoam_service_end_point_local_id_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-job={uuid}/oam-service-end-point={oam-service-uuid},{oam-service-end-point-local-id}/'.format(uuid='uuid_example', oam_service_uuid='oam_service_uuid_example', oam_service_end_point_local_id='oam_service_end_point_local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_jobuuid_oam_service_end_pointoam_service_uuidoam_service_end_point_local_id_post(self):
        """Test case for data_context_oam_context_oam_jobuuid_oam_service_end_pointoam_service_uuidoam_service_end_point_local_id_post

        
        """
        tapi_oam_oam_service_end_point_ref = TapiOamOamServiceEndPointRef()
        response = self.client.open(
            '/data/context/oam-context/oam-job={uuid}/oam-service-end-point={oam-service-uuid},{oam-service-end-point-local-id}/'.format(uuid='uuid_example', oam_service_uuid='oam_service_uuid_example', oam_service_end_point_local_id='oam_service_end_point_local_id_example'),
            method='POST',
            data=json.dumps(tapi_oam_oam_service_end_point_ref),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_jobuuid_oam_service_end_pointoam_service_uuidoam_service_end_point_local_id_put(self):
        """Test case for data_context_oam_context_oam_jobuuid_oam_service_end_pointoam_service_uuidoam_service_end_point_local_id_put

        
        """
        tapi_oam_oam_service_end_point_ref = TapiOamOamServiceEndPointRef()
        response = self.client.open(
            '/data/context/oam-context/oam-job={uuid}/oam-service-end-point={oam-service-uuid},{oam-service-end-point-local-id}/'.format(uuid='uuid_example', oam_service_uuid='oam_service_uuid_example', oam_service_end_point_local_id='oam_service_end_point_local_id_example'),
            method='PUT',
            data=json.dumps(tapi_oam_oam_service_end_point_ref),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_elapsed_time_get(self):
        """Test case for data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_elapsed_time_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-job={uuid}/pm-current-data={local-id}/elapsed-time/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_elapsed_time_periodunit_get(self):
        """Test case for data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_elapsed_time_periodunit_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-job={uuid}/pm-current-data={local-id}/elapsed-time/period={unit}/'.format(uuid='uuid_example', local_id='local_id_example', unit='unit_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_get(self):
        """Test case for data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-job={uuid}/pm-current-data={local-id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_granularity_period_get(self):
        """Test case for data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_granularity_period_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-job={uuid}/pm-current-data={local-id}/granularity-period/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_namevalue_name_get(self):
        """Test case for data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-job={uuid}/pm-current-data={local-id}/name={value-name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_pm_history_datapm_history_data_local_id_get(self):
        """Test case for data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_pm_history_datapm_history_data_local_id_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-job={uuid}/pm-current-data={local-id}/pm-history-data={pm-history-data-local-id}/'.format(uuid='uuid_example', local_id='local_id_example', pm_history_data_local_id='pm_history_data_local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_pm_history_datapm_history_data_local_id_granularity_period_get(self):
        """Test case for data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_pm_history_datapm_history_data_local_id_granularity_period_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-job={uuid}/pm-current-data={local-id}/pm-history-data={pm-history-data-local-id}/granularity-period/'.format(uuid='uuid_example', local_id='local_id_example', pm_history_data_local_id='pm_history_data_local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_pm_history_datapm_history_data_local_id_namevalue_name_get(self):
        """Test case for data_context_oam_context_oam_jobuuid_pm_current_datalocal_id_pm_history_datapm_history_data_local_id_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-job={uuid}/pm-current-data={local-id}/pm-history-data={pm-history-data-local-id}/name={value-name}/'.format(uuid='uuid_example', local_id='local_id_example', pm_history_data_local_id='pm_history_data_local_id_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_jobuuid_post(self):
        """Test case for data_context_oam_context_oam_jobuuid_post

        
        """
        tapi_oam_oam_job = TapiOamOamJob()
        response = self.client.open(
            '/data/context/oam-context/oam-job={uuid}/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_oam_oam_job),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_jobuuid_put(self):
        """Test case for data_context_oam_context_oam_jobuuid_put

        
        """
        tapi_oam_oam_job = TapiOamOamJob()
        response = self.client.open(
            '/data/context/oam-context/oam-job={uuid}/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(tapi_oam_oam_job),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_jobuuid_schedule_delete(self):
        """Test case for data_context_oam_context_oam_jobuuid_schedule_delete

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-job={uuid}/schedule/'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_jobuuid_schedule_get(self):
        """Test case for data_context_oam_context_oam_jobuuid_schedule_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-job={uuid}/schedule/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_jobuuid_schedule_post(self):
        """Test case for data_context_oam_context_oam_jobuuid_schedule_post

        
        """
        tapi_common_time_range = TapiCommonTimeRange()
        response = self.client.open(
            '/data/context/oam-context/oam-job={uuid}/schedule/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_common_time_range),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_jobuuid_schedule_put(self):
        """Test case for data_context_oam_context_oam_jobuuid_schedule_put

        
        """
        tapi_common_time_range = TapiCommonTimeRange()
        response = self.client.open(
            '/data/context/oam-context/oam-job={uuid}/schedule/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(tapi_common_time_range),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profile_post(self):
        """Test case for data_context_oam_context_oam_profile_post

        
        """
        tapi_oam_oam_profile = TapiOamOamProfile()
        response = self.client.open(
            '/data/context/oam-context/oam-profile/',
            method='POST',
            data=json.dumps(tapi_oam_oam_profile),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_delete(self):
        """Test case for data_context_oam_context_oam_profileuuid_delete

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_get(self):
        """Test case for data_context_oam_context_oam_profileuuid_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_name_post(self):
        """Test case for data_context_oam_context_oam_profileuuid_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/name/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_namevalue_name_delete(self):
        """Test case for data_context_oam_context_oam_profileuuid_namevalue_name_delete

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_namevalue_name_get(self):
        """Test case for data_context_oam_context_oam_profileuuid_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_namevalue_name_post(self):
        """Test case for data_context_oam_context_oam_profileuuid_namevalue_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_namevalue_name_put(self):
        """Test case for data_context_oam_context_oam_profileuuid_namevalue_name_put

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='PUT',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_pm_bin_data_post(self):
        """Test case for data_context_oam_context_oam_profileuuid_pm_bin_data_post

        
        """
        tapi_oam_pm_bin_data = TapiOamPmBinData()
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/pm-bin-data/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_oam_pm_bin_data),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_delete(self):
        """Test case for data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_delete

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/pm-bin-data={local-id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_get(self):
        """Test case for data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/pm-bin-data={local-id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_granularity_period_delete(self):
        """Test case for data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_granularity_period_delete

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/pm-bin-data={local-id}/granularity-period/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_granularity_period_get(self):
        """Test case for data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_granularity_period_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/pm-bin-data={local-id}/granularity-period/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_granularity_period_post(self):
        """Test case for data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_granularity_period_post

        
        """
        tapi_common_time_period = TapiCommonTimePeriod()
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/pm-bin-data={local-id}/granularity-period/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_common_time_period),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_granularity_period_put(self):
        """Test case for data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_granularity_period_put

        
        """
        tapi_common_time_period = TapiCommonTimePeriod()
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/pm-bin-data={local-id}/granularity-period/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_common_time_period),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_name_post(self):
        """Test case for data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/pm-bin-data={local-id}/name/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_namevalue_name_delete(self):
        """Test case for data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_namevalue_name_delete

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/pm-bin-data={local-id}/name={value-name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_namevalue_name_get(self):
        """Test case for data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/pm-bin-data={local-id}/name={value-name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_namevalue_name_post(self):
        """Test case for data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_namevalue_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/pm-bin-data={local-id}/name={value-name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_namevalue_name_put(self):
        """Test case for data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_namevalue_name_put

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/pm-bin-data={local-id}/name={value-name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='PUT',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_post(self):
        """Test case for data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_post

        
        """
        tapi_oam_pm_bin_data = TapiOamPmBinData()
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/pm-bin-data={local-id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_oam_pm_bin_data),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_put(self):
        """Test case for data_context_oam_context_oam_profileuuid_pm_bin_datalocal_id_put

        
        """
        tapi_oam_pm_bin_data = TapiOamPmBinData()
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/pm-bin-data={local-id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_oam_pm_bin_data),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_pm_threshold_data_post(self):
        """Test case for data_context_oam_context_oam_profileuuid_pm_threshold_data_post

        
        """
        tapi_oam_pm_threshold_data = TapiOamPmThresholdData()
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/pm-threshold-data/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_oam_pm_threshold_data),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_delete(self):
        """Test case for data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_delete

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/pm-threshold-data={local-id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_get(self):
        """Test case for data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/pm-threshold-data={local-id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_granularity_period_delete(self):
        """Test case for data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_granularity_period_delete

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/pm-threshold-data={local-id}/granularity-period/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_granularity_period_get(self):
        """Test case for data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_granularity_period_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/pm-threshold-data={local-id}/granularity-period/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_granularity_period_post(self):
        """Test case for data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_granularity_period_post

        
        """
        tapi_common_time_period = TapiCommonTimePeriod()
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/pm-threshold-data={local-id}/granularity-period/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_common_time_period),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_granularity_period_put(self):
        """Test case for data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_granularity_period_put

        
        """
        tapi_common_time_period = TapiCommonTimePeriod()
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/pm-threshold-data={local-id}/granularity-period/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_common_time_period),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_name_post(self):
        """Test case for data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/pm-threshold-data={local-id}/name/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_namevalue_name_delete(self):
        """Test case for data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_namevalue_name_delete

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/pm-threshold-data={local-id}/name={value-name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_namevalue_name_get(self):
        """Test case for data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/pm-threshold-data={local-id}/name={value-name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_namevalue_name_post(self):
        """Test case for data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_namevalue_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/pm-threshold-data={local-id}/name={value-name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_namevalue_name_put(self):
        """Test case for data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_namevalue_name_put

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/pm-threshold-data={local-id}/name={value-name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='PUT',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_post(self):
        """Test case for data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_post

        
        """
        tapi_oam_pm_threshold_data = TapiOamPmThresholdData()
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/pm-threshold-data={local-id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_oam_pm_threshold_data),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_put(self):
        """Test case for data_context_oam_context_oam_profileuuid_pm_threshold_datalocal_id_put

        
        """
        tapi_oam_pm_threshold_data = TapiOamPmThresholdData()
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/pm-threshold-data={local-id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_oam_pm_threshold_data),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_post(self):
        """Test case for data_context_oam_context_oam_profileuuid_post

        
        """
        tapi_oam_oam_profile = TapiOamOamProfile()
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_oam_oam_profile),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_profileuuid_put(self):
        """Test case for data_context_oam_context_oam_profileuuid_put

        
        """
        tapi_oam_oam_profile = TapiOamOamProfile()
        response = self.client.open(
            '/data/context/oam-context/oam-profile={uuid}/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(tapi_oam_oam_profile),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_service_post(self):
        """Test case for data_context_oam_context_oam_service_post

        
        """
        tapi_oam_oam_service = TapiOamOamService()
        response = self.client.open(
            '/data/context/oam-context/oam-service/',
            method='POST',
            data=json.dumps(tapi_oam_oam_service),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_delete(self):
        """Test case for data_context_oam_context_oam_serviceuuid_delete

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_end_point_post(self):
        """Test case for data_context_oam_context_oam_serviceuuid_end_point_post

        
        """
        tapi_oam_oam_service_end_point = TapiOamOamServiceEndPoint()
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/end-point/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_oam_oam_service_end_point),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_end_pointlocal_id_connectivity_service_end_point_delete(self):
        """Test case for data_context_oam_context_oam_serviceuuid_end_pointlocal_id_connectivity_service_end_point_delete

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/end-point={local-id}/connectivity-service-end-point/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_end_pointlocal_id_connectivity_service_end_point_get(self):
        """Test case for data_context_oam_context_oam_serviceuuid_end_pointlocal_id_connectivity_service_end_point_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/end-point={local-id}/connectivity-service-end-point/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_end_pointlocal_id_connectivity_service_end_point_post(self):
        """Test case for data_context_oam_context_oam_serviceuuid_end_pointlocal_id_connectivity_service_end_point_post

        
        """
        tapi_connectivity_connectivity_service_end_point_ref = TapiConnectivityConnectivityServiceEndPointRef()
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/end-point={local-id}/connectivity-service-end-point/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_connectivity_connectivity_service_end_point_ref),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_end_pointlocal_id_connectivity_service_end_point_put(self):
        """Test case for data_context_oam_context_oam_serviceuuid_end_pointlocal_id_connectivity_service_end_point_put

        
        """
        tapi_connectivity_connectivity_service_end_point_ref = TapiConnectivityConnectivityServiceEndPointRef()
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/end-point={local-id}/connectivity-service-end-point/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_connectivity_connectivity_service_end_point_ref),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_end_pointlocal_id_delete(self):
        """Test case for data_context_oam_context_oam_serviceuuid_end_pointlocal_id_delete

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/end-point={local-id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_end_pointlocal_id_get(self):
        """Test case for data_context_oam_context_oam_serviceuuid_end_pointlocal_id_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/end-point={local-id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_end_pointlocal_id_mep_get(self):
        """Test case for data_context_oam_context_oam_serviceuuid_end_pointlocal_id_mep_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/end-point={local-id}/mep/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_end_pointlocal_id_mip_get(self):
        """Test case for data_context_oam_context_oam_serviceuuid_end_pointlocal_id_mip_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/end-point={local-id}/mip/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_end_pointlocal_id_name_post(self):
        """Test case for data_context_oam_context_oam_serviceuuid_end_pointlocal_id_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/end-point={local-id}/name/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_end_pointlocal_id_namevalue_name_delete(self):
        """Test case for data_context_oam_context_oam_serviceuuid_end_pointlocal_id_namevalue_name_delete

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/end-point={local-id}/name={value-name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_end_pointlocal_id_namevalue_name_get(self):
        """Test case for data_context_oam_context_oam_serviceuuid_end_pointlocal_id_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/end-point={local-id}/name={value-name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_end_pointlocal_id_namevalue_name_post(self):
        """Test case for data_context_oam_context_oam_serviceuuid_end_pointlocal_id_namevalue_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/end-point={local-id}/name={value-name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_end_pointlocal_id_namevalue_name_put(self):
        """Test case for data_context_oam_context_oam_serviceuuid_end_pointlocal_id_namevalue_name_put

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/end-point={local-id}/name={value-name}/'.format(uuid='uuid_example', local_id='local_id_example', value_name='value_name_example'),
            method='PUT',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_end_pointlocal_id_post(self):
        """Test case for data_context_oam_context_oam_serviceuuid_end_pointlocal_id_post

        
        """
        tapi_oam_oam_service_end_point = TapiOamOamServiceEndPoint()
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/end-point={local-id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_oam_oam_service_end_point),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_end_pointlocal_id_put(self):
        """Test case for data_context_oam_context_oam_serviceuuid_end_pointlocal_id_put

        
        """
        tapi_oam_oam_service_end_point = TapiOamOamServiceEndPoint()
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/end-point={local-id}/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_oam_oam_service_end_point),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_end_pointlocal_id_service_interface_point_delete(self):
        """Test case for data_context_oam_context_oam_serviceuuid_end_pointlocal_id_service_interface_point_delete

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/end-point={local-id}/service-interface-point/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_end_pointlocal_id_service_interface_point_get(self):
        """Test case for data_context_oam_context_oam_serviceuuid_end_pointlocal_id_service_interface_point_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/end-point={local-id}/service-interface-point/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_end_pointlocal_id_service_interface_point_post(self):
        """Test case for data_context_oam_context_oam_serviceuuid_end_pointlocal_id_service_interface_point_post

        
        """
        tapi_common_service_interface_point_ref = TapiCommonServiceInterfacePointRef()
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/end-point={local-id}/service-interface-point/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_common_service_interface_point_ref),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_end_pointlocal_id_service_interface_point_put(self):
        """Test case for data_context_oam_context_oam_serviceuuid_end_pointlocal_id_service_interface_point_put

        
        """
        tapi_common_service_interface_point_ref = TapiCommonServiceInterfacePointRef()
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/end-point={local-id}/service-interface-point/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_common_service_interface_point_ref),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_get(self):
        """Test case for data_context_oam_context_oam_serviceuuid_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_meg_get(self):
        """Test case for data_context_oam_context_oam_serviceuuid_meg_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/meg/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_name_post(self):
        """Test case for data_context_oam_context_oam_serviceuuid_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/name/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_namevalue_name_delete(self):
        """Test case for data_context_oam_context_oam_serviceuuid_namevalue_name_delete

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_namevalue_name_get(self):
        """Test case for data_context_oam_context_oam_serviceuuid_namevalue_name_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_namevalue_name_post(self):
        """Test case for data_context_oam_context_oam_serviceuuid_namevalue_name_post

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='POST',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_namevalue_name_put(self):
        """Test case for data_context_oam_context_oam_serviceuuid_namevalue_name_put

        
        """
        tapi_common_name_and_value = TapiCommonNameAndValue()
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/name={value-name}/'.format(uuid='uuid_example', value_name='value_name_example'),
            method='PUT',
            data=json.dumps(tapi_common_name_and_value),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_oam_profile_delete(self):
        """Test case for data_context_oam_context_oam_serviceuuid_oam_profile_delete

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/oam-profile/'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_oam_profile_get(self):
        """Test case for data_context_oam_context_oam_serviceuuid_oam_profile_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/oam-profile/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_oam_profile_post(self):
        """Test case for data_context_oam_context_oam_serviceuuid_oam_profile_post

        
        """
        tapi_oam_oam_profile_ref = TapiOamOamProfileRef()
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/oam-profile/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_oam_oam_profile_ref),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_oam_profile_put(self):
        """Test case for data_context_oam_context_oam_serviceuuid_oam_profile_put

        
        """
        tapi_oam_oam_profile_ref = TapiOamOamProfileRef()
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/oam-profile/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(tapi_oam_oam_profile_ref),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_post(self):
        """Test case for data_context_oam_context_oam_serviceuuid_post

        
        """
        tapi_oam_oam_service = TapiOamOamService()
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_oam_oam_service),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_oam_serviceuuid_put(self):
        """Test case for data_context_oam_context_oam_serviceuuid_put

        
        """
        tapi_oam_oam_service = TapiOamOamService()
        response = self.client.open(
            '/data/context/oam-context/oam-service={uuid}/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(tapi_oam_oam_service),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_post(self):
        """Test case for data_context_oam_context_post

        
        """
        tapi_oam_oam_context = TapiOamOamContext()
        response = self.client.open(
            '/data/context/oam-context/',
            method='POST',
            data=json.dumps(tapi_oam_oam_context),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_put(self):
        """Test case for data_context_oam_context_put

        
        """
        tapi_oam_oam_context = TapiOamOamContext()
        response = self.client.open(
            '/data/context/oam-context/',
            method='PUT',
            data=json.dumps(tapi_oam_oam_context),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_mep_mip_list_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_mep_mip_list_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/mep-mip-list/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_mep_mip_list_mepmeg_uuidmep_local_id_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_mep_mip_list_mepmeg_uuidmep_local_id_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/mep-mip-list/mep={meg-uuid},{mep-local-id}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example', meg_uuid='meg_uuid_example', mep_local_id='mep_local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_mep_mip_list_mipmeg_uuidmip_local_id_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_mep_mip_list_mipmeg_uuidmip_local_id_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/mep-mip-list/mip={meg-uuid},{mip-local-id}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example', meg_uuid='meg_uuid_example', mip_local_id='mip_local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_create_oam_job_post(self):
        """Test case for operations_create_oam_job_post

        
        """
        inline_object3 = InlineObject3()
        response = self.client.open(
            '/operations/create-oam-job/',
            method='POST',
            data=json.dumps(inline_object3),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_create_oam_service_end_point_post(self):
        """Test case for operations_create_oam_service_end_point_post

        
        """
        inline_object4 = InlineObject4()
        response = self.client.open(
            '/operations/create-oam-service-end-point/',
            method='POST',
            data=json.dumps(inline_object4),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_create_oam_service_post(self):
        """Test case for operations_create_oam_service_post

        
        """
        inline_object5 = InlineObject5()
        response = self.client.open(
            '/operations/create-oam-service/',
            method='POST',
            data=json.dumps(inline_object5),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_delete_oam_job_post(self):
        """Test case for operations_delete_oam_job_post

        
        """
        inline_object8 = InlineObject8()
        response = self.client.open(
            '/operations/delete-oam-job/',
            method='POST',
            data=json.dumps(inline_object8),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_delete_oam_service_end_point_post(self):
        """Test case for operations_delete_oam_service_end_point_post

        
        """
        inline_object9 = InlineObject9()
        response = self.client.open(
            '/operations/delete-oam-service-end-point/',
            method='POST',
            data=json.dumps(inline_object9),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_delete_oam_service_post(self):
        """Test case for operations_delete_oam_service_post

        
        """
        inline_object10 = InlineObject10()
        response = self.client.open(
            '/operations/delete-oam-service/',
            method='POST',
            data=json.dumps(inline_object10),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_get_meg_post(self):
        """Test case for operations_get_meg_post

        
        """
        inline_object16 = InlineObject16()
        response = self.client.open(
            '/operations/get-meg/',
            method='POST',
            data=json.dumps(inline_object16),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_get_oam_job_post(self):
        """Test case for operations_get_oam_job_post

        
        """
        inline_object21 = InlineObject21()
        response = self.client.open(
            '/operations/get-oam-job/',
            method='POST',
            data=json.dumps(inline_object21),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_get_oam_service_end_point_post(self):
        """Test case for operations_get_oam_service_end_point_post

        
        """
        inline_object22 = InlineObject22()
        response = self.client.open(
            '/operations/get-oam-service-end-point/',
            method='POST',
            data=json.dumps(inline_object22),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_get_oam_service_list_post(self):
        """Test case for operations_get_oam_service_list_post

        
        """
        response = self.client.open(
            '/operations/get-oam-service-list/',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_get_oam_service_post(self):
        """Test case for operations_get_oam_service_post

        
        """
        inline_object23 = InlineObject23()
        response = self.client.open(
            '/operations/get-oam-service/',
            method='POST',
            data=json.dumps(inline_object23),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_update_oam_job_post(self):
        """Test case for operations_update_oam_job_post

        
        """
        inline_object29 = InlineObject29()
        response = self.client.open(
            '/operations/update-oam-job/',
            method='POST',
            data=json.dumps(inline_object29),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_update_oam_service_end_point_post(self):
        """Test case for operations_update_oam_service_end_point_post

        
        """
        inline_object30 = InlineObject30()
        response = self.client.open(
            '/operations/update-oam-service-end-point/',
            method='POST',
            data=json.dumps(inline_object30),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operations_update_oam_service_post(self):
        """Test case for operations_update_oam_service_post

        
        """
        inline_object31 = InlineObject31()
        response = self.client.open(
            '/operations/update-oam-service/',
            method='POST',
            data=json.dumps(inline_object31),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
