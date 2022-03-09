import discord
import re
import random
from discord.ext import commands

class Emoji(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.client.user:
            return

        if message.content.startswith(self.client.command_prefix):
            return

        database = self.client.get_cog('Database')
        await database.get_guild_settings(message.guild.id)

        #ADD TRIGGER
        if re.search(f'\\b{self.client.adder_word}\\b', message.content.lower()):
            if len(message.mentions) > 0:
                await self.distribute_for_mentions(message, message.mentions)

            await self.gain_emojis(message.author, 1)
            await message.channel.send(f'{message.author.nick}'.replace(f"{self.client.emoji}","")+f' has gained +1 {self.client.emoji}')

        #SUBTRACT TRIGGER
        if re.search(f"\\b{self.client.subtractor_word}\\b", message.content.lower()):
            x = len(message.author.nick)
            y = len(message.author.nick.replace(f"{self.client.emoji}",""))

            if x - y > 0:
                await message.author.edit(nick=f"{message.author.nick}".replace(f"{self.client.emoji}",""))

                if message.author.nick:
                    await message.channel.send(f"{message.author.nick} lost {abs(len(message.author.nick)-x)} {self.client.emoji}")
                if message.author.nick == None:
                    await message.channel.send(f"{message.author.name} lost {abs(len(message.author.name)-x)} {self.client.emoji}")

        #LOTTERY TRIGGER
        if re.search(f"\\b{self.client.lottery_word}\\b", message.content.lower()):
            members = [member for member in self.client.get_all_members() if not (member.bot or member.guild_permissions.administrator or member.nick and len(member.nick) >= 32)]

            changed = []
            spread_count = 5
            if len(members) < 5:
                spread_count = len(members)

            if spread_count == 0:
                await message.channel.send(f"There is no one I can give {self.client.emoji} to!")
                return

            for member in random.sample(members, spread_count):
                await self.gain_emojis(member, 1)

                changed.append((f'{member.nick}'.replace(f"{self.client.emoji}","")))

            changed = [value for value in changed if value != 'None']
            await message.channel.send(f"{', '.join(changed)} have gained +1 {self.client.emoji}")
            await message.channel.send(f"{self.client.emoji}'s have spread throughout {message.guild.name}!")

    # Commands
    @commands.command()
    async def giveme(self, ctx):
        database = self.client.get_cog('Database')
        await database.get_guild_settings(ctx.guild.id)

        x = int(ctx.message.content.lower().split()[1])
        if x <= 0:
            return

        y = 0
        if ctx.message.author.nick:
            name = ctx.message.author.nick
        if ctx.message.author.nick == None:
            name = ctx.message.author.name

        if (len(name) + x) >= 32:
            x = 32 - len(name)

        await self.gain_emojis(ctx.message.author, x)
        await ctx.message.channel.send(f'{ctx.message.author.nick}'.replace(f"{self.client.emoji}","")+f' has gained +{x} {self.client.emoji}')

    @commands.command()
    async def transferto(self, ctx):
        database = self.client.get_cog('Database')
        await database.get_guild_settings(ctx.guild.id)

        transfer_target = ctx.message.mentions[0]
        if transfer_target == None:
            return
        if transfer_target.bot or transfer_target.guild_permissions.administrator:
            await ctx.message.channel.send("Bots and Admins cannot be given emoji's")
            return
        if len(ctx.message.content.split()) <= 2:
            await ctx.message.channel.send("You need to specify an amount")
            return


        x = int(ctx.message.content.split()[2])
        if f'{x*self.client.emoji}' not in f'{ctx.message.author.nick}':
            x = ctx.message.author.nick.count(f'{self.client.emoji}')

        if transfer_target.nick:
            name = transfer_target.nick
        if transfer_target.nick == None:
            name = transfer_target.name

        if (len(name) + x) > 32:
            x = 32 - len(name)

        if x == 0:
            await ctx.message.channel.send(f'{transfer_target.nick}'.replace(f"{self.client.emoji}","")+' has no more room in their name for additional emojis!')
            return

        await self.gain_emojis(transfer_target, x)

        await ctx.message.author.edit(nick=f"{ctx.message.author.nick}".removesuffix(f"{self.client.emoji*x}"))
        if ctx.message.author.nick:
            await ctx.message.channel.send(f'{ctx.message.author.nick}'.replace(f"{self.client.emoji}","")+f' transfered {x} {self.client.emoji} to '+f'{transfer_target.nick}'.replace(f"{self.client.emoji}",""))
        if ctx.message.author.nick == None:
            await ctx.message.channel.send(f'{ctx.message.author.name}'+f' transfered {x} {self.client.emoji} to '+f'{transfer_target.nick}'.replace(f"{self.client.emoji}",""))


    # Helpers
    async def gain_emojis(self, member, amount):
        if member.nick:
            await member.edit(nick=f"{member.nick}"+f"{self.client.emoji * amount}")
        if member.nick == None:
            await member.edit(nick=f"{member.name}"+f"{self.client.emoji * amount}")

    async def distribute_for_mentions(self, message, mentions):
        for mention in mentions:
            if mention.bot == True or mention.guild_permissions.administrator == True:
                continue
            if mention.nick:
                await mention.edit(nick=f"{mention.nick}"+f"{self.client.emoji}")
            if mention.nick == None:
                await mention.edit(nick=f"{mention.name}"+f"{self.client.emoji}")

            await message.channel.send(f'{mention.nick}'.replace(f"{self.client.emoji}","")+f' has gained +1 {self.client.emoji}')


def setup(client):
    client.add_cog(Emoji(client))
