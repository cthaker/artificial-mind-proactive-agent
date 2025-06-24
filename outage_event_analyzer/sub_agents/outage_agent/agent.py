from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from .tools import read_all_tickets, create_new_ticket, send_sms
from ..search_agent.agent import search_agent
from .prompt import INSTRUCTIONS



search_tool = AgentTool(search_agent)


outage_agent = Agent(
    name='outage_agent',
    description="A bot that handles telecom outages",
    model="gemini-2.0-flash",
    instruction=INSTRUCTIONS,
    tools=[read_all_tickets, create_new_ticket, search_tool, send_sms],
)
