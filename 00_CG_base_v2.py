""" 00_CG_base_v2 by Sun Woo Yi
Added 02_Player_car_v3_testing_2 to the 00_CG_base_v1
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

# Have two sets of backgrounds for continuously moving background
background1 = pygame.image.load("Assessment/Car Game/Road2.png").convert_alpha()
background2 = pygame.image.load("Assessment/Car Game/Road2.png").convert_alpha()

# Set the initial positions of the images
background1_y = 0
background2_y = -window_height

# Load the player car image
PLAYER_CAR = pygame.transform.scale(pygame.image.load("Assessment/Car Game/car_1.png"), (20, 40)).convert_alpha()

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
    player_group.draw(screen)
    # Update the screen
    pygame.display.update()

# Keep the window open until the user closes it
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player_car.update(pygame.key.get_pressed())
    update_position()
    pygame.display.update()
    clock.tick(60)


pygame.quit()
