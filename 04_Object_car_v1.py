""" 04_Object_car_v1 by Sun Woo Yi
In this version of the component, the object cars will be added to the pygame
20/05/23
"""

import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_width = 261
window_height = 377

# Create the window
screen = pygame.display.set_mode((window_width, window_height))

# Changing the size of the object cars
object_car1 = pygame.transform.scale(pygame.image.load("car_2.png"), (20, 40))
object_car2 = pygame.transform.scale(pygame.image.load("car_3.png"), (20, 40))
object_car3 = pygame.transform.scale(pygame.image.load("car_4.png"), (20, 40))
object_car4 = pygame.transform.scale(pygame.image.load("car_5.png"), (20, 40))
object_car5 = pygame.transform.scale(pygame.image.load("car_6.png"), (20, 40))

# Adding the cars to the screen
screen.blit(object_car1, (0, 0))
screen.blit(object_car2, (10, 0))
screen.blit(object_car3, (20, 0))
screen.blit(object_car4, (30, 0))
screen.blit(object_car5, (40, 0))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()