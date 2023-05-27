""" 06_Score_v1 by Sun Woo Yi
This version will show a score being displayed on the top right corner 
of the screen
26/05/2023
"""

import pygame

pygame.init()

# Set the dimensions of the window
window_width = 261
window_height = 377

# Create the window
screen = pygame.display.set_mode((window_width, window_height))
game_icon = pygame.image.load('game_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Car Game - by Sun Woo Yi")
font = pygame.font.Font('freesansbold.ttf', 15)

# for testing purposes
running = True
while running:
    text = font.render("Score: ", True, (255, 255, 255))
    screen.blit(text, (10, 10))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

