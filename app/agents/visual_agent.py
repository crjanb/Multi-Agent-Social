from app.models.state import AgentState
from app.services.image_service import ImageService
from app.utils.logger import setup_logger

logger = setup_logger(__name__)

def visual_agent(state: AgentState) -> AgentState:
    """Agent that generates a visual for the tweet."""
    image_prompt = state.get("image_prompt")
    logger.info("Visual Agent started.")
    
    image_service = ImageService()
    image_path = image_service.generate_image(image_prompt)
    
    state["image_path"] = image_path
    
    # Print for user visibility
    print("\n" + "="*50)
    print("VISUAL AGENT OUTPUT:")
    print("-" * 20)
    print(f"IMAGE GENERATED AT: {image_path}")
    print("="*50 + "\n")
    
    return state
