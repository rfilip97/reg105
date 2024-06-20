import os
from tester import Tester


image_path = os.path.expanduser("./screenshots/ss11.jpg")


def main():
    tester = Tester()
    tester.run()


if __name__ == "__main__":
    main()
