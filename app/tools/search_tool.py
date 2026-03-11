from tavily import TavilyClient
from app.utils.config import Config
from app.utils.logger import setup_logger

logger = setup_logger(__name__)

class SearchTool:
    """Tool to perform web searches using Tavily."""
    
    def __init__(self):
        self.client = TavilyClient(api_key=Config.TAVILY_API_KEY)

    def search(self, query: str) -> str:
        """Performs a search and returns summarized results."""
        logger.info(f"Searching for: {query}")
        try:
            response = self.client.search(query=query, search_depth="advanced")
            results = response.get("results", [])
            
            summary = "\n".join([
                f"- {res['title']}: {res['content']} (Source: {res['url']})"
                for res in results[:3]
            ])
            return summary
        except Exception as e:
            logger.error(f"Search failed: {e}")
            return f"Search failed: {str(e)}"
