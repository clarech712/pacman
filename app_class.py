# Pac-Man
#
# Name: app_class.py
# Modified by: clarech712
# Purpose: Implement App class

# Prevent pygame from printing message to command line
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# Import pygame and sys libraries, import settings and Player class
import pygame, sys
from settings import *
from player_class import *
from enemy_class import *

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
        self.walls = [] # Empty list for wall grid positions
        self.coins = [] # Empty list for coin grid positions
        self.enemies = [] # Empty list for enemies
        self.p_pos = None # Declare position of player
        self.e_pos = [] # Empty list for enemy positions
        
        self.load() # Load all images at once
        
        self.player = Player(self, self.p_pos) # Introduce player
        self.make_enemies() # Introduce enemies
        
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
        
    # This I would eventually like adaptable to various maps
    def load(self):
        self.background = pygame.image.load("maze.png")
        self.background = pygame.transform.scale(self.background,
            (MAZE_WIDTH, MAZE_HEIGHT)) # Scale background image to window
        # Open file with walls
        with open("walls.txt", "r") as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == "1": # Create list with wall coordinates
                        self.walls.append(vec(xidx, yidx))
                    elif char == "C": # Create list with coin coordinates
                        self.coins.append(vec(xidx, yidx))
                    elif char == "P": # Set position of player
                        self.p_pos = vec(xidx, yidx)
                    elif char in ["2", "3", "4", "5"]:
                        self.e_pos.append(vec(xidx, yidx))
                    elif char == "B":
                        pygame.draw.rect(self.background, BLACK,
                            (xidx * self.cell_width, yidx * self.cell_height,
                            self.cell_width, self.cell_height))
            
    def make_enemies(self):
        for idx, pos in enumerate(self.e_pos):
            self.enemies.append(Enemy(self, pos, idx)) # Create enemies
    
    # TESTING CODE
    def draw_grid(self):
        for x in range(WIDTH // self.cell_width):
            pygame.draw.line(self.background, GREY, (x * self.cell_width, 0),
                (x * self.cell_width, HEIGHT)) # Draw vertical lines
        for x in range(HEIGHT // self.cell_height):
            pygame.draw.line(self.background, GREY, (0, x * self.cell_height),
                (WIDTH, x * self.cell_height)) # Draw horizontal lines
        # for wall in self.walls:
        #     pygame.draw.rect(self.background, (120, 60, 160),
        #         (wall.x * self.cell_width, wall.y * self.cell_height,
        #         self.cell_width, self.cell_height))
    # TESTING CODE
    
    def draw_coins(self):
        for coin in self.coins:
            pygame.draw.circle(self.screen, (120, 120, 10),
                (int(coin.x * self.cell_width)
                + self.cell_width // 2 + TOP_BOTTOM_BUFFER,
                int(coin.y * self.cell_height)
                + self.cell_height // 2 + TOP_BOTTOM_BUFFER), 5)
    
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
        for enemy in self.enemies:
            enemy.update()
        
    def playing_draw(self):
        self.screen.fill(BLACK) # Set general background
        self.screen.blit(self.background, (TOP_BOTTOM_BUFFER,
            TOP_BOTTOM_BUFFER)) # Set maze background
        self.draw_coins() # Draw coins
        # TESTING CODE
        self.draw_grid() # Draw grid
        # TESTING CODE
        # Display current score
        self.draw_text("CURRENT  SCORE:  {}".format(self.player.current_score),
            self.screen, [TOP_BOTTOM_BUFFER + 10, 0], START_TEXT_SIZE, WHITE,
            START_FONT)
        # Display hight score
        self.draw_text("HIGH  SCORE:  0", self.screen,
            [WIDTH // 2 + 10, 0], START_TEXT_SIZE, WHITE, START_FONT)
        self.player.draw() # Draw player
        for enemy in self.enemies:
            enemy.draw() # Draw each enemy
        pygame.display.update()

