from pyrogram.types import ReplyParameters, Message, LinkPreviewOptions
from TgAsk.strings import get_string
from TgAsk.logger import LOGGER
from pyrogram import filters, client
from TgAsk.Client import app

log = LOGGER(__name__)

@app.on_message(filters.command("^start$") & filters.private)
async def StartMsg(bot: client.Client, msg: Message):
    user_lang = (msg.from_user.language_code or "en").lower()
    user_id = msg.from_user.id
    log.info("User %s started the bot", user_id)
    await bot.send_message(
        chat_id=msg.chat.id,
        text=get_string(
            lang=user_lang,
            value="start_msg",
        ).format(
            mention=msg.from_user.mention,
            name=bot.me.first_name,
            username=bot.me.username,
        ),
        reply_parameters=ReplyParameters(
            message_id=msg.id,
        ),
        link_preview_options=LinkPreviewOptions(
            is_disabled=True
        )
    )