import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from modules.timeout_handler import handle_timeout, handle_clear_timeouts
from modules.text_processer_handler import preprocess_text
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
@commands.has_role('Owner')
async def clear(interaction: discord.Interaction, member: discord.Member):
    if member is None:
        await interaction.response.send_message('Please mention a valid member.', ephemeral=True)
        return
    await handle_clear_timeouts(member.id)
    await interaction.response.send_message(f'Cleared timeouts for `{member.display_name}`.', ephemeral=True)

@bot.event
async def on_message(message):
    # Don't listen to messages from bot or blu#8464
    if message.author == bot.user or message.author.id == 598261411709321216:
        return

    # For each variation if likely hood >= 85 timeout
    phrase_variations = ['heroes of the storm', 'hots']

    content = await preprocess_text(message.content)
    print(content)

    total_weight = 0
    for variation in phrase_variations:
        current_weight = fuzz.partial_ratio(variation, content)
        print(current_weight)
        total_weight += current_weight

        if current_weight >= 95:
            await handle_timeout(message)
            break

        if total_weight >= 133:
            await handle_timeout(message)

    
    await bot.process_commands(message)

if __name__ == '__main__':
    bot.run(TOKEN)