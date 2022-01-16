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
        if self.personality == "slow": # Set direction of "slow" enemy
            self.direction = self.get_path_direction()
        if self.personality == "speedy": # Set direction of "speedy" enemy
            self.direction = self.get_path_direction()
        if self.personality == "scared": # Set direction of "scared" enemy
            self.direction = self.get_path_direction()
            
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
        
    def get_path_direction(self):
        next_cell = self.find_next_cell_in_path() # Cell to move to next
        xdir = next_cell[0] - self.grid_pos[0] # Direction to move horizontally
        ydir = next_cell[1] - self.grid_pos[1] # Direction to move vertically
        return vec(xdir, ydir) # Zero/unit vector for enemy next move
        
    def find_next_cell_in_path(self):
        # Find enemy path towards player by breadth-first search
        path = self.BFS([int(self.grid_pos.x), int(self.grid_pos.y)],
            [int(self.app.player.grid_pos.x), int(self.app.player.grid_pos.y)])
        # Return next cell enemy should visit to get closer to player
        return path[1]
        
    def BFS(self, start, target):
        # Create grid of zeros copying maze grid
        grid = [[0 for x in range(28)] for x in range(30)]
        # Fill grid with ones in wall positions
        for cell in self.app.walls:
            if cell.x < 28 and cell.y < 30:
                grid[int(cell.y)][int(cell.x)] = 1
        queue = [start] # Zeroeth cell in queue current cell
        path = [] # List for ???
        visited = [] # List for cells visited
        while queue: # Implicitly true, dependent on break statement
            current = queue[0] # Current cell zeroeth cell in queue
            queue.remove(queue[0]) # Remove current cell from queue
            visited.append(current) # Add current cell to visited list
            if current == target: # If target cell reached
                break # Break while loop
            else:
                # Four directions
                neighbours = [[0, -1], [1, 0], [0, 1], [-1, 0]]
                # For each possible direction
                for neighbour in neighbours:
                    # If cell horizontal in that direction within grid
                    if (neighbour[0] + current[0] >= 0
                        and neighbour[0] + current[0] < len(grid[0])):
                        # If cell vertical in that direction within grid
                        if (neighbour[1] + current[1] >= 0
                            and neighbour[1] + current[1] < len(grid)):
                            # Set next cell to cell in direction from current
                            next_cell = [neighbour[0] + current[0],
                                neighbour[1] + current[1]]
                            # If potential next cell not yet in path
                            if next_cell not in visited:
                                # And if potential next cell not wall
                                if grid[next_cell[1]][next_cell[0]] != 1:
                                    # Add cell to queue
                                    queue.append(next_cell)
                                    # Append to path current and next
                                    path.append({"Current": current,
                                        "Next": next_cell})
        shortest = [target] # Initialise shortest path with target cell
        while target != start: # As long as the next target is not the start
            for step in path:
                if step["Next"] == target:
                    target = step["Current"] # Update target and
                    shortest.insert(0, step["Current"]) # Add to shortest path
        return shortest # Return shortest path
            
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