import discord
import json

# 様々を定義
intents = discord.Intents.none()
intents.message_content = True
client = discord.Client(intents=intents)
config = json.load(open("config.json", "r"))

@client.event
async def on_ready():
    print("-" * 16)
    print("bot is ready!")
    print("-" * 16)

client.run(config["token"])