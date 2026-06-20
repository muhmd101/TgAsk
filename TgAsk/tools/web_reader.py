from langchain_core.tools import tool
from langchain_community.document_loaders import WebBaseLoader
from TgAsk.logger import LOGGER

log = LOGGER(__name__)


@tool
def read_webpage(url: str) -> str:
    """
    Use this tool when the user provides a URL or link and asks you to read, 
    summarize, or extract information from it.
    
    Args:
        url: The full URL link to the web page or article.
    """
    log.info("Reading webpage: %s", url)
    try:
        loader = WebBaseLoader(url)
        docs = loader.load()
        content = "\n\n".join(doc.page_content for doc in docs)
        content = content.strip()
        max_chars = 15000
        if len(content) > max_chars:
            content = content[:max_chars] + "\n... [Content truncated due to length]"
        if not content:
            log.warning("Webpage returned empty content: %s", url)
            return "The webpage appears to be empty or could not be parsed."
        log.debug("Webpage read successfully: %s (%d chars)", url, len(content))
        return content
    except Exception as e:
        log.error("Failed to read webpage '%s': %s", url, e)
        return f"Failed to read the webpage. Error: {str(e)}"