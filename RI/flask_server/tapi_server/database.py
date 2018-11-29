#!/usr/bin/env python3

from tapi_server.models.tapi_common_context import TapiCommonContext

context = TapiCommonContext()

def service_interface_point_list ():
    """Retrieve all ServiceInterfacePoints

    :rtype: List(ServiceInterfacePoint)
    """
    return context.service_interface_point
       

def service_interface_point (sip_uuid):
    """Retrieve ServiceInterfacePoint by ID

    :param sip_uuid: ID of ServiceInterfacePoint
    :type sip_uuid: str

    :rtype: ServiceInterfacePoint
    """
    for sip in context.service_interface_point:
        if sip.uuid == sip_uuid:
            return sip


def topology_list ():
    """Retrieve all Topology

    :rtype: List(Topology)
    """
    return context.topology_context.topology


def topology (topo_uuid):
    """Retrieve Topology by ID

    :param topo_uuid: ID of Topology
    :type topo_uuid: str

    :rtype: Topology
    """
    for topo in context.topology_context.topology:
        if topo.uuid == topo_uuid:
            return topo


def node (topo_uuid, node_uuid):
    """Retrieve Node by ID

    :param topo_uuid: ID of Topology
    :type topo_uuid: str
    :param node_uuid: ID of Node
    :type node_uuid: str

    :rtype: Node
    """
    for topo in context.topology_context.topology:
        if topo.uuid == topo_uuid:
            for node in topo.node:
                if node.uuid == node_uuid:
                    return node
       

def link (topo_uuid, link_uuid):
    """Retrieve Link by ID

    :param topo_uuid: ID of Topology
    :type topo_uuid: str
    :param link_uuid: ID of Link
    :type link_uuid: str

    :rtype: Link
    """
    for topo in context.topology_context.topology:
        if topo.uuid == topo_uuid:
            for link in topo.link:
                if link.uuid == link_uuid:
                    return link
       

def node_edge_point (topo_uuid, node_uuid, nep_uuid):
    """Retrieve NodeEdgePoint by ID

    :param topo_uuid: ID of Topology
    :type uuid: str
    :param node_uuid: ID of Node
    :type node_uuid: str
    :param nep_uuid: ID of NodeEdgePoint
    :type nep_uuid: str

    :rtype: NodeEdgePoint
    """
    for topo in context.topology_context.topology:
        if topo.uuid == topo_uuid:
            for node in topo.node:
                if node.uuid == node_uuid:
                    for nep in node.owned_node_edge_point:
                        if nep.uuid == nep_uuid:
                            return nep
                        
                        
def connection_end_point (id, node_uuid, nep_uuid, cep_uuid):
    """Retrieve NodeEdgePoint by ID

    :param topo_uuid: ID of Topology
    :type uuid: str
    :param node_uuid: ID of Node
    :type node_uuid: str
    :param nep_uuid: ID of NodeEdgePoint
    :type nep_uuid: str
    :param cep_uuid: ID of ConnectionEndPoint
    :type cep_uuid: str

    :rtype: ConnectionEndPoint
    """
    for topo in context.topology_context.topology:
        if topo.uuid == topo_uuid:
            for node in topo.node:
                if node.uuid == node_uuid:
                    for nep in node.owned_node_edge_point:
                        if nep.uuid == nep_uuid:
                            for cep in nep.cep_list.connection_end_point:
                                if cep.uuid == cep_uuid:
                                    return cep           
                        
def connectivity_service_list ():
    """Retrieve all ConnectivityService

    :rtype: List(ConnectivityService)
    """
    return context.connectivity_context.connectivity_service


def connectivity_service (cs_uuid):
    """Retrieve ConnectivityService by ID

    :param cs_uuid: ID of ConnectivityService
    :type cs_uuid: str

    :rtype: Topology
    """
    for cs in context.connectivity_context.connectivity_service:
        if cs.uuid == cs_uuid:
            return cs   
        
def connection (conn_uuid):
    """Retrieve Connection by ID

    :param conn_uuid: ID of Connection
    :type conn_uuid: str

    :rtype: Connection
    """
    for conn in context.connectivity_context.connection:
        if conn.uuid == conn_uuid:
            return conn
                
                            
       