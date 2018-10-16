# Change Log
## Commit Range: v2.0.2..HEAD


* __Updated YANG date &amp; revision description text with 2.1 release notes__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 16 Oct 2018 14:01:02 -0400
    [08c387c3a269acabc7dbf77ff9d24411f1eb64f3](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/08c387c3a269acabc7dbf77ff9d24411f1eb64f3) 
    

* __v2.1.0 change-log updates for RC-3__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 3 Oct 2018 15:26:13 -0400
    [e520b4cdb58912ad0bdc9c326fad44f5e1fe55ea](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/e520b4cdb58912ad0bdc9c326fad44f5e1fe55ea) 
    

* __OAS updates due TAPI 2.1 YANG revision date change to 10/03/2018__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 3 Oct 2018 15:01:01 -0400
    [351a6e9d81465895221453d623fae17e15192500](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/351a6e9d81465895221453d623fae17e15192500) 
    

* __Updated TAPI 2.1 YANG revision date to 10/03/2018__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 3 Oct 2018 14:45:02 -0400
    [e8d4e7721925514dc7b0dffc27e7ab898d4ebf7c](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/e8d4e7721925514dc7b0dffc27e7ab898d4ebf7c) 
    

* __Fixes #354 as per TAPI 10/02/2018 call discussions__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 3 Oct 2018 10:45:32 -0400
    [bd3b965d9ade0708becdf71e0acec06f8cef1699](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/bd3b965d9ade0708becdf71e0acec06f8cef1699) 
    - Maintenance Entity has been removed
    - OamService will specify at least 2 OSEPs which has provisioning info for
    either
    -- 2 MEPs (OamService represents an MEG wholly contained in the domain)
    -- 1 MEP &amp; 1 MIP (OamService represents a segment of a MEG in an edge domain)
    -- 2 MIPs (OamService represents a segment of a MEG in a transit domain)
    - OamJob will specify at least 1 OSEP which points to an MEP
    - OSEPRelatesToMEP/MIP association navigability changed to one-way from OSEP to
    MEP/MIP
    - Added mepIdentifier and peerMepIdentifier attributes to OSEP
    - Added mipMac &amp; isFullMip attributes to Eth augmentation of MIP
    

* __Fix #356 - wrap &#34;uses grouping&#34; statement with a container for augments__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 1 Oct 2018 13:48:28 -0400
    [9d0b83c3692c937d0a80fe7699f4e6442afc472b](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/9d0b83c3692c937d0a80fe7699f4e6442afc472b) 
    

* __As per review comments, added spectrum property to OtsiConfig pac__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Fri, 28 Sep 2018 13:33:54 -0400
    [58678575923fd3c65e0233b7efd3f5b5ed0d47d6](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/58678575923fd3c65e0233b7efd3f5b5ed0d47d6) 
    - also fixed the descriptions for central-frequency &amp; frequency-constraint to
    remove ITU-T formula to calculate nominal-central-frequency based on channel
    spacing as this not used in TAPI anymore.

* __Partial Fixes to #351, #352 as per 09/25/2018 TAPI call agreements__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 26 Sep 2018 16:16:46 -0400
    [1af604d724e6bc93144aefacaf4366c7e2b0578b](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/1af604d724e6bc93144aefacaf4366c7e2b0578b) 
    - Renamed CentralFrequencyOrWavelength data-type to CentralFrequency
    - Renamed Spectrum data-type to SpectrumBand
    - Removed support for legacy definitions (m,n) of channel-number and 
    frequency-slot to compute CentralFrequency &amp; SpectrumBand
    - Refactored the frequency constraints properties of CentralFrequency
    (grid-type and adjustment-granularity) into a separate (new) data-type 
    FrequencyConstraint.
    - Added FrequencyConstraint property to CentralFrequency and SpectrumBand
    data-types
    - Renamed SpectrumType enumeration to PhotonicLayerQualifier
    - Added 2 additional ModulationTechniques: PAM4 &amp; PAM8
    - Clarified comments/descriptions for threshold/power configuration attributes

* __2.1.0 change log updates for RC-2__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Fri, 21 Sep 2018 16:59:04 -0400
    [8b96f486d3ae2d3c3bd1516362d309db7627d029](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/8b96f486d3ae2d3c3bd1516362d309db7627d029) 
    

