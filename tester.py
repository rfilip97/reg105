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
)


class Tester:
    def get_prompt(self, items):
        prompt = (
            "Examine the provided screenshot and verify the placement of the UI elements "
            "based on the criteria listed below. Respond with 'LGTM' if all elements are "
            "correctly placed according to the specifications. If any discrepancies are "
            "found, list them using bullet points."
        )

        prompt += "\n\nChecklist:"

        for item in items:
            prompt += f"\n- '{item}'"

        return prompt

    # TODO: Add model api factory: azure-openai vs ollama
    #    def analyze_screenshot(self, image_path):
    #        response_w_metadata = ollama.generate(
    #            model=OLLAMA_MODEL_NAME,
    #            prompt="What do you see in this image?",
    #            images=[image_path],
    #            stream=False,
    #        )
    #
    #        return response_w_metadata["response"]
    def analyze_screenshot(self, image_path, check_items):
        prompt = self.get_prompt(check_items)

        pdb.set_trace()

        # TODO: rm
        return ""

        client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_KEY"),
            api_version="2023-03-15-preview",
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        )

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Describe this picture:"},
                        {
                            "type": "image_url",
                            "image_url": {"url": image_path},
                        },
                    ],
                },
            ],
            max_tokens=200,
        )

        print(response)

        return response

    # Not used yet
    def upload_image(self, image_path):
        image = pyimgur.Imgur(CLIENT_ID)
        uploaded_image = image.upload_image(image, title="Uploaded with PyImgur")

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
        # screenshot_path = self.take_screenshot()
        screenshot_path = "https://i.imgur.com/3UbLnyX.jpeg"

        if IMAGE_MODE == IMAGE_LOCATION.LOCAL:
            print("Analysing image...")
            response = self.analyze_screenshot(screenshot_path, test_step["checks"])

            print(response)

            return response
        else:
            print("WIP")
