
from llama_cpp import Llama

from app.config.settings import settings


class LLMInference:

    def __init__(self):

        self.model = Llama(

            model_path=settings.MODEL_PATH,

            n_ctx=settings.N_CTX,

            n_threads=settings.N_THREADS,

            n_gpu_layers=settings.GPU_LAYERS

        )

    def chat(self, messages):

        response = self.model.create_chat_completion(

            messages=messages

        )

        return (

            response["choices"][0]["message"]["content"]

            .strip()

        )


llm = LLMInference()
