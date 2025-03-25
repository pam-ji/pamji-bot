# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import os
import discord
import requests
import json

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # Greeting message disabled to avoid spam
    # for guild in client.guilds:
    #     channel = discord.utils.get(guild.text_channels, name='bot-talk')
    #     if channel:
    #         await channel.send("Hello everyone! Special greetings to Malaria, Monk, and Ji!")


async def close_bot():
    for guild in client.guilds:
        channel = discord.utils.get(guild.text_channels, name='bot-talk')
        if channel:
            await channel.send("Goodbye everyone! Bot is going offline.")
    await client.close()


@client.event
async def on_message(message):
    print(message.content)
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        print("hello")
        channel = discord.utils.get(discordguild.text_channels, name='main')
        if channel:
            await channel.send(
                "Hello everyone! Special greetings to Malaria, Monk, and Ji!")

    if message.content.startswith('$shutdown'):
        await close_bot()

    if message.content.startswith('$deepseek'):
        try:
            print("deepsk")
            api_key = os.environ["DEEPSEEK_API_KEY"]
            user_input = message.content[len('$deepseek '):]
            url = "YOUR_DEEPSEEK_API_ENDPOINT"  # Replace with your DeepSeek API endpoint
            headers = {"Authorization": f"Bearer {api_key}"}
            data = {"query": user_input}
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status(
            )  # Raise HTTPError for bad responses (4xx or 5xx)
            response_json = response.json()
            await message.channel.send(json.dumps(response_json, indent=2)
                                       )  # Send formatted JSON response
        except requests.exceptions.RequestException as e:
            await message.channel.send(
                f"Error communicating with DeepSeek API: {e}")
        except KeyError:
            await message.channel.send(
                "DeepSeek API key not found. Please set the DEEPSEEK_API_KEY environment variable."
            )


try:
    token = os.getenv("TOKEN") or ""
    if token == "":
        raise Exception("Please add your token to the Secrets pane.")
    client.run(token)
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
