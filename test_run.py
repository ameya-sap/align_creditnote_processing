import subprocess
import os
import sys

def main():
    print("Starting agent flow...")
    print("Executing 'Analyze SFDC Ticket #61860676'...\n")
    
    # We clear the adk session cache to ensure a fresh run for testing
    if os.path.exists(".adk/session.db"):
        os.remove(".adk/session.db")
        
    # We run the adk CLI directly, piping in the input commands needed.
    # The 'exit' command ensures it closes cleanly after processing.
    process = subprocess.Popen(
        ["adk", "run", "."],
        stdin=subprocess.PIPE,
        text=True
    )
    
    try:
        process.communicate(input="Analyze SFDC Ticket #61860676\nexit\n")
    except KeyboardInterrupt:
        process.kill()

if __name__ == "__main__":
    main()
