import discord
from dotenv import load_dotenv
from discord.ext import commands
import re
import os
import random
import asyncio
load_dotenv('.env')

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'
    .format(client))

emoji = '🌽'
designated_channel = None
adder_word = 'this'
subtractor_word = 'that'
plague_word = 'spread'
corn = {"CORN? In mY SeVEr!?",
        "CORN? IN My sEVeR!?",
        "CORN? iN My sEvER!?",
        ":corn: :corn: :corn:",
        "A light wind swept over the CORN, and all nature laughed in the sunshine.",
        "Farming looks mighty easy when your plow is a pencil and you're a thousand miles from the CORN field."
        }

@client.event
async def on_message(message):
    global designated_channel
    global emoji
    global adder_word
    global plague_word
    global subtractor_word

    if message.author == client.user:
        return

    if message.content.lower().startswith('!setemoji'):
        if message.channel.name == f'{designated_channel}':
            if len(message.content.lower().split()[1]) == 1:
                emoji = message.content.lower().split()[1]
            else:
                await message.channel.send("Needs to be only one character. Note that discord does not support adding custom emoji's to nicknames")

    if message.content.lower().startswith('!setbotchannel'):
        if message.author.guild_permissions.administrator:
            channel = discord.utils.get(message.guild.channels, name=message.content.lower().split()[1])
            if channel:
                designated_channel = channel
                await message.channel.send(f"My new home has been set to {channel.name}")
            else:
                await message.channel.send(f'Could not find any channel named {message.content.lower().split()[1]}')

    if message.content.lower().startswith('!setaddword'):
        if designated_channel:
            adder_word = message.content.lower().split()[1]
            await message.channel.send(f"New word for adding {emoji} is '{adder_word}'")

    if message.content.lower().startswith('!setsubtractword'):
        if designated_channel:
            subtractor_word = message.content.lower().split()[1]
            await message.channel.send(f"New word for removing all {emoji} is '{subtractor_word}'")

    if message.content.lower().startswith('!setplagueword'):
        if designated_channel:
            plague_word = message.content.lower().split()[1]
            await message.channel.send(f"New word for plaguing the server with {emoji} is '{plague_word}'")

    if message.content.lower().startswith('!resetall'):
        if designated_channel:
            subtractor_word = 'that'
            adder_word = 'this'
            plague_word = 'spread'
            emoji = '🌽'
            await message.channel.send(f"Reset: Emoji to {emoji}, Add word to '{adder_word}', clear all word to '{subtractor_word}', and plague word to '{plague_word}'")

    if message.content.lower().startswith('!values'):
        if designated_channel:
            await message.channel.send(f"Emoji is set to {emoji}, Add word is set to '{adder_word}', clear all word is set to '{subtractor_word}', and plague word is set to '{plague_word}'")
            return

    if 'corn' in message.content.lower() or '🌽' in message.content.lower():
        await message.channel.send(f'{random.choice(list(corn))}')

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
        await message.author.dm_channel.send("Awe, I love you too!")
        await message.author.edit(nick="Fido's Chew Toy")

    if 'free me fido' in message.content.lower():
        await message.author.edit(nick="")

    if re.search(f'\\b{adder_word}\\b', message.content.lower()):
        for mention in message.mentions:
            if mention.bot != True:
                if mention.nick == None:
                    await mention.edit(nick=f"{mention.name}"+f"{emoji}")
                else:
                    await mention.edit(nick=f"{mention.nick}"+f"{emoji}")

                await message.channel.send(f'{mention.nick}'.replace(f"{emoji}","")+f' has gained +1 {emoji}')
            else:
                continue

        if message.author.nick == None:
            await message.author.edit(nick=f"{message.author.name}"+f"{emoji}")
        else:
            await message.author.edit(nick=f"{message.author.nick}"+f"{emoji}")

        await message.channel.send(f'{message.author.nick}'.replace(f"{emoji}","")+f' has gained +1 {emoji}')

    if re.search(f"\\b{subtractor_word}\\b", message.content.lower()):
        x = len(message.author.nick)
        await message.author.edit(nick=f"{message.author.nick}".replace(f"{emoji}",""))
        await message.channel.send(f"{message.author.nick} removed {abs(len(message.author.nick)-x)} {emoji}")

    if re.search(f"\\b{plague_word}\\b", message.content.lower()):
        members = await message.guild.fetch_members(limit=None).flatten()
        for member in random.sample(members, 5):
            if member.bot != True and member.guild_permissions.administrator != True:
                if member.nick == None:
                    await member.edit(nick=f"{member.name}"+f"{emoji}")
                else:
                    await member.edit(nick=f"{member.nick}"+f"{emoji}")

                await message.channel.send(f'{member.nick}'.replace(f"{emoji}","")+f' has gained +1 {emoji}')
            else:
                continue
        await message.channel.send(f'And so the {emoji} doth spread!')

    if message.content.lower().startswith('!removeall'):
        if message.channel.name == f"{designated_channel}":
            members = await message.guild.fetch_members(limit=None).flatten()
            filtered_members = []
            for member in members:
                if member.nick != None and f'{emoji}' in member.nick:
                    filtered_members.append(member)

            for member in filtered_members:
                await member.edit(nick=f"{member.nick}".replace(f"{emoji}",""))

            await message.channel.send(f'I have wipped out the {emoji} plague.')
            await message.channel.send(f'Everyone has lost their {emoji}')

        else:
            await message.channel.send(f'You asked me to wipe out the {emoji} plague, but not through the right channel.')

    if 'damn daniel' in message.content.lower():
        await message.channel.send(f'https://c.tenor.com/sxLBjystCmIAAAAC/damn-daniel-one-piece.gif')

    if message.content.lower().startswith('!infectme'):
        x = int(message.content.lower().split()[1])
        if x > 0:
            y = 0
            if message.author.nick == None:
                name = message.author.name
            else:
                name = message.author.nick
            if (len(name) + x) <= 32:
                pass
            else:
                x = 32 - len(name)
            if message.author.nick == None:
                await message.author.edit(nick=f"{message.author.name}"+f"{emoji*x}")
            else:
                await message.author.edit(nick=f"{message.author.nick}"+f"{emoji*x}")

            await message.channel.send(f'{message.author.nick}'.replace(f"{emoji}","")+f' has gained +{x} {emoji}')

    if message.content.lower().startswith('!transferto'):
        if message.mentions[0] != None:
            if message.mentions[0].bot != True and message.mentions[0].guild_permissions.administrator != True:
                x = int(message.content.split()[2])

                if f'{x*emoji}' in f'{message.author.nick}':
                    pass
                else:
                    x = message.author.nick.count(f'{emoji}')
                if message.mentions[0].nick == None:
                    name = message.mentions[0].name
                else:
                    name = message.mentions[0].nick
                if (len(name) + x) <= 32:
                    pass
                else:
                    x = 32 - len(name)
                if message.mentions[0].nick == None:
                    await message.mentions[0].edit(nick=f"{message.mentions[0].name}"+f"{emoji*x}")
                else:
                    await message.mentions[0].edit(nick=f"{message.mentions[0].nick}"+f"{emoji*x}")

                await message.author.edit(nick=f"{message.author.nick}".removesuffix(f"{emoji*x}"))
                await message.channel.send(f'{message.author.nick}'.replace(f"{emoji}","")+f' transfered {x} {emoji} to '+f'{message.mentions[0].nick}'.replace(f"{emoji}",""))
            else:
                await message.channel.send("Bots and Admins cannot be given emoji's")

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

    if isinstance(message.channel, discord.DMChannel):
        channel = client.get_channel(designated_channel.id)
        await channel.send(f"{message.author} sent:\n```{message.content}```")

client.run(os.getenv('DISCORD_TOKEN'))
