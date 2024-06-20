import os
from enum import Enum


class IMAGE_LOCATION(Enum):
    LOCAL = 1
    URL = 2


IMAGE_MODE = IMAGE_LOCATION.LOCAL

CLIENT_ID = os.environ.get("IMGUR_CLIENT_ID")
CLIENT_SECRET = os.environ.get("IMGUR_CLIENT_SECRET")
