import os
from datetime import datetime
import time
from mss import mss
import pyimgur

from config import (
    TMP_CONFIG_PATH,
    SCREENSHOT_DELAY_SECONDS,
    CLIENT_ID,
    MODE,
    MODES,
    LLM_ENGINE,
    LLM_ENGINES,
)


def take_screenshot():
    if MODE == MODES.DEBUG:
        return "./tmp/20240620-121650.png"

    if not os.path.exists(TMP_CONFIG_PATH):
        os.makedirs(TMP_CONFIG_PATH)

    TIMESTAMP = datetime.now().strftime("%Y%m%d-%H%M%S")
    DESTINATION_PATH = f"{TMP_CONFIG_PATH}/{TIMESTAMP}.png"

    for i in range(SCREENSHOT_DELAY_SECONDS, 0, -1):
        print(f"Taking screenshot in {i} seconds")
        time.sleep(1)
    print("Taking screenshot now!")

    with mss() as screen_capturer:
        screen_capturer.shot(mon=1, output=DESTINATION_PATH)

    print(f"Screenshot: {DESTINATION_PATH}")

    return DESTINATION_PATH


def upload_image(image_path):
    if LLM_ENGINE == LLM_ENGINES.OLLAMA:
        return image_path

    if MODE == MODES.DEBUG:
        return "https://i.imgur.com/4mMzFtj.jpeg"

    img = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = img.upload_image(image_path, title="Uploaded with PyImgur")

    print(f"Screenshot uploaded at: {uploaded_image.link}")

    return uploaded_image.link
