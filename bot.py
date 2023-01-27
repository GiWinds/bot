import discord
from discord.ext import commands
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print("Bot is online")

@bot.command()
async def picture(ctx):
    pic = discord.File("C:\\Users\\jason\\Downloads\\test.png")
    await ctx.send(file=pic)


bot.run(jdata['TOKEN'])