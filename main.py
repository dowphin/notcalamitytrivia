import os
import asyncio
import discord

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

async def main():

    await bot.load_extension("cogs.greetings")
    await bot.load_extension("cogs.trivia")
    await bot.load_extension("cogs.data_reading")
    await bot.load_extension("cogs.edit_sheet")
    await bot.load_extension("cogs.fun")
    await bot.load_extension("cogs.help")

    await bot.start(TOKEN)

asyncio.run(main())