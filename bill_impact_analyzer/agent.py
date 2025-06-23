from google.adk.agents import Agent
from .sub_agents.bill_predictor import bill_predictor
from .tools.tools import save_bill_events_to_state

from . import prompt

# Agents

root_agent = Agent(
    name='bill_impact_analyzer',
    description="Analyze bill change events",
    model="gemini-2.0-flash",
    instruction=prompt.BILL_IMPACT_ANALYZER_PROMPT,
    tools=[save_bill_events_to_state],
    sub_agents=[bill_predictor]
)
