import discord
import random
import asyncio
from discord.ext import commands

class Meme(commands.Cog):

    def __init__(self, client):
        self.client = client

def setup(client):
    client.add_cog(Meme(client))
