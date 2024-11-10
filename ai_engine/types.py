from pydantic import BaseModel
from typing import List, Optional, Literal
from enum import Enum

class UAgentResponseType(str, Enum):
    FINAL = "final"
    ERROR = "error"
    VALIDATION_ERROR = "validation_error"
    SELECT_FROM_OPTIONS = "selection_from_options"
    FINAL_OPTIONS = "final_options"

class KeyValue(BaseModel):
    key: str
    value: str

class UAgentResponse(BaseModel):
    version: Literal["v1"] = "v1"
    type: UAgentResponseType
    request_id: Optional[str]
    agent_address: Optional[str]
    message: Optional[str]
    options: Optional[List[KeyValue]]
    verbose_message: Optional[str]
    verbose_options: Optional[List[KeyValue]]

class BookingRequest(BaseModel):
    request_id: str
    user_response: str
    user_email: str
    user_full_name: str