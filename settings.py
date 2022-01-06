# Pac-Man
#
# Name: settings.py
# Modified by: clarech712
# Purpose: Store settings conveniently

# Import vector
from pygame.math import Vector2 as vec

# Screen settings
MAZE_WIDTH, MAZE_HEIGHT = 560, 620
FPS = 60
TOP_BOTTOM_BUFFER = 25
WIDTH, HEIGHT = (MAZE_WIDTH + 2 * TOP_BOTTOM_BUFFER,
    MAZE_HEIGHT + 2 * TOP_BOTTOM_BUFFER)

# Colour settings
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (227, 2, 137)
GREY = (128, 128, 128)
PLAYER_COLOUR = (190, 190, 15)

# Font settings
START_TEXT_SIZE = 16
START_FONT = "arial black"

# Player settings
PLAYER_START_POS = vec(1, 1) # Set grid starting position of player

# Mob settings