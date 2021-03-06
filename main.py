import pygame

from pygame import rect

# Getting a background image
# Make sure image is the same width and height specified by pygame.display.set_mode()

# Clock (frames per second)
clock = pygame.time.Clock();

# Initialize the pygame
pygame.init()

# create the screen (width, height)
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("images/background.png")

# Tile and Icon
pygame.display.set_caption("Dino Run")
icon = pygame.image.load('images/001-dinosaur.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("images/dinosaur.png")
playerX = 370
playerY = 480
playerX_change = 0

# Score
score_value = 0
# For any more fonts (https://www.dafont.com/),
# Move downloaded .ttf file to project folder and call it below
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Rectangles used for collisions
player_rect = pygame.Rect(playerX, playerY, playerImg.get_width(), playerImg.get_height())
test_rect = pygame.Rect(100, 480, 100, 50)


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


# Game loop
running = True
while running:
    # RGB values for screen
    screen.fill((0, 0, 0))
    # Background image
    screen.blit(background, (0, 0))

    player_rect.x = playerX
    player_rect.y = playerY

    if player_rect.colliderect(test_rect):
        pygame.draw.rect(screen, (255, 0, 0), test_rect)
    else:
        pygame.draw.rect(screen, (0, 0, 0), test_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # KEYDOWN - "checks to see if any keyboard key is being pressed"
        if event.type == pygame.KEYDOWN:
            print("A keystroke is pressed")
            if event.key == pygame.K_LEFT:
                print("Left arrow is pressed")
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                print("Right arrow is pressed")
                playerX_change = 3
        # KEYUP - "Checks to see if any key is released (stopped pressing)"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Keystroke has been released")
                playerX_change = 0

    # Incorporate player movement
    playerX += playerX_change;

    # Initialize the player image
    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
    clock.tick(60)
