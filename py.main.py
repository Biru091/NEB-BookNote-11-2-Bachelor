import streamlit as st
import pygame
import random

# Initialize pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
FALLING_OBJECT_WIDTH = 30
FALLING_OBJECT_HEIGHT = 30
SPEED = 5

# Setup the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Catch the Falling Object')

# Game Clock
clock = pygame.time.Clock()

# Define the player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 40)

    def update(self, x_change):
        self.rect.x += x_change
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

# Define the falling object class
class FallingObject(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((FALLING_OBJECT_WIDTH, FALLING_OBJECT_HEIGHT))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - FALLING_OBJECT_WIDTH)
        self.rect.y = -FALLING_OBJECT_HEIGHT  # Start above the screen

    def update(self):
        self.rect.y += SPEED
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = -FALLING_OBJECT_HEIGHT
            self.rect.x = random.randint(0, SCREEN_WIDTH - FALLING_OBJECT_WIDTH)

# Setup the player
player = Player()

# Group for sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

falling_objects = pygame.sprite.Group()

# Create initial falling objects
for _ in range(5):
    falling_object = FallingObject()
    all_sprites.add(falling_object)
    falling_objects.add(falling_object)

# Game variables
score = 0
x_change = 0
running = True

# Main game loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -SPEED
            if event.key == pygame.K_RIGHT:
                x_change = SPEED
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

    # Update game objects
    player.update(x_change)
    falling_objects.update()

    # Check for collisions
    for falling_object in falling_objects:
        if player.rect.colliderect(falling_object.rect):
            score += 1
            falling_object.rect.y = -FALLING_OBJECT_HEIGHT
            falling_object.rect.x = random.randint(0, SCREEN_WIDTH - FALLING_OBJECT_WIDTH)

    # Draw everything
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Display score
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
