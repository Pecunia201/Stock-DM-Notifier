import datetime
import asyncio
import discord
import rsi
from discord.ext import commands, tasks
import json

# Read the JSON file
with open('config.json') as file:
    data = json.load(file)

# Access the values
discord_token = data['discord_token']
discord_user_id = data['discord_user_id']
rsi_threshold = data['rsi_threshold']

# Create a new bot instance with intents
intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent
bot = commands.Bot(command_prefix='!', intents=intents)

@tasks.loop(count=1)
async def send_message():
    await bot.wait_until_ready()

    while True:
        now = datetime.datetime.now()
        rsi_result = rsi.rsi()

        if now.hour == 5 and now.minute == 0 and rsi_result < rsi_threshold:
            try:
                # Fetch the user object using the target user ID
                user = await bot.fetch_user(discord_user_id)
                # Send a direct message to the user
                await user.send(f"RSI has dropped below 30: {round(rsi_result, 2)}")
                print('Message sent successfully!')
            except discord.HTTPException:
                print('Failed to send the message.')
        
        # Wait for 1 minute before checking the time again
        await asyncio.sleep(60)

@bot.event
async def on_ready():
    print(f'Bot is ready and logged in as {bot.user.name}')
    send_message.start()

# Run the bot
bot.run(discord_token)