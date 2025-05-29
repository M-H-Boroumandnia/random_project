from typing import Optional
from pydantic import BaseModel

class Message(BaseModel):
    type: str = "text"  # "text", "image", "voice", etc.
    text: Optional[str] = None
    attachment_url: Optional[str] = None
    metadata: dict = {}

class Conversation(BaseModel):
    post_token: str
    initial_message: Message