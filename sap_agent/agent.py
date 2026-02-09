from google.adk.agents import LlmAgent
from .tools import fetch_sap_export, check_prior_credits

sap_agent = LlmAgent(
    name="sap_agent",
    model="gemini-2.5-flash",
    instruction="""You are the SAP Integration Agent.
    Use fetch_sap_export to get the raw invoice details from SAP for a given Sales Order.
    Use check_prior_credits to verify that a sales order has no prior credits to prevent duplicates.""",
    tools=[fetch_sap_export, check_prior_credits]
)
