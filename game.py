from gamefunctions import *

def python_game():
    """
    Starts the main game loop.

    Calls the `gameloop()` function from the `gamefunctions` module to initiate the game.

    Returns:
        None
    """
    load = input("1) Load game\n"
                 "2) Start new game")
    if load == "1":
        load_game()
        print('Welcome back!\n')
        gameloop()
    elif load == "2":
        print_welcome()
        gameloop()
    else:
        print("Invalid input")

def gameloop():
    """
    The main game loop, allowing the player to choose between fighting a monster, resting at an inn, or quitting.

    The game continues until the player's health reaches 0 or they choose to quit.

    Returns:
        None
    """

    choice = ''
    while choice != '5':
        if player_health <= 0:
            choice = '5'
        else:
            choice = input('What would you like to do?\n'
                           '1) Leave town (Fight Monster)\n'
                           '2) Sleep (Restore HP for 5 Gold)\n'
                           '3) View Shop\n'
                           '4) Open inventory\n'
                           '5) Save and Quit\n')
        print('You are in town.')
        print(f'Current Health: {player_health}, Current Gold: {player_gold}')

        if choice == '1':
            fight_monster()

        elif choice == '2':
            rest_at_inn(player_gold, player_health)

        elif choice == '3':
            print_shop_menu()

        elif choice == '4':
            open_inventory()

        elif choice == '5':
            save_and_quit(player)

        else:
            print('Invalid choice, try again.\n')

python_game()
