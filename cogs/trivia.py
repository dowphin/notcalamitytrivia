import asyncio
import random

import discord

from discord.ext import commands
from utils.points import add_point
from utils.questions import total_questions, fetch_by_num
from utils.embeds import build_mystic_embed, build_nerdy_embed
from utils.calculations import time_difference




class Trivia(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.active = False
        self.current_task = None
        self.total_questions = total_questions()
        self.stack = []

    @commands.command()
    async def trivia(self, ctx): # asks trivia question and handles answers

        if self.active: # so a certain filipino chud can't spam this command

            self.current_task.cancel()
            await ctx.send(embed=build_mystic_embed(title="", description="Ending trivia... do **!trivia** again to restart."))
            return

        editing_cog = self.bot.get_cog("EditSheet") # ensures trivia is not running simultaneously

        if editing_cog and editing_cog.active:
            await ctx.send(embed=build_nerdy_embed(title="Denied!", description="You cannot run trivia while editing the sheet!"))
            return

        self.active = True
        self.current_task = asyncio.current_task()

        try:

            while True:

                if not self.stack:
                    self.stack = [i for i in range(1, self.total_questions + 1)]
                    random.shuffle(self.stack)

                qna = fetch_by_num(self.stack.pop())

                question = await ctx.send(embed=build_mystic_embed(title="__**Trivia Question!**__", description=qna[0]))
                question_id = question.id

                answer_raw = qna[1].split(";")

                all_answers = ", ".join(answer_raw)

                def check(message):

                    return message.channel == ctx.channel and message.author != self.bot.user

                while True:

                    try:
                        response = await self.bot.wait_for('message', check=check, timeout=600)
                        user_message_id = response.id

                    except TimeoutError:  # probably not gonna add this as a feature
                        await ctx.send(embed=build_mystic_embed(title="", description="shouldn't have taken so long to answer... run **!trivia** again to continue!"))
                        return

                    if response.content == "!skip":
                        await ctx.send(embed=build_mystic_embed(title="**Question skipped!**", description=f"The trivia question was skipped. The answer(s): `{all_answers}`"))
                        break

                    if response.content.lower() in qna[1].split(";"):
                        await ctx.send(embed=build_mystic_embed(title="**Correct!**", description=f"{response.author.name} has won **`{1}`** point.\n\n**Trivia answered in: **`{time_difference(question_id, user_message_id):.3f}`** seconds.**"))
                        add_point(response.author.id)
                        break

                await asyncio.sleep(0.5)

        finally:
            self.active = False



async def setup(bot):
    await bot.add_cog(Trivia(bot))