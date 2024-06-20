import argparse
import os
import ollama
import base64
from PIL import Image
import io
import pyimgur

CLIENT_ID = os.environ.get("IMGUR_CLIENT_ID")
CLIENT_SECRET = os.environ.get("IMGUR_CLIENT_SECRET")

IMG_URL = "https://i.imgur.com/3UbLnyX.jpeg"


class UILlamaTester:
    def analyze_screenshot(self, image_path, description):
        stream = ollama.generate(
            model="llava",
            # prompt="Please describe this image",
            prompt="From the header of this page, are there any elements that are not alligned with the others? Answer only with yes or no",
            images=[image_path],
            stream=False,
        )

        print(stream)


def upload_image(img_path):
    #    img = pyimgur.Imgur(CLIENT_ID)
    #    uploaded_image = img.upload_image(img_path, title="Uploaded with PyImgur")
    #
    #    print(uploaded_image.link)
    #
    #    return uploaded_image.link

    return IMG_URL


def main():
    tester = UILlamaTester()

    image_path = os.path.expanduser("./screenshots/ss11.jpg")

    upload_image(image_path)

    description = (
        "Home page. On the header, on the left side, we should see the app logo, browse, movies, "
        "and live TV sections. On the right side, we should see the search, login, and subscribe buttons. "
        "The body will have a CTA with 'See Available Offers' and 'Create Account' buttons."
    )

    result = tester.analyze_screenshot(image_path, description)


if __name__ == "__main__":
    main()
