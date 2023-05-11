""" Background_v1 by Sun Woo Yi
This version will place the background image onto the screen.
01/05/2023
"""

import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_width = 500
window_height = 750

# Create the window
screen = pygame.display.set_mode((window_width, window_height))

# Set the background color to black
screen.fill((0, 0, 0))

# Update the display to show the black background
pygame.display.update()

# Keep the window open until the user closes it
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
