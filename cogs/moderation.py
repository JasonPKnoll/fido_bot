import discord
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if isinstance(message.channel, discord.DMChannel):
            for guild in message.author.mutual_guilds:
                database = self.client.get_cog('Database')
                await database.get_guild_settings(guild.id)
                channel = self.client.get_channel(self.client.designated_channel)
                if channel:
                    await channel.send(f"{message.author} sent:\n```{message.content}```")

def setup(client):
    client.add_cog(Moderation(client))
