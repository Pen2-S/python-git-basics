"""
Simple ChatGPT Tool (Educational)

What this file does:
- Takes a single text input
- Sends it to OpenAI ChatGPT 5 Nano
- Returns the model response as a string

Rules:
- No conversation history
- One request → one response
- Minimal validation only
"""

from openai import OpenAI


def ask_chatgpt(message: str) -> str:
    """
    Sends a single message to ChatGPT and returns the response text.

    :param message: User input text
    :return: Model response text
    """

    # ---- Basic input validation ----
    if not isinstance(message, str):
        raise ValueError("Input must be a string")

    if message.strip() == "":
        raise ValueError("Input cannot be empty")

    # ---- Create OpenAI client ----
    client = OpenAI()  # API key must be set in environment variable OPENAI_API_KEY

    # ---- Send request ----
    response = client.responses.create(model="gpt-5-nano", input=message)

    # ---- Extract and return text output ----
    return response.output_text
