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

    if 'corn' in message.content.lower() or '🌽' in message.content.lower():
        await message.channel.send(f'{random.choice(list(corn))}')

    if 'christmas' in message.content.lower():
        await message.channel.send('CHRISTMAS? In mY SeVEr!?')

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

    if re.search('\\bthis\\b', message.content.lower()):
        for mention in message.mentions:
            if mention.bot != True:
                if mention.nick == None:
                    await mention.edit(nick=f"{mention.name}"+"🌽")
                else:
                    await mention.edit(nick=f"{mention.nick}"+"🌽")
            else:
                continue

        if message.author.nick == None:
            await message.author.edit(nick=f"{message.author.name}"+"🌽")
        else:
            await message.author.edit(nick=f"{message.author.nick}"+"🌽")


    if re.search("\\bthat\\b", message.content.lower()):
        await message.author.edit(nick=f"{message.author.nick}".replace("🌽",""))

    if 'spread' in message.content.lower():
        members = await message.guild.fetch_members(limit=None).flatten()
        for member in random.sample(members, 5):
            if member.bot != True:
                if member.nick == None:
                    await member.edit(nick=f"{member.name}"+"🌽")
                else:
                    await member.edit(nick=f"{member.nick}"+"🌽")
            else:
                continue

        await message.channel.send('And so the corn doth spread!')

    if message.content.lower().startswith('🌽 removeall'):
        if message.channel.name == "fido-playground":
            members = await message.guild.fetch_members(limit=None).flatten()
            filtered_members = []
            for member in members:
                if member.nick != None and '🌽' in member.nick:
                    filtered_members.append(member)

            for member in filtered_members:
                await member.edit(nick=f"{member.nick}".replace("🌽",""))

            await message.channel.send('I have wipped out the 🌽 plague.')

        else:
            await message.channel.send('You asked me to wipe the 🌽 plague, but not through the right channel.')

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
