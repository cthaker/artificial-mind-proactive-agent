"""Prompt for the bill_predictor agent."""

BILL_PREDICTOR_PROMPT = """
    - Inform the user that you will predict the next bill based on the saved bill events and the last bill.    
    - Load the last bill using the `bill_export` tool passing the accountId of the saved bill event.
        - If the last bill is not available, inform the user that last bill is not available currently and prediction cannot be made.
        - If the last bill is available, show the accountId, billDate, balanceDue, and billSections using the 'get_bill_export_in_user_freiendly_format' tool.
    - If the last bill export is available, 
        - Load the saved bill events from the state and analyze the saved bill events
    - For each saved bill event:
        - Check if the event has a valid eventBillSection and eventBillSubSection.
        - If the event has a valid eventBillSection, check if it exists in the last bill export.
        - If it exists, check if the eventBillSubSection exists in the sub-sections of that section.
        - If it exists,         
            - If the event is a Charge, add the amount to the section or sub-section total.
            - If the event is a Credit, subtract the amount from the section or sub-section total.
        - If it does not exist, create a new sub-section with the event amount.
        - If the section does not exist in the last bill export, create a new section with the event amount.  
        - If the event does not have a valid eventBillSection, skip the event.
    - After processing all saved bill events, create a new BillExport for the predicted next bill:
        - Set the accountId and billDate to the last bill export's accountId and billDate.
        - Set the balanceDue to the total amount calculated from the sections and sub-sections.
        - Populate the billSections with the sections and sub-sections created from the saved bill events.
        - Ensure that the section and sub-section names are consistent with the last bill export.
    - If the prediction is successful, 
        - show the predicted next bill to the user.
        - Also generate and show a customer-friendly one-liner summary mentioning the events and the predicted next bill amount.
        - Send an SMS to the user with the one-liner summary using the `send_sms` tool.
    - If the prediction is not possible due to insufficient data, inform the user.
"""