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
            '_id': id,
            'emoji': '🌽',
            'designated_channel': None,
            'adder_word': 'this',
            'subtractor_word': 'that',
            'lottery_word': 'spread'
            }

            self.client.db_guilds.insert_one(data);

    async def update_attribute(self, ctx, attribute, new_value):
        self.client.db_guilds.update_one(
        {'_id': ctx.guild.id},
        {'$set': {attribute: new_value}}
        )

    async def update_many_attributes(self, ctx, attributes):
        self.client.db_guilds.update_one({'_id': ctx.guild.id}, attributes)

    async def get_guild_settings(self, id):
        guild_settings = self.client.db_guilds.find({'_id': id})[0]
        self.client.emoji = guild_settings['emoji']
        self.client.designated_channel = guild_settings['designated_channel']
        self.client.adder_word = guild_settings['adder_word']
        self.client.subtractor_word = guild_settings['subtractor_word']
        self.client.lottery_word = guild_settings['lottery_word']

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
