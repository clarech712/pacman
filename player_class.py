# Pac-Man
#
# Name: player_class.py
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
        self.stored_direction = None
        self.able_to_move = True
        self.current_score = 0
        self.speed = 1 # Set speed
    
    def update(self):
        if self.able_to_move: # If no wall in the way, update position
            self.pix_pos += self.direction * self.speed # accounting for speed
        # Wait until between lines and only then take turn
        if self.time_to_move():
            if self.stored_direction != None:
                self.direction = self.stored_direction
            self.able_to_move = self.can_move()
        
        # Setting grid position in reference to pixel position
        self.grid_pos.x = (self.pix_pos.x // self.app.cell_width)
        self.grid_pos.y = (self.pix_pos.y // self.app.cell_height)
        
        if self.on_coin():
            self.eat_coin()
        
    def draw(self):
        pygame.draw.circle(self.app.screen, PLAYER_COLOUR,
            (int(self.pix_pos.x) + TOP_BOTTOM_BUFFER,
            int(self.pix_pos.y) + TOP_BOTTOM_BUFFER),
            self.app.cell_width // 2) # Draw player as circle
            
        # TESTING CODE
        # Drawing the grid position rectangle
        # pygame.draw.rect(self.app.screen, RED,
        #     (self.grid_pos.x * self.app.cell_width + TOP_BOTTOM_BUFFER,
        #     self.grid_pos.y * self.app.cell_height + TOP_BOTTOM_BUFFER,
        #     self.app.cell_width, self.app.cell_height), 1)
        # TESTING CODE
        
    def on_coin(self):
        if self.grid_pos in self.app.coins and self.time_to_move():
            return True
        else:
            return False
            
    def eat_coin(self):
        self.app.coins.remove(self.grid_pos) # Eat coin
        self.current_score += 1 # Update score
            
    def move(self, direction):
        self.stored_direction = direction
        
    def get_pix_pos(self):
        return vec( # Pixel-based position for fluidity
            self.grid_pos.x * self.app.cell_width + self.app.cell_width // 2,
            self.grid_pos.y * self.app.cell_height + self.app.cell_height // 2)
            
    def time_to_move(self):
        # Only enable player to move when between grid lines
        if ((int(self.pix_pos.x) + self.app.cell_width // 2)
            % self.app.cell_width == 0):
            if self.direction == vec(-1, 0) or self.direction == vec(1, 0):
                return True
        if ((int(self.pix_pos.y) + self.app.cell_height // 2)
            % self.app.cell_height == 0):
            if self.direction == vec(0, 1) or self.direction == vec(0, -1):
                return True
        return False
                
    def can_move(self):
        for wall in self.app.walls:
            if vec(self.grid_pos + self.direction) == wall:
                return False # If next move would result in wall, do not move
        return True # If path clear, do move