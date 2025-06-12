from datetime import datetime
from google.adk import Agent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool

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