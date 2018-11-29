# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

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
from tapi_server.test import BaseTestCase


class TestTapiOduController(BaseTestCase):
    """TapiOduController integration test stubs"""

    def test_data_context_oam_context_meguuid_meplocal_id_odu_connection_end_point_spec_get(self):
        """Test case for data_context_oam_context_meguuid_meplocal_id_odu_connection_end_point_spec_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/meg={uuid}/mep={local-id}/odu-connection-end-point-spec/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_meguuid_meplocal_id_odu_connection_end_point_spec_odu_common_get(self):
        """Test case for data_context_oam_context_meguuid_meplocal_id_odu_connection_end_point_spec_odu_common_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/meg={uuid}/mep={local-id}/odu-connection-end-point-spec/odu-common/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_meguuid_meplocal_id_odu_connection_end_point_spec_odu_ctp_get(self):
        """Test case for data_context_oam_context_meguuid_meplocal_id_odu_connection_end_point_spec_odu_ctp_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/meg={uuid}/mep={local-id}/odu-connection-end-point-spec/odu-ctp/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_meguuid_meplocal_id_odu_connection_end_point_spec_odu_protection_get(self):
        """Test case for data_context_oam_context_meguuid_meplocal_id_odu_connection_end_point_spec_odu_protection_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/meg={uuid}/mep={local-id}/odu-connection-end-point-spec/odu-protection/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_meguuid_meplocal_id_odu_connection_end_point_spec_odu_term_and_adapter_accepted_payload_type_get(self):
        """Test case for data_context_oam_context_meguuid_meplocal_id_odu_connection_end_point_spec_odu_term_and_adapter_accepted_payload_type_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/meg={uuid}/mep={local-id}/odu-connection-end-point-spec/odu-term-and-adapter/accepted-payload-type/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_meguuid_meplocal_id_odu_connection_end_point_spec_odu_term_and_adapter_get(self):
        """Test case for data_context_oam_context_meguuid_meplocal_id_odu_connection_end_point_spec_odu_term_and_adapter_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/meg={uuid}/mep={local-id}/odu-connection-end-point-spec/odu-term-and-adapter/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_get(self):
        """Test case for data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/meg={uuid}/mip={local-id}/odu-mip-spec/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_odu_defect_get(self):
        """Test case for data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_odu_defect_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/meg={uuid}/mip={local-id}/odu-mip-spec/odu-defect/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_odu_mip_deg_thr_get(self):
        """Test case for data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_odu_mip_deg_thr_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/meg={uuid}/mip={local-id}/odu-mip-spec/odu-mip/deg-thr/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_odu_mip_get(self):
        """Test case for data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_odu_mip_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/meg={uuid}/mip={local-id}/odu-mip-spec/odu-mip/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_odu_ncm_get(self):
        """Test case for data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_odu_ncm_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/meg={uuid}/mip={local-id}/odu-mip-spec/odu-ncm/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_odu_pm_get(self):
        """Test case for data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_odu_pm_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/meg={uuid}/mip={local-id}/odu-mip-spec/odu-pm/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_odu_pm_uas_get(self):
        """Test case for data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_odu_pm_uas_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/meg={uuid}/mip={local-id}/odu-mip-spec/odu-pm/uas/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_odu_tcm_get(self):
        """Test case for data_context_oam_context_meguuid_miplocal_id_odu_mip_spec_odu_tcm_get

        
        """
        response = self.client.open(
            '/data/context/oam-context/meg={uuid}/mip={local-id}/odu-mip-spec/odu-tcm/'.format(uuid='uuid_example', local_id='local_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_odu_connection_end_point_spec_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_odu_connection_end_point_spec_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/odu-connection-end-point-spec/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_odu_connection_end_point_spec_odu_common_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_odu_connection_end_point_spec_odu_common_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/odu-connection-end-point-spec/odu-common/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_odu_connection_end_point_spec_odu_ctp_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_odu_connection_end_point_spec_odu_ctp_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/odu-connection-end-point-spec/odu-ctp/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_odu_connection_end_point_spec_odu_protection_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_odu_connection_end_point_spec_odu_protection_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/odu-connection-end-point-spec/odu-protection/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_odu_connection_end_point_spec_odu_term_and_adapter_accepted_payload_type_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_odu_connection_end_point_spec_odu_term_and_adapter_accepted_payload_type_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/odu-connection-end-point-spec/odu-term-and-adapter/accepted-payload-type/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_odu_connection_end_point_spec_odu_term_and_adapter_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_cep_list_connection_end_pointconnection_end_point_uuid_odu_connection_end_point_spec_odu_term_and_adapter_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/cep-list/connection-end-point={connection-end-point-uuid}/odu-connection-end-point-spec/odu-term-and-adapter/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example', connection_end_point_uuid='connection_end_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_odu_node_edge_point_spec_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_odu_node_edge_point_spec_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/odu-node-edge-point-spec/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_odu_node_edge_point_spec_odu_pool_get(self):
        """Test case for data_context_topology_context_topologyuuid_nodenode_uuid_owned_node_edge_pointowned_node_edge_point_uuid_odu_node_edge_point_spec_odu_pool_get

        
        """
        response = self.client.open(
            '/data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={owned-node-edge-point-uuid}/odu-node-edge-point-spec/odu-pool/'.format(uuid='uuid_example', node_uuid='node_uuid_example', owned_node_edge_point_uuid='owned_node_edge_point_uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
