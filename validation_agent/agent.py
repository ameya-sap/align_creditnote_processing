from google.adk.agents import LlmAgent
from .tools import query_policy, map_reason_to_category

validation_agent = LlmAgent(
    name="validation_agent",
    model="gemini-2.5-flash",
    instruction="""You are the Validation and Policy Agent.
    Your role is to enforce business logic and contract compliance.
    Use query_policy to fetch relevant policies from ChromaDB. 
    Use map_reason_to_category to normalize reasons (e.g. PSA to Clinical & Product Deficiency).
    Validate if the provided request meets regional and policy requirements.""",
    tools=[query_policy, map_reason_to_category]
)
