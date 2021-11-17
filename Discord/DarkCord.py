import discord
import os

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DarkCord_Token')

client = discord.Client()


class EnemyCreator:

    type = 'enemy'

    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attack(self, damage):
        self.health = self.health - damage
        await message.channel.send(
            'You attacked ' + soldier.name + '. ' + str(soldier.health) + ' life remaining.')


skeleton = EnemyCreator('Randy Bones', 100, 2)
soldier = EnemyCreator('Jeff', 500, 25)


@client.event
async def on_ready():
    print(
        f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    print(message.content)
    if message.author != client.user:
        if 'attack' in message.content.lower():
            if 'skeleton' in message.content.lower():
                await message.channel.send(
                    'You attacked ' + skeleton.name + '. ' + str(skeleton.health) + ' life remaining.')
            if 'soldier' in message.content.lower():
                await message.channel.send(
                    'You attacked ' + soldier.name + '. ' + str(soldier.health) + ' life remaining.')


client.run(TOKEN)
