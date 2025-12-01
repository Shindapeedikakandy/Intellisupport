import uuid
from datetime import datetime

_TICKETS = []

class TicketAPI:
    def create_ticket(self, payload: dict) -> dict:
        ticket = {
            "id": str(uuid.uuid4()),
            "customer_id": payload.get("customer_id"),
            "subject": payload.get("subject"),
            "body": payload.get("body"),
            "priority": payload.get("priority", "normal"),
            "status": "open",
            "created_at": datetime.utcnow().isoformat()
        }
        _TICKETS.append(ticket)
        return ticket

    def list_tickets(self):
        return _TICKETS
