# AWS-SCS-C02 - AWS Certified Security Specialty Certification — Study Notes

<!-- <p align="center">
  <img src="images/aws-scs-badge.png" {:height="25%" width="25%"}>
</p>
<br/> -->

<a align="center" href="https://aws.amazon.com/certification/certified-security-specialty/">
  <img src="images/aws-scs-badge.png" {:height="25%" width="25%"}>
</a>

---  

## Table of Contents  

| Section                  |
| ------------------------ | 
| [Exam Details](#exam-details)  |  
| [Exam Objectives as of May 2024](#exam-objectives-as-of-may-2024)  |  
| [Which key tools, technologies, and concepts might be covered on the exam?](#which-key-tools-technologies-and-concepts-might-be-covered-on-the-exam)  |  
| [AWS services and features](#aws-services-and-features)  |  
| [Out-of-scope AWS services and features](#out-of-scope-aws-services-and-features)  |  

---  

## Exam Details

Exam Details  |   |
------------- | - |  
Assessment Type	| Multiple choice or multiple response
Format	| Online proctored
Duration	| 170 mins
Questions | 65 questions
Price	| $300 USD / €270 EUR
Language	| English
Expiration |	3 years

---  

## [Exam Objectives as of May 2024](https://d1.awsstatic.com/training-and-certification/docs-security-spec/AWS-Certified-Security-Specialty_Exam-Guide.pdf)

| Task Statement | Exam Objective     | 
| ------------------------ | ------------------ | 
| **Domain 1** | [**Threat Detection and Incident Response (14%)**](objectives/domain1/README.md)
| 1.1 | [Design and implement an incident response plan](objectives/domain1/README.md#task-statement-1-design-and-implement-an-incident-response-plan)
| 1.2 | [Detect security threats and anomalies by using AWS services](objectives/domain1/README.md#task-statement-2-detect-security-threats-and-anomalies-by-using-aws-services)
| 1.3 | [Respond to compromised resources and workloads](objectives/domain1/README.md#task-statement-3-respond-to-compromised-resources-and-workloads)
| **Domain 2** | [**Security Logging and Monitoring (18%)**](objectives/domain2/README.md) 
| 2.1 | [Design and implement monitoring and alerting to address security events](objectives/domain2/README.md#task-statement-1-design-and-implement-monitoring-and-alerting-to-address-security-events)
| 2.2 | [Troubleshoot security monitoring and alerting](objectives/domain2/README.md#task-statement-2-troubleshoot-security-monitoring-and-alerting)
| 2.3 | [Design and implement a logging solution](objectives/domain2/README.md#task-statement-3-design-and-implement-a-logging-solution)
| 2.4 | [Troubleshoot logging solutions](objectives/domain2/README.md#task-statement-4-troubleshoot-logging-solutions)
| 2.5 | [Design a log analysis solution](objectives/domain2/README.md#task-statement-5-design-a-log-analysis-solution)
| **Domain 3** | [**Infrastructure Security (20%)**](objectives/domain3/README.md)
| 3.1 | Design and implement security controls for edge services
| 3.2 | Design and implement network security controls 
| 3.3 | Design and implement security controls for compute workloads 
| 3.4 | Troubleshoot network security
| **Domain 4** | [**Identity and Access Management (16%)**](objectives/domain4/README.md)
| 4.1 | Design, implement, and troubleshoot authentication for AWS resources
| 4.2 | Design, implement, and troubleshoot authorization for AWS resources
| **Domain 5** | [**Data Protection (18%)**](objectives/domain5/README.md)
| 5.1 | Design and implement controls that provide confidentiality and integrity for data in transit
| 5.2 | Design and implement controls that provide confidentiality and integrity for data at rest
| 5.3 | Design and implement controls to manage the lifecycle of data at rest
| 5.4 | Design and implement controls to protect credentials, secrets, and cryptographic key materials
| **Domain 6** | [**Threat Detection and Incident Response (14%)**](objectives/domain6/README.md)
| 6.1 | Develop a strategy to centrally deploy and manage AWS accounts
| 6.2 | Implement a secure and consistent deployment strategy for cloud resources
| 6.3 | Evaluate the compliance of AWS resources
| 6.4 | Identify security gaps through architectural reviews and cost analysis



## Which key tools, technologies, and concepts might be covered on the exam?
The following is a non-exhaustive list of the tools and technologies that could appear on the exam.  
- AWS CLI
- AWS SDK
- AWS Management Console
- Secure Remote Access
- Certificate management
- Infrastructure as code (IaC)

## AWS services and features
Note: Security affects all AWS services. Many services do not appear in this list because the overall service is out of scope, but the security aspects of the service are in scope. For example, a candidate for this exam would not be asked about the steps to set up replication for an S3 bucket, but the candidate might be asked about configuring an S3 bucket policy.

### Management and Governance:  
- AWS Audit Manager
- <img src="images/CloudTrailLogo.png" alt="CloudTrail logo" style="height: 20px; width:20px;"/> [AWS CloudTrail](services/cloudtrail/README.md)  
- <img src="images/CloudWatchLogo.png" alt="CloudWatch logo" style="height: 20px; width:20px;"/> [AWS CloudWatch](services/cloudwatch/README.md)  
- <img src="images/ConfigLogo.png" alt="Config logo" style="height: 20px; width:20px;"/> [AWS Config](services/config/README.md)  
- AWS Organizations
- AWS Systems Manager
- AWS Trusted Advisor

### Networking and Content Delivery:  
- Amazon Detective
- AWS Firewall Manager
- AWS Network Firewall
- AWS Security Hub
- AWS Shield
- Amazon VPC
  - VPC endpoints
  - Network ACLs
  - Security groups
  - Network Access Analyzer
- AWS WAF

### Security, Identity, and Compliance:  
- AWS Certificate Manager (ACM)
- AWS CloudHSM
- AWS Directory Service
- <img src="images/GuardDutyLogo.png" alt="GuardDuty logo" style="height: 20px; width:20px;"/> [Amazon GuardDuty](services/guardduty/README.md)  
- AWS Identity and Access Management (IAM)
- Amazon Inspector
- AWS Key Management Service (AWS KMS)
- Amazon Macie
- AWS Single Sign-On

## Out-of-scope AWS services and features
The following is a non-exhaustive list of AWS services and features that are not covered on the exam. 

- Application development services
- IoT services
- Machine learning (ML) services
- Media services
- Migration and transfer services

---  
