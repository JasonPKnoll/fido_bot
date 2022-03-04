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

def setup(client):
    client.add_cog(Database(client))
