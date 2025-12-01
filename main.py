"""
FastAPI entrypoint for IntelliSupport prototype.
Run: uvicorn app.main:app --reload --port 8000
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.agents.coordinator import Coordinator

app = FastAPI(title="IntelliSupport - Prototype")

coordinator = Coordinator()

class MessagePayload(BaseModel):
    customer_id: str
    message_text: str
    message_id: str | None = None

@app.get("/")
async def index():
    return {"status": "ok", "service": "IntelliSupport prototype"}

@app.post("/webhook/message")
async def receive_message(payload: MessagePayload):
    """
    Endpoint to receive incoming customer messages.
    For demo purposes, this returns a generated reply and ticket id.
    """
    try:
        result = await coordinator.handle_message(payload.dict())
        return {"status": "ok", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
