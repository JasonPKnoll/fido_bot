import discord
from dotenv import load_dotenv
from discord.ext import commands
import re
import os
import random
import asyncio
load_dotenv('.env')

client = commands.Bot(command_prefix = '!', intents=discord.Intents.all())

client.emoji = '🌽'
client.designated_channel = None
client.adder_word = 'this'
client.subtractor_word = 'that'
client.plague_word = 'spread'
client.corn = open("responses/corn.txt").read().splitlines()

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.event


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
        changed = []
        for member in random.sample(members, 5):
            if member.bot == False and member.guild_permissions.administrator == False:
                if member.nick == None:
                    await member.edit(nick=f"{member.name}"+f"{emoji}")
                else:
                    await member.edit(nick=f"{member.nick}"+f"{emoji}")

                changed.append((f'{member.nick}'.replace(f"{emoji}","")))
            else:
                continue
        changed = [value for value in changed if value != 'None']
        await message.channel.send(f"{', '.join(changed)} have gained +1 {emoji}")
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
            if message.mentions[0].bot == False and message.mentions[0].guild_permissions.administrator == False:
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
                if message.author.nick == None:
                    await message.channel.send(f'{message.author.name}'+f' transfered {x} {emoji} to '+f'{message.mentions[0].nick}'.replace(f"{emoji}",""))
                else:
                    await message.channel.send(f'{message.author.nick}'.replace(f"{emoji}","")+f' transfered {x} {emoji} to '+f'{message.mentions[0].nick}'.replace(f"{emoji}",""))
            else:
                await message.channel.send("Bots and Admins cannot be given emoji's")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('DISCORD_TOKEN'))
