
from google.adk.agents import Agent
from google.adk.tools import VertexAiSearchTool
from .prompt import INSTRUCTIONS

vertexai_search_tool = VertexAiSearchTool(
   data_store_id="projects/hacker2025-team-1-dev/locations/global/collections/default_collection/dataStores/call-transcripts_1750540514195"
)

past_call_analyzer_agent = Agent(
    name='past_call_analyzer',
    description="Answer questions using your data store access.",
    model="gemini-2.0-flash",
    instruction=INSTRUCTIONS,
    tools=[vertexai_search_tool]
)