* __Updated frequency unit to MHz in comments &amp; OpenModelAttr stereotype__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 19 Sep 2018 15:45:23 -0400
    [40bce8d5db61c2d95310d516e9db250b63207e9a](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/40bce8d5db61c2d95310d516e9db250b63207e9a) 
    - also removed associated value ranges for above also specified in 
    OpenModelAttribute stereotype

* __Photonic Model updates made on Tapi call 09/18/2018__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 18 Sep 2018 20:40:37 -0400
    [3e46fb3d32c32b0947aa0f169e081d3b2fa8549e](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/3e46fb3d32c32b0947aa0f169e081d3b2fa8549e) 
    - cleaned up TotalPowerThresholds attributes
    - updated OtsiTermonationPac to add selectedSpectrum and received Power. ALso
    removed the MediaChannelPac from OtsiCEP
    - updated MediaChannelPac to add measured ingress &amp; egress Power attributes
    - changed centralFrequency &amp; spectralWidth type to integer (from real) to be
    specified in MHz
    - removed C &amp; L BAND enum literals from GridType

* __Updated OAS specs using v1.2.2 yang2swagger-tapi-cli__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 17 Sep 2018 20:08:38 -0400
    [415d70f3b47a451bf490b4ee713fa69f87fd9c10](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/415d70f3b47a451bf490b4ee713fa69f87fd9c10) 
    

* __NOATION is merged with the latest notations from ONF__

    [Shrikanth Malavalli Divakar (COMMS-EGM)](mailto:SH386766@wipro.com) - Thu, 13 Sep 2018 14:55:25 +0200
    [c42c52f4e0999cc02ccc8e28d39919218c9500c0](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/c42c52f4e0999cc02ccc8e28d39919218c9500c0) 
    

* __Split the Laser Control type__

    [Shrikanth Malavalli Divakar (COMMS-EGM)](mailto:SH386766@wipro.com) - Tue, 11 Sep 2018 20:14:24 +0200
    [9da25348ef9d685d8c49c4dffe6a44ec61cc8afd](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/9da25348ef9d685d8c49c4dffe6a44ec61cc8afd) 
    

