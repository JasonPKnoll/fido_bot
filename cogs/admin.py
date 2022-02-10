import discord
from discord.ext import commands

class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Before Commands
    async def cog_check(self, ctx):
        return ctx.author.guild_permissions.administrator

    # Commands
    @commands.command()
    async def setemoji(self, ctx, message):
        if len(message) == 1:
            self.client.emoji = message
        else:
            await ctx.channel.send("Needs to be only one character. Note that discord does not support adding custom emoji's to nicknames")

def setup(client):
    client.add_cog(Admin(client))
