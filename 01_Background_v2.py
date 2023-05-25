""" 01_Background_v2 by Sun Woo Yi
This version will make a background that I made move continuosly.
01/05/2023
"""

import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_width = 261
window_height = 377

# Create the window
screen = pygame.display.set_mode((window_width, window_height))

# Have two sets of backgrounds for continuously moving background
background1 = pygame.image.load("Road2.png")
background2 = pygame.image.load("Road2.png")

# Set the initial positions of the images
background1_y = 0
background2_y = -window_height

def update_position():
    global background1_y, background2_y
    # Makes the background move downwards (speed can change throughout)
    background1_y += 1
    background2_y += 1
    # Check if the first image has gone off the screen
    if background1_y >= window_height:
        background1_y = -window_height
    # Check if the second image has gone off the screen
    if background2_y >= window_height:
        background2_y = -window_height
    # Draw the images on the screen
    screen.blit(background1, (0, background1_y))
    screen.blit(background2, (0, background2_y))
    # Update the screen
    pygame.display.flip()

# Keep the window open until the user closes it
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    update_position()
    clock.tick(60)


pygame.quit()
