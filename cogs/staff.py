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

class moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_role('Admin')
    async def warn(self, ctx, member: discord.Member=None, *, reason=None):
        with open('warnings.json', 'r') as f:
            warnings = json.load(f)
        warnings[str(member.id)] = reason
        with open('warnings.json', 'w') as f:
            json.dump(warnings, f, indent=4)
        await ctx.send(f'warned {member.mention} for {reason} by {ctx.name}')

    @commands.command()
    @commands.has_role('Admin')
    async def unwarn(self, ctx, member: discord.Member=None, *, reason=None):
        with open('warnings.json', 'r') as f:
            warnings = json.load(f)
        warnings.pop(str(member.id), str(reason))
        with open('warnings.json', 'w') as f:
            json.dump(warnings, f ,indent=4)
        await ctx.send(f'unwarned {member.mention} by {ctx.name}')

    @commands.command()
    @commands.has_role('Admin')
    async def L(self, ctx, member:discord.Member=None, *, a=None):

    @commands.command()
    @commands.has_role('Admin')
    async def ban(self, ctx, member: discord.Member, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}! For {reason} by {ctx.name}')
        with open('bans.json', 'r') as f:
            bans = json.load(f)
        bans[str(member.id)] = reason
        with open('bans.json', 'w') as f:
            json.dump(bans, f, indent=4)

    @commands.command()
    @commands.has_role('Admin')
    async def unblacklist(self, ctx, member: discord.Member=None):
        with open('bans.json', 'r') as f:
            bans = json.load(f)
        bans.pop(str(member.id))
        with open('bans.json', 'w') as f:
            json.dump(bans, f, indent=4)
            
    @commands.command()
    @commands.has_role('Staff')
    async def kick(self, ctx, member: discord.member, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention}! For {reason} by {ctx.name}')

    @commands.command()
    @commands.has_role('Staff')
    async def clear(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'Cleared {amount} Messages', delete_after=500)

def setup(bot):
    bot.add_cog(moderation(bot))
print('Modration Loaded')
