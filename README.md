# TgAskBot

A Telegram inline AI assistant bot powered by OpenAI with LangChain tool-use capabilities. Ask questions in any chat via `@HRKBOT your question` and get instant answers.

Example: [@HRKBOT](https://t.me/HRKBOT)

## Features

- **Inline Query Support** — Use the bot in any chat without leaving the conversation
- **Conversation Thread Awareness** — Replies in a thread build context from the message chain
- **AI Tool Calling** — The agent can invoke tools autonomously:
  - **Web Search** — DuckDuckGo search for real-time info
  - **Web Reader** — Extract text content from any URL
  - **Weather** — Get current weather for any city (OpenWeatherMap)
  - **Date & Time** — Get current date/time for any timezone
- **Multi-language UI** — English and Arabic (auto-detected from user's Telegram language)
- **Telegram Stars Donations** — Built-in `/support` command for star donations

## Prerequisites

- Python 3.10
- Telegram Bot Token (from [@BotFather](https://t.me/BotFather))
- Telegram API ID & Hash (from [my.telegram.org](https://my.telegram.org))
- OpenAI API Key
- OpenWeatherMap API Key (for weather tool)

## Setup

1. Clone the repository:

```bash
git clone https://github.com/muhmd101/TgAsk.git
cd TgAskbot
```

2. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Linux/macOS

pip install -r requirements.txt
```

3. Create a `.env` file in the project root:

```env
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
OPENAI_API_KEY=your_openai_api_key
OPENAI_API_BASE=https://api.openai.com/v1
OPENAI_API_MODEL=gpt-4o
```

4. Run the bot:

```bash
python -m TgAsk
```

## Docker

Build and run with Docker:

```bash
docker build -t tgaskbot .
docker run -d --name tgaskbot --env-file .env tgaskbot
```

## Project Structure

```
TgAskbot/
├── TgAsk/
│   ├── __main__.py          # Entry point
│   ├── Client.py             # Bot client & agent initialization
│   ├── config/__init__.py    # Environment config & system prompt
│   ├── plugins/
│   │   ├── start.py          # /start command handler
│   │   ├── chat.py           # Inline query handler
│   │   └── donate.py          # /support & Telegram Stars payments
│   ├── tools/
│   │   ├── search.py         # DuckDuckGo web search
│   │   ├── web_reader.py     # URL content extraction
│   │   ├── weather.py        # OpenWeatherMap integration
│   │   └── datetime.py       # Timezone-aware date/time
│   └── strings/
│       ├── __init__.py        # String loader
│       └── langs/
│           ├── en.yml         # English strings
│           └── ar.yml         # Arabic strings
├── Dockerfile
├── requirements.txt
└── .env
```

## License

This project is licensed under the MIT License.