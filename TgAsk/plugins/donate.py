from pyrogram.types import Message, LabeledPrice, PreCheckoutQuery, ReplyParameters
from pyromod.exceptions import ListenerTimeout
from TgAsk.strings import get_string
from TgAsk.logger import LOGGER
from pyrogram import filters, client
from TgAsk.Client import app

log = LOGGER(__name__)

@app.on_message(filters.command("donate"))
async def message_handler(client: client.Client, message: Message):
    user_lang = (message.from_user.language_code or "en").lower()
    user_id = message.from_user.id
    log.info("User %s initiated support command", user_id)
    try:
        amount_ = await message.chat.ask(
            filters=filters.text,
            text=get_string(lang=user_lang, value="support_ask_amount"),
            reply_parameters=ReplyParameters(
                message_id=message.id,
            ),
            timeout=15,
        )
        amount = int(amount_.text)
        if amount < 1 or amount > 10000:
            log.warning("User %s entered invalid range: %s", user_id, amount)
            await message.reply(get_string(lang=user_lang, value="support_invalid_range"))
            return
        await client.send_invoice(
            message.from_user.id,
            title=get_string(lang=user_lang, value="support_invoice_title"),
            description=get_string(lang=user_lang, value="support_invoice_description"),
            currency="XTR",
            prices=[LabeledPrice(label="⭐ Star", amount=amount)],
            payload="stars",
            reply_parameters=ReplyParameters(message_id=amount_.id)
        )
    except ListenerTimeout:
        log.info("User %s support command timed out", user_id)
        await message.reply(
            get_string(
                lang=user_lang,
                value="support_timeout"
            ).format(
                timeout=15
            ),
        )
    except ValueError:
        log.warning("User %s entered non-numeric amount", user_id)
        await message.reply(get_string(lang=user_lang, value="support_invalid_amount"))

@app.on_pre_checkout_query()
async def pre_checkout_query_handler(_: client.Client, query: PreCheckoutQuery):
    await query.answer(ok=True)

@app.on_message(filters.successful_payment)
async def successful_payment_handler(client: client.Client, message: Message):
    user_lang = (message.from_user.language_code or "en").lower()
    amount = message.successful_payment.total_amount
    user_id = message.from_user.id
    log.info("User %s donated %s stars", user_id, amount)
    await message.reply(
        get_string(lang=user_lang, value="support_thanks").format(amount=amount)
    )