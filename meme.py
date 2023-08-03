from aiohttp import request
import discord, os, random
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('gambar'))
    with open(f'gambar/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    
@bot.command()
async def sampah(ctx) : 
    img_name = random.choice(os.listdir('sampah'))
    with open(f'sampah/{img_name}', 'rb') as f: 
        picture = discord.File(f)
    await ctx.send("Berikut adalah saran kerajinan sampah dari aku : ")
    await ctx.send(file=picture)

bot.run("BOT TOKEN")