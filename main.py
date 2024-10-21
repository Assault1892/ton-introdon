import discord
from discord import app_commands
import json
import time

# 様々を定義
intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# configをロード
config = json.load(open("config.json", "r"))

# テラーリストと対応音源をロード
terror_file = json.load(open("./audio/terror.json", "r"))

@client.event
async def on_ready():
    print("-" * 16)
    # print("syncing: slash command")
    # await tree.sync() # スラコマ同期
    # print("synced: slash command")
    # ready?
    print("i'm ready!")
    print("-" * 16)

# スラッシュコマンド登録

@tree.command(name="play", 
              description="イントロドンを開始")
async def playgame(interaction: discord.Interaction):
    user_voice_channel_name =  interaction.user.voice.channel.name
    user_voice_channel_id =    interaction.user.voice.channel.id # 音声再生チャンネル
    user_answer_channel_name = interaction.channel.name
    user_answer_channel_id =   interaction.channel.id # 回答受付チャンネル
    await interaction.response.send_message(f"""
以下のボイスチャンネルに参加し、このチャンネルを回答用チャンネルとしてマークします！
ボイスチャンネル 名前: `{user_voice_channel_name}` | ボイスチャンネル ID: `{user_voice_channel_id}`
回答用チャンネル 名前: `{user_answer_channel_name}` | 回答用チャンネル ID: `{user_answer_channel_id}`

マーク解除するには `終了` と発言することでマーク解除できます！
""")
    

client.run(config["token"])