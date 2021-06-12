import discord
from discord.ext import commands

class NSFW(commands.Cog):
    """booba & women (& men)"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["booba", "tits", "cleavage", "tiddies", "chunkers", "knockers", "chest"])
    @commands.is_nsfw()
    async def boobs(self, ctx):
        """Fat on meat surrounded by skin"""
        ctx.send("booba")

def setup(bot):
    bot.add_cog(NSFW(bot))
