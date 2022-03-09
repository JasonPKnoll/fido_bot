import discord
import random
import asyncio
from discord.ext import commands

class Meme(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        if message.context.startswith(self.client.command_prefix):
            return

        if 'ping' in message.content.lower():
            await message.channel.send('pong')

        if 'pong' in message.content.lower():
            await message.channel.send('ping')

        if message.content.lower() == 'h':
            await message.channel.send(':regional_indicator_h:')

        if 'beep' in message.content.lower():
            await message.channel.send('boop')

        if 'boop' in message.content.lower():
            await message.channel.send('beep')

        if 'corn' in message.content.lower() or '🌽' in message.content.lower():
            await message.channel.send(f'{random.choice(list(self.client.corn))}')

        if 'damn daniel' in message.content.lower():
            await message.channel.send(f'https://c.tenor.com/sxLBjystCmIAAAAC/damn-daniel-one-piece.gif')

        if 'social credit' in message.content.lower():
            await message.channel.send('<:HAHAHAHAEMOJI:923651162954153984> OH WOW! sO MuCh SoCiAL CreDiT! <:HAHAHAHAEMOJI:923651162954153984>')

        if 'who' in message.content.lower():
            await message.reply('Who?')
            await asyncio.sleep(3)
            await message.channel.send('Cares '+message.author.mention)

        if 'i love fido' in message.content.lower():
            if message.author.dm_channel == None:
                await message.author.create_dm()
                next
            await message.author.edit(nick="Fido's Chew Toy")
            await message.author.dm_channel.send("Awe, I love you too!")

        if 'free me fido' in message.content.lower():
            await message.author.edit(nick="")

def setup(client):
    client.add_cog(Meme(client))
