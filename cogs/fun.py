import random
import asyncio
import bisect

from discord.ext import commands

from utils.embeds import build_cool_embed, build_nerdy_embed
from utils.calculations import generate_slot_grid
from utils.reading_gambles import read_slots

ALLOWED_CHANNEL_ID = 1547471691163115650

slots_items = [":pear:", ":tangerine:", ":strawberry:", ":lemon:", ":grapes:", ":watermelon:", "<:mystic_slime:1546711607269130342>"]
slots_odds = [0.3, 0.25, 0.2, 0.15, 0.05, 0.03, 0.02] # percent change of rolling the corresponding item. should sum to 1.0

class Fun(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
        self.active = False
        self.current_task = None

    async def cog_check(self, ctx):
        return ctx.channel.id == ALLOWED_CHANNEL_ID

    @commands.command()
    async def gamble(self, ctx):

        if self.active: # so a certain filipino chud can't spam this command
            await ctx.send(embed=build_cool_embed(title="chill out man", description="You can't gamble multiple times at once! That would be cheating..."))
            return

        self.active = True

        try:

            slots_weights = []

            for i in range(len(slots_odds)):
                if not slots_weights:
                    slots_weights.append(slots_odds[i])
                else:
                    slots_weights.append(round(slots_odds[i] + slots_weights[i - 1], 4))


            slots_grid = generate_slot_grid(slots_items, slots_weights)

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