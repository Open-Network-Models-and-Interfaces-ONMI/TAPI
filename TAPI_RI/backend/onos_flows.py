#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from requests.auth import HTTPBasicAuth
import json

IP='localhost'
PORT='8181'
USER='onos'
PASSWORD='rocks'
PRIORITY="100"

URL = 'http://' + IP + ':' + PORT + '/onos/v1/'

class onos_flows():
    def insertFlow( self, uuid, node, src_port, dst_port ):

        flow='{ "priority": '+PRIORITY+', "timeout": 0, "isPermanent": true, "deviceId": "'+node+'", "treatment": { "instructions": [ { "type": "OUTPUT", "port": "'+dst_port+'" } ] }, "selector": { "criteria": [ { "type": "IN_PORT", "port": "'+src_port+'" } ] } }'


        print "Flow: " + flow
        url = URL + 'flows/' + node + '?appId='+uuid 
        headers = {'content-type': 'application/json'}
        print url
        response = requests.post(url, data=flow,
	                        headers=headers, auth=HTTPBasicAuth(USER,
	                        PASSWORD))
        print response
        return { 'status':response.status_code, 'content': response.content}

    def deleteFlow(self, uuid):
        url = URL + 'flows/application/' + uuid
        response = requests.delete(url, auth=HTTPBasicAuth(USER, PASSWORD))
       

    def compute_path(self, src, dst ):
        print "Request path between " + src + " and " + dst
        url = URL + 'paths/' + src + '/' + dst 
        paths = requests.get(url, auth=HTTPBasicAuth(USER, PASSWORD))
        return paths.json()

if __name__ == "__main__":

    print "Setting flow"
    onos = onos_flows()
    res = onos.insertFlow(nodeId="of:0000000000000001", priority="40001", inport="1", outport="2")
    print json.dumps(res, indent=4, sort_keys=True)
 
    res = onos.insertFlow(nodeId="of:0000000000000001", priority="40002", inport="2", outport="1")
    print json.dumps(res, indent=4, sort_keys=True)
 
    res = onos.insertFlow(nodeId="of:0000000000000002", priority="40001", inport="1", outport="2")
    print json.dumps(res, indent=4, sort_keys=True)
 
    res = onos.insertFlow(nodeId="of:0000000000000002", priority="40002", inport="2", outport="1")
    print json.dumps(res, indent=4, sort_keys=True)




    
