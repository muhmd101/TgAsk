from TgAsk.config import OPENAI_API_KEY, OPENAI_API_BASE, OPENAI_API_MODEL, SYSTEM_PROMPT
from TgAsk.config import API_ID, API_HASH, BOT_TOKEN
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from TgAsk.tools import ALL_TOOLS
from TgAsk.logger import LOGGER
from pyrogram import Client
import pyromod
pyromod.config.disable_startup_logs = True

log = LOGGER(__name__)

class session(Client):
    def __init__(self):
        super().__init__(
            name="TgASK",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(
                root="TgAsk.plugins",
            ),
        )
        log.info("Initializing LLM with model: %s", OPENAI_API_MODEL)
        llm = ChatOpenAI(
            model=OPENAI_API_MODEL,
            openai_api_key=OPENAI_API_KEY,
            openai_api_base=OPENAI_API_BASE,
            max_tokens=4096,
        )
        log.info("Creating agent with %d tools", len(ALL_TOOLS))
        self.agent = create_agent(
            model=llm,
            tools=ALL_TOOLS,
            system_prompt=SYSTEM_PROMPT
        )
        log.info("Agent created successfully")


app = session()