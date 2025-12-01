class KBRetrieverAgent:
    async def retrieve(self, message_text: str):
        kb = [
            {"id": "kb_001", "title": "How to check order status", "snippet": "Go to Orders > Track Order."},
            {"id": "kb_002", "title": "Refund policy", "snippet": "Refunds processed within 5-7 business days."},
            {"id": "kb_003", "title": "Reset password", "snippet": "Click 'Forgot Password' to reset via email."}
        ]
        text = message_text.lower()
        if "refund" in text:
            return [kb[1]]
        if "password" in text:
            return [kb[2]]
        if "status" in text or "where" in text:
            return [kb[0]]
        return kb[:2]
