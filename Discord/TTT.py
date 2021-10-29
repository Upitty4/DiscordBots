import os
import discord
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN6')
client = discord.Client()

global game_state
global a
global b
global c
global d
global e
global f
global g
global h
global i


@client.event
async def on_ready():
    print(
        f'{client.user} has connected to Discord!')
    global game_state
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    a = ' '
    b = ' '
    c = ' '
    d = ' '
    e = ' '
    f = ' '
    g = ' '
    h = ' '
    i = ' '


@client.event
async def on_message(message):
    global game_state
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    if message.author == client:
        return
    if message.content.lower() == 'ttt!':
        game_state = 'on'
        await message.channel.send(
            'Welcome to Tick Tack Toe!\n'
            'type the column, then the row, then x or o\n'
            'like this: 1ao\n'
            '   1   2   3\n' 
                'a [' + a + '] [' + b + '] [' + c + ']\n' 
                'b [' + d + '] [' + e + '] [' + f + ']\n' 
                'c [' + g + '] [' + h + '] [' + i + ']\n'
        )
    if message.content.lower() == 'endgame':
        game_state = 'off'
        a = ' '
        b = ' '
        c = ' '
        d = ' '
        e = ' '
        f = ' '
        g = ' '
        h = ' '
        i = ' '
        await message.channel.send(
            'Game Over. Type ttt! to begin!'
        )

    if message.content.lower() == 'test':
        await message.channel.send(game_state)
        return
    if message.content.lower() == 'testoff':
        game_state = 'off'
        await message.channel.send(game_state)
        return
    if message.content.lower() == 'board':
        await message.channel.send(game_state)
        if game_state == 'on':
            await message.channel.send(
                '   1   2   3\n' 
                'a [' + a + '] [' + b + '] [' + c + ']\n' 
                'b [' + d + '] [' + e + '] [' + f + ']\n' 
                'c [' + g + '] [' + h + '] [' + i + ']\n'
            )
    if message.content.lower() == '1ax':
        if game_state == 'on':
            if a == ' ':
                a = 'x'
                await message.channel.send(
                    '   1   2   3\n' 
                    'a [' + a + '] [' + b + '] [' + c + ']\n' 
                    'b [' + d + '] [' + e + '] [' + f + ']\n' 
                    'c [' + g + '] [' + h + '] [' + i + ']\n'
                )
            else:
                await message.channel.send('Not a legal move.')
    if message.content.lower() == '1ao':
        if game_state == 'on':
            if a == ' ':
                a = 'O'
                await message.channel.send(
                    '   1   2   3\n' 
                    'a [' + a + '] [' + b + '] [' + c + ']\n' 
                    'b [' + d + '] [' + e + '] [' + f + ']\n' 
                    'c [' + g + '] [' + h + '] [' + i + ']\n'
                )
            else:
                await message.channel.send('Not a legal move.')
    if message.content.lower() == '2ax':
        if game_state == 'on':
            if b == ' ':
                b = 'x'
                await message.channel.send(
                    '   1   2   3\n' 
                    'a [' + a + '] [' + b + '] [' + c + ']\n' 
                    'b [' + d + '] [' + e + '] [' + f + ']\n' 
                    'c [' + g + '] [' + h + '] [' + i + ']\n'
                )
            else:
                await message.channel.send('Not a legal move.')
    if message.content.lower() == '2ao':
        if game_state == 'on':
            if b == ' ':
                b = 'O'
                await message.channel.send(
                    '   1   2   3\n' 
                    'a [' + a + '] [' + b + '] [' + c + ']\n' 
                    'b [' + d + '] [' + e + '] [' + f + ']\n' 
                    'c [' + g + '] [' + h + '] [' + i + ']\n'
                )
            else:
                await message.channel.send('Not a legal move.')
    if message.content.lower() == '3ax':
        if game_state == 'on':
            if c == ' ':
                c = 'x'
                await message.channel.send(
                    '   1   2   3\n' 
                    'a [' + a + '] [' + b + '] [' + c + ']\n' 
                    'b [' + d + '] [' + e + '] [' + f + ']\n' 
                    'c [' + g + '] [' + h + '] [' + i + ']\n'
                )
            else:
                await message.channel.send('Not a legal move.')
    if message.content.lower() == '3ao':
        if game_state == 'on':
            if c == ' ':
                c = 'O'
                await message.channel.send(
                    '   1   2   3\n' 
                    'a [' + a + '] [' + b + '] [' + c + ']\n' 
                    'b [' + d + '] [' + e + '] [' + f + ']\n' 
                    'c [' + g + '] [' + h + '] [' + i + ']\n'
                )
            else:
                await message.channel.send('Not a legal move.')
    if message.content.lower() == '1bx':
        if game_state == 'on':
            if d == ' ':
                d = 'x'
                await message.channel.send(
                    '   1   2   3\n' 
                    'a [' + a + '] [' + b + '] [' + c + ']\n' 
                    'b [' + d + '] [' + e + '] [' + f + ']\n' 
                    'c [' + g + '] [' + h + '] [' + i + ']\n'
                )
            else:
                await message.channel.send('Not a legal move.')
    if message.content.lower() == '1bo':
        if game_state == 'on':
            if d == ' ':
                d = 'O'
                await message.channel.send(
                    '   1   2   3\n' 
                    'a [' + a + '] [' + b + '] [' + c + ']\n' 
                    'b [' + d + '] [' + e + '] [' + f + ']\n' 
                    'c [' + g + '] [' + h + '] [' + i + ']\n'
                )
            else:
                await message.channel.send('Not a legal move.')
    if message.content.lower() == '2bx':
        if game_state == 'on':
            if e == ' ':
                e = 'x'
                await message.channel.send(
                    '   1   2   3\n' 
                    'a [' + a + '] [' + b + '] [' + c + ']\n' 
                    'b [' + d + '] [' + e + '] [' + f + ']\n' 
                    'c [' + g + '] [' + h + '] [' + i + ']\n'
                )
            else:
                await message.channel.send('Not a legal move.')
    if message.content.lower() == '2bo':
        if game_state == 'on':
            if e == ' ':
                e = 'O'
                await message.channel.send(
                    '   1   2   3\n' 
                    'a [' + a + '] [' + b + '] [' + c + ']\n' 
                    'b [' + d + '] [' + e + '] [' + f + ']\n' 
                    'c [' + g + '] [' + h + '] [' + i + ']\n'
                )
            else:
                await message.channel.send('Not a legal move.')
    if message.content.lower() == '3bx':
        if game_state == 'on':
            if f == ' ':
                f = 'x'
                await message.channel.send(
                    '   1   2   3\n' 
                    'a [' + a + '] [' + b + '] [' + c + ']\n' 
                    'b [' + d + '] [' + e + '] [' + f + ']\n' 
                    'c [' + g + '] [' + h + '] [' + i + ']\n'
                )
            else:
                await message.channel.send('Not a legal move.')
    if message.content.lower() == '3bo':
        if game_state == 'on':
            if f == ' ':
                f = 'O'
                await message.channel.send(
                    '   1   2   3\n' 
                    'a [' + a + '] [' + b + '] [' + c + ']\n' 
                    'b [' + d + '] [' + e + '] [' + f + ']\n' 
                    'c [' + g + '] [' + h + '] [' + i + ']\n'
                )
            else:
                await message.channel.send('Not a legal move.')
    if message.content.lower() == '1cx':
        if game_state == 'on':
            if g == ' ':
                g = 'x'
                await message.channel.send(
                    '   1   2   3\n' 
                    'a [' + a + '] [' + b + '] [' + c + ']\n' 
                    'b [' + d + '] [' + e + '] [' + f + ']\n' 
                    'c [' + g + '] [' + h + '] [' + i + ']\n'
                )
            else:
                await message.channel.send('Not a legal move.')
    if message.content.lower() == '1co':
        if game_state == 'on':
            if g == ' ':
                g = 'O'
                await message.channel.send(
                    '   1   2   3\n' 
                    'a [' + a + '] [' + b + '] [' + c + ']\n' 
                    'b [' + d + '] [' + e + '] [' + f + ']\n' 
                    'c [' + g + '] [' + h + '] [' + i + ']\n'
                )
            else:
                await message.channel.send('Not a legal move.')
    if message.content.lower() == '2cx':
        if game_state == 'on':
            if h == ' ':
                h = 'x'
                await message.channel.send(
                    '   1   2   3\n' 
                    'a [' + a + '] [' + b + '] [' + c + ']\n' 
                    'b [' + d + '] [' + e + '] [' + f + ']\n' 
                    'c [' + g + '] [' + h + '] [' + i + ']\n'
                )
            else:
                await message.channel.send('Not a legal move.')
    if message.content.lower() == '2co':
        if game_state == 'on':
            if h == ' ':
                h = 'O'
                await message.channel.send(
                    '   1   2   3\n' 
                    'a [' + a + '] [' + b + '] [' + c + ']\n' 
                    'b [' + d + '] [' + e + '] [' + f + ']\n' 
                    'c [' + g + '] [' + h + '] [' + i + ']\n'
                )
            else:
                await message.channel.send('Not a legal move.')
    if message.content.lower() == '3cx':
        if game_state == 'on':
            if i == ' ':
                i = 'x'
                await message.channel.send(
                    '   1   2   3\n' 
                    'a [' + a + '] [' + b + '] [' + c + ']\n' 
                    'b [' + d + '] [' + e + '] [' + f + ']\n' 
                    'c [' + g + '] [' + h + '] [' + i + ']\n'
                )
            else:
                await message.channel.send('Not a legal move.')
    if message.content.lower() == '3co':
        if game_state == 'on':
            if i == ' ':
                i = 'O'
                await message.channel.send(
                    '   1   2   3\n' 
                    'a [' + a + '] [' + b + '] [' + c + ']\n' 
                    'b [' + d + '] [' + e + '] [' + f + ']\n' 
                    'c [' + g + '] [' + h + '] [' + i + ']\n'
                )
            else:
                await message.channel.send('Not a legal move.')
client.run(TOKEN)
