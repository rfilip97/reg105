import os
from enum import Enum


class MODES(Enum):
    DEBUG = 1
    FULL = 2


MODE = MODES.DEBUG


class LLM_ENGINES(Enum):
    AZURE_OPEN_AI = 1
    OLLAMA = 2


LLM_ENGINE = LLM_ENGINES.AZURE_OPEN_AI

OLLAMA_MODEL_NAME = "llava"

CLIENT_ID = os.environ.get("IMGUR_CLIENT_ID")
CLIENT_SECRET = os.environ.get("IMGUR_CLIENT_SECRET")

TMP_CONFIG_PATH = "./tmp"
SCREENSHOT_DELAY_SECONDS = 5
