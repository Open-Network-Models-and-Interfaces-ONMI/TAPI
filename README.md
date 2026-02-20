**This is the release version ***2.5.2*** of the Linux Foundation ONMI Project Transport API (TAPI) SDK
This SDK is being released under the Apache 2.0 license.**

The [LF TAPI](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI-Home) project is [chartered ](https://github.com/Open-Network-Models-and-Interfaces-ONMI/onmi-home/blob/main/ONMI-charter) under the LF Projects. [OMNI ](https://github.com/Open-Network-Models-and-Interfaces-ONMI/onmi-home/wiki) TAPI is responsible for the development of this SDK as an Open Source project. 

This [release](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/tree/v2.5.2) includes technology-agnostic interfaces to the following functional modules:
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

It also includes support for the following technology-specific interface profiles:
- Photonic Media (L0-WDM)
- Optical Transport Network (L1-OTN)
- Carrier Ethernet (L2)

The SDK includes the following components:
- **_TAPI UML Information Model_** - The TAPI UML models included in this TAPI release (v2.5.2) are a partially normative part of the TAPI SDK and are the only source for subsequent generated TAPI SDK components (YANG, OAS, etc.).
  - These models are pruned/refactored from the (formerly ONF) Core Information Model (ITU-T G.7711).
  - Some of the UML model artifacts (e.g., Classes, Attributes, Types) that the TAPI contributors consider to be evolving are marked as experimental using the UML OpenModelProfile stereotypes. These artifacts could either become mature or change/evolve in future releases.
  - Note that in earlier releases the UML was fully normative. Going forward it is expected that UML will be used solely as an aid for analysis. At this point the UML is still aligned with the YANG.

- **_TAPI YANG Schema_** - The TAPI YANG models included in this TAPI release (v2.5.2) are a normative part of the TAPI SDK.
  - The YANG specifications have been generated from the corresponding UML model using the [EAGLE UML2YANG mapping tool](https://github.com/Open-Network-Models-and-Interfaces-ONMI/onmi-iisomi-uml-yang) ("Tapi_v2x" branch) and further edited manually to comply with the [IISOMI UML2YANG mapping guidelines](https://github.com/Open-Network-Models-and-Interfaces-ONMI/onmi-iisomi-home).
  - Status of YANG model artifacts can be determined by referring to the corresponding UML artifacts. As described in the UML models, some artifacts are considered experimental, and thus are the corresponding YANG artifacts.
  - The TAPI release process does not guarantee backward compatibility of YANG models across major versions of TAPI releases. The YANG model backward compatibility criteria are outlined in section 11 of [RFC7950](https://tools.ietf.org/html/rfc7950).

- **_TAPI OpenAPI Specification_** - TAPI OAS (OpenAPI Specifications) included in this TAPI release (v2.5.2) are an informative part of the TAPI SDK.
  - The OAS have been generated from the YANG data models included in this release using the [EAGLE YANG2OAS](https://github.com/Open-Network-Models-and-Interfaces-ONMI/onmi-iisomi-yang-openapi) tool following the RESTConf protocol specification [RFC8040](https://tools.ietf.org/html/rfc8040). This specification makes no assessment as to the level of RESTConf compliance of the TAPI REST APIs.
  - Implementations may use other forms of REST APIs but must be based on the YANG models defined in this release and are subject to implementation agreements between concerned parties for interoperability.
  - The OAS has not been changed from the version released with TAPI release v2.5.0.

- [Documentation associated with this release](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI-Documentation/releases/tag/v2.5.2)

As the most deployed release of TAPI at this point is TAPI 2.1.3 (TIP recommended) a detailed differences between 2.1.3 and 2.5.2 can be obtained using
- https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/compare/v2.1.3...v2.5.2

As TAPI 2.5.x is also a TIP recommended release a detailed differences between 2.5.0 and 2.5.2 can be obtained using
- https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/compare/v2.5.0...v2.5.2

[**_HighLevelDiff_Tapi2.1.3To2.5.2.pdf_**](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI-Documentation/blob/v2.5.2/DeltaDocument/HighLevelDiff_Tapi2.1.3To2.5.2.pdf)  highlights the key changes from 2.1.3 to 2.5.2

**Summary of changes**
- Correction to remove "cofig false" YANG issue
- Addition of paginated get (experimental)
- String field restrictions relaxed to “any conformant YANG string” throughout. Explanation added in TR-547 section 2.8 String fields.
- Various minor improvements to documentation

## What's Changed
* Tapi 2 5 0 fixes by @nigel-r-davis in https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/pull/660
* YANG updates for 2.5.2 by @nigel-r-davis in https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/pull/664


**Full Changelog**: https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/compare/2.5.1...v2.5.2
