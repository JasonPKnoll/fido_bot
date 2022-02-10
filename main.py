import discord
from dotenv import load_dotenv
from discord.ext import commands
import os
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

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('DISCORD_TOKEN'))
