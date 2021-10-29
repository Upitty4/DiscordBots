# bot 2

import os
import discord
import time
import asyncio
import re

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN2')
client = discord.Client()


def get_time(s):
    m = re.search(r'(\d+)', s)
    return int(m.group()) if m else None


@client.event
async def on_ready():
    print(
        f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    remind_me = 'You will be reminded '

    if 'remindme!' in message.content.lower():
        if message.content[-1] == 'h' or \
                message.content[-1] == 's' or\
                message.content[-1] == 'm':
            response = remind_me + '\'' + message.content[10:-3] + '\' in ' \
                       + str(get_time(message.content)) \
                       + message.content[-1]
            print(get_time(message.content))
            await message.channel.send(response)
        else:
            await message.channel.send('I don\'t understand.')
        if message.content[-1] == 'h':
            await asyncio.sleep(3600 * int(get_time(message.content)))
            await message.author.send('Reminder! \n' + message.content[10:-3])
        if message.content[-1] == 's':
            await asyncio.sleep(int(get_time(message.content)))
            await message.author.send('Reminder! \n' + message.content[10:-3])
        if message.content[-1] == 'm':
            await asyncio.sleep(int(get_time(message.content)*60))
            await message.author.send('Reminder! \n' + message.content[10:-3])

client.run(TOKEN)

# THINGS TO DO:
# fix it so i can have more than a single digit input
# add ability to remind based on reply
# add help menu
