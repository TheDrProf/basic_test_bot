import discord
from discord.ext import commands
import json

class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='pup', description="Description")
    async def pup(self, ctx):
        """Info"""
        await ctx.send(':wolf:')

def setup(bot):
    bot.add_cog(test(bot))
