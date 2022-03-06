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

        database = self.client.get_cog('Database')
        await database.get_guild_settings(message.guild.id)

        if re.search(f'\\b{self.client.adder_word}\\b', message.content.lower()):
            for mention in message.mentions:
                if mention.bot != True:
                    if mention.nick == None:
                        await mention.edit(nick=f"{mention.name}"+f"{self.client.emoji}")
                    else:
                        await mention.edit(nick=f"{mention.nick}"+f"{self.client.emoji}")

                    await message.channel.send(f'{mention.nick}'.replace(f"{self.client.emoji}","")+f' has gained +1 {self.client.emoji}')
                else:
                    continue

            if message.author.nick == None:
                await message.author.edit(nick=f"{message.author.name}"+f"{self.client.emoji}")
            else:
                await message.author.edit(nick=f"{message.author.nick}"+f"{self.client.emoji}")

            await message.channel.send(f'{message.author.nick}'.replace(f"{self.client.emoji}","")+f' has gained +1 {self.client.emoji}')


        if re.search(f"\\b{self.client.subtractor_word}\\b", message.content.lower()):
            x = len(message.author.nick)
            y = len(message.author.nick.replace(f"{self.client.emoji}",""))

            if x - y > 0:
                await message.author.edit(nick=f"{message.author.nick}".replace(f"{self.client.emoji}",""))
                if message.author.nick == None:
                    await message.channel.send(f"{message.author.name} removed {abs(len(message.author.name)-x)} {self.client.emoji}")
                else:
                    await message.channel.send(f"{message.author.nick} removed {abs(len(message.author.nick)-x)} {self.client.emoji}")


        if re.search(f"\\b{self.client.lottery_word}\\b", message.content.lower()):
            members = await message.guild.fetch_members(limit=None).flatten()
            changed = []
            for member in random.sample(members, 5):
                if member.bot == False and member.guild_permissions.administrator == False:
                    if member.nick == None:
                        await member.edit(nick=f"{member.name}"+f"{self.client.emoji}")
                    else:
                        await member.edit(nick=f"{member.nick}"+f"{self.client.emoji}")

                    changed.append((f'{member.nick}'.replace(f"{self.client.emoji}","")))
                else:
                    continue
            changed = [value for value in changed if value != 'None']
            await message.channel.send(f"{', '.join(changed)} have gained +1 {self.client.emoji}")
            await message.channel.send(f"The {self.client.emoji}'s has spread!")

    # Commands
    @commands.command()
    async def giveme(self, ctx):
        database = self.client.get_cog('Database')
        await database.get_guild_settings(ctx.guild.id)

        x = int(ctx.message.content.lower().split()[1])
        if x > 0:
            y = 0
            if ctx.message.author.nick == None:
                name = ctx.message.author.name
            else:
                name = ctx.message.author.nick
            if (len(name) + x) <= 32:
                pass
            else:
                x = 32 - len(name)
            if ctx.message.author.nick == None:
                await ctx.message.author.edit(nick=f"{ctx.message.author.name}"+f"{self.client.emoji*x}")
            else:
                await ctx.message.author.edit(nick=f"{ctx.message.author.nick}"+f"{self.client.emoji*x}")

            await ctx.message.channel.send(f'{ctx.message.author.nick}'.replace(f"{self.client.emoji}","")+f' has gained +{x} {self.client.emoji}')

    @commands.command()
    async def transferto(self, ctx):
        database = self.client.get_cog('Database')
        await database.get_guild_settings(ctx.guild.id)

        if ctx.message.mentions[0] != None:
            if ctx.message.mentions[0].bot == False and ctx.message.mentions[0].guild_permissions.administrator == False:
                if len(ctx.message.content.split()) <= 2:
                    await ctx.message.channel.send("You need to specify an amount")
                    return
                x = int(ctx.message.content.split()[2])

                if f'{x*self.client.emoji}' in f'{ctx.message.author.nick}':
                    pass
                else:
                    x = ctx.message.author.nick.count(f'{self.client.emoji}')
                if ctx.message.mentions[0].nick == None:
                    name = ctx.message.mentions[0].name
                else:
                    name = ctx.message.mentions[0].nick
                if (len(name) + x) <= 32:
                    pass
                else:
                    x = 32 - len(name)
                if ctx.message.mentions[0].nick == None:
                    await ctx.message.mentions[0].edit(nick=f"{ctx.message.mentions[0].name}"+f"{self.client.emoji*x}")
                else:
                    await ctx.message.mentions[0].edit(nick=f"{ctx.message.mentions[0].nick}"+f"{self.client.emoji*x}")

                await ctx.message.author.edit(nick=f"{ctx.message.author.nick}".removesuffix(f"{self.client.emoji*x}"))
                if ctx.message.author.nick == None:
                    await ctx.message.channel.send(f'{ctx.message.author.name}'+f' transfered {x} {self.client.emoji} to '+f'{ctx.message.mentions[0].nick}'.replace(f"{self.client.emoji}",""))
                else:
                    await ctx.message.channel.send(f'{ctx.message.author.nick}'.replace(f"{self.client.emoji}","")+f' transfered {x} {self.client.emoji} to '+f'{ctx.message.mentions[0].nick}'.replace(f"{self.client.emoji}",""))
            else:
                await ctx.message.channel.send("Bots and Admins cannot be given emoji's")

def setup(client):
    client.add_cog(Emoji(client))
