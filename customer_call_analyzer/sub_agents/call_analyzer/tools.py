from jira import JIRA
from google.adk.tools.agent_tool import AgentTool
from twilio.rest import Client

account_sid = '<TWILIO_SID>'
auth_token = '<TWILIO_AUTH_TOKEN>'
twilio_number = '+18483613765'
recipient_number = '<RECIPIENT_PHONE_NUMBER>'
client = Client(account_sid, auth_token)

def send_sms(message_body: str) -> dict:
    """
    Placeholder function to send SMS.
    This function can be implemented to send SMS messages.
    :param recipient_number: The phone number to send the SMS to.
    :param message_body: The body of the SMS message.
    :return: A dictionary containing the message instance.
    """
    message = client.messages.create(
        body=message_body,
        from_=twilio_number,
        to=recipient_number
        )
    return {"message_instance": message.sid} 

JIRA_URL = "https://cap-artificial-minds.atlassian.net/"
EMAIL = "sandeep.3028@gmail.com"
API_TOKEN = "<JIRA_AUTH_TOKEN>"

 
 
#Create an issue
def create_new_ticket(summary: str, description: str,resolution: list[str])-> dict:
    """
    Create new ticket in the specified JIRA project.
    :return: new ticket link"""
    jira_client = JIRA(server=JIRA_URL, basic_auth=(EMAIL, API_TOKEN))
    project_key = "KAN"
    if(summary.__len__() == 0):
        summary = "No summary found on the web search results."
    if(description.__len__() == 0):
        description = "No description found on the web search results."
    issue_dict = {
        'project': {'key': project_key},
        'summary': summary,
        'description': description,
        'issuetype': {'name': 'Task'}
    }
    new_issue = jira_client.create_issue(fields=issue_dict)
    print(f"Issue created: {new_issue.key}")
    return {"ticket_link":new_issue.permalink()}
 
