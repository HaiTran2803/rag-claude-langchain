from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
MODEL_NAME = os.getenv("MODEL_NAME", "claude-3-5-sonnet-20241022")
UPLOAD_FOLDER = BASE_DIR / os.getenv("UPLOAD_FOLDER", "data/raw")
VECTORSTORE_PATH = BASE_DIR / os.getenv("VECTORSTORE_PATH", "data/vectorstore")

UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)
VECTORSTORE_PATH.mkdir(parents=True, exist_ok=True)
