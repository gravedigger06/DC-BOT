import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi there {bot.user}! I am a bot at your disposal in order to raise awareness among people regarding the climate change issue. You can wish to posses preposterous memes and disclose the most devilish plans of evildoers!')

@bot.command()
async def I_would_like_to_get_funny_memes_regarding_the_climate_change(ctx):
    img_name = random.choice(os.listdir("M2L2"))
    print(img_name)
    with open(f'M2L2/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file = picture)

bot.run("INSERT YOUT TOKEN HERE")
