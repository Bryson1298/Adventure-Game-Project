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
import json

player = []
#On save, player = health, gold, inventory


# Player stats
player_health = 30
player_power = 5
player_gold = 10

# Monster stats
monster_health = 0
monster_power = 0
monster_reward = 0

# Player inventory
owned_items = 0
inventory = {}

# Available items
items = [
  {
    "Item": "Sword",
    "Type": "Weapon",
    "Price": 15,
    "Effect": "This item increases the user's damage, but has a limited number of uses.",
    "Max Durability": 10,
    "Current Durability": 10,
    "Equipped": False
  },
  {
    "Item": "Repel",
    "Type": "Consumable",
    "Price": 25,
    "Effect": "Defeats one monster without HP loss"
  },
  {
    "Item": "Buckler",
    "Type": "Shield",
    "Price": 15,
    "Effect": "This item decreases  taken, but has a limited number of uses.",
    "Max Durability": 6,
    "Current Durability": 6,
    "Equipped": False
  },
  {
    "Item": "Map",
    "Type": "Misc",
    "Price": 5,
  }
]

def print_welcome():
    """
    Prints a welcome message to the player.

    Asks the player for their name and prints a centered welcome message.
    """
    name = input("What is your name? ")
    welcome_message = f"Hello, {name}!"
    print(f"{welcome_message:^20}")

def print_shop_menu():
    """
    Prints a menu of available items in the shop.

    Displays the items with their prices and prompts the player to purchase an item.
    Calls the purchase_item function if the player chooses to buy an item.
    """
    item1 = items[0]["Item"]
    item2 = items[1]["Item"]
    item3 = items[2]["Item"]
    item4 = items[3]["Item"]

    price1 = items[0]["Price"]
    price2 = items[1]["Price"]
    price3 = items[2]["Price"]
    price4 = items[3]["Price"]

    print(f"{'/':-<21}\\")
    print(f"|1){item1:<10}{'$' + str(price1):>8}|")
    print(f"|2){item2:<10}{'$' + str(price2):>8}|")
    print(f"|3){item3:<10}{'$' + str(price3):>8}|")
    print(f"|4){item4:<10}{'$' + str(price4):>8}|")
    print(f"{'\\':-<21}/")

    purchase = input("Would you like to purchase an item? (y/n): ")
    if purchase == "y":
        item_to_purchase = int(input("Which item would you like to purchase?(1-4) "))
        purchase_item(item_to_purchase)


# Function to simulate purchasing an item
def purchase_item(item_to_purchase):
    """
    Simulates purchasing an item, checking if the user has enough money.
    """
    # Check if the user has enough money to buy the desired quantity
    itemPrice = items[item_to_purchase - 1]["Price"]
    global player_gold

    if player_gold >= itemPrice:
        global owned_items
        owned_items += 1
        player_gold -= itemPrice
        inventory[f'item_{owned_items}'] = (items[item_to_purchase - 1]["Item"])
        print(f"You have purchased a {items[item_to_purchase - 1]['Item']}.\n"
              f"Gold remaining: {player_gold}\n")

    else:
        # Print a message if the user doesn't have enough money
        print('\nNot enough money')

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
        if 'Repel' in inventory.values():
            use_item = input('\nDo you want to use a Repel? (y/n): ')
            if use_item == 'y':
                monster_health = 0
                remove_by_value(inventory, 'Repel')
                print('You have fled using a Repel.')

        else:
            fight_or_flee = input('\nWould you like to fight or flee?\n')

            if fight_or_flee == 'fight':
                print('You attack the monster.')
                monster_health -= player_power
                print(f'The monster has {monster_health} health.\n')
                print('\nThe monster fights back.')
                player_health -= monster_power
                print(f'You have {player_health} health.')
            elif fight_or_flee == 'flee':
                print('\nYou run away from the monster.')
                global monster_reward
                monster_reward = 0
                monster_health = 0
            else:
                print('\nInvalid input.')



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

def remove_by_value(my_dict, value):
    """
    Removes all key-value pairs from a dictionary where the value matches a given value.

    Args:
        my_dict (dict): The dictionary to modify.
        value: The value to remove from the dictionary.

    Returns:
        dict: A new dictionary with the specified value removed.
    """
    return {key: val for key, val in my_dict.items() if val != value}

def equip_items():
    """
    Allows the player to equip an item from their inventory.

    Prints a list of equipable items in the inventory and prompts the player to choose an item to equip.
    Updates the player's power if a weapon is equipped.
    """
    print('\nEquipable items:')
    for item in inventory:
        print(inventory[item])
    print('None\n')
    item_to_equip = input("What item do you want to equip? ")
    if item_to_equip == 'Sword':
        global player_power
        player_power += 5

def open_inventory():
    """
    Opens the player's inventory and allows them to equip items.

    Prints the contents of the inventory and prompts the player to equip an item.
    Calls the equip_items function if the player chooses to equip an item.
    """
    i = 0
    for item in inventory:
        print(f"{inventory[item]}")
        i += 1
    equip_choice = input("Would you like to equip an item(y/n)? ")
    if equip_choice == 'y':

        equip_items()

def save():
    player.append(player_health)
    player.append(player_gold)
    player.append(inventory)
    save_and_quit(player)

def save_and_quit(game_state, filename="save_game.json"):
    with open(filename, "w") as f:
        json.dump(game_state, f, indent=4)

def load_game(filename="save_game.json"):
    try:
        with open(filename, "r") as f:
            game_state = json.load(f)
            return game_state
    except FileNotFoundError:
        return None  # Handle case where save file doesn't exist

