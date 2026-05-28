from langchain_core.tools import tool
from TgAsk.logger import LOGGER
import pytz, datetime
log = LOGGER(__name__)


@tool
def get_current_datetime(timezone_name: str) -> str:
    """
    Use this tool to get the current exact date and time for a specific country or city.
    Args:
        timezone_name: The valid IANA timezone string for the requested location 
                       (e.g., 'Africa/Cairo', 'Asia/Riyadh', 'Europe/London', 'America/New_York'). 
                       If the user asks for a country, you must infer its capital city's timezone.
    """
    log.info("Getting datetime for timezone: %s", timezone_name)
    try:
        tz = pytz.timezone(timezone_name)
        now = datetime.datetime.now(tz)
        current_time = now.strftime("%Y-%m-%d %I:%M:%S %p")
        day_of_week = now.strftime("%A")
        return f"The current date and time in {timezone_name} is {current_time}. Today is {day_of_week}."
    except pytz.UnknownTimeZoneError:
        log.warning("Unknown timezone requested: %s", timezone_name)
        return f"Error: '{timezone_name}' is not a valid IANA timezone. Please try again with a valid timezone (e.g., 'Africa/Cairo')."
    except Exception as e:
        log.error("Failed to get datetime for '%s': %s", timezone_name, e)
        return f"Failed to get the time. Error: {str(e)}"