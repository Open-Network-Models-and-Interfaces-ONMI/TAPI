**Date**
- 23 April 2024

_Disclaimer:_
_ONF is disbanding and merging into Linux Foundation._
_Until is not fully clarified and agreed under which entity this project will land,_
_no final decisions will be taken by the TAPI team for the TAPI next versions._
_TAPI team will at most agree recommendations, with final agreement postponed._

**Attendees**
- Andrea Mazzini
- Gabriele Galimberti
- Nigel Davis
- Brian Johnson
- Jonathan Sadler
- Anders Lindgren
- Ronald Zabaleta


**Tentative agenda:**

- General update
  + Update on Linux Foundation
  + Brief review of open/closed issues
- UC 11a: “Modification of service path” and UML/YANG comments
  + Clarification of connection inclusion/exclusion constraints
- UC 11b: “Modification of service nominal route to secondary (protection) route for maintenance operations”
  + Unidirectional switching of bidirectional service/connection
- Photonic Model: continue the fix/update of the transceiver provisioning model
  + check transceiver profile and transceiver parameters
  + GOSNR (Generalized OSNR) approach and possible enhancements to the explicit profile
- Continue the discussion on digital payload of photonic media
- Model for Multi-technology Network Interface


**Next Call, April 30**

- General update
  + Update on Linux Foundation
  + Brief review of open/closed issues
- Review 2.6.0 plan, agree priorities, assign owners
- UC 11a: “Modification of service path” and UML/YANG comments
  + Clarification of connection inclusion/exclusion constraints
- UC 11b: “Modification of service nominal route to secondary (protection) route for maintenance operations”
  + Unidirectional switching of bidirectional service/connection
- Photonic Model: continue the fix/update of the transceiver provisioning model
  + check transceiver profile and transceiver parameters
  + GOSNR (Generalized OSNR) approach and possible enhancements to the explicit profile
- Continue the discussion on digital payload of photonic media
- Model for Multi-technology Network Interface


-------------------------------------------------------------------------------------
**Discussion item 1**

General update

30 mins

1) Move to LF
   + No updates regarding the TR-547/8 copyright
     - No indication if the name will remain TR or something different
   + Andrea will contact Kam to start planning the publication of TAPI at ITU-T
     - Explore a possible MoU also with ITU-T and MEF
	 - Still to understand if a liaison with ITU-T would be possible, as LF seems not supporting a centralized liaison management
   + TIP - LF MoU
     - Nigel, we still need to clarify with Scott Nicholas that we are not overcommitting with TIP, rather maintaining the previous level of commitment.
	   + We need Arturo to continue the discussion
   + Nigel: Git update
     - Nigel has admin rights over ONF git repository
	   + Will plan to coordinate migration, including Italo and Andrea
   + Nigel: Specifications in two places
     - Bernd Zeuner pointed out that the https://github.com/Open-Network-Models-and-Interfaces-ONMI/onf-specifications
	   + has old published versions of the documents, and
       + these documents are also available in other git repositories. Hence a concern over duplication and confusion.
       + Agreed that this is a historic repository of documents generated whilst the work was in ONF
       + Agreed to properly restructure the repository
   + ONMI TST
     - agreed to contact some
	   + current members to check if they are still interested and willing to contribute
	   + candidate new members (e.g. Esther and Jonathan)
	     - major role being the TAPI release approval

	 
2) Use Cases separately defined by Operators
   + Nigel: we need to find a way to keep consistent naming of
     - UC part of TR-547
	 - UC not (yet?) part of TR-547
   + Anders: Telia is updating their specification according to TR-547 3.1	 
 
 
-------------------------------------------------------------------------------------
**Discussion item 2**

[Use Case 11a: Modification of service path - Connection inclusion/exclusion constraints](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/discussions/580)

40 mins


-------------------------------------------------------------------------------------