# Change Log
## Commit Range: 2.1.1..HEAD

__[Bugfixes for issues #429 and #386 in v2.1.2](https://github.com/OpenNetworkingFoundation/TAPI/commit/f9b25d8cff935d1cc174926c024b040c94a343fa)__

    [Arturo Mayoral](mailto:arturo.mayoral.ext@telefonica.com) - Thu, 11 Jul 2019 08:25:13 +0200
    EAD -&gt; refs/heads/v2.1-bug-fixes, refs/remotes/onf/v2.1-bug-fixes
    This commit includes the following changes:
    * Fix bug on Connectivity Service End-Points (CSEPs) media-channel
    augmentation: media-channel-service-end-point-spec replaces
    media-channel-service-interface-point-spec which was wrongly used by the
    previous augment.
    * Fix bug detected in otsi-service-interface-point-spec/otsi-capability: NEW
    &#34;supportable-central-frequency-spectrum-band&#34; replaces
    &#34;supportable-lower-central-frequency&#34; and
    &#34;supportable-upper-central-frequency&#34;. After discussions into the TAPI calls
    on18/06/2019 and 25/06/2019, the group agreed on defining the tunabilty
    capabilities of otsi transmitters as a single list of bands defined by the
    lower and upper central frequencies of the band, and the frequency-contrains
    which specify the rest of feasible central frequencies within the band. An OTSi
    transmitter can have associated more than one band (i.e., C and L bands).
    
    This two changes are already present in newer v2.2.0.
    

__[Replaced TopologyConstraint pointers from references/leafref to UUID](https://github.com/OpenNetworkingFoundation/TAPI/commit/956359bbbed04472656a9394d753e32abc46fa14)__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 23 May 2019 13:30:11 -0400
    
    It was pointed on TAPI call @ 05/21/2019 that Yang 1.0 cannot handle such
    (leaf)references to read-only entities (in Topology subtree) from an
    configurable sub-tree (ConnectivityService subtree). So now the attributes are
    more loosely scoped/typed to any UUID, rather than to specific sub-tree
    namespace

__[Bug Fix: Updated NotificationSubScriptionFilter attributes to RW](https://github.com/OpenNetworkingFoundation/TAPI/commit/866c75f0f4916dc81b0bd9d14abd9a36d46d3a79)__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 20 May 2019 16:50:20 -0400
    
    

__[Bug Fix: Updated Path service attributes to RW](https://github.com/OpenNetworkingFoundation/TAPI/commit/9d87a43056b78fbbc6bd6df49688e06830f2bf1a)__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 20 May 2019 16:22:37 -0400
    


