☁️Cloud-Native Ransomware Detection and Prevention on AWS

A Proof-of-Concept (PoC) project that uses native AWS services to detect, respond to, and prevent ransomware attacks in a cloud environment.

🔍Overview

This project demonstrates how to build a cloud-native security system using services like AWS GuardDuty, CloudTrail, CloudWatch, Lambda, SNS, IAM, and S3 Object Locking to detect and mitigate ransomware threats in real time.

✨ Features

Detects ransomware activity using AWS GuardDuty
Monitors API usage with AWS CloudTrail and CloudWatch
Automatically isolates infected EC2 instances using Lambda
Protects S3 data with versioning and Object Lock
Replicates critical S3 data across regions
Sends alert notifications via SNS
Backups using AWS Backup for recovery

🛠️ Tools and AWS Services Used

AWS GuardDuty – Threat detection
AWS CloudTrail – API activity logs
AWS CloudWatch – Alarm and log monitoring
Amazon S3 – Secure object storage with versioning
AWS Lambda – Automate EC2 isolation
Amazon SNS – Notification service for alerts
AWS IAM – User and permission management
AWS Backup – Scheduled backups for recovery
EventBridge – Triggers Lambda functions on specific events

🗂️ Project Structure

aws-ransomware-detection/
README.md -
poc-guide.md -
architecture.png-
lambda ->
(isolate_ec2.py)


✅ Prerequisites

AWS account with admin or necessary service permissions
Basic knowledge of AWS Console
Python installed (for Lambda function)
AWS CLI configured 

🚀 How to Use (Steps Summary)

Set up IAM User and MFA
Enable GuardDuty and Security Hub
Set up CloudTrail and CloudWatch Logs
Enable S3 Versioning and Object Lock
Create Lambda function for EC2 isolation
Trigger Lambda via EventBridge on GuardDuty finding
Configure SNS to send alerts
Enable AWS Backup for disaster recovery
Full steps are in poc-guide.md

🙏 Credits

AWS Documentation
Project built by: Harshal Thavare
