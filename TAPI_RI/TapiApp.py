#!/usr/bin/python
# -*- coding: utf-8 -*-


import requests
from requests.auth import HTTPBasicAuth
import json
import matplotlib.pyplot as plt
import networkx as nx

IP='127.0.0.1'
PORT='8080'

def retrieveTopology(ip, port, user='', password=''):
    http_json = 'http://' + ip + ':' + port + '/restconf/config/Context/_topology/top0'
    response = requests.get(http_json, auth=HTTPBasicAuth(user, password))
    topology = response.json()
    return topology

def load_topology ( topology) :
    G=nx.Graph()
    for link in topology['_link']:
      G.add_edge( link['_node'][0], link['_node'][1] )
      print 'Link: ' + link['_node'][0] + ' ' + link['_node'][1]
    nx.draw(G)
    plt.show()

if __name__ == "__main__":
    print "Reading network-topology"
    topo = retrieveTopology(IP, PORT)
    print json.dumps(topo, indent=4, sort_keys=True)
    load_topology(topo)
