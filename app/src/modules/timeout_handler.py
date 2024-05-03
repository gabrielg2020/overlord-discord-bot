import datetime
import discord
import json

def get_user_timeouts():
  try:
    with open('app/src/modules/user_timeouts.json', 'r') as file:
      return json.load(file)
  except FileNotFoundError:
    return {}

def update_user_timeouts(dic):
  try:
    json_data = json.dumps(dic, indent=4)
    with open('app/src/modules/user_timeouts.json', 'w') as file:
      file.write(json_data)
  except Exception as e:
    print(f'Error whilst writing to user_timeouts.json: {e}')

async def handle_timeout(message):
  user_timeouts = get_user_timeouts()

  user_id = str(message.author.id)
  
  # If user id is in dictionary increase occurence by 1
  if user_id in user_timeouts:
    user_timeouts[user_id] += 1
  else: # Else add them to dictionary 
    user_timeouts[user_id] = 1
  
  # Update .json
  update_user_timeouts(user_timeouts)

  timeout_duration = 5 ** (user_timeouts[user_id])

  await message.channel.send(f"{message.author.mention} mentioned 'HOTS'! {message.author.mention} has mentioned 'HOTS' {user_timeouts[user_id]} times. As a punishment for they are timedout for {timeout_duration} seconds. Feel free to laugh at {message.author.mention}.")
  await message.author.edit(timed_out_until=discord.utils.utcnow() + datetime.timedelta(seconds=timeout_duration))

async def handle_clear_timeouts(user_id):
  user_timeouts = get_user_timeouts()

  user_id = str(user_id)

  user_timeouts[user_id] = 0

  # Update .json
  update_user_timeouts(user_timeouts)
  return True