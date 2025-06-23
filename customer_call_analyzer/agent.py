
from google.adk.agents import Agent
from .tools import tts_using_google, tts_using_microsoft, concatenate_audio_files
from google.adk.tools import VertexAiSearchTool

vertexai_search_tool = VertexAiSearchTool(
   data_store_id="projects/hacker2025-team-1-dev/locations/global/collections/default_collection/dataStores/call-transcripts_1750540514195"
)

root_agent = Agent(
    name='customer_call_analyzer',
    description="Answer questions using your data store access.",
    model="gemini-2.0-flash",
    instruction="""
    You are a helpful assistant that greets user with their name.
    Analyze recording and transcript of customer calls present in data store.
    Use the Vertex AI Search tool to search for relevant information in the data store.
    Answer user questions about the calls using the tools provided. 
    """,
    tools=[vertexai_search_tool]
)
