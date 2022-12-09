# ONF Open Transport API (TAPI)
This is the repository for the ONF Transport API (TAPI) SDK. This SDK is released under the Apache 2.0 license.

The ONF [Transport API](https://wiki.opennetworking.org/display/OTCC/TAPI) (TAPI) project charted under the [ONF Open Transport Configuration & Control](https://opennetworking.org/open-transport/) (OTCC) is responsible for the development of this SDK as an Open Source project. TAPI includes technology-agnostic interfaces to the following functional modules:
- Topology Service
- Connectivity Service
- OAM Service
- Path Computation Service
- Virtual Network Service
- Notification Service
- Equipment Inventory Service
- Streaming Service
- Fault Management

It also include support for the following technology-specific interface profiles
- Carrier Ethernet (L2)
- Optical Transport Network (L1-OTN)
- Photonic Media (L0-WDM)

The TAPI project delivers [SDKs releases](https://github.com/OpenNetworkingFoundation/TAPI/releases) periodically and includes the following components:
- ***TAPI UML Information Model*** - The TAPI UML models included in a TAPI SDK release are a **_normative_** part of the TAPI SDK and are the only source for subsequent generated TAPI SDK components (YANG, OAS, etc.).
  -  These models are pruned/refactored from the [ONF Core Information Model](https://github.com/OpenNetworkingFoundation/CoreInfoModel) 
   - Some of the UML model artifacts (e.g., Classes, Attributes, Types) that the TAPI contributors consider to be evolving are marked as ***experimental*** using the UML OpenModelProfile stereotypes.  These artifacts could either become mature or *change/evolve* in future releases.
- ***TAPI YANG Schema*** - The TAPI YANG models included in an TAPI SDK release are a ***normative*** part of the TAPI SDK.
   - The YANG specifications are generated from the corresponding UML model in the SDK release using the [ONF EAGLE UML2YANG mapping tool](https://github.com/OpenNetworkingFoundation/EagleUmlYang) and further edited manually to comply with the [ONF IISOMI UML2YANG mapping guidelines](https://wiki.opennetworking.org/display/OIMT/IISOMI+Deliverables). 
   - Status of YANG model artifacts can be determined by referring to the corresponding UML artifacts.  As described in the UML models, some artifacts are considered *experimental*, and thus are the corresponding YANG artifacts.
   - The ONF TAPI release process does not guarantee backward compatibility of YANG models across major versions of TAPI releases.  The YANG model backward compatibility criteria are outlined in section 11 of (https://tools.ietf.org/html/rfc7950).
- ***TAPI OpenAPI Specififcation*** - TAPI OAS (OpenAPI Specifications) included in an TAPI SDK release are an ***informative*** part of the TAPI SDK and are the _recommended_ REST API specifications to be used for TAPI interoperability based on a particular SDK release.
   - The OAS are generated from the YANG data models included in the corresponding SDK release using the [ONF EAGLE YANG2OAS](https://github.com/OpenNetworkingFoundation/EagleYangOpenAPI) tool following the RESTConf protocol specification (https://tools.ietf.org/html/rfc8040).  This specification makes no assessment as to the level of RESTConf compliance of the TAPI REST APIs.
   - Implementations may use other forms of REST APIs but must be based on the YANG models defined in the corresponding TAPI SDK release and are subject to implementation agreements between concerned parties for interoperability.
- ***TAPI Reference Implementation*** - the python code stubs for which are generated using the [Swagger Codegen](https://swagger.io/tools/swagger-codegen/)
- ***TAPI Implementation Guide*** - a PDF document providing an overview of the SDK.

Changes included in a TAPI release are listed in https://github.com/OpenNetworkingFoundation/TAPI/blob/develop/CHANGE_LOG/

In addition to the YANG, UML and OAS, two partly normative Reference Implementation Agreements,**_TR-547_** and **_TR-548_**, are available at https://wiki.opennetworking.org/display/OTCC/TAPI+Reference+Implementation+Agreements+and+other+Documentation

The Reference Implementation Agreements are supported by two associated documents (https://wiki.opennetworking.org/display/OTCC/TAPI+RIA+Associated+Documents)
- **_TAPI Alarm and TCA list_** at:
  - https://wiki.opennetworking.org/download/attachments/766218066/TAPI_Alarm_TCA_List.xlsx
- **_TAPI Notification and Streaming Sequences_** at:
  - https://wiki.opennetworking.org/download/attachments/766218066/TAPI_Notification_and_Streaming_Sequences.xlsx