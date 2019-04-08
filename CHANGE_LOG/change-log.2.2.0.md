# Change Log
## Commit Range: 2.1.1..HEAD

__[minor typo fix](https://github.com/OpenNetworkingFoundation/TAPI/commit/7c4372f17f5b344bce50f96121995ac564b1b691)__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 8 Apr 2019 16:06:28 -0400
    EAD -&gt; refs/heads/develop, refs/remotes/origin/develop
    

__[YANG and TREE file updates for UML commits since commit #8a59a68](https://github.com/OpenNetworkingFoundation/TAPI/commit/c0dc9f30c0936999be5cfa814163261b70bd7f1a)__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 8 Apr 2019 15:55:06 -0400
    
    

__[Temporarily removing LLDP model for TAPI 2.2 generation](https://github.com/OpenNetworkingFoundation/TAPI/commit/bc6e2e36ea8414c3c2d4615aa9142d5447efae19)__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 8 Apr 2019 15:53:03 -0400
    
    

__[Refactored TapiCommon::ObjectType to move enum-literals to approp models](https://github.com/OpenNetworkingFoundation/TAPI/commit/f79be5d388300a24ef96bf55ce0260cbf87dfb6d)__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 8 Apr 2019 15:51:20 -0400
    
    

__[Minor diagram adjustments and comments.](https://github.com/OpenNetworkingFoundation/TAPI/commit/5bdd621728f8e854f0ec778730b1665c9ec78abe)__

    [amazzini](mailto:mazzini64@tiscali.it) - Mon, 8 Apr 2019 18:24:32 +0200
    
    

__[Further TAPI Eth enhancements according to MEF NRM OAM project](https://github.com/OpenNetworkingFoundation/TAPI/commit/8fa859516491256cb66d22102e2e01c185570ced)__

    [amazzini](mailto:mazzini64@tiscali.it) - Sat, 6 Apr 2019 02:15:14 +0200
    
    TAPI Ethernet, added totalCountersFarEndLmParameters, 
    totalCountersNearEndLmParameters attributes to EthProActiveLmPerformanceData.
    Added totalCountersNearEnd1LmParameters attribute to
    EthProActive1LmPerformanceData class.
    
    TAPI Ethernet, added flrAvailabilityDeltaTime, flrAvailabilityThreshold, 
    flrAvailabilitySamples to EthMeasurementJobControlCommon.
    
    TAPI Ethernet, StatisticalLmPerformanceParameters class, uas attribute renamed
    as unavailableIntervals, ses attribute renamed as hliCount.
    
    Tapi Ethernet, EthPmParameterName enum, SEVERE_ERRORED_SECONDS replaced with
    HIGH_LOSS_INTERVALS, UNASSIGNED_ERRORED_SECONDS replaced with 
    UNAVAILABLE_INTERVALS.
    

__[TAPI Ethernet, added min/max/average Inter Frame Delay Variation](https://github.com/OpenNetworkingFoundation/TAPI/commit/6d8ca4fb3a2fc5bc0a3fc64af47e2aa3df1565f4)__

    [amazzini](mailto:mazzini64@tiscali.it) - Fri, 5 Apr 2019 17:08:39 +0200
    
    TAPI now supports both Y.1563 and G.8013/Y.1731 frame delay variation flavors.

__[Related to previous commit](https://github.com/OpenNetworkingFoundation/TAPI/commit/6ca3339394a29abd4d3a2d70f460d94d5e0356f1)__

    [amazzini](mailto:mazzini64@tiscali.it) - Fri, 5 Apr 2019 17:05:45 +0200
    
    

__[Updated Topology Constraints and Routing Constraints](https://github.com/OpenNetworkingFoundation/TAPI/commit/eb5ff71bfef4a75da0171ed5ca7b4b15601fba06)__

    [amazzini](mailto:mazzini64@tiscali.it) - Fri, 5 Apr 2019 17:04:50 +0200
    
    TAPI Path Computation, added tolerableImpact attribute to RoutingConstraint
    class. TAPI Path Computation, Removed routeDirection attribute from 
    RoutingConstraint class. TAPI Connectivity, added a comment to serviceLevel
    attribute of ConnectivityConstraint class. TAPI Path Computation, refactored
    TopologyConstraint and added constraintWeight attribute. TAPI Path Computation,
    added layerProtcolName and direction to PathComputationService class. TAPI
    Connectivity, moved layerProtocolName and direction from ConnectivityConstraint
    to ConnectivityService class.
    

__[Changed the multiplicity of Equipment::expectedEquipment to list](https://github.com/OpenNetworkingFoundation/TAPI/commit/257c14e3a580abd162eb00b79521b220ce0aa1bb)__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 4 Apr 2019 09:41:14 -0400
    
    

__[Minor Eqpt model changes as per TAPI call (4/2/19) decisions](https://github.com/OpenNetworkingFoundation/TAPI/commit/f71c14877cca766c58f044ccfccb6fe02a29cd32)__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 4 Apr 2019 09:39:23 -0400
    
    - removed the ActualEquipment:actualHolder attribute
    - changed the

__[Updated the Photonic model as per TAPI call (4/2/19) decisions](https://github.com/OpenNetworkingFoundation/TAPI/commit/19aad4873ea440492a7beb3238bcfe825ec4207e)__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 4 Apr 2019 09:34:17 -0400
    
    - Updated the PhotonicLayerQualifier enum
    - removed the MediaChannelAssemblySpec and OtsConnectionEndPointSpec
    - renamed the OtsiGServerAdaptationPac to OtsiServerAdatationPac

__[OAM and Ethernet small enhancements](https://github.com/OpenNetworkingFoundation/TAPI/commit/3c2ad2f91aea3075c4e2ac94932e0486b4c4212c)__

    [amazzini](mailto:mazzini64@tiscali.it) - Tue, 2 Apr 2019 11:32:23 +0200
    
    TAPI Eth, typo in EthPmParameterName (SEVERE_ERRORED_SECONDS) TAPI OAM, added
    to PmParameter (used in threshold config &amp; notif) an additional positive
    integer, the bin number.

__[Photonic Power Model: Uml updates to align with committed Yang](https://github.com/OpenNetworkingFoundation/TAPI/commit/be148f59da47e4f14f5c5d2c2a0e449101ff38d2)__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Fri, 29 Mar 2019 17:53:11 -0400
    
    - Refactored PowerPropertiesPac, LaserPropertiesPac &amp; FecPropertiesPac classes
    to complex data-type
    - Added PowerManagementCapabilityPac and PowerManagementConfigPac classes
    - Added powerManagementCapability attribute to the OtsiSIPSpec and 
    MediaChannelSIPSpec
    - Added powerManagementConfig attribute to the MediaChannelCSEPSpec
    - Minor re-ordering of few Yang RPC augment statements due to tool generation
    - removed Link augment statement for power-loss-characteristic as 
    TransferTimingPac in Topology has lossCharactersistic which can be used for
    now. The TopologyPacs are expected to be enhanced soon

__[TapiEqpt YANG/TREE files &amp; UML model updates to generate proper YANG](https://github.com/OpenNetworkingFoundation/TAPI/commit/1142e7dabfca188304072b8f9c891c1937710ebd)__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 28 Mar 2019 11:05:40 -0400
    
    Main Changes to UML include
    - adding Global/Local class as parent to all TapiEqpt classes
    - specifying partOfObjectKey values
    - specifying &lt;StrictComposite&gt; stereotypes
    - specifying isReadOnly=true
    - adding Augment classes for supporting PysicalSpan &amp; AccessPort

__[Minor fixes - specified objectKey for ThresholdParameter](https://github.com/OpenNetworkingFoundation/TAPI/commit/7bfbe37a56d08bb77763b70ddc8545097bce61bd)__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Sat, 23 Mar 2019 16:17:51 -0400
    
    

__[Yang/tree files updates related to PRs #403 &amp; #405](https://github.com/OpenNetworkingFoundation/TAPI/commit/7a6ab54dc01693f1b7b11dc7da81096200716aad)__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Sat, 23 Mar 2019 16:17:12 -0400
    
    

__[Replaced NodeAggregatesNEP with TopologyAggregatesNEP](https://github.com/OpenNetworkingFoundation/TAPI/commit/cf39147b85ce88174bd5b62a98b0fef361cf8367)__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 21 Mar 2019 19:58:01 -0400
    
    

__[Equipment model refactored as per agreement in Sydney.](https://github.com/OpenNetworkingFoundation/TAPI/commit/ece9abb76bcb62d472d295f4506712c030b8ad4a)__

    [Nigel Davis](mailto:ndavis@ciena.com) - Thu, 21 Mar 2019 17:38:22 +0000
    
    

__[Minor corrections.](https://github.com/OpenNetworkingFoundation/TAPI/commit/0a37fda1b0d6ab4b0051e7d39b7e312877490503)__

    [Nigel Davis](mailto:ndavis@ciena.com) - Thu, 21 Mar 2019 14:14:30 +0000
    
    

__[Change to DataTypes and addition of device.](https://github.com/OpenNetworkingFoundation/TAPI/commit/e5afa4a5ce3d8e488314f9e7e5b7409663801143)__

    [Nigel Davis](mailto:ndavis@ciena.com) - Thu, 21 Mar 2019 14:00:37 +0000
    
    

__[Alarm/Tca Updates for consistent ThresholdProfile alignment](https://github.com/OpenNetworkingFoundation/TAPI/commit/f16537eb1e9401a4f4055d4379f47bfdf5aaf1b6)__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 21 Mar 2019 01:27:14 -0400
    
    - Moved ObjectTypes enumeration to TapiCommon mdoel/module
    - Moved the Alarm/TCA info classes from TapiNotification to TapiOam 
    model/module which now augment TAPI Notification class (instead of composition)
    - Defined new TapiOam extensible enumerations - AlarmConditionName &amp; 
    PmParameterName for tighter typing (Identity instead of String)
    - Defined new TapiOam data-type - PmParameter that has PmParameterName
    (Identity) and choice different value types (need to be modeled by union in
    future)
    - Defined new TapiOam data-type - ThresholdParameter that has PmParameter,
    ThresholdCrossingType, ThresholdCrossingQualifier
    - The ThresholdParameter is used in both PmThresholdData (OamProfile) and
    ThresholdCrossingAlert (Notification)
    - Augmented TapiEth PmParameterName for G.8052 PmParameter (Statistical LM/DM)
    attributes
    - Deleted the TapiEth ThresholdData augments (both spec &amp; interfaces) &amp; related
    diagrams

__[Changes to figure](https://github.com/OpenNetworkingFoundation/TAPI/commit/16b92274e153bddbf4767db5a8695486f68010af)__

    [Nigel Davis](mailto:ndavis@ciena.com) - Wed, 20 Mar 2019 02:10:23 +0000
    
    

__[Updates to include strand](https://github.com/OpenNetworkingFoundation/TAPI/commit/7ba0f269318a397e52ae547cfaea5d8dcbb3a78f)__

    [Nigel Davis](mailto:ndavis@ciena.com) - Mon, 18 Mar 2019 22:35:55 +0000
    
    

__[Latest updates accounting for discussion at meeting](https://github.com/OpenNetworkingFoundation/TAPI/commit/d92940ee83a25b6a875f77f5db5fe457f5e4c944)__

    [Nigel Davis](mailto:ndavis@ciena.com) - Sat, 16 Mar 2019 05:42:21 +0000
    
    

__[Synchronized TAPI UML &amp; YANG - mostly updated &lt;specify&gt; target values](https://github.com/OpenNetworkingFoundation/TAPI/commit/693a043ff0a278387dd644881e413ad67f495880)__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 12 Mar 2019 21:08:34 -0400
    
    

__[Bug Fix: Updated UML files to fix yang generation errors](https://github.com/OpenNetworkingFoundation/TAPI/commit/1d253055de2c5c4290b8180067efa8ebc01434a1)__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 11 Mar 2019 18:58:35 -0400
    
    - mainly updated the &lt;specify&gt; stereotype&#39;s target to properly point to 
    augmented node.

__[OAM, Eth and LLDP modifications](https://github.com/OpenNetworkingFoundation/TAPI/commit/33f11f8074822191c5a1a6d8b9921534cdb209b2)__

    [amazzini](mailto:mazzini64@tiscali.it) - Fri, 8 Mar 2019 19:06:49 +0100
    
    - OAM, updated association label _oamServicePoint of OamJob class (it was still
    _oamServiceEndPoint)
    - Eth, some adjustments or current and history data specify labels
    - LLDP, draft model
    

__[Fix #378: Made the TopologyConstraint attributes configurable](https://github.com/OpenNetworkingFoundation/TAPI/commit/4aef91ce0eca7620432747a745da70bdb4aeb7b1)__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 4 Mar 2019 09:31:05 -0500
    
    - also specified containers for Connectivity constraints attributes

__[Removed yang/tree files named with v2.1.1 release date](https://github.com/OpenNetworkingFoundation/TAPI/commit/16d26c5a0440ec7f9b1f8816d44d55956d69d2bc)__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Fri, 1 Mar 2019 16:52:23 -0500
    
    

__[Updated yang/tree file names &amp; revision with planned v2.2.RC1 date](https://github.com/OpenNetworkingFoundation/TAPI/commit/7d3658cbca3e6987b5962b69cdd97b0f2938cf6f)__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Fri, 1 Mar 2019 16:49:56 -0500
    
    

__[Initial draft of yang/tree files generated from committed v2.2 uml files](https://github.com/OpenNetworkingFoundation/TAPI/commit/b0df54cf2e7f1314438f4664ce77e6fcb0487432)__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Fri, 1 Mar 2019 12:56:20 -0500
    
    - excludes EQPT and LLDP features as they are not mature enough

__[Non-configurable subscription filters in Data API objects](https://github.com/OpenNetworkingFoundation/TAPI/commit/e605f2282d2d6272e46ac4adbe74b4a2b62596db)__

    [Arturo Mayoral](mailto:arturo.mayoral.ext@telefonica.com) - Wed, 27 Feb 2019 18:36:07 +0100
    
    The following objects within:
    
    tapi-notification:notification-context/tapi-notification:notif-subscription-filter
    
     - requested-notification-types
    - requested-object-types
    - requested-layer-protocols
    - requested-object-identifier
    - include-content
    
    Has been modified to be configurable.
    

__[ODU OAM enhancements:](https://github.com/OpenNetworkingFoundation/TAPI/commit/39cc8c2c2a66d3d3f44d8a937519b6eb30ab2545)__

    [amazzini](mailto:mazzini64@tiscali.it) - Wed, 27 Feb 2019 12:35:53 +0100
    
    TAPI ODU, added oduMegSpec with megLevel attribute, added codirectional 
    attribute to OduTcmMipPac class.

__[Several enhancements to ETH model:](https://github.com/OpenNetworkingFoundation/TAPI/commit/faeedb9d5ff3c57485f9634eb2528d0e82edcea3)__

    [amazzini](mailto:mazzini64@tiscali.it) - Wed, 27 Feb 2019 12:33:57 +0100
    
    TAPI Eth, added EthProActive1DmSourcePerformanceData and 
    EthProActive1LmSourcePerformanceData to pro-active and on demand dual ended
    jobs. TAPI Eth, All PmParameters of Pro-active jobs have been added to 
    On-demand jobs. Renamed almost all attribute names of 
    EthProAct/OnDemandPerformanceData classes. TAPI Eth, added
    get/getList/create/update EthConnectivityService with its
    EthConnectivityServiceEndPointSpec TAPI Eth, added get/getList
    EthServiceInterfacePointSpec TAPI Eth, get/getList/create/update OamJob, added 
    EthOamMep/MipServicePoint augments. TAPI Eth, added BandwidthProfile data type,
    which now extends the Capacity data type defined n TAPI Common. TAPI Eth, all
    augments of operations are split in input/ouput targets. TAPI Eth, added
    megLevel to EthMegCommon class.

__[Several enhancements:](https://github.com/OpenNetworkingFoundation/TAPI/commit/bc1f5388d6d2fa2579eba6d67dac9e5be0cf3b2b)__

    [amazzini](mailto:mazzini64@tiscali.it) - Wed, 27 Feb 2019 12:30:33 +0100
    
    TAPI Common, removed BandwidthProfile data type and removed the reference to it
    from Capacity data type. TAPI OAM, create/update/delete/get OamServiceEndPoint,
    removed the
    “End”, reviewed all parameters of the operations. TAPI OAM, moved
    granularityPeriod and suspectIntervalFlag from TAPI CurrentData and HistoryData
    to a PM dedicated package (e.g. PmDataPac), because these two attributes are
    meaningless e.g. in Link Trace job case. TAPI OAM, Removed PmDataBin class. 
    TAPI OAM, removed mepIdentifier and peerMepIdentifier parameters from 
    createOamServicePoint. TAPI OAM, createOamJob, removed oamServicePoint input
    parameter, replaced by oamServiceId and oamServicePointId string parameters. 
    TAPI OAM, moved layerProtocolName attribute from OamConstraint to OamService
    class. Deleted direction attribute of OamConstraint class. Moved megLevel
    attribute from OamConstraint to technology specific MEGs. Removed OamConstraint
    class. TAPI OAM, removed direction attribute from OamServicePoint, Meg and Mep 
    classes. TAPI OAM, updated oamService and OamServicePoint operations according
    to above modifications.
    

__[Properties tidied up Properties are either in main classes of a few pacs.](https://github.com/OpenNetworkingFoundation/TAPI/commit/0524f19e5df9c5607b22b9b7578dfef0b40d88c3)__

    [Nigel Davis](mailto:ndavis@ciena.com) - Tue, 26 Feb 2019 16:59:51 +0000
    
    

__[LLDP Model: Highlighting Tx and Rx Parameters](https://github.com/OpenNetworkingFoundation/TAPI/commit/5387da7809e6db6488b07a591ae109f4a49bbe26)__

    [Bernd Zeuner](mailto:b.zeuner@telekom.de) - Tue, 26 Feb 2019 17:13:22 +0100
    
    Tx and Rx parameters are highlighted in the LldpDetails class diagram.

__[Minor updates during TAPI call 20190226](https://github.com/OpenNetworkingFoundation/TAPI/commit/57686fecec40634206670b04fcc37b8efdea48a5)__

    [Nigel Davis](mailto:ndavis@ciena.com) - Tue, 26 Feb 2019 15:51:03 +0000
    
    

__[Minor fixes](https://github.com/OpenNetworkingFoundation/TAPI/commit/d8587bea593c902f7f9f68f01c154aaf70739e61)__

    [Arturo Mayoral](mailto:arturo.mayoral.ext@telefonica.com) - Tue, 26 Feb 2019 16:35:44 +0100
    
    - Power-spectral-density config false was removed. This affect to previous
    paramter definitions.
    - Tree model is refractored from latest verison of the YANG file.
    

__[Issue #353 - Power management for NMC service provisioning](https://github.com/OpenNetworkingFoundation/TAPI/commit/55dcc9b1647f005c986acf3a47a3c61eff123cad)__

    [Arturo Mayoral](mailto:arturo.mayoral.ext@telefonica.com) - Tue, 26 Feb 2019 14:34:09 +0100
    
    This commit includes extensions to the tapi-photonic-media information model.
    Specifically, OTSi and Media Channel Service Interface Points (SIPs) are
    extended with capability information of the operational power range asociated
    to the related LTPs. On the other hand, the MC Connectivity Service End-Points
    (CSEPs) are extended with a set of power management constrains which can be
    configured at the connectivity service creation to denote intent-like soft
    constrains. Moreover, this commit includes an extension for photonic-media
    links which includes the expected power loss as a state characteristic to be
    specified by the TAPI server.
    

__[Initial pruning of properties from core](https://github.com/OpenNetworkingFoundation/TAPI/commit/a4ce86988e41063fc538e3b24b5b61b53eb85680)__

    [Nigel Davis](mailto:ndavis@ciena.com) - Tue, 26 Feb 2019 11:19:06 +0000
    
    

__[Pin model updated to include attribute.](https://github.com/OpenNetworkingFoundation/TAPI/commit/926ae806ad42590a7034d018767e08476c1bd6a6)__

    [Nigel Davis](mailto:ndavis@ciena.com) - Tue, 26 Feb 2019 10:08:09 +0000
    
    

__[Simplified Equipment model](https://github.com/OpenNetworkingFoundation/TAPI/commit/ba95e07112fee338e55f7295e88ba5aae527ff59)__

    [Nigel Davis](mailto:ndavis@ciena.com) - Tue, 26 Feb 2019 01:50:29 +0000
    
    

__[recovery of small error in previous commit](https://github.com/OpenNetworkingFoundation/TAPI/commit/3bbe76fea5e28995b3e9eb0b68876f39378af6e5)__

    [amazzini](mailto:mazzini64@tiscali.it) - Wed, 20 Feb 2019 17:36:48 +0100
    
    

__[Minor diagram adjustments](https://github.com/OpenNetworkingFoundation/TAPI/commit/ab174c29ef9da4119308fd9a8f0d26525b7ff58c)__

    [amazzini](mailto:mazzini64@tiscali.it) - Wed, 20 Feb 2019 17:29:44 +0100
    
    

__[LLDP model &#34;assigned&#34; to TapiOam](https://github.com/OpenNetworkingFoundation/TAPI/commit/ccd433fd35fa36144c85910fa265cd5bb75379ab)__

    [Bernd Zeuner](mailto:b.zeuner@telekom.de) - Wed, 20 Feb 2019 12:02:16 +0100
    
    Touch points of LLDP classes to OAM classes are added; according to the TAPI
    call on February 19 (still under discussion).

__[LLDP model added to Tapi](https://github.com/OpenNetworkingFoundation/TAPI/commit/e2cd93e9b7eca6e456bc6bfbdc64f7687f1c651e)__

    [A303646](mailto:A303646@BE1EB250.emea1.cds.t-internal.com) - Tue, 19 Feb 2019 09:43:22 +0100
    
    LLDP model re-engineered from 
    https://github.com/YangModels/yang/blob/master/standard/ieee/draft/802.1/ieee802-dot1ab-lldp.yang 
    revision 2018-11-11
    
    Additional change: Primitive types MacAddress, Binary and Timeticks added to
    TapiCommon and then referenced in TapiLldp.
    

__[Clean up of diagrams](https://github.com/OpenNetworkingFoundation/TAPI/commit/fb7933e8a67e53fcfa61d40eda57adc2d81b12ea)__

    [ndavis](mailto:git@github.com:ciena-1/OpenROADM_MSA_Private.git) - Wed, 13 Feb 2019 14:43:47 +0000
    
    

__[Incorporation of Equipment model (first stage)](https://github.com/OpenNetworkingFoundation/TAPI/commit/95e21af77090c2c4709bd90ebfc3b517ce8c3bae)__

    [ndavis](mailto:git@github.com:ciena-1/OpenROADM_MSA_Private.git) - Tue, 12 Feb 2019 13:40:48 +0000
    
    

__[Minor diagram adjustments](https://github.com/OpenNetworkingFoundation/TAPI/commit/1ed44ff6324a2dd589ddc208425e3874cda753b4)__

    [amazzini](mailto:mazzini64@tiscali.it) - Sun, 27 Jan 2019 00:12:42 +0100
    
    

__[Minor diagram adjustments](https://github.com/OpenNetworkingFoundation/TAPI/commit/0a7fd6501f8f0b4114b7099cd07a95b7757ab6e2)__

    [amazzini](mailto:mazzini64@tiscali.it) - Fri, 25 Jan 2019 16:46:21 +0100
    
    

__[Path Computation, added include/exclude NEP to TopologyConstraint class.](https://github.com/OpenNetworkingFoundation/TAPI/commit/209c41ecaceccc56a24611360fa5c401bafd3c52)__

    [amazzini](mailto:mazzini64@tiscali.it) - Thu, 24 Jan 2019 15:28:07 +0100
    
    OAM, Renamed &#34;timeStamp&#34; attribute as &#34;periodStartTime&#34; in both current and
    history data classes. ODU, minor correction in comment

__[Minor diagram and association adjustments](https://github.com/OpenNetworkingFoundation/TAPI/commit/32d60cb84b91acc38a67f7876832f5257173f34e)__

    [amazzini](mailto:mazzini64@tiscali.it) - Thu, 24 Jan 2019 01:10:54 +0100
    
    

__[Various minor adjustments.](https://github.com/OpenNetworkingFoundation/TAPI/commit/1a92b3c7635b970d1c3ceb8020f0129ecbe551d1)__

    [amazzini](mailto:mazzini64@tiscali.it) - Tue, 22 Jan 2019 19:01:50 +0100
    
    

__[Several minor adjustments.](https://github.com/OpenNetworkingFoundation/TAPI/commit/638816a2c32a7a6b0761a55b1da43f14513f46a9)__

    [amazzini](mailto:mazzini64@tiscali.it) - Tue, 22 Jan 2019 18:57:31 +0100
    
    - Moved priority and destinationAddress into EthLinkTraceJob, removed the pac.
    - Moved testPattern from pac to EthTestJob, moved lbmDataTlv from pac to 
    EthLoopbackJob, renamed the pac as EthOamTestLoopbackCommonPac.
    - Reorganized OAM service and OAM service end point extensions, now referring
    to “resource” classes of MEG, MEP, MIP
    - Added TestSinkPoint with only “source mac address” attribute.
    - testPattern, changed type from integer to enum.
    - Removed idPermission from EthCfmMaintenanceDomain, to prevent 
    inconsistencies.
    - Centralized attributes of ProAct and OnDmd Jobs.
    - Corrected wrong abstraction association between OAM Srv and EthOamSrv, other
    minor corrections on OamResourceSpec and OamServiceSpec associations.
    

__[Renamed history and current data without “Pm”](https://github.com/OpenNetworkingFoundation/TAPI/commit/93262de3853e2a854cff7edeb93202910aee003a)__

    [amazzini](mailto:mazzini64@tiscali.it) - Tue, 22 Jan 2019 18:54:05 +0100
    
    

__[Some modifications following MEF NRM OAM review:](https://github.com/OpenNetworkingFoundation/TAPI/commit/82a1f22036bc45a052e6c88255d348fc922636fa)__

    [amazzini](mailto:mazzini64@tiscali.it) - Fri, 11 Jan 2019 19:52:10 +0100
    
    - Remove &#34;End&#34; from OamServiceEndPoint name.
    
    - Create ETH OamServiceMep/MipPoint where to centralize all Ethernet related
    &#34;intent&#34; parameters (of both MEP and MIP), and same for ETH OamService.
    
    - EthProActiveMeasurementJobControlSource, 
    EthOnDemandMeasurementJobControlSource change &#34;messagePeriod&#34; attribute type to
    &#34;integer&#34;, milliseconds, default 1000. On the &#34;sink&#34; classes, replace &#34;period&#34;
    with the &#34;messagePeriod&#34; just defined.
    
    - Augmentation of interfaces (Job and Profile)
    

__[Some modifications following MEF NRM OAM review:](https://github.com/OpenNetworkingFoundation/TAPI/commit/c4b508c72c66f1750d12aea7a79da75b2e9c234f)__

    [amazzini](mailto:mazzini64@tiscali.it) - Fri, 11 Jan 2019 19:47:57 +0100
    
    Make optional the &#34;schedule&#34; attribute of TAPI OamJob.
    

__[Several modifications following MEF NRM OAM CfC2](https://github.com/OpenNetworkingFoundation/TAPI/commit/443cd9646bb7443ae57254bcff96733332f89eb3)__

    [amazzini](mailto:mazzini64@tiscali.it) - Thu, 10 Jan 2019 19:01:43 +0100
    
    - Added Meg/megLevel, Meg/megIdentifier, Mep/mepIdentifier, 
    Mep/peerMepIdentifier, all integers. (renamed the already defined 
    ethPeerMepIdentifier and ethMepId).
    - EthProActiveMeasurementJobControlSink and 
    EthOnDemandMeasurementJobControlSink, responderMepId renamed as sinkMepId.
    - period and messagePeriod attributes added to 
    EthProActiveMeasurementJobControlSink, EthOnDemandMeasurementJobControlSink.
    - measurementInterval and repetitionPeriod attributes added to 
    EthProActiveMeasurementJobControlSink &amp; Source, 
    EthOnDemandMeasurementJobControlSink.
    - priority attribute added to  EthProActiveMeasurementJobControlSink.
    - timeOfTheDayAlignment, offsetFromTimeOfTheDay attributes added to 
    EthProActiveMeasurementJobControlSink &amp; Source, 
    EthOnDemandMeasurementJobControlSink &amp; Source.
    - ltmFlags of EthCfmLinkTraceJob: type enhanced from integer to enum, with only
    one entry (use-fdb-only).
    - Augmented OAM Job Interface operations.
    

__[Modifications following NRM OAM CfC2](https://github.com/OpenNetworkingFoundation/TAPI/commit/4e6b0a8d893dd9ce20fb3171b604eb3519223abd)__

    [amazzini](mailto:mazzini64@tiscali.it) - Thu, 10 Jan 2019 18:58:17 +0100
    
    - Removed Meg/megLevel, Meg/megIdentifier, Mep/mepIdentifier, 
    Mep/peerMepIdentifier
    - OamServiceEndPoint class, add MIP/MEP boolean attribute, remove mepIdentifier
    and peerMepIdentifier attributes.
    - Split OAM job and OAM profile operations into their own OamJob and OamProfile
    interface classes respectively. OamService interface only contain OamService
    and OAM OSEP operations.
    - Deleted OAM Profile attribute from the OamService, hence no related hierarchy
    is modeled for OamJobProfile.

__[Minor diagram correction](https://github.com/OpenNetworkingFoundation/TAPI/commit/50e2b3668f740e937e122dda4a17f3b6ee9f519d)__

    [amazzini](mailto:mazzini64@tiscali.it) - Fri, 21 Dec 2018 00:50:04 +0100
    
    

__[Restoring diagrams with IEEE CFM classes](https://github.com/OpenNetworkingFoundation/TAPI/commit/5bc118feec6dd0c78d4bd027b83e7ec72d7d1fe5)__

    [amazzini](mailto:mazzini64@tiscali.it) - Fri, 21 Dec 2018 00:48:30 +0100
    
    

__[Introduced experimental ODU CSEP](https://github.com/OpenNetworkingFoundation/TAPI/commit/13069a934ca2dfc410c4effc10204ac8f87978a1)__

    [amazzini](mailto:mazzini64@tiscali.it) - Fri, 21 Dec 2018 00:36:12 +0100
    
    

__[Missing type from faultConditionDetermination attribute](https://github.com/OpenNetworkingFoundation/TAPI/commit/0ba824379eb41313f85a1b9652aa283111985622)__

    [amazzini](mailto:mazzini64@tiscali.it) - Fri, 21 Dec 2018 00:35:28 +0100
    
    Added CSEPIsProtectedByCSEP for multi-point protection schemes

__[Added OTN specific fault condition determination (G.873.1)](https://github.com/OpenNetworkingFoundation/TAPI/commit/8ea46ccef6c28f72e36fa5030011a340c727fe06)__

    [amazzini](mailto:mazzini64@tiscali.it) - Fri, 14 Dec 2018 19:47:25 +0100
    
    

__[Resilience update](https://github.com/OpenNetworkingFoundation/TAPI/commit/271d10ed8be190a9229f0801f55464fc2fdbec44)__

    [amazzini](mailto:mazzini64@tiscali.it) - Fri, 14 Dec 2018 19:43:36 +0100
    
    - added reference from CSEP to peer-forwarding CSEP (multi-point protection
    schemes)
    - added reference from CSEP to server CSEP (for multi-layer constraints)

__[Resilience data types updates](https://github.com/OpenNetworkingFoundation/TAPI/commit/b07f2817daa702d4cd0f534aa9699851643653f9)__

    [amazzini](mailto:mazzini64@tiscali.it) - Fri, 14 Dec 2018 19:40:34 +0100
    
    - Split the ResilienceType into two distinct attributes: ProtectionType and
    RestorationPolicy.
    - Added faultConditionDetermination attribute to ResilienceConstraint class
    according to G.808.
    - Updated ProtectionType according to G.808.

__[Update of Eth OAM with CFM items,](https://github.com/OpenNetworkingFoundation/TAPI/commit/dd582be665c904b4276a92e5e028d42fe072b0c5)__

    [amazzini](mailto:mazzini64@tiscali.it) - Wed, 12 Dec 2018 13:35:13 +0100
    
    NEP modified attribute availableCepLayerProtocol, _ownedNodeEdgePoint now
    _nodeEdgePoint

__[Added MD/MA attributes to MEG, ethMepId and ethPeerMepIdentifier](https://github.com/OpenNetworkingFoundation/TAPI/commit/a1fd4287ff5994746894db69d5c5ed6e993df32a)__

    [amazzini](mailto:mazzini64@tiscali.it) - Sun, 28 Oct 2018 00:17:00 +0200
    
    (integer) to mep, unexLtrReceived to mep, added IEEE CFM attributes to Link
    Trace and Loopback operations.

__[Added timeStamp (start time) in pmHistoryData.](https://github.com/OpenNetworkingFoundation/TAPI/commit/fda6e93531078c1817550da142f64567cd77a5c0)__

    [amazzini](mailto:mazzini64@tiscali.it) - Sun, 28 Oct 2018 00:01:24 +0200
    
    

__[Enhanced NEP attribute availableCepLayerProtocol](https://github.com/OpenNetworkingFoundation/TAPI/commit/4d515099f2b02e9594a1c20c0e3fb11ed67c008e)__

    [amazzini](mailto:mazzini64@tiscali.it) - Sat, 27 Oct 2018 23:57:42 +0200
    


