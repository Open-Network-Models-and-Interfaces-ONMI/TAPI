#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from requests.auth import HTTPBasicAuth
import json

IP='localhost'
PORT='8181'
USER='onos'
PASSWORD='rocks'

URL = 'http://' + IP + ':' + PORT + '/onos/v1/flows/'

def insertFlow( nodeId, priority, inport, outport ):

    flow='{ "priority": '+priority+', "timeout": 0, "isPermanent": true, "deviceId": "'+nodeId+'", "treatment": { "instructions": [ { "type": "OUTPUT", "port": "'+outport+'" } ] }, "selector": { "criteria": [ { "type": "IN_PORT", "port": "'+inport+'" } ] } }'


    print "Flow: " + flow
    url = URL + nodeId + '?appId=tuto' 
    headers = {'content-type': 'application/json'}
    print url
    response = requests.post(url, data=flow,
	                    headers=headers, auth=HTTPBasicAuth(USER,
	                    PASSWORD))
    print response
    return { 'status':response.status_code, 'content': response.content}

def deleteFlow(nodeId, flow_id):
    
    url = URL + '' + nodeId + '/' + flow_id 
    response = requests.delete(url, auth=HTTPBasicAuth(USER, PASSWORD))
    return {'flow_id':flow_id, 'status':response.status_code, 'content': response.content}



if __name__ == "__main__":

    print "Setting flow"
    
    res = insertFlow(nodeId="of:0000000000000001", priority="40001", inport="1", outport="2")
    print json.dumps(res, indent=4, sort_keys=True)
 
    res = insertFlow(nodeId="of:0000000000000001", priority="40002", inport="2", outport="1")
    print json.dumps(res, indent=4, sort_keys=True)
 
    res = insertFlow(nodeId="of:0000000000000002", priority="40001", inport="1", outport="2")
    print json.dumps(res, indent=4, sort_keys=True)
 
    res = insertFlow(nodeId="of:0000000000000002", priority="40002", inport="2", outport="1")
    print json.dumps(res, indent=4, sort_keys=True)




    
