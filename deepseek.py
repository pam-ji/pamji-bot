import os
import discord
import requests
import json
from openai import OpenAI
api_key = os.environ["DEEPSEEK_API_KEY"]
deep_client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

user_input = "Hello, how are you?"
response = deep_client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant"
        },
        {
            "role": "user",
            "content": user_input
        },
    ],
    stream=False)
print(response.choices[0].message.content)