from langchain_community.utilities.openweathermap import OpenWeatherMapAPIWrapper
from langchain_core.tools import tool
from TgAsk.logger import LOGGER

log = LOGGER(__name__)


@tool
def get_weather(city: str) -> str:
    """Fetch real-time weather information and forecasts for a given city."""
    log.info("Fetching weather for: %s", city)
    try:
        result = OpenWeatherMapAPIWrapper().run(city)
        log.debug("Weather fetched for: %s", city)
        return result
    except Exception as e:
        log.error("Weather fetch failed for '%s': %s", city, e)
        return f"Failed to fetch weather for {city}. Error: {str(e)}"