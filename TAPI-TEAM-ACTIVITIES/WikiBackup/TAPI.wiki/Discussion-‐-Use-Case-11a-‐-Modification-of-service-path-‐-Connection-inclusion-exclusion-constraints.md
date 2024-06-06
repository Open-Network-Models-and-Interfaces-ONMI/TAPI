### [2024‐04‐09 TAPI Meeting Minutes](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/wiki/2024%E2%80%9004%E2%80%9009-TAPI-Meeting-Minutes)

Andrea briefly shows the text of UC11a, proposing to add "connection inclusion/exclusion" to the UC
- to drive the rerouting of an existing Connectivity Service

In addition, the current comments in the UML/YANG could be extended, to allow both the:
- inclusion/exclusion of orphan Connections (Connections without intent/CS), and
- inclusion/exclusion of server layer Connections for routing constraints
  + both at creation time and update time

Discussion to be continued.

### [2024‐04‐23 TAPI Meeting Minutes](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/wiki/2024%E2%80%9004%E2%80%9023-TAPI-Meeting-Minutes)

The current comments in the UML/YANG could be extended, to allow both the:
- inclusion/exclusion of server layer Connections for routing constraints
  + both at creation time and update time
- inclusion/exclusion of orphan Connections at the same layer
  + only at creation time

Server layer Connection:
- agreed that only suitable connections can be used for inclusion constraint
  + feasible means ready for usage by client layer, e.g. terminated connection which provides the client link
  + not feasible means more corner cases where e.g. termination and adaptation is not yet available, single cross connection, etc.
- exclusion constraint can consider a wider set of Connection types
  
Same layer orphan Connection:
- it should be possible to reconcile an existing Connection to a creating Connectivity Service
  + to enable further editing through TAPI i/f
- if the existing Connection does not span the entire intended route of the creating Connectivity Service
  + then we may end up with a further partitioning level
  + Discussion to be continued

### [2024‐05‐07 TAPI Meeting Minutes](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/wiki/2024%E2%80%9005%E2%80%9007-TAPI-Meeting-Minutes)

Andrea shows some slides with examples of:
- Connectivity Service creation with Connection inclusion
  + Connection at the layer or at server layer
- Connectivity Service modification with Connection inclusion
  + Connection at the layer or at server layer
  
Agreed that there are three types of Connection:
1) Connection with intent (i.e. direcly associated to a Connectivity Service)
2) Fixed Connection, by definition not subject of any intent
3) Stranded Connection, which is an abnormal state to be corrected

Preliminary agreement on simpler use case, the inclusion of Connection at server layer
- which is conceptually redundant wrt Link inclusion constraint
  + but we agreed that Link instances are mandatory only at bottom-most layer
  
Discussion to be continued regarding Connection inclusion at the layer
- To be clarified the relationship with the "Connection adoption" use case
  + which is the only one described by UML/YANG comments, since (at least) TAPI version 2.1.3

### [2024‐05‐14 TAPI Meeting Minutes](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/wiki/2024%E2%80%9005%E2%80%9014-TAPI-Meeting-Minutes)

Andrea shows some slides updated according to last week discussions, below the reviewed text:
- Connectivity Service Creation
  + Include same layer Connection
    - Connection with intent not considered
    - Fixed Connection
      + Included in the Connection hierarchy, to inform about the relationship with a service
    - Stranded Connection
      + If fully covering the intent, adopting it by the intent
      + If partially covering the intent, disappearing as being merged in the newly created Connection with intent
        - In order to be merged, the stranded connection must be fully consistent with intent

  + Include server layer Connection, of any type
    - Must already support the proper virtual network
    - Will become part of the Connection hierarchy

- Connectivity Service Modification
  + Include same layer Connection: same as creation scenario
  + Include server layer Connection, of any type: same as creation scenario
  + In all cases, zero, one or more existing server Connections may be released
    - Released Connections may be deleted or moved to stranded state, up to local policy.

Nigel suggests that we may add the use case of forcing the deletion of a stranded connection if in conflict with an intent
  - For further discussion

### [2024‐05‐21 TAPI Meeting Minutes](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/wiki/2024%E2%80%9005%E2%80%9021-TAPI-Meeting-Minutes)

Andrea shows some slides updated according to last week discussions (onmi2024.AM.002_TAPI_RIASlides20052024.pptx, slides 445 .. 461)
- Agreed to add "fixed" boolean attribute to Connection object (similarly to TMF-MTNM)
- Agreed the proposed text
- Andrea will accordingly updated the UML comments and the RIA UC.