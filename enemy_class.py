# Pac-Man
#
# Name: enemy_class.py
# Modified by: clarech712
# Purpose: Implement Enemy class

# Import pygame, random, numpy libraries, import settings
import pygame
import random
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
        if self.time_to_move(): # Move if time to do so
            self.move()
            
        # Setting grid position in reference to pixel position
        self.grid_pos.x = (self.pix_pos.x // self.app.cell_width)
        self.grid_pos.y = (self.pix_pos.y // self.app.cell_height)
        
    def draw(self):
        pygame.draw.circle(self.app.screen, self.colour,
            (int(self.pix_pos.x) + TOP_BOTTOM_BUFFER,
            int(self.pix_pos.y) + TOP_BOTTOM_BUFFER), self.radius)
            
    def time_to_move(self):
        # Only enable enemy to move when between grid lines
        if ((int(self.pix_pos.x) + self.app.cell_width // 2)
            % self.app.cell_width == 0):
            if self.direction == vec(-1, 0) or self.direction == vec(1, 0):
                return True
        if ((int(self.pix_pos.y) + self.app.cell_height // 2)
            % self.app.cell_height == 0):
            if self.direction == vec(0, 1) or self.direction == vec(0, -1):
                return True
        return False
        
    def move(self):
        if self.personality == "random": # Set direction of "random" enemy
            self.direction = self.get_random_direction()
            
    def get_random_direction(self):
        while True:
            # Generate random unit vector in one of four directions
            number = random.randint(-2, 2)
            if number == -2:
                xdir, ydir = 1, 0
            elif number == -1:
                xdir, ydir = -1, 0
            elif number == 0:
                xdir, ydir = 0, 1
            else:
                xdir, ydir = 0, -1
            # If step in generated direction ends up in wall, repeat
            next_pos = vec(self.grid_pos.x + xdir, self.grid_pos.y + ydir)
            if next_pos not in self.app.walls:
                break
        return vec(xdir, ydir)
            
            
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