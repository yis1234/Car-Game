""" 03_Player_car_v1 by Sun Woo Yi
This version will change the size of the car to fit the screen
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

PLAYER_CAR = pygame.transform.scale(pygame.image.load("car_1.png"), (20, 40))

# place the PLAYER_CAR into the pygame
screen.blit(PLAYER_CAR, (0, 0))

pygame.display.update()

# this is used here for testing purposes
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # for testing purposes
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left")
            if event.key == pygame.K_RIGHT:
                print("right")
            if event.key == pygame.K_UP:
                print("up")
            if event.key == pygame.K_DOWN:
                print("down")
            keys = pygame.key.get_pressed()
            for i in range(len(keys)):
                if keys[i]:
                    print(pygame.key.name(i))
    clock.tick(60)

pygame.quit()
