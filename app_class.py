# Pac-Man
#
# Name: app_file.py
# Modified by: clarech712
# Purpose: Implement App class

# Prevent pygame from printing message to command line
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# Import pygame and sys libraries, import settings and Player class
import pygame, sys
from settings import *
from player_class import *

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
        self.cell_width = MAZE_WIDTH // 28 # Set cell width
        self.cell_height = MAZE_HEIGHT // 30 # Set cell height
        self.player = Player(self, PLAYER_START_POS) # Introduce player
        self.walls = []
        
        self.load() # Load all images at once
        
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
        
    # This is the function I would eventually like adaptable to various maps
    def load(self):
        self.background = pygame.image.load("maze.png")
        self.background = pygame.transform.scale(self.background,
            (MAZE_WIDTH, MAZE_HEIGHT)) # Scale background image to window
        # Open file with walls, create walls list with coordinates
        with open("walls.txt", "r") as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == "1":
                        self.walls.append(vec(xidx, yidx))
            
    # Helper function designed to visualise logic of game, for testing only
    def draw_grid(self):
        for x in range(WIDTH // self.cell_width):
            pygame.draw.line(self.background, GREY, (x * self.cell_width, 0),
                (x * self.cell_width, HEIGHT)) # Draw vertical lines
        for x in range(HEIGHT // self.cell_height):
            pygame.draw.line(self.background, GREY, (0, x * self.cell_height),
                (WIDTH, x * self.cell_height)) # Draw horizontal lines
        for wall in self.walls:
            pygame.draw.rect(self.background, (120, 60, 160),
                (wall.x * self.cell_width, wall.y * self.cell_height,
                self.cell_width, self.cell_height))
    
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
            [TOP_BOTTOM_BUFFER, 0], START_TEXT_SIZE, (255, 255, 255),
            START_FONT) # Draw high score
        pygame.display.update()
        
    # PLAYING FUNCTIONS
    
    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False # Quit game if user clicks on quit button
            # Move player according to user key choice
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move(vec(-1, 0))
                if event.key == pygame.K_RIGHT:
                    self.player.move(vec(1, 0))
                if event.key == pygame.K_UP:
                    self.player.move(vec(0, -1))
                if event.key == pygame.K_DOWN:
                    self.player.move(vec(0, 1))   
    
    def playing_update(self):
        self.player.update()
        
    def playing_draw(self):
        self.screen.fill(BLACK) # Set general background
        self.screen.blit(self.background, (TOP_BOTTOM_BUFFER,
            TOP_BOTTOM_BUFFER)) # Set maze background
        # self.draw_grid() # Draw grid
        self.draw_text("CURRENT  SCORE:  0", self.screen, [TOP_BOTTOM_BUFFER, 0],
            START_TEXT_SIZE, WHITE, START_FONT) # Display current score
        self.draw_text("HIGH  SCORE:  0", self.screen, [WIDTH // 2, 0],
            START_TEXT_SIZE, WHITE, START_FONT) # Display hight score
        self.player.draw() # Draw player
        pygame.display.update()

