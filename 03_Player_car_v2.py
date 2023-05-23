""" 03_Player_car_v2 by Sun Woo Yi
This version will place the car that the player will use onto the 
screen in the position that I want it to be in.
18/05/2023
"""

import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_width = 261
window_height = 377

# Create the window
screen = pygame.display.set_mode((window_width, window_height))

PLAYER_CAR = pygame.transform.scale(pygame.image.load("Assessment/Car Game/car_1.png"), (20, 40))

# place the PLAYER_CAR into the pygame
screen.blit(PLAYER_CAR, (120, 250))

pygame.display.update()

# this is used here for testing purposes
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(60)

pygame.quit()    