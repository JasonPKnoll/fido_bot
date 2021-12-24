import discord
from dotenv import load_dotenv
import re
import os
import random
import asyncio
load_dotenv('.env')

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'
    .format(client))

corn = {"CORN? In mY SeVEr!?",
        "CORN? IN My sEVeR!?",
        "CORN? iN My sEvER!?",
        ":corn: :corn: :corn:",
        "A light wind swept over the CORN, and all nature laughed in the sunshine.",
        "Farming looks mighty easy when your plow is a pencil and you're a thousand miles from the CORN field."
        }

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('ping'):
    if 'corn' in message.content.lower():
        await message.channel.send(f'{random.choice(list(corn))}')

    if 'i love fido' in message.content.lower():
        if message.author.dm_channel == None:
            await message.author.create_dm()
            next

        await message.author.dm_channel.send("Awe, I love you too!")
        await message.author.edit(nick="Fido's Chew Toy")

    if re.search('\\this\\b', message.content.lower()):
        await message.author.edit(nick="YOU DONE DIDDLY DID IT!")

    if re.search("\\bthat\\b", message.content.lower()):
        await message.author.edit(nick="")

    if 'free me fido' in message.content.lower():
        await message.author.edit(nick="")
        await message.channel.send('pong')

client.run(os.getenv('DISCORD_TOKEN'))
