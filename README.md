☁️Cloud-Native Ransomware Detection and Prevention on AWS

   A Proof-of-Concept (PoC) project that uses native AWS services to detect, respond to, and prevent ransomware attacks in a cloud environment.

🔍Overview

   This project demonstrates how to build a cloud-native security system using services like AWS GuardDuty, CloudTrail, CloudWatch, Lambda, SNS, IAM, and S3 Object Locking to detect and mitigate ransomware threats in real time.

✨ Features

  1. Detects ransomware activity using AWS GuardDuty
  2. Monitors API usage with AWS CloudTrail and CloudWatch
  3. Automatically isolates infected EC2 instances using Lambda
  4. Protects S3 data with versioning and Object Lock
  5. Replicates critical S3 data across regions
  6. Sends alert notifications via SNS
  7. Backups using AWS Backup for recovery

🛠️ Tools and AWS Services Used

 1. AWS GuardDuty – Threat detection

 2. AWS CloudTrail – API activity logs

 3. AWS CloudWatch – Alarm and log monitoring

 4. Amazon S3 – Secure object storage with versioning

 5. AWS Lambda – Automate EC2 isolation

 6. Amazon SNS – Notification service for alerts

 7. AWS IAM – User and permission management

 8. AWS Backup – Scheduled backups for recovery

 9. EventBridge – Triggers Lambda functions on specific events

🗂️ Project Structure

aws-ransomware-detection/
README.md -
poc-guide.md -
architecture.png-
lambda ->
(LamdaCode.py)


✅ Prerequisites

AWS account with admin or necessary service permissions

Basic knowledge of AWS Console

Python installed (for Lambda function)

AWS CLI configured 

🚀 How to Use (Steps Summary)

 1. Set up IAM User and MFA.
    
 2. Enable GuardDuty and Security Hub
  
 3. Set up CloudTrail and CloudWatch Logs
    
 4. Enable S3 Versioning and Object Lock
    
 5. Create Lambda function for EC2 isolation
     
 6. Trigger Lambda via EventBridge on GuardDuty finding
     
 7. Configure SNS to send alerts
     
 8. Enable AWS Backup for disaster recovery
     
Full steps are in poc-guide.md

🙏 Credits

AWS Documentation

Project built by: Harshal Thavare
