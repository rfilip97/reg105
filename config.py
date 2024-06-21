import os
from enum import Enum


class MODES(Enum):
    DEBUG = 1
    FULL = 2


MODE = MODES.DEBUG

CLIENT_ID = os.environ.get("IMGUR_CLIENT_ID")
CLIENT_SECRET = os.environ.get("IMGUR_CLIENT_SECRET")

TMP_CONFIG_PATH = "./tmp"
SCREENSHOT_DELAY_SECONDS = 5

OLLAMA_MODEL_NAME = "llava"
