**Date**
- 5 March 2024

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
- Kam Lam
- Qilei Wang


**Tentative agenda:**

- General update
  + Update on Linux Foundation
  + 2.5.0 Review: plan for corrections and enhancements
- Photonic Model: continue the fix/update of the transceiver provisioning model
- Continue the discussion on digital payload of photonic media
- Model for Multi-technology Network Interface


**Next Call, March 12**

- Update on Linux Foundation
- 2.5.0 Review: corrections and enhancements
- Photonic Model: continue the fix/update of the transceiver provisioning model
- Continue the discussion on digital payload of photonic media
- Model for Multi-technology Network Interface
- Review 2.6.0 plan, agree priorities, assign owners

-------------------------------------------------------------------------------------
**Discussion item 1**

General update

40 mins

1) Move to LF
   + LF has confirmed that they will provide, without costs
     - Conference call platform and Github repository
   + No updates regarding the TR-547/8 copyright
     - No indication if the name will remain TR or something different
   + Nigel and Lyndon have provided the MoU draft to TIP for review
     - to formalize the TIP strong influence on TAPI TRs
     - defending and protecting from the overly liberal environment of LF
   + Andrea will contact Kam to start planning the publication of TAPI at ITU-T
     - Explore a possible MoU also with ITU-T

2) 2.5.0 Review: plan for corrections and enhancements
   + Andrea shows the new repository for the 2.5.0 patches:
     https://github.com/OpenNetworkingFoundation/TAPI/tree/tapi-2_5_0-fixes/TAPI-FIXES
   + So far defined two patches, regarding Photonic Media and Notification modules
   + The patches are defined in separate Yang modules, as augments of 2.5.0 constructs
     - this allows to maintain unaltered the original 2.5.0 Yang modules
   + Esther comments that OpenConfig delivers a new version when corrections are necessary
     - Nigel answers that each vendor already has a framework for proprietary augments
       + the standard patches can follow same pattern
   + Nigel (and Andrea) are available to present the TAPI patch mechanism to TIP
  

-------------------------------------------------------------------------------------
**Discussion item 2**

[Transceiver Model](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/discussions/578)

50 mins

-------------------------------------------------------------------------------------