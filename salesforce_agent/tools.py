import json

def update_sfdc_ticket(ticket_number: str, status: str, comments: str) -> str:
    """Mocks updating a Salesforce ticket record."""
    return f"Ticket {ticket_number} successfully updated to status '{status}' with comments."

def send_approval_email(to: str, subject: str, body: str) -> str:
    """Mocks sending an approval email."""
    # Just printing or logging it for the prototype
    print(f"--- MOCK EMAIL TO: {to} ---\nSubject: {subject}\n\n{body}\n--------------------")
    return f"Email sent successfully to {to}"