* __Initial commit of TAPI OAS files using new Eagle Yang2OpenAPI tool__

    [Karthik Sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 10 Sep 2018 15:43:51 -0400
    [a8a9111ec0c57c4e6ef9375f4cca975dc78b06cc](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/a8a9111ec0c57c4e6ef9375f4cca975dc78b06cc) 
    

* __Created new PAC to configure and read POWER Thresholds__

    [Shrikanth Malavalli Divakar (COMMS-EGM)](mailto:SH386766@wipro.com) - Mon, 10 Sep 2018 13:08:25 +0200
    [7d8ee276c1348636e0cb414389e4802cc0e457ba](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/7d8ee276c1348636e0cb414389e4802cc0e457ba) 
    

* __PhtoniceMedia missing parameters added by Telefonica__

    [Shrikanth Malavalli Divakar (COMMS-EGM)](mailto:SH386766@wipro.com) - Fri, 7 Sep 2018 17:27:59 +0200
    [e4e33cf6ef8c2fae61b4c118157ba3d26e6aa1ee](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/e4e33cf6ef8c2fae61b4c118157ba3d26e6aa1ee) 
    

* __Fix: TapiEth Yang validation errors- renamed Eth OAM attributes uniquely__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 5 Sep 2018 12:52:00 -0400
    [eb377cfbe41f41e970b599f21b60a0de2fa7fe3d](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/eb377cfbe41f41e970b599f21b60a0de2fa7fe3d) 
    

* __Yang tree files generated using latest pyang 1.7.5__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Fri, 31 Aug 2018 21:10:35 -0400
    [be4fdf3285c4d1b35853d7a48e5713b9a526a4f2](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/be4fdf3285c4d1b35853d7a48e5713b9a526a4f2) 
    

* __Fix #333: Aligned RoutingConstraints for Connectivity &amp; PathComputation__

    [217216X710581](mailto:217216X710581@WNCAOIP014L.na-idm.na-gad.nec.com) - Fri, 31 Aug 2018 18:31:38 -0400
    [97407700245d768903207ae8953e9642f5b210da](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/97407700245d768903207ae8953e9642f5b210da) 
    - Added RoutingConstraint attribute into ConnectivityService
    - Added TopologyConstraint attribute into PathComputationService
    - Deleted duplicate attributes (CostCharacteristics, LatencyCharacteristics,
    RiskCharacterstics) from ConnectivityConstraint class since these are also
    present in RoutingConstraint class
    - Added the RouteComputePolicy class/attributes into 
    TapiPathComputation:RoutingConstraint and removed from ConnectivityConstraint
    - Moved the TopologyConstraints class from TapiConnectivity into 
    TapiPathComputation model/module
    - Also updated PathServiceEndPoint to be consistent with 
    ConnectivityServiceEndPoint by adding layerProtocol and capacity attributes
    - updated Path class with layerProtocolName and direction attributes

* __Removed the TAPI Swagger folder/project. To be replaced with OAS folder__

    [Karthik Sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 30 Aug 2018 16:19:30 -0400
    [5afc4a432038afb54ee63e9fc9cf0d4ec5d146fa](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/5afc4a432038afb54ee63e9fc9cf0d4ec5d146fa) 
    - Following the recommendation from the OpenAPI Initiative for proper usage
    when referring to the OpenAPI Specifications

* __Added Digital Signal Types as an enumeration in TapiDsr model/module__

    [Karthik Sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 29 Aug 2018 16:30:00 -0400
    [35bd14c2f1b0e5f87aff636e8e55b4d5ee6524d0](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/35bd14c2f1b0e5f87aff636e8e55b4d5ee6524d0) 
    

* __Updated OduType to augment LayerProtocolQualifier__

    [Karthik Sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 29 Aug 2018 15:24:52 -0400
    [734fe4311e6670935d53d0366753c15c40193bff](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/734fe4311e6670935d53d0366753c15c40193bff) 
    - this results in OduType enum being mapped to identity in YANG

* __Old OTSi module has been replaced by Photonic Media__

    [Karthik Sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 20 Aug 2018 15:14:28 -0400
    [c3139b4c044a52b3af1ca3c7990b59dadd909836](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/c3139b4c044a52b3af1ca3c7990b59dadd909836) 
    

* __Class/Attribute rename based on 08/16/18 IMP-TAPI call &amp; github comments__

    [Karthik Sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 20 Aug 2018 15:13:24 -0400
    [89934699b5f3232f7f9e04766f67572a754cdd75](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/89934699b5f3232f7f9e04766f67572a754cdd75) 
    

* __Added associations CEPAggregatesCEPs, ConnectionSupportsClientLinks__

    [Karthik Sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 20 Aug 2018 14:33:31 -0400
    [828e8a9b7ba8c6c2c1cdc7ed2d75fb6a55cb0741](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/828e8a9b7ba8c6c2c1cdc7ed2d75fb6a55cb0741) 
    results in addition of following attributes
    - ConnectionEndPoint::_aggregatedConnectionEndPoint
    - Connection::_supportedClientLink
    
    Also based on 08/16/18 IMP-TAPI call flipped navigability for CSEPRelatesToCEP
    association. Results in
    - removal of ConnectionEndPoint::_connectivityServiceEndPoint
    - addition of ConnectivityServiceEndPoint::_connectionEndPoint

* __Initial draft of tree files generated from 2.1 yang files__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Fri, 10 Aug 2018 10:42:39 -0400
    [955a210696e3ccd2bd93870a664841031e329c82](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/955a210696e3ccd2bd93870a664841031e329c82) 
    

* __Initial draft of the Eth Yang files for release 2.1__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Fri, 10 Aug 2018 10:39:47 -0400
    [841c1043bd3e4102f836379fbe2f0dfe5b9ec1aa](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/841c1043bd3e4102f836379fbe2f0dfe5b9ec1aa) 
    

* __Xmi2Yang config file update for release 2.1__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 9 Aug 2018 17:28:37 -0400
    [67d5387d6d9aadc955b37ee02f13bb61e542de62](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/67d5387d6d9aadc955b37ee02f13bb61e542de62) 
    

* __Initial draft of the yang model of PhotonicMedia &amp; related UML fixes__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 9 Aug 2018 17:27:57 -0400
    [46527762f9907582bc7f350cacea47d820c9ecb2](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/46527762f9907582bc7f350cacea47d820c9ecb2) 
    

* __Misc Yang compilation bug fixes__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 9 Aug 2018 17:09:57 -0400
    [8b55c18e287f135e5824b649fec23e5ba61bbc7d](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/8b55c18e287f135e5824b649fec23e5ba61bbc7d) 
    

* __cleanup old yang file__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 9 Aug 2018 12:50:23 -0400
    [6decfa5271e6640df011a1ea46e63c98c3e0b1ae](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/6decfa5271e6640df011a1ea46e63c98c3e0b1ae) 
    

* __initial draft of oam yang files for release 2.1__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 9 Aug 2018 12:49:13 -0400
    [fbd729578e3c15c46dd770113f5e42a486eab81c](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/fbd729578e3c15c46dd770113f5e42a486eab81c) 
    

* __Initial draft of yang files for release 2.1__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 8 Aug 2018 19:20:57 -0400
    [8bf4e859a607ac2ab5ccd42bb5c606d139fa05fe](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/8bf4e859a607ac2ab5ccd42bb5c606d139fa05fe) 
    

* __Added enum literals MHz, Ghz to Capacity for photonic support__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 8 Aug 2018 15:26:26 -0400
    [7d6423c3b5958d671a167e7196908cef8d3ddba1](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/7d6423c3b5958d671a167e7196908cef8d3ddba1) 
    

* __Added added McAssembly Spec &amp; power/laser Pac classes__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 8 Aug 2018 15:25:07 -0400
    [8d393ee74f0503f9afd1bab119b49b069a953b19](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/8d393ee74f0503f9afd1bab119b49b069a953b19) 
    

* __Updated OamJob to be operated on OSEP ordered-pair instead of ME__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 8 Aug 2018 12:35:52 -0400
    [fc39c9d53a3284eb748f95801328e179e9a19f5b](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/fc39c9d53a3284eb748f95801328e179e9a19f5b) 
    - this updated is based on feedback from MEF OAM discussions

* __Updated model as per TAPI calls discussions (Aug 29, 2018 week)__

    [Karthik Sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 7 Aug 2018 08:02:48 -0400
    [a34af14e62fdb26d25263b98b8d0055ed9366d16](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/a34af14e62fdb26d25263b98b8d0055ed9366d16) 
    - renamed and updated Service constructs: OtsiSIPSpec, McSIPSpec, OtsiCSEPSpec,
    SmcCSEPSpec, NmcCSEPSpec
    - added occupiedSpectrum attribute to McPoolCapabilityPac
    - added MediaChannelConfigPac (requestedSpectrum attribute) to CSEPs
    - renamed OtsiACEPSpec to OtsiGCEPSpec, OtsiCEPSpec to OtsiNmcCEPSpec
    - added McCEPSpec classes: SmcCEPSpec, NmcCEPSpec, OmsCEPSpec, OtsCEPSpec with
    MediaChannelCtpPac.occupiedSpectrum attribute

* __Fixed a typo with multiplicity of SIP.suportedLayerQualifier__

    [Karthik Sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 7 Aug 2018 07:14:06 -0400
    [c49c6b54d81eac39591607d6f7a3792d65d6e1f0](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/c49c6b54d81eac39591607d6f7a3792d65d6e1f0) 
    

* __Updates for MEF NRM OAM__

    [amazzini](mailto:mazzini64@tiscali.it) - Wed, 25 Jul 2018 17:26:08 +0200
    [1e889b1fa1c152784049d45d24a3a23550cf5f83](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/1e889b1fa1c152784049d45d24a3a23550cf5f83) 
    Added suspectIntervalFlag, oamJob, measurementInterval and TCA severity 
    attributes to TcaInfo class Added isTransient attribute to PmThresholdData
    class

* __Eclipse/Papyrus Photon Migration - fixed role-reversal in TAPI diagrams__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 19 Jul 2018 17:18:43 -0400
    [4c35fbda3d9b412214cdad3ac7bc9c27fb08c334](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/4c35fbda3d9b412214cdad3ac7bc9c27fb08c334) 
    

* __First complete draft of Ethernet operations__

    [amazzini](mailto:mazzini64@tiscali.it) - Wed, 18 Jul 2018 23:59:26 +0200
    [ce7ca9916d524bd76d9e79b53653dadc5e2d1c26](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/ce7ca9916d524bd76d9e79b53653dadc5e2d1c26) 
    

* __Tapi Call 20180717, renamed TapiOtsi to TapiPhotonicMedia__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 17 Jul 2018 18:32:47 -0400
    [7c94638546c6501420cc764209ab4c80179eeda9](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/7c94638546c6501420cc764209ab4c80179eeda9) 
    - this module has specifications for all photonic sub-layers including OTSi,
    OTSiA, NMC, NMCA, SMC, SMCA, OMS, OTS, etc

* __- added supportedCepLayerProtocolQualifier (list) to NEP__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 17 Jul 2018 18:30:10 -0400
    [525c460c0d957b98fa37f7ea2bf9fa50cb42da43](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/525c460c0d957b98fa37f7ea2bf9fa50cb42da43) 
    

* __Added LayerProtocolQualifier attribute to CSEP, CEP__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 17 Jul 2018 18:29:53 -0400
    [ac2bb2fd1a717736d7e14576b0fed774d9da3af7](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/ac2bb2fd1a717736d7e14576b0fed774d9da3af7) 
    - also re-added sharedRiskCharacteristic attribute to ConnectivityConstraint
    - renamed the layerProtocolName attribute in ResilienceConstraint to 
    preferredRestorationLayer to avoid attribute-name clash with 
    ConnectivityConstraint
    

* __Updated LayerProtocolName to move out existing &#39;sub-&#39; LayerProtocolNames__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 17 Jul 2018 17:50:36 -0400
    [e746cec56c0440e592b74dd63e7865e54f658409](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/e746cec56c0440e592b74dd63e7865e54f658409) 
    - Values moved: OTSiA, OCH, OTU &amp; ETY
    - A LayerProtocolQualifier enumeration is to be used to qualify the sub-layers
    (if applicable) for a specific LayerProtocol.
    - This extensible enumeration is intentionally empty in the common module and
    will be augmented with layer-specific qualifier values in the respective
    technology-specific modules. Examples:
    - LayerProtocolName := OPTICAL_DATA_UNIT LayerProtocolQualifier := &#34;ODU_FLEX&#34;,
    &#34;ODU_0&#34;, &#34;ODU_1&#34;, &#34;ODU_2&#34;,
    &#34;ODU_2E&#34;, &#34;ODU_3&#34;, &#34;ODU_4&#34;&#34;, &#34;ODU_CBR&#34;&#34;, &#34;ODU_GFP&#34;&#34;, etc
    - LayerProtocolName := DIGITAL_SIGNAL_RATE LayerProtocolQualifier := &#34;GBE&#34;,
    &#34;10_GBE_WAN&#34;, &#34;100_GBE&#34;, &#34;FC_100&#34;,
    &#34;FC_200&#34;, &#34;STM_64&#34;, &#34;STM_256&#34;, &#34;OC_3&#34;, &#34;OC_12&#34;, etc
    - LayerProtocolName := PHOTONIC_MEDIA LayerProtocolQualifier := OCH, OTSi,
    OTSiA, NMC, NMCA, SMC, SMCA, OMS, OTS, etc

* __Papyrus bug: Fixed Specify association source &amp; target pointers__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 17 Jul 2018 17:44:49 -0400
    [3115bceda7457c67eb756bf21bc97876a4924de7](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/3115bceda7457c67eb756bf21bc97876a4924de7) 
    

* __Updates to the TAPI &amp; ETH OAM to support Threshold &amp; Bins__

    [Karthik Sethuraman](mailto:karthik.sethuraman@necam.com) - Fri, 13 Jul 2018 20:43:36 -0400
    [ee56b0b04c3fcb379f075ab3836d2f8bed45c286](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/ee56b0b04c3fcb379f075ab3836d2f8bed45c286) 
    

* __Update README.md__

    [Jeff Groom](mailto:jgroom@ciena.com) - Mon, 2 Jul 2018 07:55:54 -0600
    [9ddde4375e576eb5fc5012bbcdc41ca901f6e1eb](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/9ddde4375e576eb5fc5012bbcdc41ca901f6e1eb) 
    

* __Initial updates to OTSi model after Photonic Media model considerations__

    [Karthik Sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 27 Jun 2018 17:54:23 -0400
    [a4ba641b9f9365827390c5cb4abe52ad5fc89007](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/a4ba641b9f9365827390c5cb4abe52ad5fc89007) 
    

* __Renamed MeasurementJobControl.mepId as controller/responder MepId__

    [Karthik Sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 25 Jun 2018 11:20:32 -0400
    [4b289470767d99ee0eff2ad1a5b1cd853da019ab](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/4b289470767d99ee0eff2ad1a5b1cd853da019ab) 
    

* __Renamed MeasurementJobControl.mepId as controller/responder MepId__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 18 Jun 2018 22:19:32 -0400
    [161596281fa01c1b46310ba22f5d6e74ce8accac](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/161596281fa01c1b46310ba22f5d6e74ce8accac) 
    

* __Moved megIdentifier attribute to Meg, added creationTime to OamJob__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 18 Jun 2018 22:14:48 -0400
    [9e39855a4f7da2d78023526e65f1287ac7e7cc50](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/9e39855a4f7da2d78023526e65f1287ac7e7cc50) 
    

* __Fix Issue #317__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 12 Jun 2018 09:53:24 -0400
    [dd60d9aed11ed82b2df8b9ab9bd4b971859b904f](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/dd60d9aed11ed82b2df8b9ab9bd4b971859b904f) 
    

* __Migrated to OpenModelProfile 0.2.14, OpenInterfaceModelProfile 0.0.9__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 6 Jun 2018 14:25:43 -0400
    [6f54b809bfa85fc4100ad20ca81448c2c43a46b8](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/6f54b809bfa85fc4100ad20ca81448c2c43a46b8) 
    

* __Fixed unintended extensible-enumerations by setting isLeaf=true__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 31 May 2018 11:21:01 -0400
    [06f4827c78a11c2bd9654b6c436734adf7deefd5](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/06f4827c78a11c2bd9654b6c436734adf7deefd5) 
    

* __Migrated to OpenModelProfile 0.2.13, OpenInterfaceModelProfile 0.0.8__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 30 May 2018 16:16:00 -0400
    [5134c5bb7af8be72186541304e3ff412ca1fcb48](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/5134c5bb7af8be72186541304e3ff412ca1fcb48) 
    

* __Updated &amp; simplified the 8052-based ProActive and OnDemand Job Specs__

    [Karthik Sethuraman](mailto:karthik.sethuraman@necam.com) - Fri, 25 May 2018 16:26:56 -0400
    [42a4e8c192ac5fb1ff409466dcfa257190e394e4](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/42a4e8c192ac5fb1ff409466dcfa257190e394e4) 
    

* __Support for OamJob, Current/History PmData based on Q.822/X.739__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 24 May 2018 11:33:48 -0400
    [d82263392fa2eaefd04ba5f3cbc45eaccc7c323d](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/d82263392fa2eaefd04ba5f3cbc45eaccc7c323d) 
    

* __Added new DataTypes TimePeriod (X.739), TimeInterval (Q.821)__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 24 May 2018 10:21:46 -0400
    [8dab8e8a4eabbde4d8c8332e11d5955cc904529d](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/8dab8e8a4eabbde4d8c8332e11d5955cc904529d) 
    

* __Initial TAPI OAM Updates based on ITU-T G.8052 OAM__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 15 May 2018 13:19:50 -0400
    [d042975e47ddd2797627e2f5284f0e78989b26d0](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/d042975e47ddd2797627e2f5284f0e78989b26d0) 
    

* __removing constrain from SIP list. fixes OpenNetworkingFoundation/TAPI#304__

    [Bartosz Michalik](mailto:Bartosz.Michalik@amartus.com) - Wed, 21 Mar 2018 10:46:08 +0100
    [874e7a3f311d915d692b27fcbd24032c89064f00](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/874e7a3f311d915d692b27fcbd24032c89064f00) 
    


