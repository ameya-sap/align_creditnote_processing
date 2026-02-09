from google.adk.agents import LlmAgent
from .tools import update_sfdc_ticket, send_approval_email

salesforce_agent = LlmAgent(
    name="salesforce_agent",
    model="gemini-2.5-flash",
    instruction="""You are the Salesforce & Communication Agent.
    Once processing is complete, use update_sfdc_ticket to attach logs to the specified ticket ID.
    Use send_approval_email to notify the requester or relevant managers if approval limits are exceeded.""",
    tools=[update_sfdc_ticket, send_approval_email]
)
