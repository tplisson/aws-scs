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
| [Exam Objectives as of Aug 2023](#exam-objectives-as-of-aug-2023)  |  
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

## [Exam Objectives as of Aug 2023](https://d1.awsstatic.com/training-and-certification/docs-security-spec/AWS-Certified-Security-Specialty_Exam-Guide.pdf)

| Task Statement | Exam Objective     | 
| ------------------------ | ------------------ | 
| **Domain 1** | [**Threat Detection and Incident Response (14%)**](domain1/README.md)
| 1 | [Design and implement an incident response plan](domain1/README.md#task-statement-1-design-and-implement-an-incident-response-plan)
| 2 | [Detect security threats and anomalies by using AWS services](domain1/README.md#task-statement-2-detect-security-threats-and-anomalies-by-using-aws-services)
| 3 | [Respond to compromised resources and workloads](domain1/README.md#task-statement-3-respond-to-compromised-resources-and-workloads)
| **Domain 2** | [**Security Logging and Monitoring (18%)**](domain2/README.md) 
| 1 | [Design and implement monitoring and alerting to address security events](domain2/README.md#task-statement-1-design-and-implement-monitoring-and-alerting-to-address-security-events)
| 2 | [Troubleshoot security monitoring and alerting](domain2/README.md#task-statement-2-troubleshoot-security-monitoring-and-alerting)
| 3 | [Design and implement a logging solution](domain2/README.md#task-statement-3-design-and-implement-a-logging-solution)
| 4 | [Troubleshoot logging solutions](domain2/README.md#task-statement-4-troubleshoot-logging-solutions)
| 5 | [Design a log analysis solution](domain2/README.md#task-statement-5-design-a-log-analysis-solution)
| **Domain 3** | [**Infrastructure Security (20%)**](domain3/README.md)
| 1 | Design and implement security controls for edge services
| 2 | Design and implement network security controls 
| 3 | Design and implement security controls for compute workloads 
| 4 | Troubleshoot network security
| **Domain 4** | [**Identity and Access Management (16%)**](domain4/README.md)
| 1 | Design, implement, and troubleshoot authentication for AWS resources
| 2 | Design, implement, and troubleshoot authorization for AWS resources
| **Domain 5** | [**Data Protection (18%)**](domain5/README.md)
| 1 | Design and implement controls that provide confidentiality and integrity for data in transit
| 2 | Design and implement controls that provide confidentiality and integrity for data at rest
| 3 | Design and implement controls to manage the lifecycle of data at rest
| 4 | Design and implement controls to protect credentials, secrets, and cryptographic key materials
| **Domain 6** | [**Threat Detection and Incident Response (14%)**](domain6/README.md)
| 1 | Develop a strategy to centrally deploy and manage AWS accounts
| 2 | Implement a secure and consistent deployment strategy for cloud resources
| 3 | Evaluate the compliance of AWS resources
| 4 | Identify security gaps through architectural reviews and cost analysis



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
- AWS CloudTrail
- Amazon CloudWatch
- [AWS Config](services/config/README.md)
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
- [Amazon GuardDuty](services/guardduty/README.md)
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
