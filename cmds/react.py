import discord
from discord.ext import commands
import json
from core.classes import Cog_Extension

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):
    @commands.command()
    async def picture(self, ctx):
        pic = discord.File(jdata['pic'])
        await ctx.send(file=pic)

async def setup(bot):
    await bot.add_cog(React(bot))