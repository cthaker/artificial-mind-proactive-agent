from google.genai import types
from typing import Optional, List, Dict
from pydantic import BaseModel, Field

from google.adk.tools.tool_context import ToolContext
import json

from twilio.rest import Client
from google.cloud import bigquery

# Twilio configuration
account_sid = 'ACce58d36458dd385cdc2dd739a984d0c4'
auth_token = '<TWILIO_AUTH_TOKEN>'
twilio_number = '+18483613765'
recipient_number = '<RECIPIENT_PHONE_NUMBER>'
client = Client(account_sid, auth_token)

# BigQuery configuration
PROJECT_ID = "hacker2025-team-1-dev"
DATASET_ID = "BillingData"
TABLE_ID = "BillingStatement"

# Schemas
class BillEvent(BaseModel):
    accountId: int 
    eventName: str
    eventDescription: Optional[str] 
    eventDate: str # ISO 8601 format (e.g., "2023-10-01")
    chargeOrCredit: str
    eventAmount: float
    eventBillSection: str = Field(
        default="One Time Charges or Credits",
        description="The section of the bill where this event is recorded, e.g., 'Monthly Services', 'Taxes and Fees', 'One Time Charges or Credits', etc."
    )
    eventBillSubSection: str = Field(
        default="Internet",
        description="The sub-section of the bill where this event is recorded, e.g., 'Internet', 'TV/Cable', 'Voice' etc."
    )

class BillSubSection(BaseModel):
    sectionName: str
    sectionDescription: Optional[str]
    sectionAmount: float = 0.0

class BillSection(BaseModel):
    sectionName: str
    sectionAmount: float = 0.0
    subSections: Optional[List[BillSubSection]] = Field(
        default_factory=list,
        description="A list of sub-sections within this bill section."
    )

class BillExport(BaseModel):
    accountId: int
    billDate: str # ISO 8601 format (e.g., "2023-10-01")
    balanceDue: float = 0.0
    billSections: List[BillSection] = Field(
        default_factory=list,
        description="A list of sections in the bill, each containing sub-sections."
    )    

# Tools 
def save_bill_events_to_state(
    tool_context: ToolContext,
    bill_events: List[BillEvent]
) -> dict[str, str]:
    """Saves the list of BillEvent objects to state["bill_events"].

    Args:
        bill_events [BillEvent]: a list of BillEvent objects to add to the list of bill events

    Returns:
        dict[str, str]: A status message indicating success
    """
    # Load existing bill_events from state. If none exist, start an empty list
    existing_bill_events = tool_context.state.get("bill_events", [])

    # Update the 'bill_events' key with a combo of old and new lists.
    # When the tool is run, ADK will create an event and make
    # corresponding updates in the session's state.
    tool_context.state["bill_events"] = existing_bill_events + bill_events

    # A best practice for tools is to return a status message in a return dict
    return {"status": "success"}

def get_bill_export(
    tool_context: ToolContext,
    accountId: str
) -> dict[str, str]:
    """Saves the last Bill Export for the accountId to state["bill_export"].

    Args:
        tool_context (ToolContext): The context of the tool, which includes the state.
        accountId (str): The account ID for which the bill export is being saved.

    Returns:
        dict[str, str]: A status message indicating success or failure.
    """

    bill_history = fetch_bill_history(accountId=accountId)
    tool_context.state["bill_history"] = bill_history

    if bill_history:
        print(f"Bill History for {accountId}:")
        for row in bill_history:
            print(bill_history[0])  
    else:
        print(f"No bill history found for {accountId}.")

    # Convert dictionary to JSON string
    json_string = json.dumps(bill_history[0], indent=4, default=str)
    print(f"JSON String: {json_string}")

    try:
        bill_export = BillExport.model_validate_json(json_string)  
        # Save the bill export to the state
        tool_context.state["bill_export"] = bill_export
    except Exception as e:
        print(f"Error: {e}")
        return {"status": "error", "message": f"Failed to save bill export for accountId {accountId}: {str(e)}"}
       
    return {"status": "success", "message": f"Bill export for accountId {accountId} loaded successfully."}
 
# Note: The above function is a mock implementation. In a real-world scenario, you would fetch the bill export from a database or an API.

def fetch_bill_history(
    accountId: str,
) -> list[dict]:
    """Fetches the billing history for a given account ID.

    Args:
        accountId (str): The account ID for which to fetch the billing history.

    Returns:
        list[dict]: A list of dictionaries, where each dictionary represents a row from the BillingStatement table.
                     Returns an empty list if no data is found or if an error occurs.
    """
    try:
        client = bigquery.Client(project=PROJECT_ID)
        query = f"""
            SELECT *
            FROM `{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}`
            WHERE accountId = {accountId}
            ORDER BY billDate DESC LIMIT 1
        """
        query_job = client.query(query)
        results = query_job.result()
        
        return [dict(row) for row in results]
    except Exception as e:
        print(f"Error fetching billing history for accountId {accountId}: {e}")
        return []  # Return an empty list if an error occurs or no data is found

def convert_bill_export_in_user_freiendly_format(
    tool_context : ToolContext,
) -> str:
    """Formats the BillExport object saved in state into a user-friendly string.

    Args:
        tool_context (ToolContext): The context of the tool, which includes the state.

    Returns:
        str: A user-friendly string representation of the bill export.
    """
    bill_export = tool_context.state.get("bill_export")
    if not bill_export:
        return "No bill export available in the state."
    sections = []
    for section in bill_export.billSections:
        sub_sections = []
        for sub_section in section.subSections:
            sub_sections.append(f"{sub_section.sectionName} ({sub_section.sectionAmount})")
        sections.append(f"{section.sectionName}: {', '.join(sub_sections)} (Total: {section.sectionAmount})\n")

    return (
        f"Account ID: {bill_export.accountId}\n"
        f"Bill Date: {bill_export.billDate}\n"
        f"Balance Due: {bill_export.balanceDue}\n"
        f"Sections:\n" + "\n".join(sections)
    )

def send_sms(message_body: str) -> dict:
    """
    Placeholder function to send SMS.
    This function can be implemented to send SMS messages.
    :param recipient_number: The phone number to send the SMS to.
    :param message_body: The body of the SMS message.
    :return: A dictionary containing the message instance.
    """
    message = client.messages.create(
        body=message_body,
        from_=twilio_number,
        to=recipient_number
        )
    return {"message_instance": message.sid} 
