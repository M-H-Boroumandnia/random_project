# src/cli.py

import asyncio
from agent.multi_session import run_research_sessions
from data.models import UserProfile ,ResearchPrompt 
from dotenv import load_dotenv
import os
load_dotenv(".env.example")
print(os.getenv('METIS_API_KEY'))
prompt = ResearchPrompt(
    prompt_id="p1",
    system_template="You are a helpful assistant helping a user from {city} looking for {listing_title}.",
    user_prompt="What are your thoughts on the new feature?plaese answer in english"
)


users = [
    UserProfile(user_id="user1", name="Alice", city="Tehran", listing_title="Used Phone", preferences=["tech", "gadgets"]),
    UserProfile(user_id="user2", name="Bob", city="Shiraz", listing_title="Bike for Sale", preferences=["sports", "outdoors"]),
    UserProfile(user_id="user3", name="Charlie", city="Tabriz", listing_title="Apartment Rental", preferences=["real estate"]),
]

async def start():
    results = await run_research_sessions(prompt, users)
    print(results)

if __name__ == "__main__":
    asyncio.run(start())
