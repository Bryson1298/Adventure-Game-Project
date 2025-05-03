# FightingEnhanced.py
import pygame
import random
from gamefunctions import *
from WanderingMonster import *

# Constants (You can adjust these)

attack_duration = 300  # Milliseconds
attack_distance = 100  # Pixels


def draw_health_bars(screen, player_health, monster_health, screen_width, screen_height):
    """Draws health bars for the player and monster."""

    # Player Health Bar (Bottom Left)
    player_health_width = int(player_health / 2)
    player_health_bar_y = screen_height - 25
    player_health_text_y = screen_height - 50
    pygame.draw.rect(screen, red, (50, player_health_bar_y, 200, 20))  # Background
    pygame.draw.rect(screen, green, (50, player_health_bar_y, player_health_width, 20))  # Health
    pygame.draw.rect(screen, white, (50, player_health_bar_y, 200, 20), 2)  # Border

    font = pygame.font.Font(None, 20)
    health_text = font.render(f"Player HP: {player_health}", True, white)
    screen.blit(health_text, (50, player_health_text_y))  # Player text

    # Monster Health Bar (Bottom Right)
    monster_health_width = int(monster_health / 2)
    monster_health_bar_y = screen_height - 275  # Same height as player health bar
    monster_health_text_y = screen_height - 300  # Same height as player text
    pygame.draw.rect(screen, red, (screen_width - 250, monster_health_bar_y, 200, 20))  # Background
    pygame.draw.rect(screen, green, (screen_width - 250, monster_health_bar_y, monster_health_width, 20))  # Health
    pygame.draw.rect(screen, white, (screen_width - 250, monster_health_bar_y, 200, 20), 2)  # Border

    monster_health_text = font.render(f"Monster HP: {monster_health}", True, white)
    screen.blit(monster_health_text, (screen_width - 250, monster_health_text_y))  # Monster text


def fight_monster_enhanced(screen, player_health, player_gold, monster, screen_width, screen_height):
    font = pygame.font.Font(None, 36)
    monster_health = monster.health
    player_attack_cooldown = 1000  # Player auto-attacks every 1 second
    monster_attack_cooldown = 1500
    last_player_attack_time = 0
    last_monster_attack_time = 0
    running = True
    player_attack_rect = None
    monster_attack_rect = None

    while running:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return player_health, player_gold, False

        # Player automatic attack
        if current_time - last_player_attack_time >= player_attack_cooldown:
            damage = random.randint(10, 20)
            monster_health -= damage
            last_player_attack_time = current_time
            player_attack_rect = pygame.Rect(screen_width - 100, screen_height // 2 - 50, attack_distance, 40)
            print(f"You attacked for {damage} damage!")
            if monster_health <= 0:
                print(f"You defeated the {monster.name}!")
                gold_gained = random.randint(5, 15)
                player_gold += gold_gained
                print(f"You found {gold_gained} gold!")
                return player_health, player_gold, True

        # Monster attack
        if current_time - last_monster_attack_time >= monster_attack_cooldown:
            if random.random() < 0.5:
                damage = random.randint(5, 15)
                player_health -= damage
                last_monster_attack_time = current_time
                monster_attack_rect = pygame.Rect(10, screen_height // 2 - 50, attack_distance, 40)
                print(f"{monster.name} attacked for {damage} damage!")
                if player_health <= 0:
                    print("You were defeated!")
                    return 100, player_gold, False

        # Drawing
        screen.fill(black)
        draw_health_bars(screen, player_health, monster_health, screen_width, screen_height)

        # Draw Player Image (Positioned Left)
        try:
            player_image = pygame.image.load('pygame.Player.jpg')
            player_image = pygame.transform.scale(player_image, (100, 100))
            player_x = 10
            player_y = screen_height // 2 - 50
            screen.blit(player_image, (player_x, player_y))
        except:
            pygame.draw.rect(screen, white, (10, screen_height // 2 - 50, 100, 100))  # Placeholder if image fails

        # Draw Monster Image (Positioned Right)
        try:
            monster_image = pygame.image.load(f'pygame.{monster.name}.jpg')
            monster_image = pygame.transform.scale(monster_image, (100, 100))
            monster_x = screen_width - 100  # Give enough space from the right edge
            monster_y = screen_height // 2 - 50
            screen.blit(monster_image, (monster_x, monster_y))
        except:
            pygame.draw.rect(screen, monster.color,
                             (screen_width - 100, screen_height // 2 - 50, 100, 100))  # Placeholder if image fails

        # Draw Attack Effects
        if player_attack_rect:
            if current_time - last_player_attack_time < attack_duration:
                pygame.draw.rect(screen, green, player_attack_rect)
            else:
                player_attack_rect = None

        if monster_attack_rect:
            if current_time - last_monster_attack_time < attack_duration:
                pygame.draw.rect(screen, red, monster_attack_rect)
            else:
                monster_attack_rect = None

        pygame.display.flip()

    return player_health, player_gold, False
