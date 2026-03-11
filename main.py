import uvicorn
from fastapi import FastAPI
from app.routes.post_routes import router as post_router
from app.utils.config import Config
from app.utils.logger import setup_logger

logger = setup_logger(__name__)

app = FastAPI(
    title="Multi-Agent AI Social Media System",
    description="A production-ready system to research, write, and post on X.",
    version="1.0.0"
)

# Include Routes
app.include_router(post_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "AI Social Media Agent is running!"}

if __name__ == "__main__":
    logger.info("Starting FastAPI server...")
    # Validate config before starting
    try:
        Config.validate()
    except ValueError as e:
        logger.warning(f"Configuration validation warning: {e}. Ensure .env is properly set.")
        
    uvicorn.run(app, host="0.0.0.0", port=8000)
