from pydantic import BaseModel
from typing import Optional, Literal
from uuid import UUID
from datetime import datetime

class BaseMessage(BaseModel):
    message_id: UUID
    timestamp: datetime

class DialogueMessage(BaseMessage):
    type: Literal["agent_message", "agent_json", "user_message"]
    agent_message: Optional[str]
    agent_json: Optional[dict]
    user_message: Optional[str]
