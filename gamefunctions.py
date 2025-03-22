"""
This module defines functions for a simple game, including:

- `print_welcome()`: Prints a welcome message to the user.
- `print_shop_menu()`: Prints a shop menu with two items and their prices.
- `purchase_item()`: Simulates purchasing an item, checking if the user has enough money.
- `new_random_monster()`: Creates a random monster with specific attributes based on the user's choice.

The module also includes example code that calls these functions to demonstrate their usage.
"""

# gamefunctions.py
# Bryson Corcoran
# 2/13/25

# This code defines purchase_item() and new_random_monster() functions using given parameters
# and calls each of them 3 times

import random

player_health = 30
player_power = 5
player_gold = 10

monster_health = 0
monster_power = 0
monster_reward = 0

def print_welcome():
    """
    Prints a welcome message to the user, asking for their name and greeting them.

    Returns:
        None
    """
    name = input("What is your name? ")
    welcome_message = f"Hello, {name}!"
    print(f"{welcome_message:^20}")

def print_shop_menu(item1, price1, item2, price2):
    """
    Prints a shop menu with two items and their prices.

    Parameters:
        item1 (str): The name of the first item.
        price1 (float): The price of the first item.
        item2 (str): The name of the second item.
        price2 (float): The price of the second item.

    Returns:
        None
    """
    price1 = '$' + str(f'{price1:.2f}')
    price2 = '$' + str(f'{price2:.2f}')
    print(f"{'/':-<21}\\")
    print(f"|{item1:<12}{price1:>8}|")
    print(f"|{item2:<12}{price2:>8}|")
    print(f"{'\\':-<21}/")

# Function to simulate purchasing an item
def purchase_item(itemPrice, startingMoney):
    """
    Simulates purchasing an item, checking if the user has enough money.

    Parameters:
        itemPrice (float): The price of the item.
        startingMoney (float): The amount of money the user starts with.

    Returns:
        float: The remaining money after the purchase.    """
    # Check if the user has enough money to buy the desired quantity
    if startingMoney >= itemPrice:
        amount_remaining = round((startingMoney - itemPrice), 2)
        quantity_purchased = 1

    else:
        # Print a message if the user doesn't have enough money
        print('\nNot enough money')
        amount_remaining = startingMoney
        quantity_purchased = 0
    # Print the purchase details
    print('\nQuantity purchased: ', quantity_purchased)
    print('Amount remaining:', amount_remaining, '\n')
    # Returns the purchase details
    return amount_remaining

# Function to create a random monster with specific attributes
def new_random_monster():
    """
    Creates a random monster with specific attributes based on the user's choice.

    Returns:
        dict: A dictionary containing the monster's attributes.
    """
    # Choose random monster to generate
    random_monster = random.randint(1, 3)
    # Check the monster type and create a dictionary with its attributes
    if random_monster == 1:

        global monster_health
        global monster_power
        global monster_reward

        name = 'Drake'
        description = ('A dragon-like creature that is smaller, less powerful, '
                       'and less intelligent than a true dragon')
        monster_health = random.randint(3, 12)
        monster_power = random.randint(4, 6)
        monster_reward = round(random.random() * 300, 2)
        monster_attributes = {'name': name, 'description': description,
                              'health': monster_health, 'power': monster_power,
                              'reward': monster_reward}

        print(f"\nYou encounter a {monster_attributes['name']}")
        print(monster_attributes['description'])
        print(f"Health: {monster_attributes['health']}")
        print(f"Power: {monster_attributes['power']}")
        print(f"Reward: {monster_attributes['reward']}")

        return monster_attributes
    # Check the monster type and create a dictionary with its attributes
    elif random_monster == 2:



        name = 'Zombie'
        description = ('A reanimated corpse with pale, '
                       'decaying flesh and glowing, vacant eyes.')
        monster_health = random.randint(1, 3)
        monster_power = random.randint(1, 3)
        monster_reward = round(random.random() * 100, 2)
        monster_attributes = {'name': name, 'description': description,
                              'health': monster_health, 'power': monster_power,
                              'reward': monster_reward}

        print(f"\nYou encounter a {monster_attributes['name']}")
        print(monster_attributes['description'])
        print(f"Health: {monster_attributes['health']}")
        print(f"Power: {monster_attributes['power']}")
        print(f"Reward: {monster_attributes['reward']}")

        return monster_attributes

    elif random_monster == 3:


        name = 'Skeleton'
        description = ('A bare, bony frame with glowing, '
                       'empty sockets for eyes.')
        monster_health = random.randint(2, 5)
        monster_power = random.randint(2, 5)
        monster_reward = round(random.random() * 200, 2)
        monster_attributes = {'name': name, 'description': description,
                          'health': monster_health, 'power': monster_power,
                          'reward': monster_reward}

        print(f"\nYou encounter a {monster_attributes['name']}")
        print(monster_attributes['description'])
        print(f"Health: {monster_attributes['health']}")
        print(f"Power: {monster_attributes['power']}")
        print(f"Reward: {monster_attributes['reward']}")

        return monster_attributes

def fight_monster():
    """
       Simulates a fight between the player and a randomly generated monster.

       The player and monster take turns attacking each other until one of them reaches 0 health.

       The player gains gold based on the monster's reward if they win the fight.

       Returns:
           None
       """
    new_random_monster()

    global player_health
    global monster_health

    while player_health > 0 and monster_health > 0:

            print('\nThe monster fights back.')
            player_health -= monster_power

            print('You attack the monster.\n')
            monster_health -= player_power

    if player_health <= 0:
        print('You are defeated by the monster.\n')


    else:
        global player_gold
        player_gold += monster_reward
        player_gold = round(player_gold, 2)
        print('You defeated the monster.')
        print(f"You have {player_health} health remaining.")
        print(f"You gain {monster_reward} gold and now have {player_gold} gold.\n")


def rest_at_inn(current_gold, current_health):
    """
    Allows the player to rest at an inn, restoring health for a cost of 5 gold.

    Parameters:
        current_gold (float): The player's current gold.
        current_health (int): The player's current health.

    Returns:
        None
    """
    if current_gold >= 5:
        global player_health
        global player_gold

        player_health = current_health + 5
        player_gold = current_gold - 5

        print('You rest at an inn and gain 5 health.')
        print(f"You have {player_health} health remaining.")
        print(f"You have {player_gold} gold remaining.\n")
    else:
        print('Not enough gold.\n')


def gameloop():
    """
    The main game loop, allowing the player to choose between fighting a monster, resting at an inn, or quitting.

    The game continues until the player's health reaches 0 or they choose to quit.

    Returns:
        None
    """
    choice = ''
    while choice != '3':
        if player_health <= 0:
            choice = '3'
        else:
            choice = input('What would you like to do?\n'
                           '1) Leave town (Fight Monster)\n'
                           '2) Sleep (Restore HP for 5 Gold)\n'
                           '3) Quit\n')
        print('You are in town.')
        print(f'Current Health: {player_health}, Current Gold: {player_gold}')

        if choice == '1':
            fight_monster()

        elif choice == '2':

            rest_at_inn(player_gold, player_health)

        elif choice == '3':

            print('\nThank you for playing.\n')
        else:

            print('Invalid choice, try again.\n')
