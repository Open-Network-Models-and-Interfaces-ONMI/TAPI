**This is the release in progress of Transport API (TAPI) SDK. This SDK is being released under the Apache 2.0 license.**

The TAPI project is charted under the [LF Open Network Modeling and Interfaces](https://github.com/Open-Network-Models-and-Interfaces-ONMI/onmi-home) (ONMI) project, which is responsible for the development of this SDK as an Open Source project. 

**The SDK includes technology-agnostic interfaces to the following functional modules:**

- Topology Service
- Connectivity Service
- Path Computation Service
- OAM Service
- Fault Management Service
- Equipment Inventory Service
- Virtual Network Service
- Notification Service
- Streaming Service
- gNMI Streaming Service

**It also includes support for the following technology-specific interface profiles:**

- Photonic Media (L0-WDM)
- Optical Transport Network (L1-OTN)
- Carrier Ethernet (L2) 

**The SDK includes the following code components:**

- **_TAPI UML Information Model_** - The TAPI UML models are a ***normative*** part of the TAPI SDK and are the only source for subsequent generated TAPI SDK components (YANG, OAS, etc.).
  
  - These models are pruned/refactored from the [ONF Core Information Model](https://github.com/OpenNetworkingFoundation/CoreInfoModel)
  - Some of the UML model artifacts (e.g., Classes, Attributes, Types) that the TAPI contributors consider to be evolving are marked as ***experimental*** using the UML OpenModelProfile stereotypes. These artifacts could either become mature or *change/evolve* in future releases.
  - [Dump of the UML models in Microsoft Word format](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/tree/tapi-team-activities/UmlDumpFiles) generated through Eclipse Gendoc tool.

- **_TAPI YANG Schema_** - The TAPI YANG models are a ***normative part*** of the TAPI SDK.
  
  - The YANG specifications have been generated from the corresponding UML model using the [ONF EAGLE UML2YANG mapping tool](https://github.com/OpenNetworkingFoundation/EagleUmlYang) ("Tapi_v2x" branch) and further edited manually to comply with the [ONF IISOMI UML2YANG mapping guidelines](https://wiki.opennetworking.org/display/OIMT/IISOMI+Deliverables).
  - Status of YANG model artifacts can be determined by referring to the corresponding UML artifacts. As described in the UML models, some artifacts are considered *experimental*, and thus are the corresponding YANG artifacts.
  - The ONF TAPI release process does not guarantee backward compatibility of YANG models across major versions of TAPI releases. The YANG model backward compatibility criteria are outlined in section 11 of (https://tools.ietf.org/html/rfc7950). 

- **_TAPI OpenAPI Specification_** - TAPI OAS (OpenAPI Specifications) are an ***informative*** part of the TAPI SDK.
  
  - The OAS have been generated from the YANG data models included in this release using the [ONF EAGLE YANG2OAS](https://github.com/OpenNetworkingFoundation/EagleYangOpenAPI) tool following the RESTConf protocol specification (https://tools.ietf.org/html/rfc8040). This specification makes no assessment as to the level of RESTConf compliance of the TAPI REST APIs.

**The SDK includes the following documentation components ([drafts available here](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/tree/tapi-team-activities/TAPI-TEAM-ACTIVITIES)):**

- **_TAPI Reference Implementation Agreement (RIA TR-547)_**
  
  - This ONF Technical Recommendation (TR) provides a set of ***guidelines and recommendations*** for a standard use of the TAPI models in combination with the RESTCONF protocol for the implementation of the interface between network systems in charge of the control/management of networks based on WDM/OTN technologies.

- **_TAPI Reference Implementation Agreement for Streaming (RIA TR-548)_**
  
  - This document is a supplement to the TR-547, to explain TAPI streaming and provide a set of ***guidelines and recommendations*** for use of TAPI streaming.

- **_TAPI Alarm TCA List_** 

- **_TAPI Notification and Streaming Sequences_**

- **_TAPI Tooling Guidelines_**

