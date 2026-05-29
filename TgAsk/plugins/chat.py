from pyrogram.types import (
    InputTextMessageContent,
    InlineQueryResultArticle,
    Message
)
from langchain_core.messages import HumanMessage, AIMessage
from TgAsk.strings import get_string
from TgAsk.logger import LOGGER
from pyrogram import Client, filters
from TgAsk.Client import app
import re

log = LOGGER(__name__)

@app.on_guest_message(filters.text)
async def askai(client: Client, message: Message):
    user_lang = (message.from_user.language_code or "en").lower()
    user_id = message.from_user.id
    msg_text = message.text
    replied = message.reply_to_message
    replied_is_bot = replied and getattr(replied.from_user, "is_bot", False)
    clean_text = re.sub(rf"@{re.escape(app.me.username)}", "", msg_text, flags=re.IGNORECASE).strip()
    if not clean_text and replied and replied.text and not replied_is_bot:
        query = re.sub(r"@\w+", "", replied.text, flags=re.IGNORECASE).strip()
        history = []
    else:
        query = clean_text
        history = []
        msg = replied
        while msg is not None:
            is_bot = getattr(msg.from_user, "is_bot", False)
            text = msg.text or ""
            if is_bot:
                history.append(
                    AIMessage(
                        content=text,
                    )
                )
            else:
                clean = re.sub(r"@\w+", "", text, flags=re.IGNORECASE).strip()
                if clean:
                    history.append(
                        HumanMessage(
                            content=clean
                        )
                    )
            msg = getattr(msg, "reply_to_message", None)
        history.reverse()
    log.info("User %s asked: %s", user_id, query[:100])
    MARKDOWN_REMINDER = (
        "\n\n[IMPORTANT REMINDER: You are responding inside Telegram. You MUST follow the formatting rules defined in your system prompt. Violating them will cause broken output.]"
    )
    messages = history + [HumanMessage(content=query + MARKDOWN_REMINDER)]
    guest = await client.answer_guest_query(
        guest_query_id=message.guest_query_id,
        result=InlineQueryResultArticle(
            "answer",
            InputTextMessageContent(
                message_text=get_string(lang=user_lang, value="inline_query_msg").format(query=query)
            )
        ),
    )
    try:
        result = await app.agent.ainvoke({"messages": messages})
        log.info("User %s - agent responded successfully", user_id)
        await client.edit_inline_text(
            inline_message_id=guest.inline_message_id,
            text=result["messages"][-1].content.strip()
        )
    except Exception as e:
        log.error("User %s - agent error: %s", user_id, e)
        await client.edit_inline_text(
            inline_message_id=guest.inline_message_id,
            text=get_string(lang=user_lang, value="error_msg")
        )