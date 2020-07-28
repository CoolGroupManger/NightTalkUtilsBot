import discord
import asyncio
import json
import random
import logging
import sqlite3
import time
import random
import re
import os
import sys

from discord.ext import commands
from discord.utils import get
from discord.ext import tasks
from itertools import cycle
from sqlite3 import connect
from async_timeout import timeout
from discord.ext.commands import has_permissions
from discord.ext.commands import MissingPermissions
from discord.ext.commands import CheckFailure
from discord.ext.commands import check
from functools import partial


#def PREFIX(bot, message):
    #with open('prefixes.json', 'r') as f:
        #prefixes = json.load(f)

        #return prefixes[str(message.guild.id)]

READY = 'Logged In NightTalk Utilities#0604 and Is Ready To Go'

bot = commands.Bot(command_prefix='+')
bot.remove_command('help')

os.chdir(r'C:\Users\arjun\Desktop\NightTalk Utilities Bot')

@bot.event
async def on_ready():
    bot.load_extension('cogs.staff')
    bot.load_extension('cogs.utils')
    bot.load_extension('cogs.mcmd')
    await bot.change_presence(activity=discord.Game('Something.'))
    print(READY)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'You Can\'t Use That Command! Error[Cant-Use-That-Command]')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'You Need More Things For That Command! Error[Missing-Args]')
    elif isinstance(error, commands.NotOwner):
        await ctx.send(f'Your Not Owner! Error[Not-Owner]')
    elif isinstance(error, commands.TooManyArguments):
        await ctx.send(f'Those Are Too Many Things There! Error[Too-Many-Args]')
    elif isinstance(error, commands.MissingAnyRole):
        await ctx.send(f'You Are Missing Roles! Error[Missing-Roles]')
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send(f'That Command Was Not Found! Error[Command-Not-Found]')

@bot.event
async def on_member_join(member: discord.Member):
    #welcome
    channel = bot.get_channel(734866973531570186)
    await channel.send(f'Welcome to The Server {member.mention}. Go to <#rules> to get setup.')
    #json
    with open('users.json', 'r') as f:
        users = json.load(f)

    users[str(member.id)] = 0

    with open('users.json', 'w') as f:
        json.dump(users, f)

@bot.event
async def on_message(message):
    with open('users.json', 'r') as f:
        users = json.load(f)



    with open('users.json', 'w') as f:
        json.dump(users, f)

@bot.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '+'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f ,indent=4)

@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f ,indent=4)

@bot.command()
async def cpe(ctx, cp=None):
    await bot.change_presence(activity=discord.Game(cp))
    await ctx.send(f'Changed It Too. {cp}')
    print(f'Changed Presence To. {cp}')

@bot.command()
async def give(ctx, *, a=None):
    await ctx.send('k gimme a sec')
    await asyncio.sleep(3)
    embed=discord.Embed(color=0xfffeff)
    embed.set_thumbnail(url="https://pics.me.me/the-fuck-you-say-to-me-you-little-shit-ninja-48784833.png")
    await ctx.send(embed=embed)

@bot.command()
async def load(ctx):
    bot.load_extension('cogs.staff')
    bot.load_extension('cogs.utils')
    print('Loaded')
    await ctx.send('Loaded Files')
    await bot.change_presence(activity=discord.Game('Something.'))

@bot.command()
async def unload(ctx):
    bot.unload_extension('cogs.staff')
    bot.unload_extension('cogs.utils')
    print('Unloaded')
    await ctx.send('Unloaded Files Do +load To Load The Files')

@bot.command()
@commands.has_role('Owners')
async def config_prefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    prefixes[str(ctx.guild.id)] = prefix
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f ,indent=4)
    await ctx.send(f'Changed The Prefix To ---> {prefix}')

def read_token():
    with open("ztoken.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()
token = read_token()
bot.run(token)
