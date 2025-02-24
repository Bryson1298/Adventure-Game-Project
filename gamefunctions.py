# gamefunctions.py
# Bryson Corcoran
# 2/13/25

# This code defines purchase_item() and new_random_monster() functions using given parameters
# and calls each of them 3 times

import random


def print_welcome():
    """
    Prints a welcome message to the user, asking for their name and greeting them.
    """
    name = input("What is your name? ")
    welcome_message = f"Hello, {name}!"
    print(f"{welcome_message:^20}")


def print_shop_menu(item1, price1, item2, price2):
    """
    Prints a shop menu with two items and their prices.

    Args:
        item1 (str): The name of the first item.
        price1 (float): The price of the first item.
        item2 (str): The name of the second item.
        price2 (float): The price of the second item.
    """
    price1 = '$' + str(f'{price1:.2f}')
    price2 = '$' + str(f'{price2:.2f}')
    print(f"{'/':-<21}\\")
    print(f"|{item1:<12}{price1:>8}|")
    print(f"|{item2:<12}{price2:>8}|")
    print(f"{'\\':-<21}/")


# Function to simulate purchasing an item
def purchase_item(itemPrice, startingMoney, quantityToPurchase):
    """
    Simulates purchasing an item, checking if the user has enough money.

    Args:
        itemPrice (float): The price of the item.
        startingMoney (float): The amount of money the user starts with.
        quantityToPurchase (int): The number of items the user wants to buy.

    Returns a tuple containing the remaining money and the quantity purchased.
    """
    # Check if the user has enough money to buy the desired quantity
    if startingMoney >= itemPrice * quantityToPurchase:
        amount_remaining = round(startingMoney - (itemPrice * quantityToPurchase), 2)
        quantity_purchased = quantityToPurchase
    else:
        # Print a message if the user doesn't have enough money
        print('\nNot enough money')
        amount_remaining = startingMoney
        quantity_purchased = 0
    # Print the purchase details
    print('\nQuantity purchased:', quantity_purchased)
    print('Amount remaining:', amount_remaining, '\n')
    # Returns the purchase details
    return amount_remaining, quantity_purchased


# Function to create a random monster with specific attributes
def new_random_monster():
    """
    Creates a random monster with specific attributes based on the user's choice.

    Returns a dictionary containing the monster's attributes.
    """
    # Get user input for the monster type
    random_monster = input('Choose a monster (Orc, Zombie or Skeleton): ')
    # Check the monster type and create a dictionary with its attributes
    if random_monster == 'Orc':
        monster = {'name': 'Orc',
                   'description': ' A brutish humanoid with greenish skin, '
                                  'tusks, and a fierce, aggressive nature.',
                   'health': random.randint(3, 12),
                   'power': random.randint(4, 6),
                   'money': round(random.random() * 300, 2)}
        # Print the monster's attributes
        print(monster['name'], 'description:', monster['description'])
        print(monster['name'], 'health:', monster['health'])
        print(monster['name'], 'power:', monster['power'])
        print(monster['name'], 'money:', monster['money'], '\n')
        return monster
    # Check the monster type and create a dictionary with its attributes
    elif random_monster == 'Zombie':
        monster = {'name': 'Zombie',
                   'description': 'A reanimated corpse with pale, '
                                  'decaying flesh and glowing, vacant eyes.',
                   'health': random.randint(1, 3),
                   'power': random.randint(1, 3),
                   'money': round(random.random() * 100, 2)}
        # Print the monster's attributes
        print(monster['name'], 'description:', monster['description'])
        print(monster['name'], 'health:', monster['health'])
        print(monster['name'], 'power:', monster['power'])
        print(monster['name'], 'money:', monster['money'], '\n')
        return monster
    # Check the monster type and create a dictionary with its attributes
    elif random_monster == 'Skeleton':
        monster = {'name': 'Skeleton',
                   'description': 'A bare, bony frame with glowing, '
                                  'empty sockets for eyes.',
                   'health': random.randint(2, 5),
                   'power': random.randint(2, 5),
                   'money': round(random.random() * 200, 2)}
        # Print the monster's attributes
        print(monster['name'], 'description:', monster['description'])
        print(monster['name'], 'health:', monster['health'])
        print(monster['name'], 'power:', monster['power'])
        print(monster['name'], 'money:', monster['money'], '\n')
        return monster
    # Raise an exception if an invalid monster name is provided
    else:
        raise Exception('Invalid Monster Name')


print_welcome()

print_welcome()

print_welcome()

shop_item1 = input("What is your first item? ")
item1_price = float(input("What is your first price? "))
shop_item2 = input("What is your second item? ")
item2_price = float(input("What is your second price? "))

print_shop_menu(shop_item1, item1_price, shop_item2, item2_price)

shop_item1 = input("What is your first item? ")
item1_price = float(input("What is your first price? "))
shop_item2 = input("What is your second item? ")
item2_price = float(input("What is your second price? "))

print_shop_menu(shop_item1, item1_price, shop_item2, item2_price)

shop_item1 = input("What is your first item? ")
item1_price = float(input("What is your first price? "))
shop_item2 = input("What is your second item? ")
item2_price = float(input("What is your second price? "))

print_shop_menu(shop_item1, item1_price, shop_item2, item2_price)

# Get user input for purchase scenarios
starting_money = float(input('What is the starting money? '))
item_price = float(input('What is the item price? '))
num_purchased = int(input('How many items would you like to purchase? '))

# Call the purchase_item function for the scenario
purchase_item(item_price, starting_money, num_purchased)

starting_money = float(input('What is the starting money? '))
item_price = float(input('What is the item price? '))
num_purchased = int(input('How many items would you like to purchase? '))

purchase_item(item_price, starting_money, num_purchased)

starting_money = float(input('What is the starting money? '))
item_price = float(input('What is the item price? '))
num_purchased = int(input('How many items would you like to purchase? '))

purchase_item(item_price, starting_money, num_purchased)

# Create a random monster based on the user's choice
new_random_monster()

new_random_monster()

new_random_monster()
