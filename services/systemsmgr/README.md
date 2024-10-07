# <img src="../../images/SystemsManagerLogo.png" alt="AWS Systems Manager" style="height: 50px; width:50px;"/>  AWS Systems Manager
---  

![AWS Systems Manager Diagram](../../images/SystemsMgrDiagram.png)

---  
## Overview  
- 

---  
## Exam topics
- 


---  
## Systems Manager's Capabilities
- Application Management
- Change Management
- Operations Management
- Shared Resources
- Node Management
  - Patch manager
  - Run command
  - Session manager


---  
## Node Management - Patch manager
- Free to use!
- Patch any EC2, edge, on-prem devices
- Patch baselines for auto-approval
- Automatically deploy patches (during maintenance windows for e.g.)
- On-Demand compliance: 
  - only scan
  - scan & install
- Reporting in S3
- Important: AWS does not test patches before making them available !
  - Dev > Test > Prod env

Pre-Requisites:
- SSM Agent installed 
- Access to internet / repo sources
- Access to S3 !

Default:
- only installs 
- Linux support
- Smart patching (skipping unrelevant patching Win/Lunix)
- Installation commands via `Run Command`

Patch Baselings
- based on OS
- Predefined or Custom
- Approval Rules (including denies)
- Auto-Approval: Delays
- Auto-Approval: Cutoffs

Patch Groups:
- associate managed instances together
- using tags: "Patch Group" (case sensitive!)
- Patch groups are associated with patch baselines to ensure rules are applied


---  
## Node Management - Session manager
- Agent-based console
- requires: 
  - SSM agent insttalled
  - IAM role 
  - Network connectivity (IGW/TGW  or VPCE)

<!-- ---   -->
<!-- ## Example  -->

<!-- ![Image](../../images/ImageName.jpg) -->

---  
## AWS Resources  

https://aws.amazon.com/systems-manager/

Documentation  
https://docs.aws.amazon.com/systems-manager/
