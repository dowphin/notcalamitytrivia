import asyncio
from discord.ext import commands
from utils.questions import insert, delete_by_row_id, total_questions, fetch_by_num, fetch_by_question
from utils.embeds import build_nerdy_embed

ALLOWED_CHANNEL_ID = 1547471670447706153


class EditSheet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.active = False
        self.current_task = None

    async def cog_check(self, ctx):
        return ctx.channel.id == ALLOWED_CHANNEL_ID

    @commands.command()

    async def add_question(self, ctx):

        if self.active: # so a certain filipino chud can't spam this command
            self.current_task.cancel()
            await ctx.send(embed=build_nerdy_embed(title="Error!", description="Already editing sheet! Cancelling process."))
            return


        self.active = True
        self.current_task = asyncio.current_task()

        try:

            def check(message):
                return message.channel == ctx.channel and message.author == ctx.author

            await ctx.send(embed=build_nerdy_embed(title="**__Adding Question__**", description="What question do you want to add? Type \"cancel\" to cancel this process."))

            while True:
                try:

                    response = await self.bot.wait_for('message', check=check, timeout=300)

                except TimeoutError:
                    await ctx.send(embed=build_nerdy_embed(title="Timed Out", description=""))
                    return

                if response.content.lower() == "cancel":
                    await ctx.send(embed=build_nerdy_embed(title="Process Terminated", description=""))
                    return

                if response.content.lower()[0] != "!":
                    question = response.content
                    break


            await ctx.send(embed=build_nerdy_embed(title="**__Adding Question__**", description="What should the answers be? Separate multiple answers with a `;`."))

            while True:
                try:
                    response = await self.bot.wait_for('message', check=check, timeout=300)

                except TimeoutError:
                    await ctx.send(embed=build_nerdy_embed(title="Timed Out", description=""))
                    return

                if response.content.lower() == "cancel":
                    await ctx.send(embed=build_nerdy_embed(title="Process Terminated", description=""))
                    return

                if response.content.lower()[0] != "!":
                    answer = response.content
                    break

            answer_test = answer.split(";")

            final_answers = set()

            for i in answer_test:
                if len(i) == 0:
                    await ctx.send(embed=build_nerdy_embed(title="Process Terminated", description="Invalid answer type detected!"))
                    return
                final_answers.add(i.strip())

            final_answers = list(final_answers)

            answer = ";".join(final_answers)

            insert(question, answer)
            await ctx.send(embed=build_nerdy_embed(title="**__Adding Question__**", description="Question added!"))

            return

        finally:
            self.active = False

    @commands.command()

    async def delete_question(self, ctx):

        if self.active:  # so a certain filipino chud can't spam this command
            self.current_task.cancel()
            await ctx.send(embed=build_nerdy_embed(title="Error!", description="Already editing sheet! Cancelling process."))
            return

        self.active = True
        self.current_task = asyncio.current_task()

        try:
            def check(message):
                return message.channel == ctx.channel and message.author == ctx.author

            await ctx.send(embed=build_nerdy_embed(title="**__Deleting Question__**", description="What question do you want to delete?\n\nYou can delete a question by its row number or the question itself. Type:\n1 -> Delete question by row number\n2 -> Delete question by question content\ncancel -> Cancel anytime"))

            while True:
                try:
                    response = await self.bot.wait_for('message', check=check, timeout=300)


                except TimeoutError:
                    await ctx.send(embed=build_nerdy_embed(title="Timed Out", description=""))
                    return

                if response.content.lower() == "cancel":
                    await ctx.send(embed=build_nerdy_embed(title="Process Terminated", description=""))
                    return

                if response.content.lower()[0] != "!":

                    match response.content:
                        case "1":
                            await ctx.send(embed=build_nerdy_embed(title="**__Deleting Question__**", description="Please enter the row number of the question you want to delete."))
                            while True:

                                try:
                                    response = await self.bot.wait_for('message', check=check, timeout=300)

                                except TimeoutError:
                                    await ctx.send(embed=build_nerdy_embed(title="Timed Out", description=""))
                                    return

                                if response.content.lower() == "cancel":
                                    await ctx.send(embed=build_nerdy_embed(title="Process Terminated", description=""))
                                    return

                                if response.content[0] != "!":

                                    if not response.content.isdigit():
                                        await ctx.send(embed=build_nerdy_embed(title="**__Deleting Question__**", description="Please input a valid number!"))

                                    elif int(response.content) <= total_questions():
                                        await ctx.send(embed=build_nerdy_embed(title="**__Deleting Question__**", description=f'Deleting question: `{fetch_by_num(int(response.content))[0]}`'))
                                        row_num = int(response.content)
                                        await ctx.send(embed=build_nerdy_embed(title="**__Deleting Question__**", description="Are you sure? Enter `confirm` to confirm this change"))

                                        try:
                                            response = await self.bot.wait_for('message', check=check, timeout=300)

                                        except TimeoutError:
                                            await ctx.send(embed=build_nerdy_embed(title="Timed Out", description=""))
                                            return

                                        if response.content == "confirm":
                                            delete_by_row_id(row_num)
                                            await ctx.send(embed=build_nerdy_embed(title="**__Deleting Question__**", description="Question deleted!"))
                                            return

                                        else:
                                            await ctx.send(embed=build_nerdy_embed(title="**__Deleting Question__**", description="`confirm` not found, cancelling process."))
                                            return

                                    elif int(response.content) > total_questions():
                                        await ctx.send(embed=build_nerdy_embed(title="**__Deleting Question__**", description="That row does not exist yet! Try again."))


                        case "2":

                            await ctx.send(embed=build_nerdy_embed(title="**__Deleting Question__**", description="Please enter the *exact* text of the question you want to delete, or enter `cancel` to cancel anytime."))

                            while True:

                                try:
                                    response = await self.bot.wait_for('message', check=check, timeout=300)


                                except TimeoutError:
                                    await ctx.send(embed=build_nerdy_embed(title="Timed Out", description=""))
                                    return

                                if response.content.lower() == "cancel":
                                    await ctx.send(embed=build_nerdy_embed(title="Process Terminated", description=""))
                                    return

                                if response.content[0] != "!":
                                    if fetch_by_question(response.content) is None:
                                        await ctx.send(embed=build_nerdy_embed(title="**__Deleting Question__**", description="That question was not found! Try again."))
                                    else:
                                        await ctx.send(embed=build_nerdy_embed(title="**__Deleting Question__**", description=f"Question located in row `{fetch_by_question(response.content)[0]}`. Type `confirm` to confirm this change."))

                                        row_num = int(fetch_by_question(response.content)[0])

                                        try:
                                            response = await self.bot.wait_for('message', check=check, timeout=300)
                                        except TimeoutError:
                                            await ctx.send(embed=build_nerdy_embed(title="Timed Out", description=""))
                                            return

                                        if response.content == "confirm":
                                            delete_by_row_id(row_num)
                                            await ctx.send(embed=build_nerdy_embed(title="**__Deleting Question__**", description="Question deleted!"))
                                            return
                                        else:
                                            await ctx.send(embed=build_nerdy_embed(title="**__Deleting Question__**", description="`confirm` not found, cancelling process."))
                                            return
                        case _:
                            await ctx.send(embed=build_nerdy_embed(title="**__Deleting Question__**", description="Please send a valid response! Try again."))

        finally:
            self.active = False

        return

async def setup(bot):
    await bot.add_cog(EditSheet(bot))