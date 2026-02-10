from google.adk.agents import LlmAgent
from .tools import fetch_sap_export, check_prior_credits

sap_agent = LlmAgent(
    name="sap_agent",
    model="gemini-2.5-flash",
    instruction="""You are the SAP Integration Agent.
    Use fetch_sap_export to get the raw invoice details from SAP for a given Sales Order.
    Use check_prior_credits to verify that a sales order has no prior credits to prevent duplicates.
    
    IMPORTANT: When you summarize the found SAP data for the next agent, you MUST NOT summarize or truncate the raw SAP export dictionary. You MUST pass the ENTIRE dictionary verbatim in your output so the Calculation Agent has all 29 columns to work with.""",
    tools=[fetch_sap_export, check_prior_credits]
)
