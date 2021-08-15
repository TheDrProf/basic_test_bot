import discord
from discord.ext import commands
import json

class cogs_name(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(cogs_name(bot))
