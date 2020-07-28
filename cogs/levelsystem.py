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
import datetime
import math
from math import sqrt

from discord.ext import commands
from discord.utils import get
from discord.ext import tasks
from itertools import cycle
from sqlite3 import connect
from async_timeout import timeout
from discord.ext.commands import has_permissions, MissingPermissions
from functools import partial

class levelsystem(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()

def setup(bot):
    bot.add_cog(levelsystem(bot))
print('Level System Loaded')