# Feature priority for TAPI 2.6.0 (July to September 2024)
- Note that some planned features may need only RIA update
- (H) High priority
- (M) Mediun priority
- (L) Low priority

## Topology Management
  1) (H) UNI/ENNI: deprecation of DSR and OTN as layer names for UNI/ENNI SIP/NEP (Andrea)
     - For both fixed and configurable UNI/ENNI use instead either PHOTONIC_MEDIA or (new) ELECTRICAL_MEDIA

## Connectivity Management
  1) Staged provisioning of Connectivity Service (lifecycle intent and state) (Andrea)
	 - (H) Fixing consistency between YANG and RIA
     - (L) Including schedule / temporal management
  2) Development of Path Computation UCs (Nigel)
     (H) - Connectivity Service constraints on PathSet (e.g. inclusion)
     (M) - Connectivity Service related to computation service, including preparation for specific work in 2.7+
  3) (L) Review of SIP/NEP capability model
     - E.g. a given SIP instance may potentially support services at more layers

## Photonic Connectivity Management
  1) (H) Complex digital payload of photonic media (Andrea)
     - Describe how a DSR (perhaps directly supporting IP) can be carried directly by photonics 
     - OTSiG on multiple line ports
  2) (H) Remote Pluggable (e.g. ZR/ZR+) Use Cases (Nigel)
     - Consider OIF/IETF for the pluggable model
	 - IETF: lifecycle of the pluggable
  3) (M) 3R Scenarios
     - Further development of Connectivity UCs including 3R
     - In relationship with Asymmetric Service model
     - In relationship to Resiliency
     - See IETF related works (https://github.com/ietf-ccamp-wg/draft-ietf-ccamp-optical-impairment-topology-yang)
  4) (H) Linkage between TAPI model and IETF model to allow navigation from photonic/OTN to IP layers (Nigel)
     - Initially e.g. minimal navigation capability (RFC 8345, RFC 8795)

## OAM Management
  1) (L) Problem / Incident reporting (elementary fault analysis / synthesis) (Nigel)
     - Some work ongoing @ IETF
  2) PM streaming enhancements (Nigel)
     - (H) Validate that the PM streaming model aligns with the most recent moves in OAM
     - (H) Additional properties in enums
     - (H) Spotlight/snapshot stream to "get current data" e.g. on periodical time on selected monitors
     - (H) Fix to some strings in the protobuf data (not in correct case) - note that this will not impact compatibility.
     - (M) Zero and same value suppression

## Photonic OAM Management
  1) (H) Further development of Optical Impairments UCs (Esther)
     - Work ongoing @ IETF
	   + so far coherent is predominant
	 
  2) (M) Further developments of Photonic OAM model (Andrea)
     - Power along a Connection (Nigel)

## Equipment Management
  1) (H) Node to Device relationship (Nigel)

## RESTCONF
  1) (H) Improve documentation on POST/DELETE/etc. (Nigel)
     - Following the removal of all RPCs
  2) (L) Response codes for use cases

## General applications
  1) All properties are conditional (Nigel)
  2) Security: identity, authentication, authorization, confidentiality, etc. (STRIDE) (Jonathan)
     - TLS, SSH
     - NACM
  3) RIA structure needs improvements
     - Consider strategies to e.g. break the monolitic document
	 - Numbering of Use Cases - relationship with Use Cases initially developed not by TAPI team
	   + should be candidate for std adoption, if not then using a numbering not overlapping with TR-547


**_Note that:_**

- All features and enhancements should start with business scenarios and/or use cases along with requirements.

  + These may initially be lightweight and be developed as the solution is developed

- For a feature/enhancement to be completed, the necessary UML, Yang, RIA etc. changes/additions must be provided by the team. 

- Where a feature is being delivered over multiple releases, it is an option to deliver draft Use Cases and model in the first one or two release(s).

- Effort should be made to achieve backward compatibility with previous releases.
