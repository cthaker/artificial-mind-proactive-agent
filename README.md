# SmartReach - an Agentic AI-driven Proactive Telecom Outreach
![SmartReach](https://github.com/user-attachments/assets/54118c0a-7426-4e8f-9d5d-005126ce7158)

_Presented By:_ **Artifical Minds**__

## Explore Our Project
- [Problem Statement](problem_statement)
- [Our Solution](our_solution)
- Solution Design
- Meet Our Agents
- Impact and Scalability
- Execution Plan
- SmartReach's Future Reach

## Problem Statement
In telecom, customer churn remains a critical concern, directly undermining revenue and growth potential.
The top factors leading to customer aattrition are:
* Inconsistent service reliability
* Lack of service disruption notifications
* Unanticipated changes in billing
* Unaddressed customer queries

## Our Solution
Our vision is to prioritize customer-centric initiatives to enhance retention and drive loyalty, provide initial troubleshooting framework for support engineers, and optimize support operations. 
**SmartReach** is an Agentic AI powered proactive outreach system for the Telecom industry that helps anticipate and address customer needs before they arise!
It's key features include:
* Hyper-Personalized Billing Insight with next bill prediction
* Proactive notifications for service interruptions/ongoing outages
* Advise for the Support Engineer with Preliminary Resolution Steps to Expedited Troubleshooting
* Customer re-engagement via proactive outreach

## Solution Design 


### Project Structure
```
.
├── README.md
├── bill_impact_analyzer/
│   └── deployment/
│   └── sub_agents/
│       ├── bill_predictor/
│   └── tools/
├── customer_call_analyzer/
│   └── deployment/
│   └── sub_agents/
│       ├── call_analyzer/
│       ├── past_call_analyzer/
├── outage_event_analyzer/
│   └── deployment/
│   └── sub_agents/
│       ├── outage_agent/
│       ├── search_agent/
│   └── tools/
│   └── deployment/
├── pyproject.toml
└── .env.example
```

# Prerequisite
1. Python312
2. Checkout repo from git (https://github.com/cthaker/artificial-mind-proactive-agent.git)

# Installation steps
1. Set API Key (Google Cloud Console > Credentials) in .env file
2. Add Python Scripts directory (e.g. 'C:\Program Files\Python312\Scripts') to PATH environment variable for your account
# To be executed on terminal/PowerShell
3. pip3 install poetry
4. cd artificial-mind-proactive-agent
5. poetry install
6. python -m venv .venv
7. .\.venv\Scripts\activate (for MAC-> source $(poetry env info --path)/bin/activate)
8. pip3 install google-adk
9. pip3 install twilio
10. pip3 install jira
11. pip3 install --upgrade google-cloud-bigquery
# To be executed on google cloud cli
12. gcloud auth application-default login 
13. gcloud init (Select GCP project-id)

Run adk web to launch ADK Dev UI (or use ADK CLI)

# Google Cloud Platform Project Information
  > Project Name: Team Alpha - Innovation

# BigQuery Information
  > Service Account: dbconnect
 
  > DataSet: BillingData

  > Table: BillingStatement
  
  > Data imported in BillingStatement

# Cloud Storage Information
  > Created as a Data Store under AI Applications

  > Name: Call Transcripts

  > Type: Unstructured data


# JIRA (Incident Management System)
  > JIRA Project: https://cap-artificial-minds.atlassian.net/jira/software/projects/KAN/boards/1


