
from google.adk.agents import Agent
from .sub_agents.outage_agent.agent import outage_agent




root_agent = Agent(
    name='agent_main',
    description="A bot that grrets user",
    model="gemini-2.0-flash",
    instruction="""
    You are a helpful assistant that greets user with their name.
    Ask zodiac sign of user. 
    Call sub_agent with zodiac sign as a input.
    - basic_agent
    If user inputs outage details, call below sub_agent:
    - outage_agent
    """,
    sub_agents=[outage_agent]
)
