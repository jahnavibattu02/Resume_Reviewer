
"""
Global configuration settings.
Loads values from .env using python-dotenv.
"""

from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(BASE_DIR / ".env")


class Settings:

    # ----------------------------
    # LLM
    # ----------------------------

    MODEL_PATH = os.getenv(
        "MODEL_PATH",
        str(BASE_DIR / "models" / "zephyr-7b-alpha.Q4_K_M.gguf")
    )

    N_CTX = int(os.getenv("N_CTX", 2048))
    N_THREADS = int(os.getenv("N_THREADS", 8))
    GPU_LAYERS = int(os.getenv("GPU_LAYERS", 35))

    # ----------------------------
    # APP
    # ----------------------------

    APP_NAME = "Resume Reviewer"

    VERSION = "2.0"

    DEBUG = os.getenv("DEBUG", "False").lower() == "true"


settings = Settings()
