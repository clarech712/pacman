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
        self.state = "start" # Default state
        
    def run(self):
        while self.running:
            if self.state == "start": # In start state
                self.start_events() # Check events
                self.start_update()
                self.start_draw() # Draw to screen
            elif self.state == "playing": # In playing state
                self.playing_events() # Check events
                self.playing_update()
                self.playing_draw() # Draw to screen
            else:
                self.running = False
            self.clock.tick(FPS)
        # Quit game engine
        pygame.quit()
        sys.exit()
        
    # HELPER FUNCTIONS
    
    def draw_text(self, words, screen, pos, size, colour, font_name,
        centered = False):
        font = pygame.font.SysFont(font_name, size) # Set font and size
        text = font.render(words, False, colour) # Set colour
        text_size = text.get_size() # Get text rectangle dimensions
        if centered:
            pos[0] = pos[0] - text_size[0] // 2 # Find x-position for centered
            pos[1] = pos[1] - text_size[1] // 2 # Find y-position for centered
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
        self.draw_text("PUSH  SPACE  BAR", self.screen,
            [WIDTH // 2, HEIGHT // 2 - 25], START_TEXT_SIZE, (255, 200, 64),
            START_FONT, centered = True) # Draw instructions
        self.draw_text("1  PLAYER  ONLY", self.screen,
            [WIDTH // 2, HEIGHT // 2 + 25], START_TEXT_SIZE, (40, 170, 200),
            START_FONT, centered = True) # Draw number of players info
        self.draw_text("HIGH  SCORE", self.screen,
            [5, 0], START_TEXT_SIZE, (255, 255, 255),
            START_FONT) # Draw high score
        pygame.display.update()
        
    # PLAYING FUNCTIONS
    
    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False # Quit game if user clicks on quit button
    
    def playing_update(self):
        pass
        
    def playing_draw(self):
        self.screen.fill(RED) # Set background colour
        pygame.display.update()

