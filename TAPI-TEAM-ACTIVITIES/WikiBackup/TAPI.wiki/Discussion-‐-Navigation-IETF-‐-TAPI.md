### [2024‐05‐14 TAPI Meeting Minutes](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/wiki/2024%E2%80%9005%E2%80%9014-TAPI-Meeting-Minutes)

Nigel presents some slides from
  - https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/blob/tapi-team-activities/TAPI-TEAM-ACTIVITIES/Contributions/otcc2024.ND.001_VariousTapiAssociations.pptx
  - It is proposed an
    + extension to RFC8345 as an augmentation maintained by ONF TAPI
      - a reference to "supporting-tapi-cep"
    + extension to TAPI as an augmentation maintained by ONF TAPI
      - list of "client-rfc8345-termination-point"
 
Esther confirms that RFC 8345 foresees both unidirectional and bidirectional links
  - With optical links always considered bidirectional
  
Andrea asks about possible overlapping between modeling entities representing same resource but from different viewpoints
  - IETF already defines augments for L0
  - Nigel clarifies that the proposed solution assumes the complete split of management domains

### [2024‐06‐04 TAPI Meeting Minutes](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/wiki/2024%E2%80%9006%E2%80%9004-TAPI-Meeting-Minutes)

Nigel confirms that so far only the navigation between termination points has been considered
- It is assumed that there is no model overlap, i.e. IETF and TAPI have distinct, separated management domains
- Introduced the concept of _shared identifier_, i.e an identifier which is same for the IETF and TAPI termination points
  + this identifier should be based, for both IETF and TAPI, on the naming of the common supporting physical port 