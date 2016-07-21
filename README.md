# ONF Open Transport (SNOWMASS)
This is a repository for the ONF Transport API SDK. This SDK is being released under the Apache 2.0 license.

The ONF Transport API (TAPI) project charted under the [ONF Open Transport Working Group] (https://www.opennetworking.org/technical-communities/areas/specification) (OTWG) is responsible for the development of this SDK as an Open Source SDN project [SNOWMASS] (http://opensourcesdn.org/projects/project-snowmass/). This release is based on [Functional Requirements for Transport API](https://www.opennetworking.org/images/stories/downloads/sdn-resources/technical-reports/TR-527_TAPI_Functional_Requirements.pdf) (June 2016 | TR-527) and supports interfaces to the following functional modules:
* Topology Service
* Connectivity Service
* Path Computation Service
* Virtual Network Service
* Notification Service

The SDK includes the following components:
* TAPI UML Information Model - which is pruned/refactored from the [ONF Core Information Model 1.1] (https://www.opennetworking.org/images/stories/downloads/sdn-resources/technical-reports/ONF-CIM_Core_Model_base_document_1.1.pdf) 
* TAPI YANG Schema - which is generated using the [OSSDN EAGLE UML-to-YANG mapping tool] (https://github.com/OpenNetworkingFoundation/EAGLE-Open-Model-Profile-and-Tools/tree/UmlYangTools)
* TAPI SWAGGER definitions - which is generated using the [OSSDN EAGLE YANG-to-JSON tool] (https://github.com/OpenNetworkingFoundation/EAGLE-Open-Model-Profile-and-Tools/tree/YangJsonTools)
* TAPI Reference Implementation - the code stubs for which are generated using the [OSSDN EAGLE JSON-to-Python tool] (https://github.com/OpenNetworkingFoundation/EAGLE-Open-Model-Profile-and-Tools/tree/JsonCodeTools)
* TAPI Development Guide - a PDF document providing an overview of the SDK.

