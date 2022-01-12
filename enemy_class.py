# Pac-Man
#
# Name: enemy_class.py
# Modified by: clarech712
# Purpose: Implement Enemy class

# Import pygame library, import settings
import pygame
from settings import *
vec = pygame.math.Vector2

class Enemy:
    def __init__(self, app, pos):
        self.app = app # Relation with app using class
        self.grid_pos = pos # Set grid position of Enemy
        # Determine pixel position of Enemy with respect to maze background
        self.pix_pos = self.get_pix_pos()
        
    def get_pix_pos(self):
        return vec( # Pixel-based position for fluidity
            self.grid_pos.x * self.app.cell_width + self.app.cell_width // 2,
            self.grid_pos.y * self.app.cell_height + self.app.cell_height // 2)
        
    def update(self):
        pass
        
    def draw(self):
        pygame.draw.circle(self.app.screen, WHITE,
            (int(self.pix_pos.x) + TOP_BOTTOM_BUFFER,
            int(self.pix_pos.y) + TOP_BOTTOM_BUFFER), 10) # Draw as circle