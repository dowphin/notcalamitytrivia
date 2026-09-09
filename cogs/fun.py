import random
import asyncio


from discord.ext import commands
from utils.embeds import build_cool_embed, build_nerdy_embed
from utils.reading_gambles import read_slots

class Fun(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
        self.active = False
        self.current_task = None

    @commands.command()
    async def gamble(self, ctx):

        if self.active: # so a certain filipino chud can't spam this command
            await ctx.send(embed=build_cool_embed(title="chill out man", description="You can't gamble multiple times at once! That would be cheating..."))
            return

        editing_cog = self.bot.get_cog("EditSheet") # ensures trivia is not running simultaneously

        if editing_cog and editing_cog.active:
            await ctx.send(embed=build_nerdy_embed(title="Denied!", description="You cannot gamble while editing the sheet!"))
            return

        self.active = True

        try:

            slots_grid = []
            slots_items = [":pear:", ":tangerine:", ":lemon:", ":strawberry:", ":grapes:", ":watermelon:", "<:mystic_slime:1546711607269130342>"]
            slots_items_indexes = [i for i in range(len(slots_items))]


            for i in range(3):

                row = []

                for j in range(5):

                    row.append(slots_items[random.choice(slots_items_indexes)])

                slots_grid.append(row)

            slots_grid_str = ""

            for i in slots_grid:
                str_row = " ".join(i)
                slots_grid_str += str_row + "\n"

            await ctx.send(embed=build_cool_embed(title="Gamble!", description=f"{slots_grid_str}"))

            patterns = read_slots(slots_grid)

            for i in patterns:
                for j in i:
                    await ctx.send(j)
                    await asyncio.sleep(0.5)

            return

        finally:

            self.active = False


async def setup(bot):
    await bot.add_cog(Fun(bot))