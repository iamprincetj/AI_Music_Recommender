from langchain_openai import ChatOpenAI
from src.config.base import MY_GITHUB_TOKEN, BASE_URL


def chat_openai():
    return ChatOpenAI(
            model='gpt-4o',
            temperature='0.7',
            api_key=MY_GITHUB_TOKEN,
            base_url=BASE_URL
    )
