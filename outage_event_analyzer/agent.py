
from google.adk.agents import Agent
from .sub_agents.outage_agent.agent import outage_agent
from .prompt import INSTRUCTIONS



root_agent = Agent(
    name='outage_agent_main',
    description="A bot that greets user and handles telecom outages",
    model="gemini-2.0-flash",
    instruction=INSTRUCTIONS,
    sub_agents=[outage_agent]
)
