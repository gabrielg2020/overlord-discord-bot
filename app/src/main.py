import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from modules.timeout_handler import handle_timeout, handle_clear_timeouts
from fuzzywuzzy import fuzz,process

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(e)

@bot.tree.command(name='clearto')
async def clear(interaction: discord.Interaction, member: discord.Member):
    if member is None:
        await interaction.response.send_message('Please mention a valid member.', ephemeral=True)
        return
    await handle_clear_timeouts(member.id)
    await interaction.response.send_message(f'Cleared timeouts for `{member.display_name}`.', ephemeral=True)

@bot.event
async def on_message(message):
    if message.author == bot.user or message.author.id == 598261411709321216:
      return

    phrase_variations = ['heroes of the strom', 'hots']

    for variation in phrase_variations:
        if fuzz.partial_ratio(variation, message.content.lower()) >= 85:
            await handle_timeout(message)
            await bot.process_commands(message)

if __name__ == '__main__':
    bot.run(TOKEN)