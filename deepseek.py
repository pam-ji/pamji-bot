import os
import discord
import requests
import json
from openai import OpenAI

api_key = os.environ["DEEPSEEK_API_KEY"]
print(api_key)
deep_client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")



API_URL = 'https://api.deepseek.com'

response = deep_client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)


# def translate_text(text, source_language, target_language):
#     response = deep_client.chat.completions.create(
#         model="deepseek-translate",
#         messages=[
#             {
#                 "role": "system",
#                 "content": f"Translate {text} from {source_language} to {target_language}"
#             }
#         ],
#         stream=False
#     )
#     return response.choices[0].message.content

# # Beispielaufruf
# text = "Hallo, wie geht es dir?"
# source_language = "de"
# target_language = "en"

# translated_text = translate_text(text, source_language, target_language)
# print(translated_text)