from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from src.config.base import MY_GITHUB_TOKEN, BASE_URL
from openai import OpenAI
from langchain_groq import ChatGroq


def chat_openai():
        return ChatOpenAI(
                model='gpt-4o',
                temperature='0.7',
                api_key=MY_GITHUB_TOKEN,
                base_url=BASE_URL
        )


def chat_ollama():
    return ChatOllama(
        model="llama3.1",
        temperature=0.7
    )



def chat_groq():
        return ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0,
        max_retries=2,
        )