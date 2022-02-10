import discord
import re
import random
from discord.ext import commands

class Emoji(commands.Cog):

    def __init__(self, client):
        self.client = client


def setup(client):
    client.add_cog(Emoji(client))
