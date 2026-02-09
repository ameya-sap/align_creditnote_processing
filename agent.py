from google.adk.agents import SequentialAgent, LlmAgent
from .shared.document_parsers import extract_sales_orders_from_pdf, parse_csv_to_dict
from .validation_agent.agent import validation_agent
from .sap_agent.agent import sap_agent
from .calculation_agent.agent import calculation_agent
from .salesforce_agent.agent import salesforce_agent

# Intake Agent
intake_agent = LlmAgent(
    name="intake_agent",
    model="gemini-2.5-flash",
    instruction="""You are the Intake Orchestrator.
    Extract the list of Sales Orders and details from the provided SFDC ticket attachments (the file is located at `Sample Data/File1-SFDC-Credit-Request-Ticket.pdf`) using extract_sales_orders_from_pdf.
    Pass the clear context and extracted structured data forward to the next steps.""",
    tools=[extract_sales_orders_from_pdf]
)

# Root Orchestrator
root_agent = SequentialAgent(
    name="credit_note_processor",
    sub_agents=[
        intake_agent,
        validation_agent,
        sap_agent,
        calculation_agent,
        salesforce_agent
    ]
)
