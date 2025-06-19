from google.genai import types
from typing import Optional, List, Dict
from pydantic import BaseModel, Field

from google.adk.tools.tool_context import ToolContext
import json

from twilio.rest import Client

account_sid = 'ACce58d36458dd385cdc2dd739a984d0c4'
auth_token = '3d943ceb3a2087894f643858cd5138a5'
twilio_number = '+18483613765'
recipient_number = '+12269617507'
client = Client(account_sid, auth_token)

# Schemas
class BillEvent(BaseModel):
    accountId: str 
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
    accountId: str
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


def bill_export(
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

    json_data = """
    {
        "accountId": "37715101",
        "billDate": "2025-05-20",
        "balanceDue": 135.00,
        "billSections": [
            {
                "sectionName": "Monthly Services",
                "sectionAmount": 90.00,
                "subSections": [
                    {
                        "sectionName": "Internet",
                        "sectionDescription": "High-speed internet service",
                        "sectionAmount": 40.00
                    },
                    {
                        "sectionName": "TV",
                        "sectionDescription": "Premium Cable TV",
                        "sectionAmount": 30.00
                    },
                    {
                        "sectionName": "Telephone",
                        "sectionDescription": "Home phone service",
                        "sectionAmount": 20.00
                    }				
                ]
            },
            {
                "sectionName": "One Time Charges or Credits",
                "sectionAmount": 25.00,
                "subSections": [
                    {
                        "sectionName": "Late Payment Fee",
                        "sectionDescription": "Late payment fee for the previous month",
                        "sectionAmount": 25.00
                    }			
                ]
            },
            {
                "sectionName": "Taxes and Fees",
                "sectionAmount": 20.00,
                "subSections": [
                    {
                        "sectionName": "Federal Tax",
                        "sectionDescription": "Federal tax on services",
                        "sectionAmount": 10.00
                    },
                    {
                        "sectionName": "State Tax",
                        "sectionDescription": "State tax on services",
                        "sectionAmount": 10.00
                    }                    			
                ]
            }            		
        ]
    }
    """

    try:
        bill_export = BillExport.model_validate_json(json_data)
        # Save the bill export to the state
        if bill_export.accountId != accountId:
            raise ValueError(f"Bill Export Not found for Account ID {accountId}")
        tool_context.state["bill_export"] = bill_export
    except Exception as e:
        print(f"Error: {e}")
        return {"status": "error", "message": f"Failed to save bill export for accountId {accountId}: {str(e)}"}
       
    return {"status": "success", "message": f"Bill export for accountId {accountId} loaded successfully."}
 
# Note: The above function is a mock implementation. In a real-world scenario, you would fetch the bill export from a database or an API.

def get_bill_export_in_user_freiendly_format(
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