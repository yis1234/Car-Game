""" 05_Collisions_v1_testing_2 by Sun Woo Yi
This version will show a colliion being detected between two objects
for testing purposes, "Collision" will be printed when the objects collide
This version will use pygame.sprite.collide_rect() method to detect collisions
This way will be more helpful for adding on to current team
26/05/2023
"""

import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_width = 261
window_height = 377

# Create the window
screen = pygame.display.set_mode((window_width, window_height))

class GreenBox(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class BlueBox(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Set up the green box
green_box_x = window_width/2 - 50/2
green_box_y = 377 - 50
green_box = GreenBox(green_box_x, green_box_y)
all_sprites = pygame.sprite.Group(green_box)

# Set up the blue box
blue_box_x = window_width/2 - 50/2
blue_box_y = 0
blue_box = BlueBox(blue_box_x, blue_box_y)
all_sprites.add(blue_box)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the boxes
    green_box.rect.y -= 1
    blue_box.rect.y += 1

    # Check for collisions
    if pygame.sprite.collide_rect(green_box, blue_box):
        print("Collision")

    # Draw the boxes
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()
