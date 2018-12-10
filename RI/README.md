# TAPI Reference Implementation

## Overview
The TAPI server implementations are generated using the [OpenAPI Generator](https://openapi-generator.tech) tools.
By using the [OpenAPI-Spec](https://openapis.org), you can easily generate a server stubs.

Currently the RI includes following implementations:
- Python-flask server
- Python client)
- JSON network database

## Requirements
These implementations have been tested on [Ubuntu 18.04.1 LTS](https://www.ubuntu.com/download/desktop).

## Coverage
For this release (TAPI 2.1.1), the [tapi-photonic-media OpenAPI file](https://github.com/OpenNetworkingFoundation/TAPI/blob/develop/OAS/tapi-photonic-media@402018-10-16.yaml) has been used to generate the server stubs.

Only a limited set of following APIs have been implemented in this release:
* _GET_ /data/context/
* _GET_ /data/context/service-interface-point={uuid}/
* _GET_ /data/context/topology-context/
* _GET_ /data/context/topology-context/topology={uuid}/
* _GET_ /data/context/topology-context/topology={uuid}/link={link-uuid}/
* _GET_ /data/context/topology-context/topology={uuid}/node={node-uuid}/
* _GET_ /data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={nep-uuid}/
* _GET_ /data/context/connectivity-context/
* _GET_ /data/context/connectivity-context/connectivity-service={uuid}/
* _GET_ /data/context/connectivity-context/connection={uuid}/
* _GET_ /data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={nep-uuid}/cep-list/
* _GET_ /data/context/topology-context/topology={uuid}/node={node-uuid}/owned-node-edge-point={nep-uuid}/cep-list/connection-end-point={cep-uuid}/
* _POST_ /operations/get-topology-list/
* _POST_ /operations/get-topology-details/
* _POST_ /operations/get-link-details/
* _POST_ /operations/get-node-details/
* _POST_ /operations/get-node-edge-point-details/
* _POST_ /operations/get-connectivity-service-list/
* _POST_ /operations/get-connectivity-service-details/
* _POST_ /operations/get-connection-details/
* _POST_ /operations/get-connection-end-point-details/

The following set of APIs are planned to be implemented soon:
* _POST_ /operations/create-connectivity-service/
* _POST_ /operations/delete-connectivity-service/

