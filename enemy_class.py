# Pac-Man
#
# Name: enemy_class.py
# Modified by: clarech712
# Purpose: Implement Enemy class

# Import pygame library, numpy library, import settings
import pygame
import numpy as np
from settings import *
vec = pygame.math.Vector2

class Enemy:
    def __init__(self, app, pos, number):
        self.app = app # Relation with app using class
        self.grid_pos = pos # Set grid position of Enemy
        # Determine pixel position of Enemy with respect to maze background
        self.pix_pos = self.get_pix_pos()
        self.radius = self.app.cell_width // 2
        self.number = number # ??? Might be useless if using random colour
        self.colour = self.set_colour() # Set random colour of enemy
        self.direction = vec(1, 0)
        self.personality = self.set_personality()
        
    def update(self):
        self.pix_pos += self.direction # Update pixel position
        if self.time_to_move: # Move if time to do so
            self.move()
        
    def draw(self):
        pygame.draw.circle(self.app.screen, self.colour,
            (int(self.pix_pos.x) + TOP_BOTTOM_BUFFER,
            int(self.pix_pos.y) + TOP_BOTTOM_BUFFER), self.radius)
            
    def time_to_move(self):
        pass
        
    def move(self):
        pass
            
    def get_pix_pos(self):
        return vec( # Pixel-based position for fluidity
            self.grid_pos.x * self.app.cell_width + self.app.cell_width // 2,
            self.grid_pos.y * self.app.cell_height + self.app.cell_height // 2)
            
    # def set_colour(self):
    #    return tuple(np.random.randint(256, size = 3)) # Generate random colour
        
    # Set enemy colour based on number
    def set_colour(self):
        if self.number == 0:
            return (40, 80, 200)
        if self.number == 1:
            return (200, 200, 30)
        if self.number == 2:
            return (200, 30, 30)
        if self.number == 3:
            return (200, 160, 30)
    
    # Set enemy personality based on number
    def set_personality(self):
        if self.number == 0:
            return "speedy"
        elif self.number == 1:
            return "slow"
        elif self.number == 2:
            return "random"
        elif self.number == 3:
            return "scared"