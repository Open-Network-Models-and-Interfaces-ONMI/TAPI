#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import json
import requests
from requests.auth import HTTPBasicAuth
import matplotlib.pyplot as plt
import networkx as nx


def main ():
    sips = []
    topologies = []
    for port in sys.argv:
        if not port.isnumeric():
            continue
        retrieve_context(sips, topologies, port)
    draw_network_topology(sips, topologies)
    
    
def retrieve_context(sips, topologies, port, user='', password=''):
    url = 'http://0.0.0.0' + ':' + port + '/data/context/'
    print ("Retrieving TAPI Context from " + url)
    response = requests.get(url, auth=HTTPBasicAuth(user, password))
    context = response.json()
    print ("Retrieved TAPI Context: " + context['uuid'])
    for sip in context['service-interface-point']:
        sips.append(sip)
    for topo in context['topology-context']['topology']:
        topologies.append(topo)


def draw_network_topology (sips, topologies) :
    plt.axis('off')
    nwk_graph = nx.Graph()
    for sip in sips:
        uuid = sip['uuid']
        nwk_graph.add_node(uuid, col='#00ffff', size=300)
        
    for topo in topologies:
        for node in topo['node']:
            uuid = node['uuid']
            nwk_graph.add_node(uuid, col='#ff9966', size=1500)
            for nep in node['owned-node-edge-point']:
                nep_uuid = nep['uuid']
                sip = nep['mapped-service-interface-point']
                nwk_graph.add_node(nep_uuid, col='#9900cc', size=300)
                nwk_graph.add_edge(uuid, nep_uuid, col='#ff9966')
                if sip:
                    nwk_graph.add_edge(sip[0]['service-interface-point-uuid'], nep_uuid, col='#00ffff')
                    
        for link in topo['link']:
            nep1_uuid = link['node-edge-point'][0]['node-edge-point-uuid']
            nep2_uuid = link['node-edge-point'][1]['node-edge-point-uuid']
            nwk_graph.add_edge(nep1_uuid, nep2_uuid, col='#9900cc')

    node_list = list(nx.get_node_attributes(nwk_graph, 'col').keys())
    node_col = list(nx.get_node_attributes(nwk_graph, 'col').values())
    node_size = list(nx.get_node_attributes(nwk_graph, 'size').values())
    edge_list = list(nx.get_edge_attributes(nwk_graph, 'col').keys())
    edge_col = list(nx.get_edge_attributes(nwk_graph, 'col').values())
    nx.draw_networkx(nwk_graph, nodelist=node_list, edgelist=edge_list, node_size=node_size, node_color=node_col, edge_color=edge_col, font_size='6', width=3.0)
    plt.show()
    

if __name__ == "__main__":
    main()
    
