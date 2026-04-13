import os

# Maximum number of retry attempts for fixing the code
MAX_RETRIES = 3

# Model to use
MODEL_NAME = "gpt-4o"

# OpenAI API key (ensure it's set in your environment variables)
# If using a different LLM or OpenAI-compatible endpoint, update the base URL in fixer.py
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
