import discord

# basic info to run discord app
from dotenv import load_dotenv

load_dotenv()
TOKEN = ''

client = discord.Client()

# this holds all of the info running the class and functions
npc_info = []
npc_list = []


# enemy creator, just pass this class some info to add enemies
class EnemyCreator:

    type = 'enemy'

    def __init__(self, name, enemy_type, health, ap):
        self.name = name
        self.enemy_type = enemy_type
        self.health = health
        self.ap = ap
        info = (name + ', ' + str(health) + ', ' + str(ap))
        npc_info.append(info)
        npc_list.append(self)
        npc_list.append(self.name)


# class to build the player character. Will be used to store starting class info and current player info
class PlayerCharacter:
    type = 'player'

    def __init__(self, name, player_type, health, ap):
        self.name = name
        self.player_type = player_type
        self.health = health
        self.ap = ap
        info = (name + ', ' + str(health) + ', ' + str(ap))
        npc_info.append(info)


# defines all of the attacks
def attack(enemy):
    for thing in npc_list:
        if str(enemy) in str(thing):
            enemy = (npc_list[npc_list.index(thing) - 1])
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
    for thing in npc_info:
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
            print(npc_info)
            print(npc_list)
        if '!attack' in message.content.lower():
            print(message.content[8::])
            await message.channel.send(
                attack(message.content[8::]))
        if '!info' in message.content.lower():
            await message.channel.send(
                getinfo(message.content[6::]))

# necessary to run the code
client.run(TOKEN)
