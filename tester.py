import ollama
import os
import pyimgur
import time
from datetime import datetime
from mss import mss
from openai import AzureOpenAI
import pdb

from config import (
    IMAGE_LOCATION,
    IMAGE_MODE,
    TMP_CONFIG_PATH,
    SCREENSHOT_DELAY_SECONDS,
    OLLAMA_MODEL_NAME,
    CLIENT_ID,
)


PREPROMPT = (
    "You are a regression tester. Examine the provided screenshot and verify the placement of the UI elements "
    "based on the criteria listed below. Respond only with 'LGTM'(and nothing more) if all elements are "
    "correctly placed according to the specifications. If any discrepancies are "
    "found, list them using bullet points."
)


class Tester:
    def get_prompt(self, items):
        prompt = (
            "\n\nCheck if the following statements are true for the received image:"
        )

        for item in items:
            prompt += f"\n- '{item}'"

        return (
            prompt
            + "\n\nRemember to respond with 'LGTM' and nothing more if you find all the above checks to be true."
        )

    def analyze_screenshot(self, image_path, check_items):
        prompt = self.get_prompt(check_items)

        client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_KEY"),
            api_version="2023-03-15-preview",
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        )

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": PREPROMPT},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {"url": image_path},
                        },
                    ],
                },
            ],
            max_tokens=200,
        )

        print(response.choices[0])

        return response.choices[0]

    def upload_image(self, image_path):
        img = pyimgur.Imgur(CLIENT_ID)
        uploaded_image = img.upload_image(image_path, title="Uploaded with PyImgur")

        return uploaded_image.link

    def take_screenshot(self):
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

        return DESTINATION_PATH

    def run(self, test_step):
        screenshot_path = self.take_screenshot()

        if IMAGE_MODE == IMAGE_LOCATION.URL:
            screenshot_path = self.upload_image(screenshot_path)

        response = self.analyze_screenshot(screenshot_path, test_step["checks"])
        print(response)

        return response
