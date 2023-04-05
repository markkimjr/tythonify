import openai
import settings
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = settings.OPENAI_API_KEY


def tythonify(prompt: str) -> str:
    response = openai.Completion.create(
        model="text-davinci-003",
        max_tokens=settings.MAX_TOKENS,
        prompt=generate_prompt(prompt),
        temperature=settings.TEMPERATURE,
    )
    res = response.choices[0].text
    parsed_res = parse_string(res)

    return parsed_res


def generate_prompt(prompt: str) -> str:
    return f"Rewrite the following text in a way that Mike Tyson would say it: {prompt}"


def parse_string(text: str) -> str:
    return text.replace("s", "th")


if __name__ == "__main__":
    test_prompt = "We’ve trained a model called ChatGPT which interacts in a conversational way. The dialogue format makes it possible for ChatGPT to answer follow-up questions, admit its mistakes, challenge incorrect premises, and reject inappropriate requests."
    tythonify(test_prompt)

