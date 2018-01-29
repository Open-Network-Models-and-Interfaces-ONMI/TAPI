#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from requests.auth import HTTPBasicAuth
import json
import matplotlib.pyplot as plt
import networkx as nx
import random

IP = '127.0.0.1'
PORT = '8080'


def retrieveTopologies(ip, port, user='', password=''):
    print ("Reading network-topology")
    topologies = []
    topo_list_url = 'http://' + ip + ':' + port + '/restconf/config/context/topology/'
    response = requests.get(topo_list_url, auth=HTTPBasicAuth(user, password))
    topo_uris = response.json()
    print ("Retrieved Topology List\n" + json.dumps(topo_uris, indent=4))
    for topo_uri in topo_uris:
        topo_url = 'http://' + ip + ':' + port + topo_uri + '/'
        response = requests.get(topo_url, auth=HTTPBasicAuth(user, password))
        topology = response.json()
        print ("Retrieved Topology: " + json.dumps(topology['link'], indent=4))
        topologies.append(topology)
    return topologies


def draw_topologies (topologies) :
    plt.figure(figsize=(12, 8))
    plt.axis('off')
    nwk_graph = nx.Graph()
    for topo in topologies:
        for node in topo['node']:
            if node['owned-node-edge-point']:
                uuid = node['uuid']
                layer = node['layer-protocol-name'][0]
                posx = uuid.split('-')[3]
                posy = 0
                col = 'y'
                if layer == 'ETH':
                    posy = random.randint(6, 10)
                    col = '#4dffa6'
                elif layer == 'ODU':
                    posy = random.randint(1, 5)
                    col = '#4da6ff'
                nwk_graph.add_node(uuid, pos=(int(posx), posy), col=col)
                    
        for link in topo['link']:
            nep1_path = link['node-edge-point'][0].split('/')
            nep2_path = link['node-edge-point'][1].split('/')
            layer = link['layer-protocol-name'][0]
            col = 'y'
            if len(link['layer-protocol-name']) > 1:
                col = '#00ffff'
            elif layer == 'ETH':
                col = '#336600'
            elif layer == 'ODU':
                col = '#000099'
            nwk_graph.add_edge(nep1_path[7], nep2_path[7], col=col)

    node_pos = nx.get_node_attributes(nwk_graph, 'pos')
    node_list = list(nx.get_node_attributes(nwk_graph, 'col').keys())
    node_col = list(nx.get_node_attributes(nwk_graph, 'col').values())
    edge_list = list(nx.get_edge_attributes(nwk_graph, 'col').keys())
    edge_col = list(nx.get_edge_attributes(nwk_graph, 'col').values())
    nx.draw_networkx(nwk_graph, pos=node_pos, nodelist=node_list, node_color=node_col, edgelist=edge_list, edge_color=edge_col, node_size=3500, font_size='8', width=3.0)


if __name__ == "__main__":
    topologies = retrieveTopologies(IP, PORT)
    draw_topologies(topologies)
    plt.show()
