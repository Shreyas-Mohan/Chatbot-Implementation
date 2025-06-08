from openai import OpenAI
from src.prompt import system_instructions
import os
client = OpenAI(
    api_key=os.getenv('GOOGLE_API_KEY'),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
messages=[{'role': 'system', 'content':system_instructions}]  # List containing message history
def ask_order(messages):
    response = client.chat.completions.create(
        model='gemini-2.0-flash',
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content