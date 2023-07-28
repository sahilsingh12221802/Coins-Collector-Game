import pygame
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
AVATAR_SIZE = 200
COIN_SIZE = 90
AVATAR_SPEED = 5
COIN_SPAWN_INTERVAL = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collect the Coins")

# Load images
avatar_img = pygame.image.load("avatar.png")
avatar_img = pygame.transform.scale(avatar_img, (AVATAR_SIZE, AVATAR_SIZE))
coin_img = pygame.image.load("coin.png")
coin_img = pygame.transform.scale(coin_img, (COIN_SIZE, COIN_SIZE))

# Avatar initial position
avatar_x = WIDTH // 2
avatar_y = HEIGHT // 2

# Coin variables
coins = []
coin_spawn_counter = 0

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Avatar movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        avatar_x -= AVATAR_SPEED
    if keys[pygame.K_RIGHT]:
        avatar_x += AVATAR_SPEED
    if keys[pygame.K_UP]:
        avatar_y -= AVATAR_SPEED
    if keys[pygame.K_DOWN]:
        avatar_y += AVATAR_SPEED

    # Coin spawning
    coin_spawn_counter += 1
    if coin_spawn_counter >= COIN_SPAWN_INTERVAL:
        coin_spawn_counter = 0
        coin_x = random.randint(0, WIDTH - COIN_SIZE)
        coin_y = random.randint(0, HEIGHT - COIN_SIZE)
        coins.append((coin_x, coin_y))

    # Collision detection
    avatar_rect = pygame.Rect(avatar_x, avatar_y, AVATAR_SIZE, AVATAR_SIZE)
    for coin in coins[:]:
        coin_rect = pygame.Rect(coin[0], coin[1], COIN_SIZE, COIN_SIZE)
        if avatar_rect.colliderect(coin_rect):
            coins.remove(coin)

    # Draw everything on the screen
    screen.fill(WHITE)
    for coin in coins:
        screen.blit(coin_img, coin)
    screen.blit(avatar_img, (avatar_x, avatar_y))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
