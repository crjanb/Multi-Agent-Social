from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.controllers.post_controller import PostController

router = APIRouter()
controller = PostController()

class PostRequest(BaseModel):
    topic: str

@router.post("/generate-post")
async def generate_post(request: PostRequest):
    """Endpoint to generate and post a tweet based on a topic."""
    result = await controller.generate_and_post(request.topic)
    if result.get("status") == "failed":
        raise HTTPException(status_code=500, detail=result.get("error"))
    return result
