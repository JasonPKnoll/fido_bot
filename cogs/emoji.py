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
            await message.author.edit(nick=f"{message.author.nick}".replace(f"{self.client.emoji}",""))
            if message.author.nick == None:
                await message.channel.send(f"{message.author.name} removed {abs(len(message.author.name)-x)} {self.client.emoji}")
            else:
                await message.channel.send(f"{message.author.nick} removed {abs(len(message.author.nick)-x)} {self.client.emoji}")

        if re.search(f"\\b{self.client.plague_word}\\b", message.content.lower()):
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
            await message.channel.send(f'And so the {self.client.emoji} doth spread!')

def setup(client):
    client.add_cog(Emoji(client))
