import discord
import os

# basic info to run discord app
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DarkCord_Token')

client = discord.Client()

# this holds all of the info running the class and functions
npc = []


# enemy creator, just pass this class some info to add enemies
class EnemyCreator:

    type = 'enemy'

    def __init__(self, name, enemy_type, health, ap):
        self.name = name
        self.enemy_type = enemy_type
        self.health = health
        self.ap = ap
        info = (name + ', ' + str(health) + ', ' + str(ap))
        npc.append(info)


# class to build the player character. Will be used to store starting class info and current player info
class PlayerCharacter:
    type = 'player'

    def __init__(self, name, player_type, health, ap):
        self.name = name
        self.player_type = player_type
        self.health = health
        self.ap = ap
        info = (name + ', ' + str(health) + ', ' + str(ap))
        npc.append(info)


# defines all of the attacks
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


# current list of characters that have been passed to the creator
boss = EnemyCreator('Charles Hammerdick', 'boss', 10000, 200)
skeleton = EnemyCreator('Randy Bones', 'skeleton', 100, 2)
soldier = EnemyCreator('Jeff', 'soldier', 500, 25)
playerChar = PlayerCharacter('Jimbo', 'playerChar', 500, 50)


# defines the current information on npcs, and player
def getinfo(character):
    for thing in npc:
        print(thing)
        print(character)
        if character in thing:
            return str(thing)


# tells us it connected okay
@client.event
async def on_ready():
    print(
        f'{client.user} has connected to Discord!')


# this is the bulk of the code. Everything passes through here.
@client.event
async def on_message(message):
    print(message.content)
    if message.author != client.user:
        if 'test' in message.content.lower():
            print(npc)
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
            await message.channel.send(
                getinfo(message.content[6::]))

# necessary to run the code
client.run(TOKEN)
