from gamefunctions import *
from WanderingMonster import WanderingMonster

import pygame
import pickle
import os

# Global variables for player
player_health = 100
player_gold = 50


def save_monsters(monsters, filename="monster_data.pickle"):
    """Saves the list of monsters to a file."""
    try:
        with open(filename, "wb") as f:
            pickle.dump(monsters, f)
        print(f"Monster data saved to {filename}")
    except Exception as e:
        print(f"Error saving monster data: {e}")


def load_monsters(filename="monster_data.pickle", grid_width=10, grid_height=10, town_x=0, town_y=0):
    """Loads the list of monsters from a file."""
    monsters = []
    if os.path.exists(filename):  # Check if the file exists before attempting to load
        try:
            with open(filename, "rb") as f:
                monsters = pickle.load(f)
            print(f"Monster data loaded from {filename}")
        except Exception as e:
            print(f"Error loading monster data: {e}")
            monsters = create_initial_monsters(grid_width, grid_height, town_x, town_y)
    else:
        monsters = create_initial_monsters(grid_width, grid_height, town_x, town_y)
    return monsters


def create_initial_monsters(grid_width, grid_height, town_x, town_y):
    """Creates initial monsters for the game."""
    monsters = []
    for _ in range(2):
        monster = WanderingMonster.new_random_monster(grid_width, grid_height, town_x, town_y)
        monsters.append(monster)
    return monsters


def python_game():
    """Starts the main game loop."""
    load = input("1) Load game\n2) Start new game\n")
    if load == "1":
        monsters = load_monsters()
        print('Welcome back!\n')
        gameloop(monsters)
    elif load == "2":
        print_welcome()
        monsters = create_initial_monsters(10, 10, 0, 0)  # Create monsters for a new game
        gameloop(monsters)
    else:
        print("Invalid input")


def gameloop(monsters):
    """The main game loop, allowing the player to choose between fighting a monster, resting at an inn, or quitting."""
    choice = ''
    global player_health, player_gold
    running = True  # Ensure the game loop runs until the player quits
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

    # Square size
    square_size = 32

    # Player position (starts at town)
    player_x = 0
    player_y = 0

    # Town position
    town_x = 0
    town_y = 0

    # Function to draw the map
    def draw_map():
        screen.fill(black)  # Clear the screen

        # Draw the town
        pygame.draw.circle(screen, (0, 255, 0),
                           (town_x * square_size + square_size // 2, town_y * square_size + square_size // 2),
                           square_size // 3)

        # Draw monsters
        for monster in monsters:
            pygame.draw.circle(screen, monster.color,
                               (monster.x * square_size + square_size // 2, monster.y * square_size + square_size // 2),
                               square_size // 3)

        # Draw the player
        player_rect = pygame.Rect(player_x * square_size, player_y * square_size, square_size, square_size)
        pygame.draw.rect(screen, white, player_rect)

        pygame.display.flip()  # Update the display

    while running:
        choice = input('What would you like to do?\n'
                       '1) Leave town (Fight Monster)\n'
                       '2) Sleep (Restore HP for 5 Gold)\n'
                       '3) View Shop\n'
                       '4) Open inventory\n'
                       '5) Save and Quit\n')

        print('You are in town.')
        print(f'Current Health: {player_health}, Current Gold: {player_gold}')

        if choice == '1':
            # Start the game loop for exploring
            player_x, player_y = town_x, town_y  # Start at town position
            while running:  # New loop for map exploration
                player_moved = False  # Reset the flag

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP and player_y > 0:
                            player_y -= 1
                            player_moved = True
                        if event.key == pygame.K_DOWN and player_y < 9:
                            player_y += 1
                            player_moved = True
                        if event.key == pygame.K_LEFT and player_x > 0:
                            player_x -= 1
                            player_moved = True
                        if event.key == pygame.K_RIGHT and player_x < 9:
                            player_x += 1
                            player_moved = True

                        # Check for town interaction
                        if player_x == town_x and player_y == town_y:
                            print("You are back in town.")
                            gameloop(monsters)  # Return to town menu without quitting

                        # Check for monster encounter
                        for monster in monsters:
                            if player_x == monster.x and player_y == monster.y:
                                print(f"You encountered a {monster.name}!")
                                fight_monster()  # Implement this function for combat
                                monsters.remove(monster)  # Remove the defeated monster
                                if not monsters:  # Check if there are no monsters left
                                    print("All monsters defeated! Generating new monsters...")
                                    new_monsters = create_initial_monsters(10, 10, town_x, town_y)
                                    monsters.extend(new_monsters)  # Add new monsters to the list
                                break

                # Monster movement after player input
                if player_moved:
                    for monster in monsters:
                        monster.move()

                draw_map()

        elif choice == '2':
            rest_at_inn(player_gold, player_health)

        elif choice == '3':
            print_shop_menu()

        elif choice == '4':
            open_inventory()

        elif choice == '5':
            save_monsters(monsters)  # Save before quitting
            print("Game saved. Exiting...")
            running = False

        else:
            print('Invalid choice, try again.\n')

    # Quit Pygame
    pygame.quit()
    save_monsters(monsters)  # Save monster data before quitting


python_game()
