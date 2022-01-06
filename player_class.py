# Pac-Man
#
# Name: app_file.py
# Modified by: clarech712
# Purpose: Implement Player class

# Import pygame library, import settings
import pygame
from settings import *
vec = pygame.math.Vector2

# Implement Player class
class Player:
    def __init__(self, app, pos):
        self.app = app # Store attributes from App class
        self.grid_pos = pos # Store position as grid coordinates
        self.pix_pos = vec( # This is very ugly, and I know it
            self.grid_pos.x * self.app.cell_width + TOP_BOTTOM_BUFFER
            + self.app.cell_width // 2,
            self.grid_pos.y * self.app.cell_height + TOP_BOTTOM_BUFFER
            + self.app.cell_height // 2) # Pixel-based position for fluidity
    
    def update(self):
        pass
        
    def draw(self):
        pygame.draw.circle(self.app.screen, PLAYER_COLOUR,
            (int(self.pix_pos.x), int(self.pix_pos.y)),
            self.app.cell_width // 2 - 1) # Draw player as circle
        