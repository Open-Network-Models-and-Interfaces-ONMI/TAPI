#!/bin/bash          

#Load server database with scenario (server_backend_state.json)
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8080/backend/load_state/

#Scenario
#    
#SE1-PE1---PE3---PE2-SE2
#     \   |    /
#      \  |   /
#        PE4


#Get Context
curl -X GET --no-keepalive -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/Context/

#Get topology Top0
curl -X GET --no-keepalive -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/Context/_topology/top0/

#Get Service End Points
curl -X GET --no-keepalive -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/Context/_serviceEndPoint/se1/
curl -X GET --no-keepalive -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/Context/_serviceEndPoint/se2/

#Create Connection
curl -X POST --no-keepalive -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/Context/_connectivityService/cs1/ -d'{"uuid":"cs1", "_connConstraints":{"serviceType":"POINT_TO_POINT_CONNECTIVITY", "serviceLayer":["OCH"] }, "_servicePort":[ { "localId":"sp1", "serviceLayer":"OCH" , "direction":"BIDIRECTIONAL", "role":"SYMMETRIC", "_serviceEndPoint":"http://127.0.0.1:8080/restconf/config/Context/_serviceEndPoint/se1"}, { "localId":"sp2", "serviceLayer":"OCH" , "direction":"BIDIRECTIONAL", "role":"SYMMETRIC", "_serviceEndPoint":"http://127.0.0.1:8080/restconf/config/Context/_serviceEndPoint/se2"} ] }'

curl -X GET --no-keepalive -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/Context/_connectivityService/

#curl -X GET --no-keepalive -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/modules/

#curl -X GET --no-keepalive -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/modules/module/Tapi_TypeDefinitions/0000-00-00/schema/


