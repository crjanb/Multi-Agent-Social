from typing import TypedDict, Optional

class AgentState(TypedDict):
    """Shared state for the multi-agent workflow."""
    topic: str
    research: Optional[str]
    tweet_content: Optional[str]
    image_prompt: Optional[str]
    image_path: Optional[str]
    post_url: Optional[str]
    error: Optional[str]
