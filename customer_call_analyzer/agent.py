
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from .prompt import INSTRUCTIONS
from .sub_agents.call_analyzer.agent import call_analyzer_agent
from .sub_agents.past_call_analyzer.agent import past_call_analyzer_agent


call_analyzer_tool = AgentTool(call_analyzer_agent)
past_call_analyzer_tool = AgentTool(past_call_analyzer_agent)

root_agent = Agent(
    name='customer_call_analyzer',
    description="A bot that analyzes customer calls and provides insights based on the call transcript/recording provided by user or stored in Data store.",
    model="gemini-2.0-flash",
    instruction=INSTRUCTIONS,
    tools=[call_analyzer_tool, past_call_analyzer_tool],
    
)
