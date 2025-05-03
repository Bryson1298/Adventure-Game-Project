import random


class WanderingMonster:
    """
    Represents a wandering monster on the game map.

    Attributes:
        x (int): The x-coordinate of the monster on the grid.
        y (int): The y-coordinate of the monster on the grid.
        color (tuple): The RGB color of the monster.
        name (str): The name of the monster.
        gold (int): The amount of gold the monster has.
        health (int): The amount of health the monster has.
        grid_width (int): The width of the game grid.
        grid_height (int): The height of the game grid.
        town_x (int): The x-coordinate of the town.
        town_y (int): The y-coordinate of the town.
    """

    def __init__(self, x, y, color, name, gold, health, grid_width, grid_height, town_x, town_y):
        self.x = x
        self.y = y
        self.color = color
        self.name = name
        self.gold = gold
        self.health = health
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.town_x = town_x
        self.town_y = town_y
        self.move_counter = 0  # <--- NEW: initialize move counter

    def move(self):
        """
        Attempts to move the monster every other turn.
        """
        self.move_counter += 1  # <--- increment counter

        if self.move_counter % 2 != 0:
            # Skip this turn (move every other turn)
            return False

        possible_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Down, Up, Right, Left
        random.shuffle(possible_moves)

        for dx, dy in possible_moves:
            new_x, new_y = self.x + dx, self.y + dy

            if (0 <= new_x < self.grid_width and
                    0 <= new_y < self.grid_height and
                    (new_x != self.town_x or new_y != self.town_y)):
                self.x, self.y = new_x, new_y
                return True  # Monster moved

        return False  # Monster did not move

    @staticmethod
    def new_random_monster(grid_width, grid_height, town_x, town_y):
        """
        Creates a random monster with specific attributes.

        Returns:
            WanderingMonster: A new instance of WanderingMonster.
        """
        monster_types = {
            "Drake": {"name": "Drake", "color": (255, 255, 0), "gold": random.randint(50, 150), "health": random.randint(80, 100)},
            "Zombie": {"name": "Zombie","color": (255, 0, 0), "gold": random.randint(10, 50), "health": random.randint(30, 50)},
            "Skeleton": {"name": "Skeleton","color": (255, 255, 255), "gold": random.randint(20, 75), "health": random.randint(45, 65)}
        }
        monster_name = random.choice(list(monster_types.keys()))
        monster_data = monster_types[monster_name]

        x = random.randint(0, grid_width - 1)
        y = random.randint(0, grid_height - 1)

        # Ensure the monster does not spawn in the town
        while (x == town_x and y == town_y):
            x = random.randint(0, grid_width - 1)
            y = random.randint(0, grid_height - 1)

        return WanderingMonster(x, y, monster_data["color"], monster_name, monster_data["gold"], monster_data["health"], grid_width,
                                grid_height, town_x, town_y)
