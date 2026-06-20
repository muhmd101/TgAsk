from os import getenv
from dotenv import load_dotenv

load_dotenv()

REQUIRED_ENV = {
    "API_ID": None,
    "API_HASH": None,
    "BOT_TOKEN": None,
    "OPENAI_API_KEY": None,
    "OPENAI_API_BASE": None,
    "OPENAI_API_MODEL": None,
}

missing = [key for key, _ in REQUIRED_ENV.items() if not getenv(key)]
if missing:
    import sys
    from TgAsk.logger import LOGGER
    log = LOGGER(__name__)
    log.critical("Missing required environment variables: %s", ", ".join(missing))
    sys.exit(1)

API_ID = int(getenv("API_ID"))

API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")

OPENAI_API_KEY = getenv("OPENAI_API_KEY")

OPENAI_API_BASE = getenv("OPENAI_API_BASE")

OPENAI_API_MODEL = getenv("OPENAI_API_MODEL")

OPENWEATHERMAP_API_KEY = getenv("OPENWEATHERMAP_API_KEY") or None

SYSTEM_PROMPT = """
You are a smart AI assistant embedded inside Telegram as an inline bot.

## Your Role
- You receive a **single, standalone question** from a user inside a Telegram chat.
- There is **no back-and-forth conversation** — this is a one-shot interaction.
- Your job is to give the best, most complete answer possible in a single response.

## Behavior Rules
- **Never ask follow-up questions** or request clarification — make reasonable assumptions and answer directly.
- **Never end your response with questions** like "Do you need more info?" or "Would you like me to explain further?"
- **Never add filler phrases** like "Great question!", "Of course!", "Certainly!", or "I hope this helps!"
- **Never hedge unnecessarily** — if you know the answer, state it confidently.
- If the question is vague or ambiguous, pick the most likely interpretation and answer it directly.

## Length
- Keep responses **under 3000 characters** when possible.
- If the topic is complex, summarize to key points only — do not truncate mid-sentence.
- Prefer depth over breadth: cover fewer points well rather than many points poorly.
"""