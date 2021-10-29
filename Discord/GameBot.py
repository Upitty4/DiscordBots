import os
import discord


from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN5')
client = discord.Client()
global game_state
global location
global armor
global jason_alive
global shadow_alive


@client.event
async def on_ready():
    print(
        f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):

    if message.author == client.user:
        return

# BASIC COMMAND DESC

    available_options = ' \n \n LOOK    MOVE    ATTACK     PICK UP     INVENTORY    USE    HELP'
    help = 'LOOK - can be used to look at your surroundings. Add a word location (shown with capitol letters) to learn ' \
           'more about an object. \n MOVE -  can be used to move around. Type MOVE and a direction (north, south, east, west' \
           ') to move in that direction. \n ATTACK - begins combat. Be wary of this one. Make sure you are well suited to' \
           'fight someone or something. \n PICK UP - can be used in conjunction with key items. Very few things can be picked up.' \
           '\n INVENTORY shows what you are currently holding. \n USE - can be used in conjunction with items in your inventory.' \
           '\n HELP - brings up this helpful menu.'
    opening = 'You begin your adventure outside a small shoppe. The shoppe keep has just thrown you out for trying to ' \
              'steal. What do you want to do first?'
    start_game = 'Let\'s play! Type \'begin\' to begin your adventure'
    end_game = 'Thanks for playing!'
    death = 'Your journey ends here. You die like you lived, sad and alone. The shadows are ruthless, ripping you apart.' \
            ' Maybe the shoppe has some armor? \n If you want to start over, type: startgame!'
    armor_save = 'Thanks to your armor, you easily pass through the shadows.'
    area_desc = 'You are in the town of Windflower. South of you stands an angry shoppe keep named JASON. He is guarding' \
                ' the entrance to the GENERAL STORE. North of you ' \
                'is the road into TOWN. East of you is the long road to the neighboring town: FLECKTON. West is the WILD' \
                'ERNESS.'

# DIALOG DESC

    jason_dialog = 'Jason stares at you. Gun trained at your chest. \"Stay out of my store!\"'

# LOCATION DESC

    store_desc = 'The general store is your one-stop-shoppe for anything you would need. Here you can stock up on supplies' \
                 'that can be helpful on your journey. You will have to get past Jason if you want to see whats inside.'
    windflower_desc = 'The town of Windflower is a small town. Less than 50 people still live here. After the calamity, most ' \
                'townsfolk left and headed East to FLECKTON. The town consists of a GENERAL STORE and a small collection' \
                ' of houses on the North end of town.'
    fleckton_desc = 'The town of Fleckton managed to survive the calamity, but not through luck. As a military town, they ' \
                    'were able to fight off what came their way. Now, low on resources, they keep anyone looking to enter' \
                    'at bay. The road ahead is filled with shadows. You won\'t make it far without some gear from the general store.'
    wilderness_desc = 'The wilderness is filled with the aftermath of the calamity. Burned out houses and \"shadows' \
                      '\" as far as you can see. You won\'t make it far without some gear from the general store.'
    store_inner_desc = 'The store is filled with useless items, except a set of ARMOR hanging on a wall behind the register.'
    cave_desc = 'The cave is filled with the powerful smell of rotting flesh. In front of you a SHADOW is hunched over a' \
                'body. It looks like the BODY of a Fleckton knight. To the East is the town of Windflower.'
    body_desc = 'The body of the Fleckton knight is decaying rapidly. You can barely make out that he is holding a SEAL' \
                'in his right hand.'
    shadow_desc = 'The shadows is old, but still has a lot of fight left in it. Maybe an attack with a sword could deal' \
                  'with it?'

# MOVE DESC

    move_without_armor = 'Without armor, you don\'t make it far.'
    move = 'Where do you want to go? Type move, then a direction.'
    move_east = 'You being moving towards Fleckton. The road is long, and the journey is tedious.'
    move_west_cave = 'You make your way into the wilderness.'
    move_east_starting = 'You make your way back to Windflower.'
    move_north = 'You make your way into the heart of Windflower. Here you are surrounded by houses, most vacant and ' \
                 'burned out.'

    global game_state
    global location
    location = 'starting'
    global armor
    armor = 'none'
    global jason_alive
    jason_alive = 'yes'
    global shadow_alive
    shadow_alive = 'yes'

# BASIC FUNTIONS

    if 'startgame!' in message.content.lower():
        game_state = 'ON'
        print(game_state)
        await message.channel.send(start_game)
        return game_state

    if 'endgame!' in message.content.lower():
        game_state = 'OFF'
        print(game_state)
        await message.channel.send(end_game)
        return game_state

    if 'gamestate!' in message.content.lower():
        await message.channel.send(game_state)

    if 'begin' in message.content.lower():
        if game_state == 'ON':
            await message.channel.send(opening + available_options)
            return
        else:
            return

    if message.content.lower() == 'help':
        if game_state == 'ON':
            await message.channel.send(help)

# LOOK COMMANDS

    if message.content.lower() == 'look':
        if game_state == 'ON':
            if location == 'starting':
                await message.channel.send(area_desc + available_options)
            if location == 'cave':
                await message.channel.send(cave_desc + available_options)

    if message.content.lower() == 'look jason':
        if game_state == 'ON':
            await message.channel.send(jason_dialog + available_options)

    if message.content.lower() == 'look general store':
        if game_state == 'ON':
            await message.channel.send(store_desc + available_options)

    if message.content.lower() == 'look town':
        if game_state == 'ON':
            if location == 'starting':
                await message.channel.send(windflower_desc + available_options)

    if message.content.lower() == 'look fleckton':
        if game_state == 'ON':
            await message.channel.send(fleckton_desc + available_options)

    if message.content.lower() == 'look wilderness':
        if game_state == 'ON':
            await message.channel.send(wilderness_desc + available_options)

    if message.content.lower() == 'look body':
        if game_state == 'ON':
            if location == 'cave':
                await message.channel.send(body_desc)

    if message.content.lower() == 'look shadow':
        if game_state == 'ON':
            if location == 'cave':
                await message.channel.send(shadow_desc)

# MOVE COMMANDS

    if message.content.lower() == 'move':
        if game_state == 'ON':
            await message.channel.send(move + available_options)

    if message.content.lower() == 'move east':
        if game_state == 'ON':
            if armor == 'none':
                if location == 'starting':
                    game_state = 'OFF'
                    await message.channel.send(move_east + '\n' + move_without_armor + '\n' + death)
                    return game_state
            if location == 'cave':
                location = 'starting'
                await message.channel.send(move_east_starting + available_options)
            else:
                location = 'Fleckton'
                await message.channel.send(move_east + available_options)

    if message.content.lower() == 'move north':
        if game_state == 'ON':
            location = 'windflower_town'
            await message.channel.send(move_north + available_options)
            return location

    if message.content.lower() == 'move south':
        if game_state == 'ON':
            if jason_alive == 'yes':
                await message.channel.send(jason_dialog + available_options)
            if jason_alive == 'no':
                await message.channel.send(store_inner_desc + available_options)

    if message.content.lower() == 'move west':
        if game_state == 'ON':
            if armor == 'none':
                await message.channel.send(move_west_cave + '\n' + death)
            else:
                location = 'cave'
                await message.channel.send(move_east_starting + armor_save)
                return location
    return
client.run(TOKEN)
