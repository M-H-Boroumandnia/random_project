# multi_session.py
# src/agent/multi_session.py

import asyncio
import random
from typing import List, Dict, Any

from agent.conversation import ConversationHandler
from integrations.llm_client import OpenAIGPTClient, GeminiClient, DeepSeekClient
from data.models import ResearchPrompt, UserProfile
from utils.display import print_info

# Agent wrapper with load tracking
class AgentInstance:
    def __init__(self, name: str, client):
        self.name = name
        self.client = client
        self.active_sessions = 0

    async def run_conversation(self, prompt: ResearchPrompt, user: UserProfile) -> Dict[str, Any]:
        self.active_sessions += 1
        try:
            handler = ConversationHandler(llm_client=self.client)
            result = await handler.run(prompt, user)
            return result
        finally:
            self.active_sessions -= 1

# Multi-agent load balancer
class MultiAgentOrchestrator:
    def __init__(self):
        self.agents = [
            AgentInstance("DeepSeek" , DeepSeekClient()),
            AgentInstance("GPT-4", OpenAIGPTClient()),
            AgentInstance("Gemini", GeminiClient()),
        ]

    def get_least_loaded_agent(self) -> AgentInstance:
        # Find the minimum active sessions count
        min_load = min(agent.active_sessions for agent in self.agents)

        # Filter agents with that minimum load
        least_loaded_agents = [agent for agent in self.agents if agent.active_sessions == min_load]

        # Choose one randomly among the least loaded agents to distribute load evenly
        chosen_agent = random.choice(least_loaded_agents)
        return chosen_agent

    async def run_conversations(self, prompt: ResearchPrompt, users: List[UserProfile]) -> List[Dict[str, Any]]:
        tasks = []
        for user in users:
            agent = self.get_least_loaded_agent()
            print_info(f"Assigning user {user.user_id} to agent {agent.name}")
            tasks.append(agent.run_conversation(prompt, user))
        return await asyncio.gather(*tasks)

# Entry for CLI
async def run_research_sessions(prompt: ResearchPrompt, users: List[UserProfile]):
    orchestrator = MultiAgentOrchestrator()
    results = await orchestrator.run_conversations(prompt, users)
    return results
