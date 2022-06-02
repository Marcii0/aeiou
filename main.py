import asyncio
import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot=commands.Bot(command_prefix="?",intents=intents)
TOKEN=0
@bot.event
async def on_ready():
    print("ready to aeiou")
    await doaeiou()


async def doaeiou():
    em=discord.Embed(title="AEIOU", color=discord.Color.dark_gray())
    em.add_field(name="AEIOU", value="AEIOU")
    while True:
        await bot.get_channel(876533413472002048).send(embed=em)
        asyncio.sleep(108000)

bot.run(TOKEN)