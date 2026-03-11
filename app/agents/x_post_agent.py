from app.models.state import AgentState
from app.services.social_service import SocialService
from app.utils.logger import setup_logger

logger = setup_logger(__name__)

def post_agent(state: AgentState) -> AgentState:
    """Agent that posts the content to X."""
    tweet_content = state.get("tweet_content")
    image_path = state.get("image_path")
    logger.info("Post Agent started.")
    
    social_service = SocialService()
    post_url = social_service.post_tweet(tweet_content, image_path)
    
    state["post_url"] = post_url
    return state
