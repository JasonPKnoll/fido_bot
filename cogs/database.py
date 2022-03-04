import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import pymongo
from pymongo import MongoClient
load_dotenv('.env')

class Database(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def add_guild(self, id):
        try:
            self.client.db_guilds.find({'_id': id})[0]
        except IndexError:
            data = {
            '_id': guild.id,
            'emoji': '🌽',
            'designated_channel': None,
            'adder_word': 'this',
            'subtractor_word': 'that',
            'lottery_word': 'spread'
            }

            self.client.db_guilds.insert_one(data);

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.client.guilds:
            await self.add_guild(guild.id)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await self.add_guild(guild.id)

def setup(client):
    client.add_cog(Database(client))
