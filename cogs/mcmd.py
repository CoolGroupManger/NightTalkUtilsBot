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

class mcmd(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def suggest(self, ctx, *, suggest1=None):
        with open('suggest.json', 'r') as f:
            suggest2 = json.load(f)
        suggest2[str(ctx.author.id)] = suggest1
        with open('suggest.json', 'w') as f:
            json.dump(suggest2, f, indent=4)
        await ctx.send(f'Suggested {suggest1} Under The Name {ctx.author.mention}')

    @commands.command()
    async def unsuggest(self, ctx):
        with open('suggest.json', 'r') as f:
            suggest2 = json.load(f)
        suggest2.pop(str(ctx.author.id))
        with open('suggest.json', 'w') as f:
            json.dump(suggest2, f)
        await ctx.send(f'Unsuggested Something From The Name {ctx.author.mention}')     

def setup(bot):
    bot.add_cog(mcmd(bot))
print('Suggest Command Loaded!')