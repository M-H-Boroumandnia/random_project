from typing import Dict, Any
from data.models import ResearchPrompt, UserProfile
from utils.display import print_info
from utils.vector_store import VectorStore  # your wrapper

class ConversationHandler:
    def __init__(self, llm_client, vector_store: VectorStore):
        self.llm = llm_client
        self.vdb = vector_store  # vector DB handler

    async def run(self, prompt: ResearchPrompt, user: UserProfile) -> Dict[str, Any]:
        history = []
        chat_id = f"{user.user_id}-{prompt.prompt_id}"  # Unique session ID

        print_info(f"Starting conversation with {user.name} (ID: {user.user_id})")

        # System + user prompt
        system_prompt = prompt.system_template.format(**use# conversation.py
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
r.dict())
        user_question = prompt.user_prompt.format(**user.dict())

        history.append({"role": "system", "content": system_prompt})
        history.append({"role": "user", "content": user_question})

        # Store initial prompts
        self.vdb.add(chat_id, "system", system_prompt)
        self.vdb.add(chat_id, "user", user_question)

        # Get response from LLM
        response = await self.llm.chat(history)
        history.append({"role": "assistant", "content": response})

        # Store assistant response
        self.vdb.add(chat_id, "assistant", response)

        return response
