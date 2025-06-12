from google.adk.agents import Agent
from .tools.tools import get_current_date, search_tool



root_agent = Agent(
    name='telecom_agent_main',
    description="A bot that grrets user",
    model="gemini-2.0-flash",
    instruction="""
    You are a helpful assistant that greets user with their name.
    Ask zodiac sign of user. 
    Call sub_agent with zodiac sign as a input.
    - basic_agent
    """,
    tools=[get_current_date, search_tool],
)
