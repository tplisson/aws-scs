## Domain 2	- Security Logging and Monitoring (18%)

## Exam Objectives 

| Task Statement | Exam Objective     | 
| ------------------------ | ------------------ | 
| **Domain 2** | **Security Logging and Monitoring (18%)**
| 1 | [Design and implement monitoring and alerting to address security events](#task-statement-1-design-and-implement-monitoring-and-alerting-to-address-security-events)  
| 2 | [Troubleshoot security monitoring and alerting](#task-statement-2-troubleshoot-security-monitoring-and-alerting)
| 3 | [Design and implement a logging solution](#task-statement-3-design-and-implement-a-logging-solution)
| 4 | [Troubleshoot logging solutions](#task-statement-4-troubleshoot-logging-solutions)
| 5 | [Design a log analysis solution](#task-statement-5-design-a-log-analysis-solution)


--- 

## Task Statement 1: Design and implement monitoring and alerting to address security events. 

Knowledge of:
- AWS services that monitor events and provide alarms (for example, [CloudWatch](../../services/cloudwatch/README.md), [EventBridge](../../services/eventbridge/README.md))
- AWS services that automate alerting (for example, Lambda, Amazon Simple Notification Service [Amazon SNS], Security Hub)
- Tools that monitor metrics and baselines (for example x, Systems Manager)

Skills in:
- Analyzing architectures to identify monitoring requirements and sources of data for security monitoring
- Analyzing environments and workloads to determine monitoring requirements
- Designing environment monitoring and workload monitoring based on business and security requirements
- Setting up automated tools and scripts to perform regular audits (for example, by creating
custom insights in Security Hub)
- Defining the metrics and thresholds that generate alerts

---  

## Task Statement 2: Troubleshoot security monitoring and alerting. 

Knowledge of:
- Configuration of monitoring services (for example, Security Hub)
- Relevant data that indicates security events

Skills in:
- Analyzing the service functionality, permissions, and configuration of resources after an event that did not provide visibility or alerting
- Analyzing and remediating the configuration of a custom application that is not reporting its statistics
- Evaluating logging and monitoring services for alignment with security requirements 

---  

## Task Statement 3: Design and implement a logging solution.

Knowledge of:
- AWS services and features that provide logging capabilities (for example, VPC Flow Logs, DNS logs, [AWS CloudTrail](../../services/cloudtrail/README.md), Amazon CloudWatch Logs)
- Attributes of logging capabilities (for example, log levels, type, verbosity)
- Log destinations and lifecycle management (for example, retention period)

Skills in:
- Configuring logging for services and applications
- Identifying logging requirements and sources for log ingestion
- Implementing log storage and lifecycle management according to AWS best practices and organizational requirements

---  

## Task Statement 4: Troubleshoot logging solutions. 

Knowledge of:
- Capabilities and use cases of AWS services that provide data sources (for example, log level, type, verbosity, cadence, timeliness, immutability)
- AWS services and features that provide logging capabilities (for example, VPC Flow Logs, DNS logs, [CloudTrail](../../services/cloudtrail/README.md), [CloudWatch Logs](../../services/cloudwatch/README.md))
- Access permissions that are necessary for logging 

Skills in:
- Identifying misconfiguration and determining remediation steps for absent access permissions that are necessary for logging (for example, by managing read/write permissions, S3 bucket permissions, public access, and integrity)
- Determining the cause of missing logs and performing remediation steps 

---  

## Task Statement 5: Design a log analysis solution.

Knowledge of:
- Services and tools to analyze captured logs (for example, Athena, CloudWatch Logs filter)
- Log analysis features of AWS services (for example, CloudWatch Logs Insights, [AWS CloudTrail Insights](../../services/cloudtrail/README.md), Security Hub insights)
- Log format and components (for example, [CloudTrail logs](../../services/cloudtrail/README.md))

Skills in:
- Identifying patterns in logs to indicate anomalies and known threats
- Normalizing, parsing, and correlating logs

---  

