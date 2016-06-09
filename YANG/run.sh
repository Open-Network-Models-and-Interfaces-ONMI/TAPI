#!/bin/bash

YANG="Tapi-TypeDefinitions Tapi-ObjectClasses Tapi-Interfaces-TopologyService Tapi-Interfaces-ConnectivityService Tapi-Interfaces-PathComputationService Tapi-Interfaces-VirtualNetworkService Tapi-Interfaces-NotificationSubscriptionService TapiOchSpec-ObjectClasses TapiOduSpec-ObjectClasses TapiSpec-ObjectClasses TapiOchSpec-TypeDefinitions TapiOduSpec-TypeDefinitions"

for file in $YANG;
    do
        echo $file.yang
        echo "TREE"
        pyang -f tree $file.yang -o tree/$file.tree
        echo "SWAGGER"
        pyang -f swagger $file.yang -o ../SWAGGER/$file.swagger
        echo "UML"
        pyang -f uml $file.yang -o $file.uml
        java -jar plantuml.7997.jar $file.uml
        echo "JSON SCHEMA"
        pyang -f json_schema $file.yang -o ../JSON/$file.json
    done

cp img/*.png pyang_uml/
