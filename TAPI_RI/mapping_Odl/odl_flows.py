#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from requests.auth import HTTPBasicAuth
import json

IP='localhost'
PORT='8181'
USER='admin'
PASSWORD='admin'

URL = 'http://' + IP + ':' + PORT + '/restconf/config/opendaylight-inventory:nodes/node/'

def insertFlow( nodeId, flow_id, priority, inport, outport ):

    flow = '{"flow-node-inventory:flow": [{"priority": ' + priority + ',"hard-timeout": 0,"idle-timeout": 0, "flags": "", "cookie": 7,"match": {"in-port":"'+ inport + '"},"id":"'+flow_id+'","table_id": 0,"instructions": {"instruction": [{"order": "0","apply-actions": {"action": [{"order": "0","output-action": {"output-node-connector": "'+nodeId+':'+outport+'", "max-length": "65535"}}]}}]}}]}'

    print "Flow: " + flow
    url = URL + nodeId + '/flow-node-inventory:table/0/flow/' + flow_id 
    headers = {'content-type': 'application/json'}
    print url
    response = requests.put(url, data=flow,
	                    headers=headers, auth=HTTPBasicAuth(USER,
	                    PASSWORD))
    print response
    return {'flow_id':flow_id, 'status':response.status_code, 'content': response.content}

def deleteFlow(nodeId, flow_id):
    
    url = URL + '' + nodeId + '/flow-node-inventory:table/0/flow/' + flow_id + ''
    response = requests.delete(url, auth=HTTPBasicAuth(USER, PASSWORD))
    return {'flow_id':flow_id, 'status':response.status_code, 'content': response.content}



if __name__ == "__main__":

    print "Setting flow"
    
    res = insertFlow(nodeId="openflow:1", flow_id='12', priority="15", inport="1", outport="2")
    print json.dumps(res, indent=4, sort_keys=True)
    res = insertFlow(nodeId="openflow:2", flow_id='21', priority="15", inport="2", outport="1")
    print json.dumps(res, indent=4, sort_keys=True)
    res = insertFlow(nodeId="openflow:1", flow_id='21', priority="16", inport="2", outport="1")
    print json.dumps(res, indent=4, sort_keys=True)
    res = insertFlow(nodeId="openflow:2", flow_id='12', priority="16", inport="1", outport="2")
    print json.dumps(res, indent=4, sort_keys=True)

    #res = deleteFlow(nodeId="openflow:1", flow_id="12")
    #print json.dumps(res, indent=4, sort_keys=True)



    
