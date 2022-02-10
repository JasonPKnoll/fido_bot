import discord
from dotenv import load_dotenv
from discord.ext import commands
import re
import os
import random
import asyncio
load_dotenv('.env')

client = commands.Bot(command_prefix = '!', intents=discord.Intents.all())

client.emoji = '🌽'
client.designated_channel = None
client.adder_word = 'this'
client.subtractor_word = 'that'
client.plague_word = 'spread'
client.corn = open("responses/corn.txt").read().splitlines()

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.event

    if message.content.lower().startswith('!transferto'):
        if message.mentions[0] != None:
            if message.mentions[0].bot == False and message.mentions[0].guild_permissions.administrator == False:
                x = int(message.content.split()[2])

                if f'{x*emoji}' in f'{message.author.nick}':
                    pass
                else:
                    x = message.author.nick.count(f'{emoji}')
                if message.mentions[0].nick == None:
                    name = message.mentions[0].name
                else:
                    name = message.mentions[0].nick
                if (len(name) + x) <= 32:
                    pass
                else:
                    x = 32 - len(name)
                if message.mentions[0].nick == None:
                    await message.mentions[0].edit(nick=f"{message.mentions[0].name}"+f"{emoji*x}")
                else:
                    await message.mentions[0].edit(nick=f"{message.mentions[0].nick}"+f"{emoji*x}")

                await message.author.edit(nick=f"{message.author.nick}".removesuffix(f"{emoji*x}"))
                if message.author.nick == None:
                    await message.channel.send(f'{message.author.name}'+f' transfered {x} {emoji} to '+f'{message.mentions[0].nick}'.replace(f"{emoji}",""))
                else:
                    await message.channel.send(f'{message.author.nick}'.replace(f"{emoji}","")+f' transfered {x} {emoji} to '+f'{message.mentions[0].nick}'.replace(f"{emoji}",""))
            else:
                await message.channel.send("Bots and Admins cannot be given emoji's")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('DISCORD_TOKEN'))
