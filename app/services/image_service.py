import os
from app.services.llm_service import LLMService
from app.utils.logger import setup_logger

logger = setup_logger(__name__)

class ImageService:
    """Service to handle image saving and orchestration."""
    
    def __init__(self):
        self.llm_service = LLMService()

    def generate_image(self, prompt: str) -> str:
        """
        Orchestrates image generation via LLMService and saves to disk.
        """
        logger.info(f"Generating image for prompt: {prompt}")
        
        image_dir = "static/images"
        if not os.path.exists(image_dir):
            os.makedirs(image_dir)
            
        file_path = os.path.join(image_dir, f"tweet_image_{hash(prompt)}.jpg")
        
        try:
            # Call the refactored method in LLM Service
            output = self.llm_service.image_generation_llm(prompt)
            
            # Write the file to disk
            with open(file_path, "wb") as file:
                file.write(output.read())
            
            logger.info(f"Image generated and saved to {file_path}")
            return file_path
            
        except Exception as e:
            logger.error(f"Image generation failed: {e}")
            return "placeholder_image_path.png"
