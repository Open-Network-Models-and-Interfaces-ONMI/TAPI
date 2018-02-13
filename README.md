# ONF Open Transport (SNOWMASS)
This is a repository for the ONF Transport API SDK. This SDK is being released under the Apache 2.0 license.

The ONF Transport API (TAPI) project charted under the [ONF Open Transport Configuration & Control](https://www.opennetworking.org/projects/open-transport/) (OTCC) is responsible for the development of this SDK as an Open Source project [SNOWMASS](https://www.opennetworking.org/projects/snowmass/). The TAPI SDK supports interfaces to the following functional modules:
- Topology Service
- Connectivity Service
- OAM Service
- Path Computation Service
- Virtual Network Service
- Notification Service

The SDK includes the following components:
- TAPI UML Information Model - which is pruned/refactored from the [ONF Core Information Model 1.2](https://www.opennetworking.org/images/stories/downloads/sdn-resources/technical-reports/TR-512_CIM_(CoreModel)_1.2.zip) 
- TAPI YANG Schema - which is generated using the [OSSDN EAGLE UML-to-YANG mapping tool](https://github.com/OpenNetworkingFoundation/EAGLE-Open-Model-Profile-and-Tools/tree/ToolChain/UmlYangTools)
- TAPI SWAGGER definitions - which is generated using the [OSSDN EAGLE YANG-to-JSON tool](https://github.com/OpenNetworkingFoundation/EAGLE-Open-Model-Profile-and-Tools/tree/ToolChain/YangJsonTools)
- TAPI Reference Implementation - the code stubs for which are generated using the [OSSDN EAGLE JSON-to-Python tool](https://github.com/OpenNetworkingFoundation/EAGLE-Open-Model-Profile-and-Tools/tree/ToolChain/JsonCodeTools)
- TAPI Development Guide - a PDF document providing an overview of the SDK.
