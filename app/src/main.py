import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import re
from modules.timeout_handler import handle_timeout

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user or message.author == 'blu8646':
        return

    patterns = [
        re.compile(r'h\W*o\W*t\W*s'),
        re.compile(r'[o|0][^\w]*f[^\w]*[t|7][^\w]*h[^\w]*e[^\w]*[s|$][^\w]*t[^\w]*o[^\w]*r[^\w]*m')
    ]

    for pattern in patterns:
        if pattern.search(message.content.lower()):
            await handle_timeout(message)
            await bot.process_commands(message)

if __name__ == "__main__":
    bot.run(TOKEN)