from langgraph.graph import StateGraph, END
from app.models.state import AgentState
from app.agents.research_agent import research_agent
from app.agents.writer_agent import writer_agent
from app.agents.visual_agent import visual_agent
from app.agents.post_agent import post_agent
from app.utils.logger import setup_logger

logger = setup_logger(__name__)

def create_workflow():
    """Compiles the multi-agent workflow into a runnable graph."""
    logger.info("Initializing LangGraph workflow.")
    
    workflow = StateGraph(AgentState)

    # Add Nodes
    workflow.add_node("researcher", research_agent)
    workflow.add_node("writer", writer_agent)
    workflow.add_node("visualizer", visual_agent)
    workflow.add_node("poster", post_agent)

    # Define Edges
    workflow.set_entry_point("researcher")
    workflow.add_edge("researcher", "writer")
    workflow.add_edge("writer", "visualizer")
    workflow.add_edge("visualizer", "poster")
    workflow.add_edge("poster", END)

    # Compile
    return workflow.compile()
