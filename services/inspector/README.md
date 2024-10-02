# <img src="../../images/InspectorLogo.png" alt="Inspector" style="height: 50px; width:50px;"/>  Amazon Inspector
---  

![Inspector Diagram](../../images/InspectorDiagram.png)

---  
## Overview  
- Automatic **vulnerability scans**
- Generates findings reported via lists
- Generates assessment reports

---  
## Exam topics
- Centalized managment
  - single delegated account in OU
- Automatic discovery and scanning of eligible resources 
  - Avoid manual steps
  - EC2 instances
  - ECR images
- Findings
- Tailored scores based on NVD/CVSS


---  
## Assessment Types  
- Triggered situations for EC2 Instances  
  - New instance is launched
  - New software installed on existing EC2 instances
  - New EC2 insrtances discovered
  - New vulnerability descovered
- **Network Assessment <-- Agentless every 24hrs**
- **Host Assessment <-- SSM Agent required**  

---  
## Intergrations
- EventBridge
- Security Hub
- S3 Buckets <-- KMS key + permissions

---  
## Exported formations
- CSV 
- JSON 

---  
## Findings Status
- Active
- Suppressed
- Closed


<!-- ---   -->
<!-- ## Example  -->

<!-- ![Image](../../images/ImageName.jpg) -->

---  
## AWS Resources  

https://aws.amazon.com/inspector/

Documentation  
https://docs.aws.amazon.com/inspector/