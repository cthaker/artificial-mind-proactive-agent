# SmartReach - an Agentic AI-driven Proactive Telecom Outreach
![SmartReach](https://github.com/user-attachments/assets/54118c0a-7426-4e8f-9d5d-005126ce7158)

_Presented By:_ **Artifical Minds**__


## Explore Our Project
- [Problem Statement](#problem-statement)
- [Our Solution](#our-solution)
- [Solution Architecture and Technical Components](#solution_architecture_and-technical-components)
- [Meet Our Agents](#meet-our-agents)
- [Installation and Setup Guide](#installation-and-setup-guide)
- [Impact and Metrics](#impact-and-metrics)
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
4. pip3 install poetry  
5. cd artificial-mind-proactive-agent  
6. poetry install  
7. python -m venv .venv  
8. .\.venv\Scripts\activate (for MAC-> source $(poetry env info --path)/bin/activate)  
9. pip3 install google-adk  
10. pip3 install twilio  
11. pip3 install jira  
12. pip3 install --upgrade google-cloud-bigquery  
13. gcloud auth application-default login
14. gcloud init (Select GCP project-id)
  
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

### 3rd Party Tools
* **JIRA** _(Incident Management System)_
  * JIRA Project: https://cap-artificial-minds.atlassian.net/jira/software/projects/KAN/boards/1


## Impact and Metrics
### Impact 
* **Business Impact**
  * Cost per Contact: Lowered by reducing inbound volume.
  * Churn Rate: Reduction in customer attrition due to proactive engagement.
* **Customer Experience**
  * Timely, personalized interaction addressing billing and service issues.
  * Higher satisfaction and trust through transparency and responsiveness.
* **Operational Efficiency**
  * Automated monitoring and outreach, reducing manual workload.
  * Improved agent utilization by focusing on high-value interactions. 

### Metrics
With Vertex AI Agent Engine, agents can be seamlessly scaled in a managed environment optimized for production readiness. Monitoring the performance and behavior of AI agents is crucial for continuous improvement and auditing. 
Here are some key metrics and monitoring capabilities available for Vertex AI Agent Engine:
* **Built-in Metrics via Cloud Monitoring** - Vertex AI Agent Engine automatically collects and visualizes a set of built-in metrics, which help understand the overall health and performance of the agents. These can be viewed using the Metrics Explorer:
  * Request count: the total number of requests served by an agent
  * Error rates: the percentage of requests that resulted in errors
  * Latency/Response times: How quickly AN agent responds to requests
  * Resource utilization: Metrics related to the compute resources used by the agent, such as CPU and memory usage
  * Agent memory usage: Specifically tracks the memory consumed by an agent
  * Model usage: Tracks usage fees based on input and output tokens of the models used by an agent  
* **Custom Metrics (Log-based Metrics)** - For more granular insights, custom log-based metrics can be created. This allows to define metrics based on specific log entries generated by the agent like Tool calling count, Agent-specific interactions.
* **Monitoring Agent Behavior and Quality** - Beyond resource and request metrics, monitoring the quality and efficacy of the agent's responses is vital. While direct metrics for "agent confidence" or "response accuracy" aren't always explicitly listed as built-in metrics, Vertex AI Agent Builder provides tools and best practices to help you evaluate and improve these aspects:
  * Evaluation tools: Vertex AI offers evaluation capabilities for generative AI models, which can be applied to agents. This includes evaluating responses based on various quality metrics.
  * Logging inputs and outputs: Comprehensive logging of agent inputs and outputs is crucial for debugging, analyzing agent behavior, and identifying areas for improvement.
  * Testing and debugging tools: Vertex AI Agent Builder provides features for testing an agent with various scenarios and for debugging issues like misinterpretations or tool invocation failures.
  * Training data and instructions: Continuous monitoring of agent performance helps to identify shortcomings in the training data, instructions, or prompt engineering, allowing for iterative refinement.
  * Human-in-the-loop: For critical applications, maintaining a human-in-the-loop feedback mechanism can help identify and correct agent errors in real-time and provide valuable data for retraining.  
* **Dashboards and Reporting** - Google Cloud provides a default dashboard for Vertex AI Agent Engine, often called "Vertex AI Agent Engine Overview," which displays key performance indicators at a glance. Custom dashboards can be built using Cloud Monitoring and integrating with third-party monitoring tools like Datadog.  
_By leveraging these metrics and monitoring capabilities, oragnizations can ensure that Vertex AI agents are performing optimally, identify and resolve issues quickly, and continuously improve their effectiveness in production._


## SmartReach's Future Reach
* SmartReach supports integration with a wide range of CRM systems (e.g., SAP, Salesforce), enabling access to customer records and call transcripts.
* It can easily connect with diverse Incident Management Systems (like ServiceNow, BMC Helix ITSM) to enhance workflow efficiency.
