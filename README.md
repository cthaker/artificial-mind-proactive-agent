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
2. Checkout repo from git url->https://github.com/cthaker/artificial-mind-proactive-agent.git

# Installation steps
1. Set API Key (Google Cloud Console > Credentials) in .env file
2. Add Python Scripts directory (e.g. 'C:\Program Files\Python312\Scripts') to PATH environment variable for your account
# To be executed on terminal/PowerShell
3. pip3 install poetry
3. cd artificial-mind-proactive-agent
4. poetry install
5. python -m venv .venv
6. .\.venv\Scripts\activate (for MAC-> source $(poetry env info --path)/bin/activate)
7. pip3 install google-adk
8. pip3 install twilio
9. pip3 install jira
10. pip3 install --upgrade google-cloud-bigquery
# To be executed on google cloud cli
11. gcloud auth application-default login (update values in .env)
12. gcloud init (Select project-id)

Run adk web to launch ADK Dev UI

# BigQuery  Information
  > Service Account "dbconnect" have been created for connection

  > Created New DataSet "BillingData" and table "BillingStatement"

  > Data imported in "BillingStatement" 
