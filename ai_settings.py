import os
from dotenv import load_dotenv
from openai import OpenAI
from MessageLogger.message_logger import MessageLogger

load_dotenv()
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

storage = MessageLogger()

client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

async def get_ai_response(messages: list, model='deepseek-chat', max_tokens=300) -> str | None:

    messages = messages if len(messages) <= 16 else [messages[0]] + messages[-15:]

    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=0.7
        )

        storage.add_record('assistant', response.choices[0].message.content)

        return response.choices[0].message.content
    except Exception as e:
        print(f'API Error: {e}')
        return None