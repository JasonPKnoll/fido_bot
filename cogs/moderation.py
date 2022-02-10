import discord
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if isinstance(message.channel, discord.DMChannel):
            channel = self.client.get_channel(self.client.designated_channel.id)
            await channel.send(f"{message.author} sent:\n```{message.content}```")

def setup(client):
    client.add_cog(Moderation(client))
