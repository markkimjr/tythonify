import os
from dotenv import load_dotenv
from pathlib import Path


# env_path = Path('.env')
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TEMPERATURE = 0.7
MAX_TOKENS = 300
