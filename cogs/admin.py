import discord
from discord.ext import commands

class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('We have logged in as {0.user}'
        .format(self.client))

    # Before Commands
    async def cog_check(self, ctx):
        return ctx.author.guild_permissions.administrator

    # Commands
    @commands.command()
    async def setbotchannel(self, ctx, message):
        channel = discord.utils.get(ctx.guild.channels, name=message)
        if channel:
            database = self.client.get_cog('Database')
            await database.update_attribute(ctx, 'designated_channel', channel.id)
            await ctx.channel.send(f"My new home has been set to {channel.name}")
        else:
            await ctx.channel.send(f'Could not find any channel named {message}')

    @commands.command()
    async def setemoji(self, ctx, message):
        if len(message) == 1:
            database = self.client.get_cog('Database')
            await database.update_attribute(ctx, 'emoji', message)
            await ctx.channel.send(f'New emoji set to {message}!')

        else:
            await ctx.channel.send("Needs to be only one character. Note that discord does not support adding custom emoji's to nicknames")

    @commands.command()
    async def setaddword(self, ctx, message):
        database = self.client.get_cog('Database')
        await database.get_guild_settings(ctx.guild.id)
        await database.update_attribute(ctx, 'adder_word', message)
        await ctx.channel.send(f"New word for adding {self.client.emoji} is '{message}'")

    @commands.command()
    async def setsubtractword(self, ctx, message):
        database = self.client.get_cog('Database')
        await database.get_guild_settings(ctx.guild.id)
        await database.update_attribute(ctx, 'subtractor_word', message)
        await ctx.channel.send(f"New word for removing all {self.client.emoji} is '{message}'")

    @commands.command()
    async def setlotteryword(self, ctx, message):
        database = self.client.get_cog('Database')
        await database.get_guild_settings(ctx.guild.id)
        await database.update_attribute(ctx, 'lottery_word', message)
        await ctx.channel.send(f"New word for randomly distributing {self.client.emoji} in the server is '{message}'")

    @commands.command()
    async def resetall(self, ctx):
        attributes = [
        {'$set':{'subtractor_word': 'that'}},
        {'$set':{'adder_word': 'this'}},
        {'$set':{'lottery_word': 'spread'}},
        {'$set':{'emoji': '🌽'}}
        ]

        database = self.client.get_cog('Database')
        await database.update_many_attributes(ctx, attributes)
        await database.get_guild_settings(ctx.guild.id)
        await ctx.channel.send(f"Reset: Emoji to {self.client.emoji}, Add word to '{self.client.adder_word}', clear all word to '{self.client.subtractor_word}', and lottery word to '{self.client.lottery_word}'")

    @commands.command()
    async def values(self, ctx):
        database = self.client.get_cog('Database')
        await database.get_guild_settings(ctx.guild.id)

        await ctx.channel.send(f"Emoji is set to {self.client.emoji}, Add word is set to '{self.client.adder_word}', clear all word is set to '{self.client.subtractor_word}', and lottery word is set to '{self.client.lottery_word}'")

    @commands.command()
    async def removeall(self, ctx):
        database = self.client.get_cog('Database')
        await database.get_guild_settings(ctx.guild.id)

        members = await ctx.guild.fetch_members(limit=None).flatten()
        filtered_members = []
        for member in members:
            if member.nick != None and f'{self.client.emoji}' in member.nick:
                filtered_members.append(member)

        for member in filtered_members:
            await member.edit(nick=f"{member.nick}".replace(f"{self.client.emoji}",""))

        await ctx.channel.send(f"I have wipped out all {self.client.emoji}'s from the server.")

def setup(client):
    client.add_cog(Admin(client))
