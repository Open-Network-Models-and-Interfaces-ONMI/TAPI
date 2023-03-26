This is the release version ***2.4.1*** of the ONF Transport API (TAPI) SDK. This SDK is being released under the Apache 2.0 license.

The ONF [Transport API](https://wiki.opennetworking.org/display/OTCC/TAPI) (TAPI) project charted under the [ONF Open Transport Configuration & Control](https://opennetworking.org/open-transport/) (OTCC) is responsible for the development of this SDK as an Open Source project. 

This release includes technology-agnostic interfaces to the following functional modules:
- Topology Service
- Connectivity Service
- Path Computation Service
- OAM Service
- Fault Management Service
- Equipment Inventory Service
- Virtual Network Service
- Notification Service
- Streaming Service

It also includes support for the following technology-specific interface profiles
- Photonic Media (L0-WDM)
- Optical Transport Network (L1-OTN)
- Carrier Ethernet (L2) 

The SDK includes the following components:

- **_TAPI UML Information Model_** - The TAPI UML models included in this TAPI release (v2.4.1) are a ***normative*** part of the TAPI SDK and are the only source for subsequent generated TAPI SDK components (YANG, OAS, etc.).
  - These models are pruned/refactored from the [ONF Core Information Model](https://github.com/OpenNetworkingFoundation/CoreInfoModel)
  - Some of the UML model artifacts (e.g., Classes, Attributes, Types) that the TAPI contributors consider to be evolving are marked as ***experimental*** using the UML OpenModelProfile stereotypes. These artifacts could either become mature or *change/evolve* in future releases.
  - [**_TapiGenDoc_v2.4.1.pdf_**](https://github.com/OpenNetworkingFoundation/TAPI/blob/develop/TapiGenDoc_v2.4.1.pdf)  is the dump of the whole UML model in Microsoft Word format, generated through Eclipse Gendoc tool.

- **_TAPI YANG Schema_** - The TAPI YANG models included in this TAPI release (v2.4.1) are a ***normative part*** of the TAPI SDK.
  - The YANG specifications have been generated from the corresponding UML model using the [ONF EAGLE UML2YANG mapping tool](https://github.com/OpenNetworkingFoundation/EagleUmlYang) ("Tapi_v2x" branch) and further edited manually to comply with the [ONF IISOMI UML2YANG mapping guidelines](https://wiki.opennetworking.org/display/OIMT/IISOMI+Deliverables).
  - Status of YANG model artifacts can be determined by referring to the corresponding UML artifacts. As described in the UML models, some artifacts are considered *experimental*, and thus are the corresponding YANG artifacts.
  - The ONF TAPI release process does not guarantee backward compatibility of YANG models across major versions of TAPI releases. The YANG model backward compatibility criteria are outlined in section 11 of (https://tools.ietf.org/html/rfc7950). YANG models included in this release are backward compatible with previous release 2.4.0.

- **_TAPI OpenAPI Specification_** - TAPI OAS (OpenAPI Specifications) included in this TAPI release (v2.4.1) are an ***informative*** part of the TAPI SDK.
  -  The OAS have been generated from the YANG data models included in this release using the [ONF EAGLE YANG2OAS](https://github.com/OpenNetworkingFoundation/EagleYangOpenAPI) tool following the RESTConf protocol specification (https://tools.ietf.org/html/rfc8040). This specification makes no assessment as to the level of RESTConf compliance of the TAPI REST APIs.
  -   Implementations may use other forms of REST APIs but must be based on the YANG models defined in this release and are subject to implementation agreements between concerned parties for interoperability.

- [**_TAPI Reference Implementation Agreement (RIA TR-547 2.1)_**](https://github.com/OpenNetworkingFoundation/TAPI/blob/develop/TR-547-TAPI%20Reference%20Implementation%20Agreement_v2.1.pdf)
  - This ONF Technical Recommendation (TR) provides a set of ***guidelines and recommendations*** for a standard use of the TAPI models in combination with the RESTCONF protocol for the implementation of the interface between network systems in charge of the control/management of networks based on WDM/OTN technologies.
- [**_TAPI Reference Implementation Agreement for Streaming (RIA TR-548 2.0)_**](https://github.com/OpenNetworkingFoundation/TAPI/blob/develop/TR-548-TAPI_ReferenceImplementationAgreement-Streaming_v2.0.pdf)
  - This document is a supplement to the TR-547, to explain TAPI streaming and provide a set of ***guidelines and recommendations*** for use of TAPI streaming.
 
The Reference Implementation Agreements are supported by two associated documents [(TAPI RIA Associated Documents):](https://wiki.opennetworking.org/display/OTCC/TAPI+RIA+Associated+Documents)
- [**_TAPI_Alarm_TCA_List_v2.1.0.xlsx_**](https://wiki.opennetworking.org/download/attachments/766218066/TAPI_Alarm_TCA_List_v2.1.0.xlsx?api=v2) 
- [**_TAPI Notification and Streaming Sequences_**](https://wiki.opennetworking.org/download/attachments/766218066/TAPI_Notification_and_Streaming_Sequences.xlsx?api=v2)

As the most deployed release of TAPI at this point is TAPI 2.1.3 a detailed differences between 2.1.3 and 2.4.1 can be obtained using
- [v2.1.3...v2.4.1](https://github.com/OpenNetworkingFoundation/TAPI/compare/v2.1.3...v2.4.1)

See also  [**_changelog_**](https://github.com/OpenNetworkingFoundation/TAPI/blob/develop/changelog.txt)

[**_HighLevelDiff_Tapi2.1.3To2.4.1.pdf_**](https://github.com/OpenNetworkingFoundation/TAPI/blob/develop/HighLevelDiff_Tapi2.1.3To2.4.1.pdf)  highlights the key changes from 2.1.3 to 2.4.1
