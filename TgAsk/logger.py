import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    force=True
)

logging.getLogger("pyrogram").setLevel(logging.CRITICAL)
logging.getLogger("httpx").setLevel(logging.CRITICAL)
logging.getLogger("primp").setLevel(logging.CRITICAL)
logging.getLogger("ddgs").setLevel(logging.CRITICAL)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)