# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import os
import discord
import requests
import json
from openai import OpenAI
from google import genai

GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
gemini_client = genai.Client(api_key=GEMINI_API_KEY)
deepseek_api_key = os.environ["DEEPSEEK_API_KEY"]
deep_client = OpenAI(api_key=deepseek_api_key, base_url="https://api.deepseek.com")
intents = discord.Intents.default()
intents.message_content = True
discord_client = discord.Client(intents=intents)
gemini_models=gemini_client.models.list()

def generate_gemini_text(prompt):
    response = gemini_client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    return response.text

def generate_deepseek_text(prompt):
    response = deep_client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant"
            },
            {
                "role": "user",
                "content": prompt
            },
        ],
        stream=False
    )
    return response.choices[0].message.content

async def send_response(channel, response):
  for guild in discord_client.guilds:
            channel = discord.utils.get(guild.text_channels, name=channel)
            if channel:
                try:
                    await channel.send(response)
                except requests.exceptions.RequestException as e:
                    await channel.send(
                        f"Error: {e}")
                except KeyError:
                    await channel.send(
                        "Error: Channel not found."
                    )
@discord_client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(discord_client))
    # Greeting message disabled to avoid spam
    await send_response('bot-talk', 'Hello! How can I help you today?')


async def close_bot():
    for guild in discord_client.guilds:
        channel = discord.utils.get(guild.text_channels, name='bot-talk')
        if channel:
            await channel.send("Goodbye everyone! Bot is going offline.")
    await discord_client.close()


@discord_client.event
async def on_message(message):
    print(message.content)
    if message.author == discord_client.user:
        return
    if message.content.startswith('$hello'):
        print("hello")
        await send_response('bot-talk', 'Hello! How can I help you today?')
    if message.content.startswith('$shutdown'):
        await close_bot()
    if message.content.startswith('gemini'):
            print("gemini")
            user_input = message.content[len('gemini '):]
            response = generate_gemini_text(user_input)
            await send_response('bot-talk', response)
    if message.content.startswith('$deepseek'):
            print("deepsk")
            user_input = message.content[len('$deepseek '):]
            response = generate_deepseek_text(user_input)
            await send_response('bot-talk', response)

try:
    token = os.getenv("TOKEN") or ""
    if token == "":
        raise Exception("Please add your token to the Secrets pane.")
    discord_client.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print(
            "The Discord servers denied the connection for making too many requests"
        )
        print(
            "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
        )
    else:
        raise e
