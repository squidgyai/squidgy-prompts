
import openai
import os
import pytest

class Gpt3Client:

    def __init__(self):
        openai.api_key = os.environ['OPENAI_API_KEY']

    def invoke_from_file(
        self, 
        prompt_file: str, 
        params: dict[str,str],
        additional_text: str = None,
        engine='text-davinci-003',
        temperature=0, 
        stop=['}', '###'], 
        max_tokens=300,
        frequency_penalty=0.15,
        presence_penalty=0.3,
    ) -> str:
        with open(prompt_file) as f:
            prompt = f.read()

            if additional_text is not None:
                prompt += additional_text

            for param in params:
                if params[param] is not None:
                    prompt = prompt.replace("{%s}" % param, params[param])

            return self.invoke(prompt, engine, temperature, stop, max_tokens, frequency_penalty, presence_penalty)

    def invoke(
        self, 
        prompt: str, 
        engine='text-davinci-003',
        temperature=0, 
        stop=['}', '###'],
        max_tokens=160,
        frequency_penalty=0.15,
        presence_penalty=0.3,
    ) -> str:
        response = openai.Completion.create(
            prompt=prompt,
            model=engine,
            temperature=temperature,
            max_tokens=max_tokens,
            stop=stop,
            top_p=1,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            timeout=15
        )

        return response['choices'][0]['text'].strip()

@pytest.fixture
def gpt3_client():
    return Gpt3Client()