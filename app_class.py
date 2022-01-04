# Pac-Man
#
# Name: app_file.py
# Modified by: clarech712
# Purpose: Implement App class

# Prevent pygame from printing message to command line
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# Import pygame and sys libraries, import settings
import pygame, sys
from settings import *

# Initialise game engine
pygame.init()

# Store vector to be used for position and velocity
vec = pygame.math.Vector2

# Define App class
class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = "intro"
        
    def run(self):
        while self.running:
            if self.state == "intro":
                self.intro_events()
                self.intro_update()
                self.intro_draw()
            self.clock.tick(FPS)
        # Quit game engine
        pygame.quit()
        sys.exit()
        
    # INTRO FUNCTIONS
    
    def intro_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def intro_update(self):
        pass
        
    def intro_draw(self):
        pygame.display.update()

