import os
from dotenv import load_dotenv
import assemblyai as aai
from google import genai

# Environment variables
load_dotenv()

# API Keys
ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# AssemblyAI configuration
if ASSEMBLYAI_API_KEY:
    aai.settings.api_key = ASSEMBLYAI_API_KEY

# Gemini configuration
if GEMINI_API_KEY:
    gemini_client = genai.Client(api_key=GEMINI_API_KEY)
else:
    gemini_client = None

# Gemini model
GEMINI_MODEL = "gemini-3.8-flash"


# API key validation
def check_assemblyai_key():
    return bool(ASSEMBLYAI_API_KEY)


def check_gemini_key():
    return bool(GEMINI_API_KEY)