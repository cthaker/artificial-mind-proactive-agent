from google.adk.agents import Agent
from google.adk.tools import google_search
from .prompt import INSTRUCTIONS

# Create a Google Search tool instance
# This tool allows the agent to perform web searches using Google
search_agent = Agent(
    name="search_agent",
    model="gemini-2.0-flash",
    description="A bot that performs web searches",
    instruction=INSTRUCTIONS,
    tools=[google_search],
)