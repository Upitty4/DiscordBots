import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN4')
client = discord.Client()


@client.event
async def on_ready():
    print(
        f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'googlethis!' in message.content.lower():
        response = 'https://letmegooglethat.com/?q=' + message.content[11::].replace(' ', '%20')
        await message.channel.send(response)

client.run(TOKEN)
