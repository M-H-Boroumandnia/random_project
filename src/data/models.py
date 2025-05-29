# models.py
# src/data/models.py

from pydantic import BaseModel
from typing import List, Optional

class ResearchPrompt(BaseModel):
    prompt_id: str
    system_template: str
    user_prompt: str

class UserProfile(BaseModel):
    user_id: str
    name: str
    city: Optional[str]
    listing_title: Optional[str]
    preferences: Optional[List[str]] = []
