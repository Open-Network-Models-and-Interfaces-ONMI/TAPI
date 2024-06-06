**Date**
- 26 March 2024

_Disclaimer:_
_ONF is disbanding and merging into Linux Foundation._
_Until is not fully clarified and agreed under which entity this project will land,_
_no final decisions will be taken by the TAPI team for the TAPI next versions._
_TAPI team will at most agree recommendations, with final agreement postponed._

**Attendees**
- Andrea Mazzini
- Gabriele Galimberti
- Esther Le Rouzic (TIP OOPT/MUST)
- Nigel Davis
- Brian Johnson
- Anders Lindgren
- Kam Lam
- Arturo Mayoral
- Dominique Verchere


**Tentative agenda:**

- General update
  + Update on Linux Foundation
  +	New https://github.com/orgs/Open-Network-Models-and-Interfaces-ONMI/repositories
  + 2.5.0 Review: final approval of draft patches
  + Brief review of open/closed issues
- Photonic Model: continue the fix/update of the transceiver provisioning model
  + check transceiver profile and transceiver parameters
- Continue the discussion on digital payload of photonic media
- Model for Multi-technology Network Interface


**Next Call, April 2**

- General update
  + Update on Linux Foundation
  + 2.5.1 Delivery
  +	New https://github.com/orgs/Open-Network-Models-and-Interfaces-ONMI/repositories
  + Brief review of open/closed issues
- Photonic Model: continue the fix/update of the transceiver provisioning model
  + check transceiver profile and transceiver parameters
- Continue the discussion on digital payload of photonic media
- Model for Multi-technology Network Interface
- Review 2.6.0 plan, agree priorities, assign owners

-------------------------------------------------------------------------------------
**Discussion item 1**

General update

60 mins

1) Move to LF
   + No updates regarding the TR-547/8 copyright
     - No indication if the name will remain TR or something different
   + Nigel and Lyndon have provided the MoU draft to TIP for review
     - Lyndon has forwarded the copy reviewed by TIP to Scott Nicholas at Linux Foundation for final review and approval 
   + Andrea will contact Kam to start planning the publication of TAPI at ITU-T
     - Explore a possible MoU also with ITU-T and MEF
   + Last Wednesday Lyndon and myself had a call with LF assistant for some practical items (ONMI Github, mailing lists, etc.)
   + Tomorrow is scheduled another call, including more LF representatives   

2) New https://github.com/orgs/Open-Network-Models-and-Interfaces-ONMI/repositories
   + Andrea shows the initial editing of new ONMI Github repository
   + Esther: better to store the meeting minutes in a repository rather than in the wiki
     This allows control on possible modifications
   + Esther, is there any LF recommendation / best practice?
     - Nigel, more likely to find recommendations in some specific project

3) [2.5.0 Review: approve draft patches](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/discussions/579)

4) [Proposal to close all issues older than 2023](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/discussions/579)

5) IETF 119 (https://www.ietf.org/how/meetings/119/)
   + Nigel provides a summary of the discussions which may concern TAPI
     - Pluggable Use Cases under development, see:
       + https://github.com/oscargdd/draft-poidt-ccamp-actn-poi-pluggable-usecases-gaps/pull/6#pullrequestreview-1915210804
       + https://datatracker.ietf.org/doc/draft-poidt-ccamp-actn-poi-pluggable-usecases-gaps/
       + Discussion on the photonic parameters of the pluggable, trying to rationalize the definitions coming from different sources
       + Still to be explored the electrical parameters of the pluggable
	   + Each parameter shall be considered in terms of
	     1) capability,
	     2) configurable property,
	     3) state,
	     all crossed with lifecycle.
	   + Notable use case foresees the installation of a pluggable as a result of network planning
	     - Pluggable are expensive and their installation needs careful evaluation
	     - The equipment shows the capability to install a transceiver - this capability being a potential end point of a service
	 - Digital Map, see:
	   + https://datatracker.ietf.org/doc/draft-havel-nmop-digital-map/
	   + Model for the evaluation of traffic patterns and failure consequences
	   + An opportunity for the alignment of TAPI and RFC 8345 topology models
	 - Nigels also underlines that in IETF seems missing the representation of the TAPI Connection End Point (CEP)
	   + for further evaluation
	 - Inventory (https://datatracker.ietf.org/wg/ivy/about/)
	   + Agreed the following distinct areas:
	     - Functional (not in the IVY scope)
		 - Physical, i.e. that can be measured by a ruler
		 - Info, e.g. PM data, Sw (the code)
		 - Motivational, e.g. the power supply (not in the IVY scope)
	 - Incident / Problem analysis, see:
	   + https://datatracker.ietf.org/doc/draft-feng-nmop-network-incident-yang/
	   + Development of concepts that can be brought in TAPI
	 
 
-------------------------------------------------------------------------------------
**Discussion item 2**

[Transceiver Model](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/discussions/578)

10 mins

-------------------------------------------------------------------------------------
**Discussion item 3**

[Progress on digital payload of photonic media](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/discussions/575)

40 mins

-------------------------------------------------------------------------------------