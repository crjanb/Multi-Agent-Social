import tweepy
from app.utils.config import Config
from app.utils.logger import setup_logger

logger = setup_logger(__name__)

class SocialService:
    """Service to post content to X (Twitter)."""
    
    def __init__(self):
        self.client = None
        if all([Config.X_API_KEY, Config.X_API_SECRET, Config.X_ACCESS_TOKEN, Config.X_ACCESS_TOKEN_SECRET]):
            try:
                self.client = tweepy.Client(
                    consumer_key=Config.X_API_KEY,
                    consumer_secret=Config.X_API_SECRET,
                    access_token=Config.X_ACCESS_TOKEN,
                    access_token_secret=Config.X_ACCESS_TOKEN_SECRET
                )
            except Exception as e:
                logger.error(f"Failed to initialize X API: {e}")

    def post_tweet(self, text: str, image_path: str = None) -> str:
        """Posts a tweet. Image support in X V2 API requires media upload via v1.1 or third party."""
        logger.info(f"Posting tweet: {text[:50]}...")
        
        if not self.client:
            logger.warning("X API not configured. Simulating post.")
            return f"https://x.com/simulated_post_{hash(text)}"
            
        try:
            # Simple text post for now (V2 API)
            response = self.client.create_tweet(text=text)
            tweet_id = response.data['id']
            return f"https://x.com/user/status/{tweet_id}"
        except Exception as e:
            logger.error(f"Failed to post tweet: {e}")
            return "Post failed"
