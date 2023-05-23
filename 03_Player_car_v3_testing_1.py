""" 03_Player_car_v3_testing_1 by Sun Woo Yi
This version will allow the car to move from left to right so
that it is able to avoid incoming cars in future steps. This test 
will use the pygame.key.get_pressed() method.
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
player_x = 120
player_x_change = 0
screen.blit(PLAYER_CAR, (player_x, 250))


# this is used here for testing purposes
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
    
    player_x += player_x_change
    screen.fill((255, 255, 255))
    screen.blit(PLAYER_CAR, (player_x, 250))
    pygame.display.update()
    clock.tick(60)

pygame.quit()    