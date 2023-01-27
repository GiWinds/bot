import discord
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix = '.', intents = intents)

@bot.event
async def on_ready():
    print("Bot is online")

bot.run('MTA2ODQzMDgyNDc4NzE2OTMxMA.GrlhYO.YpV3q8vR94NNrSE9xzI_gBySTUGbp93m_Dtwf0')