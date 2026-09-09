from discord.ext import commands
from utils.embeds import *

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):

        await ctx.send(embed=build_diva_embed(title="Hello!", description=f"Hi there, {ctx.author}!"))

        return

async def setup(bot):
    await bot.add_cog(Greetings(bot))