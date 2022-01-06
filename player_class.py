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
        self.pix_pos = self.get_pix_pos() # Store position as pixel coordinates
        self.direction = vec(1, 0) # Set direction as unit vector
    
    def update(self):
        self.pix_pos += self.direction # Update position on direction
        
        # Setting grid position in reference to pixel position
        self.grid_pos.x = ((self.pix_pos.x - 2 * TOP_BOTTOM_BUFFER
            + self.app.cell_width // 2) // self.app.cell_width + 1)
        self.grid_pos.y = ((self.pix_pos.y - 2 * TOP_BOTTOM_BUFFER
            + self.app.cell_height // 2) // self.app.cell_height + 1)
        
    def draw(self):
        pygame.draw.circle(self.app.screen, PLAYER_COLOUR,
            (int(self.pix_pos.x), int(self.pix_pos.y)),
            self.app.cell_width // 2) # Draw player as circle
            
        # Drawing the grid position rectangle
        pygame.draw.rect(self.app.screen, RED,
            (self.grid_pos.x * self.app.cell_width + TOP_BOTTOM_BUFFER,
            self.grid_pos.y * self.app.cell_height + TOP_BOTTOM_BUFFER,
            self.app.cell_width, self.app.cell_height), 1)
            
    def move(self, direction):
        self.direction = direction
        
    def get_pix_pos(self):
        return vec(
            self.grid_pos.x * self.app.cell_width + TOP_BOTTOM_BUFFER
            + self.app.cell_width // 2,
            self.grid_pos.y * self.app.cell_height + TOP_BOTTOM_BUFFER
            + self.app.cell_height // 2) # Pixel-based position for fluidity