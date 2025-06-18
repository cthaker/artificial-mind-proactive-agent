from google.adk.agents import Agent
from ...tools.tools import bill_export, get_bill_export_in_user_freiendly_format

from . import prompt

# Agents

bill_predictor = Agent(
    name='bill_predictor',
    description="Compare the last bill against the saved bill events and predict next bill",
    model="gemini-2.0-flash",
    instruction=prompt.BILL_PREDICTOR_PROMPT,
    tools=[bill_export, get_bill_export_in_user_freiendly_format],
#    sub_agents=[notification_agent]  
)
