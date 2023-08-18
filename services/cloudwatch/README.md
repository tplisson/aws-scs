# AWS CloudWatch
- __Logging and Monitoring__
  - within AWS and external (can send to CloudWatch)
- __Centralized and Secured__
  - KMS encryption
- __Easy Analysis__
  - Query language for interacrtive search
- Integration with CloudTrail
  - Alarm creation for specified API activities
- Log Retention options
- Storage
  - long-term with S3 
- Networking logs
  - Route53 DNS queries
  - Flow logs

## Usage

## Subscription & Metric Filters

- Real-time Data
- Subscription Filters
  - do or do not sent to target AWS services
  - subscribe to a feed to be sent to target AWS services
- Metric Filter 
  - similar to Subscription Filters but for relevant CloudWatch metrics log data 
  - create alarms or graphs using filtered data

Limitations:
- each log group can have up to 2 Subscription Filters

   
Example #1  
![Example1](img/example1.jpg)

Example #2  
![Example2](img/example2.jpg)

## CloudWatch Agent   

Support for *Windows* and *Linux*

`awslogs.conf` defines which logs are passed to CloudWatch. 

### Legacy vs Unified

***Legacy***  
- EC2 agent publishing logs to CloudWatch

***Unified***  
- Supports __IMDSv2__ (Instance MetaData - Service)
- Supports __both__ apps logs + system-level logs and metrics from EC2 __and__ on-premise instances.  
- from `StatsD` & `collectD`




## Exam terms

  
---  

Sample    
![Sample](img/sample.jpg)

---  

