import ollama
import os
import pyimgur

from config import IMAGE_LOCATION, IMAGE_MODE

# TODO: take screenshot
image_path = os.path.expanduser("./screenshots/ss11.jpg")


class Tester:
    def analyze_screenshot(self, image_path):
        response_w_metadata = ollama.generate(
            model="llava",
            prompt="What do you see in this image?",
            images=[image_path],
            stream=False,
        )

        return response_w_metadata["response"]

    def upload_image(self, image_path):
        image = pyimgur.Imgur(CLIENT_ID)
        uploaded_image = image.upload_image(image, title="Uploaded with PyImgur")

        return uploaded_image.link

    def run(self):
        if IMAGE_MODE == IMAGE_LOCATION.LOCAL:
            response = self.analyze_screenshot(image_path)

            print(response)

            return response
        else:
            print("WIP")
