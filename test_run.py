import asyncio
import os
import sys

# Ensure the root directory is in the Python path for imports
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from agent import root_agent

async def main():
    print("Starting agent flow...")
    print("Executing 'Analyze SFDC Ticket #61860676'...\n")
    
    # We clear the adk session cache to ensure a fresh run for testing
    if os.path.exists(".adk/session.db"):
        os.remove(".adk/session.db")
        
    async for event in root_agent.run_async("Analyze SFDC Ticket #61860676"):
        print(f"[{event.author}]: {event.text}")

if __name__ == "__main__":
    asyncio.run(main())
