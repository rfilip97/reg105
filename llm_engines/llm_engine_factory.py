from llm_engines.azure_openai import AzureOpenAiEngine
from llm_engines.ollama import OllamaEngine
from config import LLM_ENGINE


class LLMEngineFactory:
    def create(self, llm_engine_type):
        if llm_engine_type == LLM_ENGINE.AZURE_OPEN_AI:
            return AzureOpenAiEngine()
        else:
            return OllamaEngine()
