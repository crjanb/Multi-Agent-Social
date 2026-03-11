from langchain_groq import ChatGroq
from app.utils.config import Config

class LLMService:
    """Service to interact with Groq LLM using LangChain."""
    
    def __init__(self, model_name: str = "qwen/qwen3-32b"):
        self.llm = ChatGroq(
            api_key=Config.GROQ_API_KEY,
            model_name=model_name,
            temperature=0.7
        )

    def get_llm(self):
        return self.llm

    def image_generation_llm(self, prompt: str):
        """Generates an image using Replicate's google/imagen-4."""
        import replicate
        import os
        
        # Ensure token is in environment for the library
        if Config.REPLICATE_API_TOKEN:
            os.environ["REPLICATE_API_TOKEN"] = Config.REPLICATE_API_TOKEN
            
        return replicate.run(
            "google/imagen-4",
            input={
                "prompt": prompt,
                "image_size": "1K",
                "aspect_ratio": "16:9",
                "output_format": "jpg",
                "safety_filter_level": "block_medium_and_above"
            }
        )
