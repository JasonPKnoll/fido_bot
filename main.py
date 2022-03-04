import discord
from dotenv import load_dotenv
from discord.ext import commands
import os
import pymongo
from pymongo import MongoClient
import urllib.parse

load_dotenv('.env')

client = commands.Bot(command_prefix = '!', intents=discord.Intents.all())

DB_USER = urllib.parse.quote_plus(os.getenv('DB_USER'))
DB_PASSWORD = urllib.parse.quote_plus(os.getenv('DB_PASSWORD'))
client.cluster = MongoClient(os.getenv('MONGO_URL').format(DB_USER, DB_PASSWORD))
client.db = client.cluster[os.getenv('DB_NAME')]
client.db_guilds = client.db["db_guilds"]

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
