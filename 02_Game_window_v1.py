""" 02_Game_window_v1 by Sun Woo Yi
In this component version I will be naming the window and changing the 
game icon
15/05/2023
"""

import pygame

pygame.init()

# Set the dimensions of the window
window_width = 261
window_height = 377

# Create the window
screen = pygame.display.set_mode((window_width, window_height))
game_icon = pygame.image.load('Assessment/Car Game/game_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Car Game - by Sun Woo Yi")
font = pygame.font.Font(None, 20)

# for testing purposes
running = True
while running:
    text = font.render("Testing", True, (255, 255, 255))
    screen.blit(text, (10, 10))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
