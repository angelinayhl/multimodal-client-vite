import os
from dotenv import load_dotenv

def load_env():
    """Load environment variables from .env file"""
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(env_path)
    
def require_keys(keys):
    """Validate that required environment keys are present"""
    missing = []
    for key in keys:
        if not os.getenv(key):
            missing.append(key)
    
    if missing:
        raise ValueError(f"Missing required environment variables: {', '.join(missing)}")

