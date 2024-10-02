# <img src="../../images/ConfigLogo.png" alt="Config" style="height: 50px; width:50px;"/>  AWS Config
---  

![Config Diagram](../../images/ConfigDiagram.png)

---  
## Overview  
- Offers detailed view of  AWS resources within AWS accounts
- Provides ***historial tracking*** i.e. configuration recording timeline
- ***DOES NOT prevent*** changes <--
- a ***regional*** service 
- use ***Aggregators*** to collect across regions and across accounts
- ***need to enable and start the recorder***, not enabled out-of-the-box
- Using ***Rules***, managed or custom
- Centralized notification
- Remediation using EventBridge or Lambda
- SNS integration for real-time notifications

## Usage  
- Audit and Compliance, Governance
  - main usage
  - detailed autiting info for resource changes
- Resource administration
  - easily detect and notify of misconfigs
- Troubleshooting
- Security Analysis
  - view low level changes to resources

## Exam terms  
- Resources
  - any entity managed by AWS
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

## Config Rules  

Rules 
- Managed Rules (predefined but customizable)
- Custom Rules (using Lambda)

Trigger Types:
- Configuration changes
- Periodic
- Hybrid
- ? Compliance (mark as compliant or noncompliant)
  
Evaluation Modes:
- Proactive mode  
  - evaluate resources before they have been deployed
  - COMPLIANT or NON_COMPLIANT
- Detective mode
  - evaluate resources that have already been deployed
  - 

---  
## Example using Multi-Account / Multi-Region Data Aggregation  

![Aggregator](../../images/ConfigAggregator.jpg)

---  
## AWS Resources  

https://aws.amazon.com/config/

Documentation  
https://docs.aws.amazon.com/config/