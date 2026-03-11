from app.models.state import AgentState
from app.tools.search_tool import SearchTool
from app.utils.logger import setup_logger

logger = setup_logger(__name__)

def research_agent(state: AgentState) -> AgentState:
    """Agent that researches the given topic."""
    topic = state.get("topic")
    logger.info(f"Research Agent started for topic: {topic}")
    
    search_tool = SearchTool()
    research_results = search_tool.search(topic)
    
    state["research"] = research_results
    return state
