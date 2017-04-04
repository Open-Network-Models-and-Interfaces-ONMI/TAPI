#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from requests.auth import HTTPBasicAuth
from objects_TapiTopology.node import Node as Node
from objects_TapiTopology.topology import Topology as Topology
from objects_TapiTopology.nodeEdgePoint import NodeEdgePoint as NodeEdgePoint
from objects_TapiTopology.linkPort import LinkPort as LinkPort
from objects_TapiTopology.link import Link as Link
from objects_Tapi._serviceEndPointSchema import _serviceEndPointSchema

import json
import backend as be

IP='127.0.0.1'
PORT='8181'
USER='onos'
PASSWORD='rocks'
TOPOLOGY_UUID="top0"

class onos_topology():

    def retrieveTopology(self,ip, port, user, password):
        be.Context._topology[TOPOLOGY_UUID] = Topology({"uuid":TOPOLOGY_UUID})
        self.getDevices(ip, port, user, password)
        self.getLinks( ip, port, user, password)

    def getDevices(self,ip, port, user, password):
        http_json = 'http://' + ip + ':' + port + '/onos/v1/devices'
        response = requests.get(http_json, auth=HTTPBasicAuth(user, password))
        devices = response.json()
        print json.dumps(devices, indent=4, sort_keys=True)
        self.parseDevices(ip, port, user, password, devices)
    
    def getPortsByDevice(self, ip, port, user, password, device_id ):
        http_json = 'http://' + ip + ':' + port + '/onos/v1/devices/'+str(device_id)+'/ports'
        response = requests.get(http_json, auth=HTTPBasicAuth(user, password))
        ports = response.json()
        print json.dumps(ports, indent=4, sort_keys=True)
        return ports
        
    def getLinks(self, ip, port, user, password):
        http_json = 'http://' + ip + ':' + port + '/onos/v1/links'
        response = requests.get(http_json, auth=HTTPBasicAuth(user, password))
        links = response.json()
        print json.dumps(links, indent=4, sort_keys=True)
        self.parseLinks(links)

    def parseDevices(self, ip, port, user, password, devices):
        for dev in devices["devices"]:
            node_id=dev["id"]
            node = Node({   "uuid":node_id, 
                            "_ownedNodeEdgePoint": [], 
                            "_state": {"administrativeState": "UNLOCKED","lifecycleState": "POTENTIAL","operationalState": "ENABLED"},
                            "_transferCapacity": { "availableCapacity": {"totalSize": "100MBPS"}, "totalPotentialCapacity": { "totalSize": "100MBPS"} },
                            "layerProtocolName": ["OCH"]})
            ports=self.getPortsByDevice(ip, port, user, password,node_id)
            
            for nep in ports["ports"]:
                print nep
                nep_obj=NodeEdgePoint({"uuid":nep['port']})
                node._ownedNodeEdgePoint[nep['port']]=nep_obj
            be.Context._topology[TOPOLOGY_UUID]._node[node_id] = node
            sep = _serviceEndPointSchema({"uuid": node_id })
            be.Context._serviceEndPoint[node_id]=sep
    def parseLinks(self, links):
        link_id=0
        for link in links["links"]:
            print link
            link_id=link_id+1
            link_obj = Link({   "uuid":"link"+str(link_id), 
                                "_node": [],
                                "_linkPort" : []
                            })
            link_obj._node.append("restconf/config/Context/_topology/"+TOPOLOGY_UUID+"/_node/"+link["src"]["device"]+"/")
            link_obj._node.append("restconf/config/Context/_topology/"+TOPOLOGY_UUID+"/_node/"+link["dst"]["device"]+"/")
            link_port_src = LinkPort({  "_nodeEdgePoint": "restconf/config/Context/_topology/"+TOPOLOGY_UUID+"/_node/"+ link["src"]["device"] +"/_ownedNodeEdgePoint/"+ link["src"]["port"]+"/",
                                        "direction": "BIDIRECTIONAL",
                                        "localId": "lp"+str(link_id)+"1",
                                        "role": "SYMMETRIC" })  
            link_port_dst = LinkPort({  "_nodeEdgePoint": "restconf/config/Context/_topology/"+TOPOLOGY_UUID+"/_node/"+ link["dst"]["device"] +"/_ownedNodeEdgePoint/"+ link["dst"]["port"]+"/",
                                        "direction": "BIDIRECTIONAL",
                                        "localId": "lp"+str(link_id)+"2",
                                        "role": "SYMMETRIC" })  
            link_obj._linkPort["lp"+str(link_id)+"1"] = link_port_src
            link_obj._linkPort["lp"+str(link_id)+"2"] = link_port_dst
            be.Context._topology[TOPOLOGY_UUID]._link[link_id] = link_obj
                    
if __name__ == "__main__":

    print "Reading network-topology"
    topo = onos_topology()
    topo.retrieveTopology(IP, PORT, USER, PASSWORD)
    print json.dumps(topo, indent=4, sort_keys=True)


    
