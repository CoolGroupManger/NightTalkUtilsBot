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
from discord.ext.commands import has_permissions, MissingPermissions
from functools import partial

class utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Ping! {round(self.bot.latency * 1000)}')

    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(title="Help", description="Public Commands", color=0x93afdc)
        embed.add_field(name="+help", value="(Shows This Command)", inline=False)
        embed.add_field(name="+ping", value="Ping Pong!", inline=False)
        embed.add_field(name="+cpe", value="Change The Bots Presence", inline=False)
        embed.set_footer(text="Help")
        await ctx.send(embed=embed)

    @commands.command()
    async def admincommands(self, ctx):
        embed=discord.Embed(title="Help", description="Public Commands", color=0x93afdc)
        embed.add_field(name="+kick", value="+kick [person] [reason]", inline=False)
        embed.add_field(name="+ban", value="+ban [person] [reason]", inline=False)
        embed.add_field(name="+warn", value="+warn [person] [reason]", inline=False)
        embed.add_field(name="+unwarn", value="+warn [person]", inline=False)
        embed.set_footer(text="Help")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(utils(bot))
print('Utils Loaded')