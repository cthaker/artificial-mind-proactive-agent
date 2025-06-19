from datetime import datetime
from google.adk import Agent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool
from twilio.rest import Client

account_sid = 'ACce58d36458dd385cdc2dd739a984d0c4'
auth_token = '3d943ceb3a2087894f643858cd5138a5'
twilio_number = '+18483613765'
recipient_number = '+12269617507'
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
def get_current_date() -> dict:
    """
    Get the current date in the format YYYY-MM-DD
    """
    return {"current_date": datetime.now().strftime("%Y-%m-%d")}

search_agent = Agent(
    name="search_agent",
    model="gemini-2.0-flash",
    description="A bot that performs web searches",
    instruction="""
    You can use the google_search tool to find information on the web.
    Use this tool when you need to answer questions that require up-to-date information or general knowledge.
    """,
    tools=[google_search],
)

search_tool = AgentTool(search_agent)