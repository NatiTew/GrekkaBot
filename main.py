import discord
from discord.ext import commands
from config import *

bot = commands.Bot(command_prefix=PREFIX, description="AepmongBot")


@bot.event
async def on_ready():
    print("Aepmong")


@bot.command(pass_context=True)
async def hello(ctx):
    await ctx.send('hello I am AepmongBot')


bot.run(TOKEN, bot=True, reconnect=True)