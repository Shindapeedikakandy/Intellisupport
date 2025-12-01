import random

class TriageAgent:
    async def classify(self, message_text: str) -> dict:
        text = message_text.lower()
        if "refund" in text or "money back" in text:
            intent = "refund"
        elif "password" in text or "login" in text:
            intent = "auth"
        elif "status" in text or "where is my order" in text:
            intent = "order_status"
        else:
            intent = "general"

        confidence = 0.9 if intent != "general" else float(0.5 + 0.4 * random.random())
        severity = "high" if "urgent" in text or "immediately" in text else "normal"
        return {"intent": intent, "confidence": confidence, "severity": severity}
