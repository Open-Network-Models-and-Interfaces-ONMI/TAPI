**Date**
- 20 Feb 2024

_Disclaimer:_
_ONF is disbanding and merging into Linux Foundation._
_Until is not fully clarified and agreed under which entity this project will land,_
_no final decisions will be taken by the TAPI team for the TAPI next versions._
_TAPI team will at most agree recommendations, with final agreement postponed._

**Attendees**
- Andrea Mazzini
- Esther Le Rouzic (TIP OOPT/MUST)
- Nigel Davis
- Brian Johnson
- Jonathan Sadler
- Anders Lindgren
- Leo Nederlof
- Gabriele Galimberti


**Tentative agenda:**
- General update
  + Update on Linux Foundation
    - MOU with TIP
    - Still open the copyright of TR-547/8
  + Update on multi-SDO harmonization of Photonic Metrics
  + Update on Problem / Incident API
  + Outline a 2.5.1 delivery or early 2.6.0?
- Photonic Model: fix the transceiver provisioning model
- Continue the discussion on digital payload of photonic media
- Model for Multi-technology Network Interface
- Review 2.6.0 plan, agree priorities, assign owners

**Next Call, Feb 27**

- Update on Linux Foundation
- Photonic Model: continue the fixing of the transceiver provisioning model
- Continue the discussion on digital payload of photonic media
- Model for Multi-technology Network Interface

-------------------------------------------------------------------------------------
**Discussion item 1**

General update

60 mins

1) Move to LF
   + LF provided the draft of a MOU
     - Nigel: the candidate SDOs are TIP and OIF
     - Nigel: to be clarified how to fill the "Intended Area of Collaboration" of the MOU
   + Agreed that TAPI YANG will continue with Apache 2.0
   + Still under discussion the copyright of TR-547 and TR-548
   + Still no move of ONF Github repository
     - Agreed to solicit LF

2) Update on multi-SDO harmonization of Photonic Metrics
   + Nigel outlines the harmonization activity taking place in IETF
     - Focus is significally but not exclusively the plugs
     - Gathering and rationalization of the photonic metrics, currently defined across several SDOs
       + IETF CCAMP, ITU-T, OIF-CMIS, OpenConfig, TAPI
     - To define which is the appropriate list of properties, to be incorporated in IETF and TAPI.
     - Opportunity is that the involved models are there but also relatively recent,
       hence improvements for consistency are likely not affecting a large implemented base.

3) Update on Problem / Incident API
   + Nigel presents this work, currently ongoing in IETF, which outcomes can be adopted by TAPI.
   + References are
     - https://datatracker.ietf.org/doc/draft-feng-opsawg-incident-management/
     - https://datatracker.ietf.org/doc/draft-davis-nmop-incident-terminology/

4)  Outline a 2.5.1 delivery or early 2.6.0?
    + Andrea indicates that the ongoing review of version 2.5.0 is highlighting bugs and need for rapid improvements.
    + After a brief discussion, agreed that Andrea will present a snapshot of candidate modifications
      - in support of the evaluation of a 2.5.1 or a 2.6.0 next step.
    + Nigel recalls that TIP MUST has selected TAPI 2.5.0 as its reference version
      - Anders suggests that the evaluation shall be brought back to MUST.


-------------------------------------------------------------------------------------
**Discussion item 2**

[Transceiver Model](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/discussions/578)

20 mins

-------------------------------------------------------------------------------------
**Discussion item 3**

[Digital payload of photonic media - Model enhancements and generalizations](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/discussions/575)

40 mins

-------------------------------------------------------------------------------------