import discord
import os
import random

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN3')
client = discord.Client()


@client.event
async def on_ready():
    print(
        f'{client.user} has connected to discord channel {client.get_channel(789001522474254337)}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    channel = client.get_channel(789001522474254337)
    all_quotes = await channel.history(limit=200).flatten()
    hofq = random.choice(all_quotes)

    if 'quote!' in message.content.lower():
        response = hofq.content
        print(random.choice(all_quotes).content)
        await message.channel.send(response)

    channel = client.get_channel(789001522474254337)
    get_quote = await channel.history(limit=200).flatten()
    make_quote = get_quote[1].content + '\n -' + str(get_quote[1].author)[:-5]

    if 'quotethis!' in message.content.lower():
        response = make_quote
        print(response)
        await channel.send(response)
        await message.channel.send('This is funny. I\'ll add it to the quotes!')

client.run(TOKEN)
