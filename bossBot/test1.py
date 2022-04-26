# --- Embed Options ---
Title = 'Embed'
Description = 'Embed created by a bot'
Header = 'This is a header'
Text = 'This is a long text'
Url = ''
#----------------------

import discord
from discord.ext import commands
from config import *

bot = commands.Bot(command_prefix=".")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="GitHub"))

# If start succeed
print('Bot is running...')

#if embed command in discord chat
@bot.command()
@commands.has_role("Bot Engine")
async def embed(ctx):
    embed = discord.Embed(title=Title, description=Description, color=0xF7EBC5)
    embed.add_field(name=Header, value=Text, inline=False)
    embed.set_thumbnail(url=Url)
    await ctx.send(embed=embed)

# Fast print. If you dont have time to write an embed just use print in discord chat followed by the text you want the bot to post.
@bot.command()
async def print(ctx, arg):
	await ctx.channel.send(arg)

bot.run(TOKEN, bot=True, reconnect=True)