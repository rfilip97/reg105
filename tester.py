import ollama
from screen_shotter import take_screenshot, upload_image
from llm_engines.llm_engine_factory import LLMEngineFactory
from config import LLM_ENGINE


class Tester:
    def __init__(self):
        self.llm_engine = LLMEngineFactory().create(LLM_ENGINE)

    def analyze_screenshot(self, image_path, check_items):
        return self.llm_engine.query(image_path, check_items)

    def run(self, test_step):
        screenshot_path = upload_image(take_screenshot())

        response = self.analyze_screenshot(screenshot_path, test_step["checks"])
        print(response)

        return response
