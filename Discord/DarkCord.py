import discord
import os

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DarkCord_Token')

client = discord.Client()


class EnemyCreator:

    type = 'enemy'

    def __init__(self, name, health, ap):
        self.name = name
        self.health = health
        self.ap = ap


class PlayerCharacter:
    type = 'player'

    def __init__(self, name, health, ap):
        self.name = name
        self.health = health
        self.ap = ap


def attack(enemy):
    enemy.health = enemy.health - playerChar.ap
    if enemy.health > 0:
        playerChar.health = playerChar.health - enemy.ap
        return ('You attacked ' + enemy.name + '. ' + str(enemy.health) + ' life remaining. \n'
                + enemy.name + ' attacks back! You take ' + str(enemy.ap) + ' damage. You have ' + str(playerChar.health)
                + ' remaining!')
    if enemy.health <= 0:
        return enemy.name + ' has been defeated!'
    if playerChar.health <= 0:
        return 'You died idiot.'


def getinfo(character):
    if character == skeleton:
        return skeleton.name, skeleton.health, skeleton.ap
    if character == soldier:
        return soldier.name, soldier.health, soldier.ap
    if character == playerChar:
        return playerChar.name, playerChar.health, playerChar.ap
    if character == boss:
        return boss.name, boss.health, boss.ap
    else:
        return 'Nothing here'


boss = EnemyCreator('Charles Hammerdick', 10000, 200)
skeleton = EnemyCreator('Randy Bones', 100, 2)
soldier = EnemyCreator('Jeff', 500, 25)
playerChar = PlayerCharacter('Jimbo', 500, 50)


@client.event
async def on_ready():
    print(
        f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    print(message.content)
    if message.author != client.user:
        if '!attack' in message.content.lower():
            if 'skeleton' in message.content.lower():
                await message.channel.send(
                    attack(skeleton)
                )
            if 'soldier' in message.content.lower():
                await message.channel.send(
                    attack(soldier)
                )
            if 'boss' in message.content.lower():
                await message.channel.send(
                    attack(boss)
                )
        if '!info' in message.content.lower():
            if 'skeleton' in message.content.lower():
                await message.channel.send(
                    getinfo(skeleton)
                )
            if 'soldier' in message.content.lower():
                await message.channel.send(
                    getinfo(soldier)
                )
            if 'playerchar' in message.content.lower():
                await message.channel.send(
                    getinfo(playerChar)
                )
            if 'boss' in message.content.lower():
                await message.channel.send(
                    getinfo(boss)
                )
            else:
                await message.channel.send(
                    getinfo(" ")
                )

client.run(TOKEN)
