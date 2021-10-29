# bot.py

import os
import discord
import random

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(
        f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    help_message = [
        'Need some help? Check this out: \n'
        'Type any of these commands and see what happens. \n'
        '1 - deez nuts - Bot replies with \'HA GOTEEM\' \n'
        '2 - DNsetup - Bot sets up a good joke \n'
        '3 - DNsuggestion -Feel like making a suggestion? Type this command to pull up the request desk.'
    ]

    deez_nuts = ['HA GOTEEM!']

    good_setup = ['Have you heard of sea of thieves?',
                  'I love Wendy\'s'
                  ]

    request_desk = ['Fuck off',
                    'You think you can do better? Do you? Kill yourself, pig.',
                    'Bitch, please. You can\'t code. Don\'t even try.',
                    'Thanks for opening the request desk! You are number ' + str(random.randint(1, 9999)) + ' in line.']

    botlist = 'Below are a list of bot that are available on this channel and their commands \n' \
              'DeezNuts bot \n' \
              'RemindMe bot \n' \
              'QuoteHoF bot \n' \
              'GoogleThat bot \n'

    if 'DNsuggestion' in message.content:
        response = random.choice(request_desk)
        await message.channel.send(response)

    if 'DNsetup' in message.content:
        response = random.choice(good_setup)
        await message.channel.send(response)

    if 'deez nuts' in message.content.lower():
        response = random.choice(deez_nuts)
        await message.channel.send(response)

    if 'DNhelp' in message.content:
        response = random.choice(help_message)
        await message.channel.send(response)

    if 'help!' in message.content:
        response = botlist
        await message.channel.send(response)

client.run(TOKEN)
