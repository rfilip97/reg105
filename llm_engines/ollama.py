import ollama
from prompts import PREPROMPT, get_prompt
from config import OLLAMA_MODEL_NAME


class OllamaEngine:
    def query(self, image_path, check_items):
        prompt = get_prompt(check_items)

        response_w_metadata = ollama.generate(
            model=OLLAMA_MODEL_NAME,
            prompt=prompt,
            images=[image_path],
            stream=False,
        )

        return response_w_metadata["response"]
