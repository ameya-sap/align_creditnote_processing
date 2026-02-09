from google.adk.agents import LlmAgent
from .tools import calculate_discount, generate_zmemo_csv

calculation_agent = LlmAgent(
    name="calculation_agent",
    model="gemini-2.5-flash",
    instruction="""You are the Calculation Agent.
    calculate_discount helps you apply percentage logic to net amounts.
    Use generate_zmemo_csv to compile the final approved credit lines into the required batch file format.""",
    tools=[calculate_discount, generate_zmemo_csv]
)
