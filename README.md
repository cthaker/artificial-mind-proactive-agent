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
# Note: If Python312 is not installed on your system you can install it from Software Catalogue.
# Checkout repo from git url->https://github.com/cthaker/artificial-mind-proactive-agent.git

# Installation steps
1. Set API Key in .env file, you can get it from google cloud console under Credentials
2. Set add 'C:\Program Files\Python312\Scripts' to PATH in env for your account
# To be executed on terminal/PowerShell
3. pip3 install poetry
3. cd artificial-mind-proactive-agent
4. poetry install
5. python -m venv .venv
6. .\.venv\Scripts\activate
 for MAC-> source $(poetry env info --path)/bin/activate
7. pip3 install google-adk
# To be executed on google cloud cli
8. gcloud auth application-default login (update values in .env)
9. gcloud init (Select project-id)
11. adk web 