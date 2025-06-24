
from google.adk.agents import Agent
from .prompt import INSTRUCTIONS
from .tools import create_new_ticket, send_sms


call_analyzer_agent = Agent(
    name='call_analyzer',
    description="A bot that analyzes customer calls and provides insights based on the call transcript or recording.",
    model="gemini-2.0-flash",
    instruction=INSTRUCTIONS,
    tools=[create_new_ticket, send_sms,]
)
