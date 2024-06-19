import argparse
import os
import ollama
import base64
from PIL import Image
import io

class UILlamaTester:
    def analyze_screenshot(self, image_path, description):
         stream = ollama.generate(
                   model="llava",
                   #prompt="Please describe this image",
                   prompt="From the header of this page, are there any elements that are not alligned with the others? Answer only with yes or no",
                   images=[image_path],
                   stream=False
                 )

         print(stream)


def main():
    tester = UILlamaTester()

    image_path = os.path.expanduser('./screenshots/ss11.jpg')
    description = (
        "Home page. On the header, on the left side, we should see the app logo, browse, movies, "
        "and live TV sections. On the right side, we should see the search, login, and subscribe buttons. "
        "The body will have a CTA with 'See Available Offers' and 'Create Account' buttons."
    )

    result = tester.analyze_screenshot(image_path, description)

if __name__ == "__main__":
    main()

