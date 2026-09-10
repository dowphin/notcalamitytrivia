from discord.ext import commands

from utils.embeds import build_surly_embed
from assets.help_strings import * # contains all HELP_DATA descriptions

HELP_DATA = {
    "_description": page1,
    "1":page1,
    "2":page2,
    "gamble": {
        "_description": gamble_description,
        "slots": slots_description
    },

    "trivia": {
        "_description": trivia_description,
        "points": points_description,
        "leaderboard": leaderboard_description
    },

    "points": points_description,
    "leaderboard": leaderboard_description,

    "add_question": add_question_description,
    "delete_question": delete_question_description,

    "hello": "Figure it out genius. Why do you even care? This is my test command to try out embed parameters."

}

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, *args):

        data = HELP_DATA

        last_arg = ""

        for arg in args:
            if isinstance(data, dict) and arg in data:
                data = data[arg]
            else:
                await ctx.send(embed=build_surly_embed(title="Error!", description=f"Invalid help command requested. Try again!"))
                return
            last_arg = arg

        exceptions_to_last_arg = {
            "add_question": "Add question",
            "delete_question": "Delete question"
        }

        if len(last_arg) > 0:
            if last_arg.isdigit():
                last_arg = f"__**Commands (Page {last_arg})**__"
            elif last_arg in exceptions_to_last_arg:
                last_arg = f"__**{exceptions_to_last_arg[last_arg]}**__"
            elif last_arg == "hello":
                last_arg = "**__moron__**"
            else:
                last_arg = last_arg.capitalize()
                last_arg = f"__**{last_arg}**__"

        else:
            last_arg = "__**Commands (Page 1)**__"

        if isinstance(data, dict):
            await ctx.send(embed=build_surly_embed(title=last_arg, description=data["_description"]))
            return
        else:
            await ctx.send(embed=build_surly_embed(title=last_arg, description=data))
            return

async def setup(bot):
    await bot.add_cog(Help(bot))