#Set Context
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/ -d @context.json

#Get Context
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/ 

#Get Service End Points
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/service-interface-point/

#Get Service End Points
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/service-interface-point/sip-pe1-uni1/
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/service-interface-point/sip-pe2-uni2/

curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/service-interface-point/sip2/

#Get topologies
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/topology/

#Get topology Top0
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/topology/topo-nwk/

#Get nodes
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/topology/topo-nwk/node/

#Get node 1
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/topology/topo-nwk/node/node-pi4-odu/

#Get node edge points
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/topology/topo-nwk/node/node-pi4-odu/owned-node-edge-point/

#Get node edge point 1
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/topology/topo-nwk/node/node-pi4-odu/owned-node-edge-point/nep-pi4-odu4-nni1/

#Get links
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/topology/top-nwk/link/

#Get link 1-3
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/topology/top-nwk/link/link-pe1-odu4-nni1-pi4-odu4-nni2/


#Create Connectivity Service
#curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/connectivity-service/cs1/ -d @cs1.json

#Get Connectivity Services
#curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/connectivity-service/
#curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/connectivity-service/cs1/

#Delete Connectivity Services
#curl -X DELETE -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/connectivity-service/cs1/

#Get connection
#curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/connection/

