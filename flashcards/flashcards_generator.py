from genanki import Deck, Note, Model, Package

# Define a unique ID for the deck and model to avoid conflicts with other decks
DECK_ID = 1234567890
MODEL_ID = 987654321

# Define model for front/back flashcards
basic_model = Model(
    MODEL_ID,
    'Basic Model',
    fields=[
        {'name': 'Front'},
        {'name': 'Back'}
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Front}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Back}}',
        },
    ]
)

# Define the deck 
deck = Deck(
    DECK_ID,
    'AWS SCS-C02 - Domain 1 - AWS Incident Response and Threat Detection'
)

# Define flashcards based on the table
flashcards = [
    ("What is the main goal of an incident response plan in AWS?", "To design and implement structured responses to mitigate and resolve security incidents effectively."),
    ("Which AWS document provides best practices for incident response?", "The AWS Security Incident Response Guide."),
    ("What is the purpose of the NIST SP 800-61 guide in incident response?", "It outlines structured procedures for preparation, detection, containment, recovery, and post-incident learning."),
    ("Name one key AWS service used for detecting security threats.", "Amazon GuardDuty."),
    ("How does Amazon GuardDuty help in threat detection?", "It provides threat detection by continuously monitoring for malicious activity and unauthorized behavior."),
    ("What does AWS Security Finding Format (ASFF) enable for security data?", "Efficient ingestion and standardization of security findings data across AWS services."),
    ("Which AWS service helps with vulnerability scanning for cloud assets?", "Amazon Inspector."),
    ("Describe a key function of Amazon CloudWatch Logs Anomaly Detection.", "It provides log aggregation and anomaly detection to identify unusual activity."),
    ("Which service in AWS aids in automatic compliance reporting?", "AWS Artifact."),
    ("How does Amazon Macie contribute to AWS security?", "It helps identify and protect sensitive data using machine learning."),
    ("What is the role of the AWS IAM Access Analyzer?", "It analyzes IAM policies to identify and reduce unintended access."),
    ("Which AWS service is typically used for monitoring and visualization to detect anomalies?", "Amazon CloudWatch."),
    ("Name one tool to isolate compromised AWS resources.", "Amazon EC2 isolation or stopping instances."),
    ("What AWS service can be used to store forensics data securely?", "Amazon S3 with Object Lock for data immutability."),
    ("What is the purpose of AWS EventBridge in incident response?", "To automate responses by routing event data to specific AWS or third-party services."),
    ("How can Amazon Detective support root cause analysis?", "By visualizing and analyzing security data to help identify the cause of incidents."),
    ("What is the role of AWS Systems Manager in incident remediation?", "To automate operational tasks and manage security incidents with runbooks."),
    ("What is an AWS playbook in the context of incident response?", "A predefined set of steps to identify security issues."),
    ("What is an AWS runbook, and how is it used in security incidents?", "A guide with predefined steps for remediating security incidents."),
    ("Which AWS service can help prevent unauthorized IAM access?", "AWS Identity and Access Management (IAM)."),
    ("What AWS service aggregates and correlates security findings?", "AWS Security Hub."),
    ("What is the purpose of Amazon Athena in incident response?", "To perform queries on security data for validation and investigation."),
    ("How does AWS Trusted Advisor assist in maintaining security best practices?", "By providing recommendations based on industry standards to improve security posture."),
    ("Describe the function of Amazon Detective in security investigations.", "It enables deep analysis of AWS security data to investigate and visualize security findings."),
    ("Which AWS service helps detect unauthorized access attempts?", "Amazon GuardDuty, by monitoring for suspicious activity."),
    ("What is the AWS solution for storing immutable forensic evidence?", "Amazon S3 with Object Lock and isolated forensic accounts."),
    ("How are AWS Lambda and AWS Step Functions used in security incident response?", "They automate security responses and orchestrate workflows for remediation tasks."),
    ("What AWS service is used to aggregate threat intelligence and security findings?", "AWS Security Hub."),
    ("What does the AWS Config service do for security?", "Tracks and assesses changes in AWS resource configurations for compliance and risk management."),
    ("What technique is recommended by AWS for root cause analysis after an incident?", "Reviewing logs and event details using Amazon Detective and related services."),
    ("How can AWS Secrets Manager be used in a compromised account?", "By rotating credentials to protect sensitive data and accounts."),
    ("What is the AWS approach to preventing future security incidents based on past ones?", "Post-incident analysis to identify lessons learned and adjust security policies."),
    ("What is the purpose of AWS Artifact in the security domain?", "To provide on-demand compliance reports and legal documentation for AWS compliance."),
    ("Which service can centralize AWS security findings across regions and accounts?", "AWS Security Hub."),
    ("Name one AWS service that provides continuous monitoring of AWS workloads for security threats.", "Amazon GuardDuty."),
    ("How does AWS Config help in maintaining compliance?", "By assessing and tracking configuration changes to ensure alignment with best practices."),
    ("What kind of data does Amazon S3 Object Lock secure for forensic purposes?", "Immutable forensic data."),
    ("Which AWS tool assists in detecting data loss risks related to sensitive data?", "Amazon Macie."),
    ("Describe a method for responding to AWS Abuse Alerts.", "Monitoring alerts, identifying compromised resources, and isolating or remediating them."),
    ("Which AWS feature allows you to isolate an EC2 instance if it’s compromised?", "EC2 instance isolation through security group updates or network ACL adjustments.")
]

# Create notes (flashcards) and add to the deck
for front, back in flashcards:
    note = Note(
        model=basic_model,
        fields=[front, back]
    )
    deck.add_note(note)

# Save the deck to an .apkg file
output_path = "AWS-SCS-C02-Domain1-AWS-Incident-Response-and-Threat-Detection.apkg"
Package(deck).write_to_file(output_path)

print(f"Anki package created: {output_path}")
