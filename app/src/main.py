import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from modules.timeout_handler import handle_timeout
from fuzzywuzzy import fuzz,process

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

    phrase_variations = ['heroes of the strom', 'hots']

    for variation in phrase_variations:
        if fuzz.partial_ratio(variation, message.content.lower()) >= 85:
            await handle_timeout(message)
            await bot.process_commands(message)

if __name__ == "__main__":
    bot.run(TOKEN)