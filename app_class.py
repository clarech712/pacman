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
        self.state = "start"
        
    def run(self):
        while self.running:
            if self.state == "start":
                self.start_events()
                self.start_update()
                self.start_draw()
            self.clock.tick(FPS)
        # Quit game engine
        pygame.quit()
        sys.exit()
        
    # HELPER FUNCTIONS
    
    def draw_text(self, words, screen, pos, size, colour, font_name):
        font = pygame.font.SysFont(font_name, size) # Set font and size
        text = font.render(words, False, colour) # Set colour
        text_size = text.get_size() # Get text rectangle dimensions
        pos[0] = pos[0] - text_size[0] // 2 # Find x-position for centered text
        pos[1] = pos[1] - text_size[1] // 2 # Find y-position for centered text
        screen.blit(text, pos) # Display centered text
    
    # START FUNCTIONS
    
    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False # Quit game if user clicks on quit button
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = "playing" # Start game if user presses space bar
    
    def start_update(self):
        pass
        
    def start_draw(self):
        self.screen.fill(BLACK) # Set background colour
        self.draw_text("PUSH SPACE BAR", self.screen,
            [WIDTH // 2, HEIGHT // 2], START_TEXT_SIZE, (170, 130, 60),
            START_FONT) # Draw instructions
        pygame.display.update()

