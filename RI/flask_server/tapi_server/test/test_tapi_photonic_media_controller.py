# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

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
from tapi_server.test import BaseTestCase


class TestTapiPhotonicMediaController(BaseTestCase):
    """TapiPhotonicMediaController integration test stubs"""

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/media-channel-service-interface-point-spec/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/media-channel-service-interface-point-spec/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_mc_pool_available_spectrumupper_frequencylower_frequency_frequency_constraint_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_mc_pool_available_spectrumupper_frequencylower_frequency_frequency_constraint_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/media-channel-service-interface-point-spec/mc-pool/available-spectrum={upper-frequency},{lower-frequency}/frequency-constraint/'.format(uuid='uuid_example', local_id='local_id_example', upper_frequency=56, lower_frequency=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_mc_pool_available_spectrumupper_frequencylower_frequency_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_mc_pool_available_spectrumupper_frequencylower_frequency_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/media-channel-service-interface-point-spec/mc-pool/available-spectrum={upper-frequency},{lower-frequency}/'.format(uuid='uuid_example', local_id='local_id_example', upper_frequency=56, lower_frequency=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_mc_pool_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_mc_pool_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/media-channel-service-interface-point-spec/mc-pool/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_mc_pool_occupied_spectrumupper_frequencylower_frequency_frequency_constraint_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_mc_pool_occupied_spectrumupper_frequencylower_frequency_frequency_constraint_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/media-channel-service-interface-point-spec/mc-pool/occupied-spectrum={upper-frequency},{lower-frequency}/frequency-constraint/'.format(uuid='uuid_example', local_id='local_id_example', upper_frequency=56, lower_frequency=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_mc_pool_occupied_spectrumupper_frequencylower_frequency_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_mc_pool_occupied_spectrumupper_frequencylower_frequency_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/media-channel-service-interface-point-spec/mc-pool/occupied-spectrum={upper-frequency},{lower-frequency}/'.format(uuid='uuid_example', local_id='local_id_example', upper_frequency=56, lower_frequency=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_mc_pool_supportable_spectrumupper_frequencylower_frequency_frequency_constraint_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_mc_pool_supportable_spectrumupper_frequencylower_frequency_frequency_constraint_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/media-channel-service-interface-point-spec/mc-pool/supportable-spectrum={upper-frequency},{lower-frequency}/frequency-constraint/'.format(uuid='uuid_example', local_id='local_id_example', upper_frequency=56, lower_frequency=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_mc_pool_supportable_spectrumupper_frequencylower_frequency_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_mc_pool_supportable_spectrumupper_frequencylower_frequency_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/media-channel-service-interface-point-spec/mc-pool/supportable-spectrum={upper-frequency},{lower-frequency}/'.format(uuid='uuid_example', local_id='local_id_example', upper_frequency=56, lower_frequency=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_post

        
        """
        tapi_photonic_media_media_channel_service_interface_point_spec = TapiPhotonicMediaMediaChannelServiceInterfacePointSpec()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/media-channel-service-interface-point-spec/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_photonic_media_media_channel_service_interface_point_spec),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_media_channel_service_interface_point_spec_put

        
        """
        tapi_photonic_media_media_channel_service_interface_point_spec = TapiPhotonicMediaMediaChannelServiceInterfacePointSpec()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/media-channel-service-interface-point-spec/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_photonic_media_media_channel_service_interface_point_spec),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_application_identifier_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_application_identifier_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/otsi-config/application-identifier/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_application_identifier_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_application_identifier_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/otsi-config/application-identifier/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_application_identifier_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_application_identifier_post

        
        """
        tapi_photonic_media_application_identifier = TapiPhotonicMediaApplicationIdentifier()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/otsi-config/application-identifier/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_photonic_media_application_identifier),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_application_identifier_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_application_identifier_put

        
        """
        tapi_photonic_media_application_identifier = TapiPhotonicMediaApplicationIdentifier()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/otsi-config/application-identifier/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_photonic_media_application_identifier),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/otsi-config/central-frequency/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_frequency_constraint_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_frequency_constraint_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/otsi-config/central-frequency/frequency-constraint/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_frequency_constraint_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_frequency_constraint_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/otsi-config/central-frequency/frequency-constraint/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_frequency_constraint_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_frequency_constraint_post

        
        """
        tapi_photonic_media_frequency_constraint = TapiPhotonicMediaFrequencyConstraint()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/otsi-config/central-frequency/frequency-constraint/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_photonic_media_frequency_constraint),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_frequency_constraint_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_frequency_constraint_put

        
        """
        tapi_photonic_media_frequency_constraint = TapiPhotonicMediaFrequencyConstraint()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/otsi-config/central-frequency/frequency-constraint/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_photonic_media_frequency_constraint),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/otsi-config/central-frequency/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_post

        
        """
        tapi_photonic_media_central_frequency = TapiPhotonicMediaCentralFrequency()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/otsi-config/central-frequency/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_photonic_media_central_frequency),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_central_frequency_put

        
        """
        tapi_photonic_media_central_frequency = TapiPhotonicMediaCentralFrequency()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/otsi-config/central-frequency/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_photonic_media_central_frequency),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/otsi-config/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/otsi-config/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_post

        
        """
        tapi_photonic_media_otsi_termination_config_pac = TapiPhotonicMediaOtsiTerminationConfigPac()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/otsi-config/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_photonic_media_otsi_termination_config_pac),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_put

        
        """
        tapi_photonic_media_otsi_termination_config_pac = TapiPhotonicMediaOtsiTerminationConfigPac()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/otsi-config/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_photonic_media_otsi_termination_config_pac),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/otsi-config/spectrum/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_frequency_constraint_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_frequency_constraint_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/otsi-config/spectrum/frequency-constraint/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_frequency_constraint_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_frequency_constraint_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/otsi-config/spectrum/frequency-constraint/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_frequency_constraint_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_frequency_constraint_post

        
        """
        tapi_photonic_media_frequency_constraint = TapiPhotonicMediaFrequencyConstraint()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/otsi-config/spectrum/frequency-constraint/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_photonic_media_frequency_constraint),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_frequency_constraint_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_frequency_constraint_put

        
        """
        tapi_photonic_media_frequency_constraint = TapiPhotonicMediaFrequencyConstraint()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/otsi-config/spectrum/frequency-constraint/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_photonic_media_frequency_constraint),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/otsi-config/spectrum/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_post

        
        """
        tapi_photonic_media_spectrum_band = TapiPhotonicMediaSpectrumBand()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/otsi-config/spectrum/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_photonic_media_spectrum_band),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_spectrum_put

        
        """
        tapi_photonic_media_spectrum_band = TapiPhotonicMediaSpectrumBand()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/otsi-config/spectrum/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_photonic_media_spectrum_band),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_transmit_power_delete(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_transmit_power_delete

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/otsi-config/transmit-power/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_transmit_power_get(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_transmit_power_get

        
        """
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/otsi-config/transmit-power/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_transmit_power_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_transmit_power_post

        
        """
        tapi_photonic_media_power_properties_pac = TapiPhotonicMediaPowerPropertiesPac()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/otsi-config/transmit-power/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_photonic_media_power_properties_pac),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_transmit_power_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_otsi_config_transmit_power_put

        
        """
        tapi_photonic_media_power_properties_pac = TapiPhotonicMediaPowerPropertiesPac()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/otsi-config/transmit-power/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_photonic_media_power_properties_pac),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_post(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_post

        
        """
        tapi_photonic_media_otsi_connectivity_service_end_point_spec = TapiPhotonicMediaOtsiConnectivityServiceEndPointSpec()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='POST',
            data=json.dumps(tapi_photonic_media_otsi_connectivity_service_end_point_spec),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_put(self):
        """Test case for data_context_connectivity_context_connectivity_serviceuuid_end_pointlocal_id_otsi_connectivity_service_end_point_spec_put

        
        """
        tapi_photonic_media_otsi_connectivity_service_end_point_spec = TapiPhotonicMediaOtsiConnectivityServiceEndPointSpec()
        response = self.client.open(
            '/data/context/connectivity-context/connectivity-service={uuid}/end-point={local-id}/otsi-connectivity-service-end-point-spec/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='PUT',
            data=json.dumps(tapi_photonic_media_otsi_connectivity_service_end_point_spec),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_delete(self):
        """Test case for data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_delete

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/media-channel-service-interface-point-spec/'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_get(self):
        """Test case for data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/media-channel-service-interface-point-spec/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_mc_pool_available_spectrumupper_frequencylower_frequency_frequency_constraint_get(self):
        """Test case for data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_mc_pool_available_spectrumupper_frequencylower_frequency_frequency_constraint_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/media-channel-service-interface-point-spec/mc-pool/available-spectrum={upper-frequency},{lower-frequency}/frequency-constraint/'.format(uuid='uuid_example', upper_frequency=56, lower_frequency=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_mc_pool_available_spectrumupper_frequencylower_frequency_get(self):
        """Test case for data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_mc_pool_available_spectrumupper_frequencylower_frequency_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/media-channel-service-interface-point-spec/mc-pool/available-spectrum={upper-frequency},{lower-frequency}/'.format(uuid='uuid_example', upper_frequency=56, lower_frequency=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_mc_pool_get(self):
        """Test case for data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_mc_pool_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/media-channel-service-interface-point-spec/mc-pool/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_mc_pool_occupied_spectrumupper_frequencylower_frequency_frequency_constraint_get(self):
        """Test case for data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_mc_pool_occupied_spectrumupper_frequencylower_frequency_frequency_constraint_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/media-channel-service-interface-point-spec/mc-pool/occupied-spectrum={upper-frequency},{lower-frequency}/frequency-constraint/'.format(uuid='uuid_example', upper_frequency=56, lower_frequency=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_mc_pool_occupied_spectrumupper_frequencylower_frequency_get(self):
        """Test case for data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_mc_pool_occupied_spectrumupper_frequencylower_frequency_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/media-channel-service-interface-point-spec/mc-pool/occupied-spectrum={upper-frequency},{lower-frequency}/'.format(uuid='uuid_example', upper_frequency=56, lower_frequency=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_mc_pool_supportable_spectrumupper_frequencylower_frequency_frequency_constraint_get(self):
        """Test case for data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_mc_pool_supportable_spectrumupper_frequencylower_frequency_frequency_constraint_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/media-channel-service-interface-point-spec/mc-pool/supportable-spectrum={upper-frequency},{lower-frequency}/frequency-constraint/'.format(uuid='uuid_example', upper_frequency=56, lower_frequency=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_mc_pool_supportable_spectrumupper_frequencylower_frequency_get(self):
        """Test case for data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_mc_pool_supportable_spectrumupper_frequencylower_frequency_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/media-channel-service-interface-point-spec/mc-pool/supportable-spectrum={upper-frequency},{lower-frequency}/'.format(uuid='uuid_example', upper_frequency=56, lower_frequency=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_post(self):
        """Test case for data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_post

        
        """
        tapi_photonic_media_media_channel_service_interface_point_spec = TapiPhotonicMediaMediaChannelServiceInterfacePointSpec()
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/media-channel-service-interface-point-spec/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_photonic_media_media_channel_service_interface_point_spec),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_put(self):
        """Test case for data_context_service_interface_pointuuid_media_channel_service_interface_point_spec_put

        
        """
        tapi_photonic_media_media_channel_service_interface_point_spec = TapiPhotonicMediaMediaChannelServiceInterfacePointSpec()
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/media-channel-service-interface-point-spec/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(tapi_photonic_media_media_channel_service_interface_point_spec),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_otsi_service_interface_point_spec_delete(self):
        """Test case for data_context_service_interface_pointuuid_otsi_service_interface_point_spec_delete

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/otsi-service-interface-point-spec/'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_otsi_service_interface_point_spec_get(self):
        """Test case for data_context_service_interface_pointuuid_otsi_service_interface_point_spec_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/otsi-service-interface-point-spec/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_otsi_service_interface_point_spec_otsi_capability_get(self):
        """Test case for data_context_service_interface_pointuuid_otsi_service_interface_point_spec_otsi_capability_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/otsi-service-interface-point-spec/otsi-capability/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_otsi_service_interface_point_spec_otsi_capability_supportable_application_identifierapplication_code_get(self):
        """Test case for data_context_service_interface_pointuuid_otsi_service_interface_point_spec_otsi_capability_supportable_application_identifierapplication_code_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/otsi-service-interface-point-spec/otsi-capability/supportable-application-identifier={application-code}/'.format(uuid='uuid_example', application_code='application_code_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_otsi_service_interface_point_spec_otsi_capability_supportable_lower_central_frequencycentral_frequency_frequency_constraint_get(self):
        """Test case for data_context_service_interface_pointuuid_otsi_service_interface_point_spec_otsi_capability_supportable_lower_central_frequencycentral_frequency_frequency_constraint_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/otsi-service-interface-point-spec/otsi-capability/supportable-lower-central-frequency={central-frequency}/frequency-constraint/'.format(uuid='uuid_example', central_frequency=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_otsi_service_interface_point_spec_otsi_capability_supportable_lower_central_frequencycentral_frequency_get(self):
        """Test case for data_context_service_interface_pointuuid_otsi_service_interface_point_spec_otsi_capability_supportable_lower_central_frequencycentral_frequency_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/otsi-service-interface-point-spec/otsi-capability/supportable-lower-central-frequency={central-frequency}/'.format(uuid='uuid_example', central_frequency=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_otsi_service_interface_point_spec_otsi_capability_supportable_upper_central_frequencycentral_frequency_frequency_constraint_get(self):
        """Test case for data_context_service_interface_pointuuid_otsi_service_interface_point_spec_otsi_capability_supportable_upper_central_frequencycentral_frequency_frequency_constraint_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/otsi-service-interface-point-spec/otsi-capability/supportable-upper-central-frequency={central-frequency}/frequency-constraint/'.format(uuid='uuid_example', central_frequency=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_otsi_service_interface_point_spec_otsi_capability_supportable_upper_central_frequencycentral_frequency_get(self):
        """Test case for data_context_service_interface_pointuuid_otsi_service_interface_point_spec_otsi_capability_supportable_upper_central_frequencycentral_frequency_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/otsi-service-interface-point-spec/otsi-capability/supportable-upper-central-frequency={central-frequency}/'.format(uuid='uuid_example', central_frequency=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_otsi_service_interface_point_spec_otsi_capability_total_power_warn_threshold_get(self):
        """Test case for data_context_service_interface_pointuuid_otsi_service_interface_point_spec_otsi_capability_total_power_warn_threshold_get

        
        """
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/otsi-service-interface-point-spec/otsi-capability/total-power-warn-threshold/'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_otsi_service_interface_point_spec_post(self):
        """Test case for data_context_service_interface_pointuuid_otsi_service_interface_point_spec_post

        
        """
        tapi_photonic_media_otsi_service_interface_point_spec = TapiPhotonicMediaOtsiServiceInterfacePointSpec()
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/otsi-service-interface-point-spec/'.format(uuid='uuid_example'),
            method='POST',
            data=json.dumps(tapi_photonic_media_otsi_service_interface_point_spec),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_service_interface_pointuuid_otsi_service_interface_point_spec_put(self):
        """Test case for data_context_service_interface_pointuuid_otsi_service_interface_point_spec_put

        
        """
        tapi_photonic_media_otsi_service_interface_point_spec = TapiPhotonicMediaOtsiServiceInterfacePointSpec()
        response = self.client.open(
            '/data/context/service-interface-point={uuid}/otsi-service-interface-point-spec/'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(tapi_photonic_media_otsi_service_interface_point_spec),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_media_channel_assembly_spec_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_media_channel_assembly_spec_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/media-channel-assembly-spec/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_media_channel_connection_end_point_spec_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_media_channel_connection_end_point_spec_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/media-channel-connection-end-point-spec/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_media_channel_connection_end_point_spec_media_channel_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_media_channel_connection_end_point_spec_media_channel_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/media-channel-connection-end-point-spec/media-channel/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_media_channel_connection_end_point_spec_media_channel_measured_power_egress_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_media_channel_connection_end_point_spec_media_channel_measured_power_egress_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/media-channel-connection-end-point-spec/media-channel/measured-power-egress/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_media_channel_connection_end_point_spec_media_channel_measured_power_ingress_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_media_channel_connection_end_point_spec_media_channel_measured_power_ingress_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/media-channel-connection-end-point-spec/media-channel/measured-power-ingress/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_media_channel_connection_end_point_spec_media_channel_occupied_spectrum_frequency_constraint_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_media_channel_connection_end_point_spec_media_channel_occupied_spectrum_frequency_constraint_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/media-channel-connection-end-point-spec/media-channel/occupied-spectrum/frequency-constraint/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_media_channel_connection_end_point_spec_media_channel_occupied_spectrum_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_media_channel_connection_end_point_spec_media_channel_occupied_spectrum_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/media-channel-connection-end-point-spec/media-channel/occupied-spectrum/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_ots_connection_end_point_spec_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_ots_connection_end_point_spec_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/ots-connection-end-point-spec/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_ots_connection_end_point_spec_ots_media_channel_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_ots_connection_end_point_spec_ots_media_channel_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/ots-connection-end-point-spec/ots-media-channel/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_ots_connection_end_point_spec_ots_media_channel_measured_power_egress_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_ots_connection_end_point_spec_ots_media_channel_measured_power_egress_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/ots-connection-end-point-spec/ots-media-channel/measured-power-egress/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_ots_connection_end_point_spec_ots_media_channel_measured_power_ingress_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_ots_connection_end_point_spec_ots_media_channel_measured_power_ingress_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/ots-connection-end-point-spec/ots-media-channel/measured-power-ingress/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_ots_connection_end_point_spec_ots_media_channel_occupied_spectrum_frequency_constraint_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_ots_connection_end_point_spec_ots_media_channel_occupied_spectrum_frequency_constraint_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/ots-connection-end-point-spec/ots-media-channel/occupied-spectrum/frequency-constraint/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_ots_connection_end_point_spec_ots_media_channel_occupied_spectrum_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_ots_connection_end_point_spec_ots_media_channel_occupied_spectrum_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/ots-connection-end-point-spec/ots-media-channel/occupied-spectrum/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_assembly_connection_end_point_spec_fec_parameters_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_assembly_connection_end_point_spec_fec_parameters_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/otsi-assembly-connection-end-point-spec/fec-parameters/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_assembly_connection_end_point_spec_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_assembly_connection_end_point_spec_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/otsi-assembly-connection-end-point-spec/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_assembly_connection_end_point_spec_otsi_adapter_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_assembly_connection_end_point_spec_otsi_adapter_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/otsi-assembly-connection-end-point-spec/otsi-adapter/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/otsi-connection-end-point-spec/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/otsi-connection-end-point-spec/otsi-termination/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_laser_properties_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_laser_properties_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/otsi-connection-end-point-spec/otsi-termination/laser-properties/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_received_power_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_received_power_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/otsi-connection-end-point-spec/otsi-termination/received-power/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_selected_application_identifier_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_selected_application_identifier_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/otsi-connection-end-point-spec/otsi-termination/selected-application-identifier/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_selected_central_frequency_frequency_constraint_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_selected_central_frequency_frequency_constraint_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/otsi-connection-end-point-spec/otsi-termination/selected-central-frequency/frequency-constraint/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_selected_central_frequency_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_selected_central_frequency_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/otsi-connection-end-point-spec/otsi-termination/selected-central-frequency/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_selected_spectrum_frequency_constraint_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_selected_spectrum_frequency_constraint_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/otsi-connection-end-point-spec/otsi-termination/selected-spectrum/frequency-constraint/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_selected_spectrum_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_selected_spectrum_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/otsi-connection-end-point-spec/otsi-termination/selected-spectrum/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_transmited_power_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_otsi_connection_end_point_spec_otsi_termination_transmited_power_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/otsi-connection-end-point-spec/otsi-termination/transmited-power/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/media-channel-node-edge-point-spec/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_mc_pool_available_spectrumupper_frequencylower_frequency_frequency_constraint_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_mc_pool_available_spectrumupper_frequencylower_frequency_frequency_constraint_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/media-channel-node-edge-point-spec/mc-pool/available-spectrum={upper-frequency},{lower-frequency}/frequency-constraint/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', upper_frequency=56, lower_frequency=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_mc_pool_available_spectrumupper_frequencylower_frequency_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_mc_pool_available_spectrumupper_frequencylower_frequency_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/media-channel-node-edge-point-spec/mc-pool/available-spectrum={upper-frequency},{lower-frequency}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', upper_frequency=56, lower_frequency=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_mc_pool_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_mc_pool_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/media-channel-node-edge-point-spec/mc-pool/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_mc_pool_occupied_spectrumupper_frequencylower_frequency_frequency_constraint_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_mc_pool_occupied_spectrumupper_frequencylower_frequency_frequency_constraint_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/media-channel-node-edge-point-spec/mc-pool/occupied-spectrum={upper-frequency},{lower-frequency}/frequency-constraint/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', upper_frequency=56, lower_frequency=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_mc_pool_occupied_spectrumupper_frequencylower_frequency_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_mc_pool_occupied_spectrumupper_frequencylower_frequency_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/media-channel-node-edge-point-spec/mc-pool/occupied-spectrum={upper-frequency},{lower-frequency}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', upper_frequency=56, lower_frequency=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_mc_pool_supportable_spectrumupper_frequencylower_frequency_frequency_constraint_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_mc_pool_supportable_spectrumupper_frequencylower_frequency_frequency_constraint_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/media-channel-node-edge-point-spec/mc-pool/supportable-spectrum={upper-frequency},{lower-frequency}/frequency-constraint/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', upper_frequency=56, lower_frequency=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_mc_pool_supportable_spectrumupper_frequencylower_frequency_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_media_channel_node_edge_point_spec_mc_pool_supportable_spectrumupper_frequencylower_frequency_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/media-channel-node-edge-point-spec/mc-pool/supportable-spectrum={upper-frequency},{lower-frequency}/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', upper_frequency=56, lower_frequency=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
