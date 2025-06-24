# SmartReach - an Agentic AI-driven Proactive Telecom Outreach
![SmartReach](https://github.com/user-attachments/assets/54118c0a-7426-4e8f-9d5d-005126ce7158)

_Presented By:_ **Artifical Minds**__


## Explore Our Project
- [Problem Statement](#problem-statement)
- [Our Solution](#our-solution)
- [Solution Architecture and Technical Components](#solution_architecture_and-technical-components)
- [Meet Our Agents](#meet-our-agents)
- [Installation and Setup Guide](#installation-and-setup-guide)
- [Impact and Scalability](#impact-and-scalability)
- [Execution Plan](#execution-plan)
- [SmartReach's Future Reach](#smartreachs-future-reach)


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


## Solution Architecture and Technical Components 
![ProactiveReachOutAgents-Overall_Architecture](https://github.com/user-attachments/assets/19c368df-ac10-43f0-8488-eff7cbab45ed)  

### Technical Components
* **Google Cloud Platform** – Cloud services used in the solution:
  * Vertex AI Agent Engine – Provides fully managed, serverless runtime used for deploying and scaling AI agents
  * AI Agents – Each AI agent is designed to pursue its own goals and complete tasks through reasoning, planning, and a level of autonomy
  * BigQuery – Serverless, enterprise data warehouse used to store customer billing history
  * Cloud Storage – Used to store customer call transcripts
  * Pub/Sub - Publish/Subscribe messaging service used to receive events from in-house/external systems 

* **Enterprise Systems** - Entrprise Systems may be on-prem or on the cloud:
  * Network Performance Monitoring System – publishes outage events
  * Billing and Usage System – publishes usage and bill change events
  * Customer Call Log Analyzer Job – Scheduled job to trigger call log analysis

* **3rd Party Tools**
  * OSS Ticketing System (JIRA) - Service Outage ticketing system for Engineers
  * Twilio - Programmable tool used to send out communications


## Meet Our Agents
![ProactiveReachOutAgents-Agent_Design](https://github.com/user-attachments/assets/80ade3dd-d241-48d3-a458-92403119e63b)
To support SmartReach’s diverse feature set, the solution deploys three dedicated agent groups, each focused on a specific functional domain. 

* **Service Outage/Restoration**


* **Bill Impact Analysis**

* **Customer Success**


## Installation and Setup Guide
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

### Prerequisite
1. Python312
2. Checkout repo from git (https://github.com/cthaker/artificial-mind-proactive-agent.git)
   
### Installation steps
1. Set API Key (Google Cloud Console > Credentials) in .env file
2. Add Python Scripts directory (e.g. 'C:\Program Files\Python312\Scripts') to PATH environment variable for your account  
_**To be executed on terminal/PowerShell**_
3. pip3 install poetry
4. cd artificial-mind-proactive-agent
5. poetry install
6. python -m venv .venv
7. .\.venv\Scripts\activate (for MAC-> source $(poetry env info --path)/bin/activate)
8. pip3 install google-adk
9. pip3 install twilio
10. pip3 install jira
11. pip3 install --upgrade google-cloud-bigquery  
_**To be executed on google cloud cli**_
12. gcloud auth application-default login 
13. gcloud init (Select GCP project-id)  

_**Run adk web to launch ADK Dev UI (or use ADK CLI)**_

### Google Cloud Platform Features
* GCP Project Name: Team Alpha - Innovation  
* **BigQuery** 
  * Service Account: dbconnect
  * DataSet: BillingData
  * Table: BillingStatement  
* **Cloud Storage** - _created as a Data Store under AI Applications_
  * Name: Call Transcripts
  * Type: Unstructured data
  * 
### 3rd Party Tools
* **JIRA** _(Incident Management System)_
  * JIRA Project: https://cap-artificial-minds.atlassian.net/jira/software/projects/KAN/boards/1


## Impact and Scalability

## Execution Plan

## SmartReach's Future Reach
