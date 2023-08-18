# AWS Config
- Offers detailed view of  AWS resources within AWS accounts
- Provides historial tracking i.e. configuration recording timeline
- NOT a preventive service
- a ***regional*** service
- SNS integration

## Usage
- Audit and Compliance
  - Main usage
- Resource administration
  - easily detect and notify of misconfigs
- Troubleshooting
- Security Analysis
  - view low level changes to resources

## Exam terms
- Resources
  - any entity managed by AWS
- Configuration History
- Configuration Items
  - point-in-time views of different attributes
- Configuration Recorder
  - must create and start a recorder before configs are stored!
- **Aggregator**
  - to aggregate views from multiple sources (regions, accounts, org...)  
  - requires authorization
  - centralized notification
- Conformance Packs
  - Collection of Config rules & remediation actions deployed as a single entity

## Config Rules

Rules 
- Managed Rules 
- Custom Rules

Evaluation Types:
- configuration changes
- Periodic
- Compliance 
  
---  

<a align="center" href="https://docs.aws.amazon.com/config/latest/developerguide/aggregate-data.html">
  <img src="img
/aggregator.jpg" {:height="25%" width="25%"}>
</a>

---  

