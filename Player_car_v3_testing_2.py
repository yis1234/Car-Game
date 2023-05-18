""" Player_car_v3_testing_2 by Sun Woo Yi
This version will allow the car to move from left to right so
that it is able to avoid incoming cars in future steps. This test will
use a class and get the rect of the image.
19/05/2023
"""

import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_width = 261
window_height = 377

# Create the window
screen = pygame.display.set_mode((window_width, window_height))

# Load the player car image
PLAYER_CAR = pygame.transform.scale(pygame.image.load("Assessment/Car Game/car_1.png"), (20, 40))

# Create the player car sprite
class PlayerCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = PLAYER_CAR
        self.rect = self.image.get_rect(center=(window_width/2, window_height-50))

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)
        self.rect.clamp_ip(screen.get_rect())  # to make sure that the car does not go out of the screen

player_car = PlayerCar()

# Create a sprite group for the player car
player_group = pygame.sprite.Group(player_car)

# this is used here for testing purposes
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player_car.update(pygame.key.get_pressed())
    screen.fill((255, 255, 255))
    player_group.draw(screen)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
