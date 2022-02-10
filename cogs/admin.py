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
    async def setbotchannel(self, ctx, message):
        channel = discord.utils.get(ctx.guild.channels, name=message)
        if channel:
            self.client.designated_channel = channel
            await ctx.channel.send(f"My new home has been set to {channel.name}")
        else:
            await ctx.channel.send(f'Could not find any channel named {message}')

    @commands.command()
    async def setemoji(self, ctx, message):
        if len(message) == 1:
            self.client.emoji = message
        else:
            await ctx.channel.send("Needs to be only one character. Note that discord does not support adding custom emoji's to nicknames")

def setup(client):
    client.add_cog(Admin(client))
