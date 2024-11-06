# <img src="../../images/ConfigLogo.png" alt="Config" style="height: 50px; width:50px;"/>  AWS Config
---  

![Config Diagram](../../images/ConfigDiagram.png)

---  
## Overview  
- Provides ***historial tracking*** i.e. configuration recording timeline
- ***DOES NOT prevent*** changes <--
- **Configuration Recorder** *must be enabled* to start recording & storing configurations
- ***need to enable and start the recorder***, not enabled by default
- Using ***Rules***: managed or custom
- a ***regional*** service 
- For OU | multi-account: use ***Aggregators*** (and across accounts)  
- Centralized notification
  - SNS integration for real-time notifications
- Remediation possible via EventBridge or Lambda

---  
## Usage  
- Audit and Compliance, Governance
  - main usage
  - detailed autiting info for resource changes
- Resource administration
  - easily detect and notify of misconfigs
- Troubleshooting
- Security Analysis
  - view low level changes to resources
  - integration with other tools such as [Security Hub](../securityhub/README.md)

---  
## Operations  
- Resource = any entity managed by AWS
- Configuration History = timeline
- Configuration Items
  - point-in-time views of different attributes
- Configuration **Recorder**
  - must create and start a recorder before configs are stored! <--
- **Aggregator**
  - to aggregate views from multiple sources for multi-account, multi-region deployments 
  - requires authorization
  - can provide centralized notification
- Conformance Packs
  - Collection of Config rules & remediation actions deployed as a single entity

---  
## Config Rules  

Rules 
- Managed Rules (predefined but customizable)
- Custom Rules (using Lambda)

Trigger Types:
- Configuration changes
- Periodic
- Hybrid
- ? Compliance (mark as compliant or noncompliant)

Evaluation Results:  
- COMPLIANT  
- NON_COMPLIANT  
- ERROR  
- NOT_APPLICABLE  

Evaluation Modes:  
- Proactive mode  
  - evaluate resources before they have been deployed
  - COMPLIANT or NON_COMPLIANT
- Detective mode
  - evaluate resources that have already been deployed
  - 

Sample rule:  
[]`ec2-instance-managed-by-systems-manager`](https://docs.aws.amazon.com/config/latest/developerguide/ec2-instance-managed-by-systems-manager.html)  
http://s3.amazonaws.com/aws-configservice-us-east-1/cloudformation-templates-for-managed-rules/EC2_INSTANCE_MANAGED_BY_SSM.template


---  
## Example using Multi-Account / Multi-Region Data Aggregation  

![Aggregator](../../images/ConfigAggregator.jpg)

---  
## AWS Resources  

Features  
https://aws.amazon.com/config/

Documentation  
https://docs.aws.amazon.com/config/

FAQs  
https://aws.amazon.com/config/faqs/

Workshops  
- [ ] https://awsworkshop.io/tags/aws-config/  
- [x] https://mng.workshop.aws/config.html  

