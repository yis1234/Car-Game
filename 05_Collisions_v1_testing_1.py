""" 05_Collisions_v1_testing_1 by Sun Woo Yi
This version will show a collision being detected between two objects
for testing purposes, "Collision" will be printed when the objects collide
This version will use .colliderect() method to detect collisions
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

# For testing purposes
green_box_width = 50
green_box_height = 50
green_box_x = window_width/2 - green_box_width/2
green_box_y = 377 - green_box_height
green_box = pygame.Rect(green_box_x, green_box_y, green_box_width,
                        green_box_height)

# For testing purposes
blue_box_width = 50
blue_box_height = 50
blue_box_x = window_width/2 - blue_box_width/2
blue_box_y = 0
blue_box = pygame.Rect(blue_box_x, blue_box_y, blue_box_width, blue_box_height)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    green_box_y -= 1
    blue_box_y += 1
    # For testing purposes
    if blue_box.colliderect(green_box):
        print("Collision")

    # Draw the objects
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 255, 0), green_box)
    pygame.draw.rect(screen, (0, 0, 255), blue_box)
    pygame.display.update()
    
    green_box = pygame.Rect(green_box_x, green_box_y, green_box_width,
                            green_box_height)
    blue_box = pygame.Rect(blue_box_x, blue_box_y, blue_box_width,
                           blue_box_height)

pygame.quit()
