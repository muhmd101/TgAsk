from TgAsk.tools.search import web_search
from TgAsk.tools.web_reader import read_webpage
from TgAsk.tools.datetime import get_current_datetime
from TgAsk.config import OPENWEATHERMAP_API_KEY
from TgAsk.logger import LOGGER

log = LOGGER(__name__)

ALL_TOOLS = [
    web_search,
    read_webpage,
    get_current_datetime,
]

if OPENWEATHERMAP_API_KEY:
    from TgAsk.tools.weather import get_weather
    ALL_TOOLS.append(get_weather)
    log.info("Weather tool enabled (OpenWeatherMap API key found)")
else:
    log.warning("OPENWEATHERMAP_API_KEY not set — weather tool disabled")