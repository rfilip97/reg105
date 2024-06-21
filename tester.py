import ollama
from openai import AzureOpenAI
from prompts import PREPROMPT, get_prompt
from screen_shotter import take_screenshot, upload_image
import os


class Tester:
    def analyze_screenshot(self, image_path, check_items):
        prompt = get_prompt(check_items)

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

    def run(self, test_step):
        screenshot_path = take_screenshot()
        screenshot_path = upload_image(screenshot_path)

        response = self.analyze_screenshot(screenshot_path, test_step["checks"])
        print(response)

        return response
