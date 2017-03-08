#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from requests.auth import HTTPBasicAuth
import json

IP='127.0.0.1'
PORT='8181'
USER='admin'
PASSWORD='admin'

def retrieveTopology(ip, port, user, password):
    http_json = 'http://' + ip + ':' + port + '/restconf/operational/network-topology:network-topology/'
    response = requests.get(http_json, auth=HTTPBasicAuth(user, password))
    topology = response.json()
    return topology

def retrieveNodes(ip, port, user, password):
    http_json = 'http://' + ip + ':' + port + '/restconf/operational/opendaylight-inventory:nodes/'

    response = requests.get(http_json, auth=HTTPBasicAuth(user, password))
    nodes = response.json()
    return nodes


if __name__ == "__main__":

    print "Reading network-topology"
    topo = retrieveTopology(IP, PORT, USER, PASSWORD)
    print json.dumps(topo, indent=4, sort_keys=True)

    print "Reading opendaylight-inventory:nodes"
    nodes = retrieveNodes(IP, PORT, USER, PASSWORD)
    print json.dumps(nodes, indent=4, sort_keys=True)

    
