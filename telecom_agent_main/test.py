from jira import JIRA
 
JIRA_URL = "https://cap-artificial-minds.atlassian.net/"
EMAIL = "sandeep.3028@gmail.com"
API_TOKEN = "ATATT3xFfGF0T7Tsahj1mziAk_R_JRywLBgcV-X4d6Zmt88euaXA_2a0Eem1cXZIVG08LY7L50Jo5EkOokKUrvS9uz6HMPyAbtSzp_ri-sDmLy2pvmoca7SYQZUxVlB2BUgdUcnqFjgmwfoUXuP3nH4W9OYVA6cfkFs_fPBELg1ykVKBzOI1Ckw=7C17B23E"
PROJECT_KEY = "KAN"
 
jira = JIRA(server=JIRA_URL, basic_auth=(EMAIL, API_TOKEN))
 
#Create an issue
def create_test_issue(jira_client, project_key):
    issue_dict = {
        'project': {'key': project_key},
        'summary': 'Test Issue from Python',
        'description': 'This is a test issue created using the JIRA Python client.',
        'issuetype': {'name': 'Task'}
    }
    new_issue = jira_client.create_issue(fields=issue_dict)
    print(f"Issue created: {new_issue.key}")
    return new_issue
 
def list_task_issues(jira_client, project_key, max_results=5):
    issues = jira_client.search_issues(f'project={project_key} AND issuetype=Task', maxResults=max_results)
    for issue in issues:
        print("==========================")
        print(f"{issue.key}: {issue.fields.summary} - {issue.fields.status.name} - {issue.fields.description}")
 
#create_test_issue(jira, PROJECT_KEY)
list_task_issues(jira, PROJECT_KEY)