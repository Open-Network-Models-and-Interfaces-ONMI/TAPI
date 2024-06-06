### [2024‐05‐14 TAPI Meeting Minutes](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/wiki/2024%E2%80%9005%E2%80%9014-TAPI-Meeting-Minutes)

Nigel presents a slide with a proposal to simplify the relationship between Node and Device
  - https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/blob/tapi-team-activities/TAPI-TEAM-ACTIVITIES/Contributions/otcc2024.ND.001_VariousTapiAssociations.pptx
  - Currently the Node/Device relationship can be derived from NEP/Access Port relationship
  - Considering that 
    + this level of flexibility is not always/often necessary
    + more common case is that one Device refers more Nodes, and one Node refers one Device
	it is proposed to add the Node to Device direct relationship
	
  - Roshan asks whether the new relationship is backward compatible
    + Nigel confirms, we are not removing existing NEP-AP relationship, only adding a new relationship for the simpler scenarios

### [2024‐05‐21 TAPI Meeting Minutes](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/wiki/2024%E2%80%9005%E2%80%9021-TAPI-Meeting-Minutes)

Nigel presents a slide with the detailed proposal regarding the simplification of the relationship between Node and Device
  - A new reference by name will be added from Node to Device, many to many.
  - Proposal is agreed

### [2024‐06‐04 TAPI Meeting Minutes](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/wiki/2024%E2%80%9006%E2%80%9004-TAPI-Meeting-Minutes)

Nigel presents an updated slide showing the _node_ object, augmented by _supporting-device_ list of references. 
- Model is agreed, Nigel will update UML and RIA accordingly