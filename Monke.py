#!/usr/bin/env python

import discord
import asyncio
import os
import json # For custom prefixes later on
import traceback

from dotenv import load_dotenv
from discord.ext import commands
from os.path import isfile, join

# Loadeth dotenv
load_dotenv()

# Geteth tokeneth
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix = "m!",
                   description = 'Monke Bot was made to fuel discord induced autism',
                   case_insensitive=True) # Discord Bot <- BOT!
                                          # (Some retarded tutorials will tell u to
                                          # switch client and bot like FUCKING RETARDS)
client = discord.Client() # Discord Client

# Help is bad!
bot.remove_command("help")

@bot.event
async def on_ready():
    # 1337 Console Text
    print('I shall fuck Discord up')
    await LoadCogs()

# Load all the Cogs in Folder "Modules"
async def LoadCogs():
    for cog in [f.replace('.py', "") for f in os.listdir("Modules") if isfile(join("Modules", f))]:
        try:
            if not "__init__" in cog:
                bot.load_extension("Modules." + cog)
                print("Loaded {}".format(cog))
        except Exception as e:
            print("Couldn't load {}.".format(cog))
            traceback.print_exc()

if __name__ == '__main__':
    bot.run(TOKEN, reconnect=True)
else:
    del bot
