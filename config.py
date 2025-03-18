import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

LLAMA_CLOUD_API_KEY = os.getenv("LLAMA_CLOUD_API_KEY")

# Debug: Check if key is loaded
print("Llama Cloud API Key:", LLAMA_CLOUD_API_KEY)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf"}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
