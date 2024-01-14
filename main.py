
import random
import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.message_content = True

description = '''An example bot to showcase the discord.ext.commands extension
module.'''

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):

    await ctx.send(random.choice(choices))
@bot.command()
async def summa(ctx, biber=0,  dolik=0):
    
    await ctx.send(biber+dolik)


bot.run("MTE5NDMyOTQ4NzIwNzMxMzQ4OQ.GGHfmn.ERzjxKipUoIDlYBcILFOJX9T80G_DiDRjDsi3E")