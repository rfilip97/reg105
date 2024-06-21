from tester import Tester
from driver import Driver
import json


class Delegator:
    def __init__(self):
        self.driver = Driver()
        self.tester = Tester()

    def run(self):
        with open("./scenarios/app_sections/main_page/login.json", "r") as file:
            data = json.load(file)
            for test_step in data["steps"]:
                if test_step["type"] == "action":
                    self.driver.run(test_step)
                else:
                    self.tester.run(test_step)
