#!/bin/bash          

URL="http://127.0.0.1:8080"
VENDOR="TAPI_RI"
TOPOLOGY_UUID="top0"
CONNECTIVITY_SERVICE_UUID="140"
CONNECTION_ID="140"
CS_FILE="TAPIRI_CreateConnectivityService.json"

#Load server database with scenario (server_backend_state.json)
#curl -X POST -H "Content-Type: application/json" $URL/backend/load_state/ > STATE_$(date +%Y%m%d)_$VENDOR.txt

#Get topology list
curl -X GET -H "Content-Type: application/json" $URL/restconf/config/Context/_topology/ > TOPOLOGY_$(date +%Y%m%d)_$VENDOR.txt

#Get topology with uuid
curl -X GET -H "Content-Type: application/json" $URL/restconf/config/Context/_topology/$TOPOLOGY_UUID/ > TOPOLOGY_UUID_$(date +%Y%m%d)_$VENDOR.txt

#Get Service End Points
curl -X GET -H "Content-Type: application/json" $URL/restconf/config/Context/_serviceEndPoint/ > SEP_$(date +%Y%m%d)_$VENDOR.txt

#Getting Connectivity Service list:
curl -X GET -H "Content-Type: application/json" $URL/restconf/config/Context/_connectivityService/ > CS_$(date +%Y%m%d)_$VENDOR.txt

#Getting connectivity Service by id:
curl -X GET -H "Content-Type: application/json" $URL/restconf/config/Context/_connectivityService/$CONNECTIVITY_SERVICE_UUID/ > CS_UUID_$(date +%Y%m%d)_$VENDOR.txt

#Getting connection by id
curl -X GET -H "Content-Type: application/json" $URL/restconf/config/Context/_connection/$CONNECTION_ID/ > CONNECTION_UUID_$(date +%Y%m%d)_$VENDOR.txt

#Creating a connectivity service
curl -X POST -i -H "Content-Type: application/json" -H "Accept: application/json" --data @$CS_FILE $URL/restconf/config/Context/_connectivityService/ > CS_UUID_CREATED_$(date +%Y%m%d)_$VENDOR.txt

UUID=$(cat CS_UUID_CREATED_$(date +%Y%m%d)_$VENDOR.txt | grep uuid | cut -d'"' -f4)
echo $UUID

#Deleting a connectivity service
curl -X DELETE $URL/restconf/config/Context/_connectivityService/$UUID/ > CS_UUID_DELETED_$(date +%Y%m%d)_$VENDOR.txt

