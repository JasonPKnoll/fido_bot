import discord
from dotenv import load_dotenv
import os
load_dotenv('.env')

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'
    .format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('ping'):
        await message.channel.send('pong')

client.run(os.getenv('DISCORD_TOKEN'))
