#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from requests.auth import HTTPBasicAuth
import json

IP='127.0.0.1'
PORT='8181'
USER='onos'
PASSWORD='rocks'

def retrieveTopology(ip, port, user, password):
    http_json = 'http://' + ip + ':' + port + '/onos/v1/links'
    response = requests.get(http_json, auth=HTTPBasicAuth(user, password))
    topology = response.json()
    return topology

if __name__ == "__main__":

    print "Reading network-topology"
    topo = retrieveTopology(IP, PORT, USER, PASSWORD)
    print json.dumps(topo, indent=4, sort_keys=True)


    
