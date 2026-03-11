from app.graph.workflow import create_workflow
from app.models.state import AgentState
from app.utils.logger import setup_logger

logger = setup_logger(__name__)

class PostController:
    """Controller to handle post generation and orchestration."""
    
    def __init__(self):
        self.workflow = create_workflow()

    async def generate_and_post(self, topic: str):
        """Triggers the multi-agent workflow for a given topic."""
        logger.info(f"Starting post generation for topic: {topic}")
        
        initial_state: AgentState = {
            "topic": topic,
            "research": None,
            "tweet_content": None,
            "image_prompt": None,
            "image_path": None,
            "post_url": None,
            "error": None
        }
        
        try:
            final_state = self.workflow.invoke(initial_state)
            return {
                "tweet": final_state.get("tweet_content"),
                "image_path": final_state.get("image_path"),
                "post_url": final_state.get("post_url"),
                "status": "success"
            }
        except Exception as e:
            logger.error(f"Workflow execution failed: {e}")
            return {
                "error": str(e),
                "status": "failed"
            }
