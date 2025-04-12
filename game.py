from gamefunctions import *

import random
import pygame


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
            global running
            running = True


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


        # Initialize Pygame
        pygame.init()

        # Screen dimensions
        screen_width = 320  # 10 squares * 32 pixels/square
        screen_height = 320  # 10 squares * 32 pixels/square
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Map Exploration")

        # Colors
        black = (0, 0, 0)
        white = (255, 255, 255)
        green = (0, 255, 0)
        red = (255, 0, 0)

        # Square size
        square_size = 32

        # Player position (starts at town)
        player_x = 0
        player_y = 0

        # Town position
        town_x = 0
        town_y = 0

        # Monster position
        monster_x = random.randint(1, 8)
        monster_y = random.randint(1, 8)

        # Function to draw the map
        def draw_map():
            screen.fill(black)  # Clear the screen

            # Draw the town
            pygame.draw.circle(screen, green,
                               (town_x * square_size + square_size // 2, town_y * square_size + square_size // 2),
                               square_size // 3)

            # Draw the monster
            pygame.draw.circle(screen, red,
                               (monster_x * square_size + square_size // 2, monster_y * square_size + square_size // 2),
                               square_size // 3)

            # Draw the player
            player_rect = pygame.Rect(player_x * square_size, player_y * square_size, square_size, square_size)
            pygame.draw.rect(screen, white, player_rect)

            pygame.display.flip()  # Update the display

        # Main game loop


        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and player_y > 0:
                        player_y -= 1
                    if event.key == pygame.K_DOWN and player_y < 9:
                        player_y += 1
                    if event.key == pygame.K_LEFT and player_x > 0:
                        player_x -= 1
                    if event.key == pygame.K_RIGHT and player_x < 9:
                        player_x += 1

                    # Check for town interaction
                    if player_x == town_x and player_y == town_y:
                        # Return to town menu
                        pygame.quit()
                        running = False

                    # Check for monster encounter
                    if player_x == monster_x and player_y == monster_y:
                        # Trigger monster battle
                        pygame.quit()
                        fight_monster()
                        running = False

            # Only fill the screen if the game is running
            if running:
                screen.fill(black)  # Clear the screen
                draw_map()  # Call your draw function here

        # Quit Pygame
        pygame.quit()


python_game()
