import os
from openai import AzureOpenAI
from prompts import PREPROMPT, get_prompt


class AzureOpenAiEngine:
    def __init__(self):
        self.client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_KEY"),
            api_version="2023-03-15-preview",
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        )

    def query(self, image_path, check_items):
        prompt = get_prompt(check_items)

        response = self.client.chat.completions.create(
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
