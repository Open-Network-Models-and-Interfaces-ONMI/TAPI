### [2024‐02‐06 TAPI Meeting Minutes](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/wiki/2024%E2%80%9002%E2%80%9006-TAPI-Meeting-Minutes)

Andrea shows the related UML diagrams of version 2.5.0
- After some discussion, it was agreed that:
  + The purpose of the transceiver profile (aka template or spec) is to provide the library of capabilities.
    - Hence the proper SIP/NEP shall include a list of one or more supported profiles,
      representing the supported transceiver modes.
    - This capability information is normally available at server controller.
  + The transceiver profile is read-only.
  + The main use case of the transceiver provisioning is by specifying
    - the central frequency and other info which are orthogonal to the transceiver mode,
    - the reference to the chosen profile instance (transceiver mode).
  + To be further explored the explicit provisioning of some "capability" parameters
    - with or without specifying a profile.
    - Arturo confirms that some legacy transceivers required some parameters "on the fly".

- Esther indicates that TAPI needs an alignment to the more recent versions of OpenConfig and IETF specifications.
  + IETF: https://datatracker.ietf.org/doc/draft-ietf-ccamp-optical-impairment-topology-yang/14/

- Esther also clarifies that the transceiver standard profile needs also the line-coding-rate parameter to be fully defined.
  + ITU-T it was decided to not include this parameter to improve flexibility.

### [2024‐02‐20 TAPI Meeting Minutes](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/wiki/2024%E2%80%9002%E2%80%9020-TAPI-Meeting-Minutes)

Andrea shows the IETF drafts he is parsing to update TAPI
- Gabriele and Esther clarify that
  + The reference for transceiver capability and state models is
    - https://datatracker.ietf.org/doc/draft-ietf-ccamp-optical-impairment-topology-yang/
  + The reference for transceiver configuration model is
    - https://datatracker.ietf.org/doc/draft-ietf-ccamp-dwdm-if-param-yang/10/
      + specifically the structure "provisioning-opt-if-och-mode-params"
  + The common library of data types is
    - https://datatracker.ietf.org/doc/draft-ietf-ccamp-rfc9093-bis/
  + With a warning that "optical-impairment-topology-yang" is more advanced wrt "wdm-if-param-yang"
    regarding overlapping definitions

- Andrea will review the indicated IETF drafts, for inclusion in TAPI
  + and provide feedback to Gabriele as necessary

### [2024‐02‐27 TAPI Meeting Minutes](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/wiki/2024%E2%80%9002%E2%80%9027-TAPI-Meeting-Minutes)


Andrea shows the updated UML diagrams
- Andrea asks for a clarification regarding the comment of in-band-osnr "measured at reference point Ss"
  + Esther and Gabriele indicate that
    - "measured at reference point Ss" is to be intended as
    - "measured at transmission point", reference being G.698.2
    - It is the quality of the transceiver regarding the inserted noise, in trasmission
- Andrea asks for clarification regarding OSNR and Penalty unit of measurements
  + Esther confirms that, as defined by the IETF draft
    - the OSNR is "measured over 0.1 nm resolution bandwidth"
    - the Penalty is measured in pure dB, as it is a ratio applied to the OSNR
- Ronald suggests to consider the provisioning of the frequency offset, or drift
  + indicated the reference: IA OIF-C-CMIS-01.1 Table 7
  + for further discussion

### [2024‐03‐05 TAPI Meeting Minutes](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/wiki/2024%E2%80%9003%E2%80%9005-TAPI-Meeting-Minutes)

Andrea shows the updated UML diagrams
- Esther clarifies that the transceiver profile models both capabilities and configuration
  + no need of further tuning at configuration time, the selected profile instance tells it all
  + in other words, the profile instance constrains the provisioning
- Nigel suggests that a more generic model should be the target, where each parameter can be expressed for 
  + capability, intent/setting, state/threshold
- Esther clarifies that minOsnrMargin and totalChannelOutputPower are PM metrics
  + hence shall be removed from the Explicit Profile
  + Also _powerManagementConfigPac to be removed

- Esther provides the list of OpenConfig PM metrics:
  https://github.com/OpenNetworkingFoundation/TAPI/tree/tapi-team-activities/TAPI-TEAM-ACTIVITIES/Contributions/openconfig-pms.txt
  + Andrea will review and map/add to TAPI
    - Purpose is the correct mapping of PM metrics detected on OpenConfig side and then passed to TAPI i/f

### [2024‐03‐12 TAPI Meeting Minutes](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/wiki/2024%E2%80%9003%E2%80%9012-TAPI-Meeting-Minutes)

