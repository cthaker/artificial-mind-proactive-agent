from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools import google_search
from .tools import read_all_tickets, create_new_ticket, send_sms

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


outage_agent = Agent(
    name='outage_agent',
    description="A bot that handles telecom outages",
    model="gemini-2.0-flash",
    instruction="""
    You are a helpful assistant that takes outage event as input.
    Use the below tool to read the outage events from the JIRA project without asking any additional details.
    - read_all_tickets
    Check if the given outage information is similar to any existing outage events listed by read_all_tickets .
    If the outage event is similar/related to any existing outage events having status as 'TODO' Or 'IN_PROGRESS'.
    Then inform the user that the outage event is already being handled by the team and do not send notification.
    If the outage event is similar/related to any existing outage events having status as 'DONE' or 'CLOSED'.
    Then create a new ticket in the JIRA project with the summary and description to existing ticket.
    - create_new_ticket
    if the outage event is not similar/related to any existing outage events in the suumary then search the web for similar outage events.
    - search_tool
    If outage information is not found in the search results, then
    create a new ticket in the JIRA project with the summary, description and resolution with the help of the user.
    If the outage information is found in the search results, then
    create a new ticket with the summary and troubleshooting steps as a description .
    - create_new_ticket
    Share the ticket link with the user and suggest the user to update the ticket with any additional information if required.
    send notification to the support team with the ticket link and the summary of the outage event.
    - send_sms
    """,
    tools=[read_all_tickets, create_new_ticket, search_tool, send_sms],
)
