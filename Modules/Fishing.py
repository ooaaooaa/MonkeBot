import random
import asyncio
import numpy as np
from warnings import filterwarnings
filterwarnings("ignore", category=np.VisibleDeprecationWarning)
from discord.ext import commands
import discord

class Fishing(commands.Cog):
    """Fish fish"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 6, commands.BucketType.user)
    async def fish(self, ctx):
        """Fish for fish"""
        num = random.randint(1, 100)
        special = 0
        if num < 95:
            _catch = await catch()
        else:
            _catch = await special_catch()
            special = 1
        e = discord.Embed(title="Fishing", description="You go fishing!", colour=0xf54242)
        e.set_thumbnail(url="https://i.imgur.com/3Q3VDp9.jpg")
        msg = await ctx.send(embed=e)
        await asyncio.sleep(3)
        e = discord.Embed(title="Fishing", description="Something's biting!", colour=0xd4f542)
        e.set_thumbnail(url="https://i.imgur.com/Y3mpQhm.jpg")
        await msg.edit(embed=e)
        await asyncio.sleep(3)
        e = discord.Embed(title="Fishing", description=f"You caught {_catch[0]}!", colour=0x919191)
        e.set_thumbnail(url="https://i.imgur.com/59TKpfE.jpg")
        if special == 0:
            basePrice = _catch[2]
            minWeight = _catch[3]
            maxWeight = _catch[4]
            goldWeight = _catch[5]
            weight = round(random.uniform(minWeight, maxWeight), 3)
            # PRICE
            price = 0
            a=""
            if weight >= goldWeight:
                price = round(basePrice+((basePrice/50)*weight*3),2)
                a="\nThis fish extraordinarily large!"
            else:
                price = round(basePrice+((basePrice/100)*weight),2)
            if _catch[0] == "Nothing":
                e.add_field(name=_catch[0],
                            value="I've wasted your time!")
                e.set_thumbnail(url="https://i.imgur.com/C6rQmPZ.gif")
            else:
                e.add_field(name=_catch[0],
                            value=f"**Weight**: `{weight}lb`\n"
                                 +f"**Value**: `𝐌{price}`" + a)
        else:
            price = _catch[2]
            description = _catch[3]
            icon = _catch[4]
            e.set_thumbnail(url="https://live.staticflickr.com/22/25807800_4f776527bb_b.jpg")
            e = discord.Embed(title="Fishing", description=f"**Special Item! You caught {_catch[0]}!!!**", colour=0xcc00ff)
            e.add_field(name=icon + " " +_catch[0],
                        value=f"**Description**: `{description}`\n"
                             +f"**Value**: `𝐌{price}`")

        await msg.edit(embed=e)

fishes = (
    # 0Name, 1Weight (Chance), 2Base Price, 3minWeight, 4maxWeight, 5goldWeight
    ("Nothing",   30,   0,   0,    0,     1),
    ("Bass",      10,   10,  1,    22.4,  16),
    ("Minnow",    17,   5,   0.3,  4,     25),
    ("Trout",     10,   12,  8,    48,    35),
    ("Cod",       10,   10,  3,    212,   180)
)
special = (
    # Name, Weight, Price, Description, Icon
    ("Monke", 1, 6969, "https://github.com/ooaaooaa", ":monkey:"),
    ("x352", 0.01, 69, "self-proclaimed femboy, possibly gay.", "x352cheats"),
    ("Boot", 4, 3, "Old and stinky boot", ":boot:"),
    ("Hooker", 2, 200, "Turn your eyes to god.", ":dancer:"),
    ("Dildo", 3, 23, "Wet and used (because of the water)", ":baby_bottle:"),
    ("Gamesense.pub Invite", 3, 200, "So rare and hard to find", ":skateboard:"),
    ("Skeet.gg Invite", 0.0001, 99999, "%skrt%", ":skateboard:"), # actually still tempted to buy skeet.gg domain or host it myself xd
    ("Dogshit", 6, 1, "Smells like dogshit in here.", ":poop:"),
    ("Your mom", 0.005, 2, "Shes fat but not worth a lot.", ":cap:"),
    ("Gentoo install script", 0.5, 500, "rtfm", ":scroll:")
)
async def catch():

    pr = []
    for i in range(0,len(fishes)):
        pr.append(fishes[i][1])
    pr = round_to_100_percent(pr)
    return fishes[np.random.choice(len(fishes), p=pr)]

async def special_catch():
    pr = []
    for i in range(0,len(special)):
        pr.append(special[i][1])
    pr = round_to_100_percent(pr)
    return special[np.random.choice(len(special), p=pr)]
def round_to_100_percent(number_set, digit_after_decimal=2):
    unround_numbers = [x / float(sum(number_set)) * 100 * 10 ** digit_after_decimal for x in number_set]
    decimal_part_with_index = sorted([(index, unround_numbers[index] % 1) for index in range(len(unround_numbers))], key=lambda y: y[1], reverse=True)
    remainder = 100 * 10 ** digit_after_decimal - sum([int(x) for x in unround_numbers])
    index = 0
    while remainder > 0:
        unround_numbers[decimal_part_with_index[index][0]] += 1
        remainder -= 1
        index = (index + 1) % len(number_set)
    return [(int(x) / float(10 ** digit_after_decimal))/100 for x in unround_numbers]

def setup(bot):
    bot.add_cog(Fishing(bot))
