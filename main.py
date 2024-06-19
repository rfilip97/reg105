import argparse
import os
from langchain_community.llms import Ollama
import base64
from PIL import Image
import io

class UILlamaTester:
    def __init__(self):
        self.model = Ollama(model="llama3")

    def encode_image_base64(self, image_path):
        with Image.open(image_path) as image:
            if image.mode == 'RGBA':
                image = image.convert('RGB')
            buffered = io.BytesIO()
            image.save(buffered, format="JPEG")
            img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
        return img_str

    def analyze_screenshot(self, image_path, description):
        image_base64 = self.encode_image_base64(image_path)
        prompt = (
            f"As a regression tester, analyze this UI screenshot encoded in base64: {image_base64}. \n"
            "Your tasks are: \n"
            "- Verify the presence of specific UI elements as described. \n"
            "- Use your judgment to identify any additional issues")

        response = self.model.invoke(prompt, temperature=0)
        return response

def main():
    tester = UILlamaTester()

    image_path = os.path.expanduser('./screenshots/ss1.png')
    description = (
        "Home page. On the header, on the left side, we should see the app logo, browse, movies, "
        "and live TV sections. On the right side, we should see the search, login, and subscribe buttons. "
        "The body will have a CTA with 'See Available Offers' and 'Create Account' buttons."
    )

    result = tester.analyze_screenshot(image_path, description)
    print(f"\nResult:\n{result}")

if __name__ == "__main__":
    main()

