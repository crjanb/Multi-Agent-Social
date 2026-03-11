from app.models.state import AgentState
from app.services.llm_service import LLMService
from app.utils.logger import setup_logger

logger = setup_logger(__name__)

import re

def clean_llm_response(text: str) -> str:
    """Removes <think>...</think> tags from the LLM response."""
    return re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL).strip()

def writer_agent(state: AgentState) -> AgentState:
    """Agent that generates tweet content based on research."""
    research = state.get("research")
    logger.info("Writer Agent started.")
    
    llm_service = LLMService()
    llm = llm_service.get_llm()
    
    prompt = f"Based on the following research, write a viral tweet about {state['topic']}:\n\n{research}\n\nReturn ONLY the tweet content, no preamble, no thinking, no quotes."
    
    response = llm.invoke(prompt)
    state["tweet_content"] = clean_llm_response(response.content)
    
    # Also generate an image prompt
    img_prompt_req = f"Create a short image generation prompt for a tweet about: {state['tweet_content']}. Return ONLY the prompt text."
    img_response = llm.invoke(img_prompt_req)
    state["image_prompt"] = clean_llm_response(img_response.content)
    
    # Print for user visibility
    print("\n" + "="*50)
    print("WRITER AGENT OUTPUT:")
    print("-" * 20)
    print(f"TWEET CONTENT:\n{state['tweet_content']}")
    print("="*50 + "\n")
    
    return state