Discussed the https://datatracker.ietf.org/doc/draft-ietf-ccamp-optical-impairment-topology-yang
  - Nigel asks clarification regarding the standard mode, where only G.698.2 is mentioned, while TAPI currently lists:
	+ G.698.1 : Multichannel DWDM applications with single ...
    + G.698.2 : Amplified multichannel dense wavelength ...
    + G.695   : Optical interfaces for coarse wavelength division ...
    + G.696.1 : Longitudinally compatible intra-domain DWDM ...
    + G.959.1 : Optical transport network physical layer interfaces
  - Gabriele replies that G.698.2 is the only one specifying application identifiers
    + Three fundamental types of photonics: CWDM, DWDM, Flex Grid.
	+ Gabriele will verify if the other ITU-T recommendations may be included as further references for standard modes
  - Discussion for clarification of table 8-1 of G.698.2 11/2018
  - Nigel asks why some parameters shall be specified in addition to the reference to a standard mode
	+ a given standard mode should include all the necessary parameters
	+ Esther explains that a vendor may test and publish a profile which is 
	  - compliant to a standard one
	  - while improving some aspects
    + Andrea shows the differences in transceiver profiles between:
      - https://datatracker.ietf.org/doc/draft-ietf-ccamp-optical-impairment-topology-yang/14/
      - https://datatracker.ietf.org/doc/draft-ietf-ccamp-optical-impairment-topology-yang/15/
    + Esther indicates that the tx/rx min/max power parameters are associated to the transceiver instance,
	  i.e. these parameters are not / cannot be centralized in a profile
	  - the "explicit profile" being in the "templates" subtree.
  - Further investigation is necessary on draft-ietf-ccamp-optical-impairment-topology before to complete the mapping to TAPI

### [2024‐03‐19 TAPI Meeting Minutes](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/wiki/2024%E2%80%9003%E2%80%9019-TAPI-Meeting-Minutes)

Andrea is editing a document including the OpenConfig and CCAMP PM metrics
  - References are
    + https://github.com/openconfig/public/blob/master/release/models/optical-transport/openconfig-terminal-device.yang
	+ https://datatracker.ietf.org/doc/draft-ietf-ccamp-dwdm-if-param-yang/10/
  - Regarding Transceiver Modes, it seems confirmed that G.698.2 left a degree of freedom regarding line-coding-bitrate
    + For the following parameters it seems that they could be needed for both profile/template and transceiver instance:
	
	 +--ro min-central-frequency?
 	 |       frequency-thz
 	 +--ro max-central-frequency?
 	 |       frequency-thz
 	 +--ro transceiver-tunability?
 	 |       frequency-ghz
 	 +--ro tx-channel-power-min?     power-dbm
 	 +--ro tx-channel-power-max?     power-dbm
 	 +--ro rx-channel-power-min?     power-dbm
 	 +--ro rx-channel-power-max?     power-dbm
 	 +--ro rx-total-power-max?       power-dbm

  - Instead to add further parameters to the standard profile, maybe define a new, fourth one like "standard delta".

### [2024‐03‐26 TAPI Meeting Minutes](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/wiki/2024%E2%80%9003%E2%80%9026-TAPI-Meeting-Minutes)

Andrea asks if there are news/progresses in https://datatracker.ietf.org/doc/draft-ietf-ccamp-optical-impairment-topology-yang/
  - No news, hence agreed that Andrea will adapt TAPI transceiver model according to currently available definitions

### [2024‐04‐02 TAPI Meeting Minutes](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/wiki/2024%E2%80%9004%E2%80%9002-TAPI-Meeting-Minutes)

Andrea shows slides regarding the model of transceiver
- capabilities
- provisioning (intent)
- configuration (result of the intent)

Esther and Gabriele provide some clarifications:
- the instance related data structure is useful when the capabilities are context sensitive
  + e.g. the capabilitity of a pluggable (identified by a part number) may change depending on where it is installed
- the capability description granularity is on single transceiver, which in CCAMP is defined as a topological item
  + while in TAPI the logical model item representing the transceiver function is the OTSiMC CEP
    - which does not exist until involved in a Connection
- Andrea will adapt the model proposal according to the above clarifications.

Jonathan: the draft-ietf-ccamp-optical-impairment-topology-yang-15 is assuming a GOSNR (Generalized OSNR) approach, which is only valid to uncompensated coherent networks.
-  It does not allow for OOK interferers such as 10G or non-coherent 40G.
-  To accommodate those signals, the network needs to provide XPM/SPM/4WM parameters to compute the cross-talk.
-  Lets continue the discussion on next week’s call.
 
### [2024‐06‐04 TAPI Meeting Minutes](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI/wiki/2024%E2%80%9006%E2%80%9004-TAPI-Meeting-Minutes)

Andrea shows the updated slides regarding the model of transceiver modes, from the perspective of:
- capability
- provisioning (intent)
- configuration (result of the intent)

Esther explains that in both IETF CCAMP and OpenConfig the transceiver function is described (instantiated) regardless it is configured or not, in other words it is described if the underlying equipment supports it.
- Andrea recalls that TAPI model decouples the physical and logical models, and describes capabilities through dedicated structures referenced by NEP instances
  + Andrea will update the figures