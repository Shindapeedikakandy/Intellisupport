from datetime import datetime

class ResponseAgent:
    async def generate(self, message_text: str, kb_results: list, triage_res: dict) -> dict:
        intent = triage_res.get("intent", "general")
        snippets = "\n".join([f"- {item['title']}: {item['snippet']}" for item in kb_results])
        reply_text = (
            f"Hi — thanks for contacting support about {intent}.\n"
            f"Helpful resources:\n{snippets}\n\n"
            "If this doesn't solve your issue, reply and we'll assist further."
        )
        return {"text": reply_text, "created_at": datetime.utcnow().isoformat()}
