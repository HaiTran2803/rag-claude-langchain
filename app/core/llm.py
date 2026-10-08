from langchain_anthropic import ChatAnthropic

from app.config import ANTHROPIC_API_KEY, MODEL_NAME


def create_llm():
    if not ANTHROPIC_API_KEY:
        raise ValueError("ANTHROPIC_API_KEY is missing. Please add it to the .env file.")

    return ChatAnthropic(
        model=MODEL_NAME,
        anthropic_api_key=ANTHROPIC_API_KEY,
        temperature=0,
    )
