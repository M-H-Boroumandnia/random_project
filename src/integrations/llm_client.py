# llm_client.py
# src/integrations/llm_client.py

import os
import openai
from typing import List, Dict
from openai import OpenAI
import httpx
import google.generativeai as genai
from google.api_core.client_options import ClientOptions
# Base interface
class LLMClient:
    async def chat(self, messages: List[Dict[str, str]]) -> str:
        raise NotImplementedError

    async def extract_summary(self, messages: List[Dict[str, str]]) -> str:
        raise NotImplementedError

class OpenAIGPTClient(LLMClient):
    def __init__(self):
        self.api_key = os.getenv("METIS_API_KEY")
        self.client = OpenAI(api_key=self.api_key, base_url="https://api.metisai.ir/openai/v1")

    async def chat(self, messages: List[Dict[str, str]]) -> str:
        # Note: The OpenAI python client is sync, so we run it in threadpool or change to sync method
        # Here for simplicity, assuming sync usage wrapped in async
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )
        return response.choices[0].message.content.strip()

    async def extract_summary(self, messages: List[Dict[str, str]]) -> str:
        messages.append({"role": "user", "content": "لطفاً این مکالمه را خلاصه کن."})
        return await self.chat(messages)

class GeminiClient(LLMClient):
    def __init__(self):
        self.api_key = os.getenv("METIS_API_KEY")
        genai.configure(
            api_key=self.api_key,
            transport="rest",
            client_options=ClientOptions(api_endpoint="https://api.metisai.ir")
        )
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    async def chat(self, messages: List[Dict[str, str]]) -> str:
        # Convert your messages list to a single prompt text
        prompt = "\n".join(m['content'] for m in messages if m['role'] == 'user' or m['role'] == 'system')
        response = self.model.generate_content(prompt)
        return response.text.strip()

    async def extract_summary(self, messages: List[Dict[str, str]]) -> str:
        messages.append({"role": "user", "content": "please summarize this conversation"})
        return await self.chat(messages)

class DeepSeekClient(LLMClient):
    def __init__(self):
        self.api_key = os.getenv("METIS_API_KEY")
        self.endpoint = "https://api.metisai.ir/api/v1/wrapper/deepseek/chat/completions"

    async def chat(self, messages: List[Dict[str, str]]) -> str:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        payload = {
            "model": "deepseek-chat",
            "messages": messages
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(self.endpoint, headers=headers, json=payload , timeout = 60)
            response.raise_for_status()
            data = response.json()
            
            messages = data["choices"][0]['message']['content']

            #print(messages)
            #assistant_messages = [msg for msg in messages if msg['role'] == 'assistant']

            #if assistant_messages:
            #    chatbot_answer = assistant_messages[-1]['content']
            #else:
            #    chatbot_answer = None

            return messages

    async def extract_summary(self, messages: List[Dict[str, str]]) -> str:
        messages.append({"role": "user", "content": "please summerize this conversation"})
        return await self.chat(messages)