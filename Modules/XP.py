import discord
import json

from discord.ext import commands
from tinydb import TinyDB, Query
from random import randint

class XP(commands.Cog):
    """Experience"""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        """who can bot the most xp?"""
        if message.author.bot:
            return
        author = message.author.id

        db = TinyDB('Database/XP.json')
        User = Query()

        query = db.search(User.user == author)
        if not query:
            db.insert({'user': author, 'xp': 0, 'lvl': 1})
        else:
            lvl = query[0]['lvl']
            print(get_max(lvl))
            xp = query[0]['xp']
            xp = xp+randint(1,5) # "algorithm"
            if xp >= get_max(lvl):
                db.update({'lvl': lvl+1}, User.user == author)
                db.update({'xp': 0}, User.user == author)
                e = discord.Embed(title=f"Level up! You're now `{lvl}`",
                                  description="Yo monkey ass levelled up",
                                  color=0x00ff69)
                e.set_thumbnail(url="https://www.placemonkeys.com/{}".format(randint(400,600)))

                await message.author.send(embed=e)
            else:
                db.update({'xp': xp}, User.user == author)

    @commands.command(aliases=['experience', 'exp', 'cp'])
    async def xp(self, ctx, member: discord.Member=None):
        """xp xp xp"""
        if not member:
            member = ctx.author
        xp = _XP(member.id)
        lvl = _LVL(member.id)
        e = discord.Embed(title=f"XP of {member.name}",
                          color=0x0069ff)
        if not lvl: # If member has never gotten any xp (dont use xp, it'll also return true if xp=0)
            e.add_field(name="Monkey is poor", value="Monkey is poor")
        else:
            e.add_field(name=f"Level: {lvl}", value=f"**⏣{xp_to_bar(xp, get_max(lvl))}⏣** {xp}/{get_max(lvl)}")
        await ctx.send(embed=e)
def test():
    db = TinyDB('Database/XP.json')
    query = Query()

    db.update({'xp': 10}, query.user == 123)
def _XP(id):
    db = TinyDB('Database/XP.json')
    query = Query()
    xp = db.search(query.user == id)[0]['xp']

    return xp

def _LVL(id):
    db = TinyDB('Database/XP.json')
    query = Query()
    lvl = db.search(query.user == id)[0]['lvl']

    return lvl

def xp_to_bar(xp, max):
    meth = xp / max
    bar = ""
    for i in range(10):
        if meth > i/10:
            bar += "━"
        else:
            bar += "─"
    return bar
def get_max(lvl):
    with open('Database/levels.json', 'r') as monkey:
        lvls = json.load(monkey)
    return lvls['Levels'][lvl-1][str(lvl)] #-1 cuz my brain a monkey brain

def setup(bot):
    bot.add_cog(XP(bot))
