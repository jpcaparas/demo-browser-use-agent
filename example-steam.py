import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
import os

from langchain_openai import AzureChatOpenAI
from pydantic import SecretStr

from browser_use.agent.service import Agent
from browser_use.browser.browser import Browser, BrowserConfig, BrowserContextConfig

browser = Browser(
	config=BrowserConfig(
		headless=False,  # This is True in production
		disable_security=True,
		new_context_config=BrowserContextConfig(
			disable_security=True,
			minimum_wait_page_load_time=1,  # 3 on prod
			maximum_wait_page_load_time=10,  # 20 on prod
			# no_viewport=True,
			browser_window_size={
				'width': 1280,
				'height': 1100,
			},
			# trace_path='./tmp/web_voyager_agent',
		),
	)
)

llm = AzureChatOpenAI(
	model='gpt-4o',
	api_version='2024-10-21',
	azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT', ''),
	api_key=SecretStr(os.getenv('AZURE_OPENAI_KEY', '')),
)

TASK = """
Go to https://store.steampowered.com/ and find the best deal for the game "Cyberpunk 2077". Also, check the reviews for that game by most recent.
"""

async def main():
	agent = Agent(
		task=TASK,
		llm=llm,
		browser=browser,
		validate_output=True,
	)
	history = await agent.run(max_steps=50)
	history.save_to_file('./tmp/history.json')


if __name__ == '__main__':
	asyncio.run(main())

