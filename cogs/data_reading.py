import discord
from discord.ext import commands
from utils.points import read_points, sort_points
from utils.embeds import build_diva_embed


class DataReading(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.active = False





    @commands.command()
    async def points(self, ctx):

        await ctx.send(embed=build_diva_embed(title=f"{ctx.author.name}'s Points", description=f"{ctx.author} has {read_points(ctx.author.id)} points!"))

        return

    @commands.command()
    async def leaderboard(self, ctx):

        str_leaderboard = ""
        iterator = 0
        sorted_points = sort_points()

        for i in sorted_points:
            if iterator == 0:
                str_leaderboard += ":first_place: "
            elif iterator == 1:
                str_leaderboard += ":second_place: "
            elif iterator == 2:
                str_leaderboard += ":third_place: "
            else:
                str_leaderboard += f"({iterator + 1}) "
            player = await self.bot.fetch_user(int(i))

            str_leaderboard += f"{player.name} has {sorted_points[i]} points.\n"

            iterator += 1

            if iterator > 10:
                break


        await ctx.send(embed=build_diva_embed(title="**__Points Leaderboard__**", description=str_leaderboard))

        return

async def setup(bot):
    await bot.add_cog(DataReading(bot))


