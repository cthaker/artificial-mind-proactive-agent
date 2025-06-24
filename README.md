# Telecom Agent


### Project Structure
```
.
├── README.md
├── pyproject.toml
├── telecom_agent_main/
│   └── sub_agents/
│       ├── greeting_agent/
├── tests/
│   └── unit/
├── eval/
│   └── data/
└── deployment/
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
12. gcloud auth application-default login (update values in .env)
13. gcloud init (Select project-id)

Run adk web to launch ADK Dev UI (or use ADK CLI)

# Google Cloud Platform Project Information
  > Project Name: Team Alpha - Innovation
  > Project ID: hacker2025-team-1-dev

# BigQuery Information
  > Service Account: dbconnect
 
  > DataSet: BillingData

  > Table: BillingStatement
  
  > Data imported in BillingStatement

# Cloud Storage Information
  > Service Account: dbconnect

# JIRA (Incident Management System)
  > JIRA Project: https://cap-artificial-minds.atlassian.net/jira/software/projects/KAN/boards/1


