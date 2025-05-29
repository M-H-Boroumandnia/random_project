# conversation.py
# src/agent/conversation.py

from typing import Dict, Any
from data.models import ResearchPrompt, UserProfile
from utils.display import print_info

class ConversationHandler:
    def __init__(self, llm_client):
        self.llm = llm_client

    async def run(self, prompt: ResearchPrompt, user: UserProfile) -> Dict[str, Any]:
        history = []
        print_info(f"Starting conversation with {user.name} (ID: {user.user_id})")

        # System initialization
        system_prompt = prompt.system_template.format(**user.dict())
        user_question = prompt.user_prompt.format(**user.dict())

        history.append({"role": "system", "content": system_prompt})
        history.append({"role": "user", "content": user_question})

        # Generate LLM response
        response = await self.llm.chat(history)
        history.append({"role": "assistant", "content": response})

        #print_info(f"Conversation with {user.name} completed.")

        return response
