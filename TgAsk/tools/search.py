from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from TgAsk.logger import LOGGER

log = LOGGER(__name__)


@tool
def web_search(query: str) -> str:
    """Search the web using DuckDuckGo for recent news or real-time information."""
    log.info("Searching: %s", query)
    try:
        result = DuckDuckGoSearchRun().run(query)
        log.debug("Search completed for: %s", query)
        return result
    except Exception as e:
        log.error("Search failed for '%s': %s", query, e)
        return f"Search failed. Error: {str(e)}"