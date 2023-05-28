""" 06_Score_v3 by Sun Woo Yi
This version will show the score being reset to 0 when r is pressed
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
clock = pygame.time.Clock()

# Set the start time
start_time = pygame.time.get_ticks()

# for testing purposes
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                start_time = pygame.time.get_ticks()  # Reset the start time

    # Calculate the elapsed time and score
    elapsed_time = pygame.time.get_ticks() - start_time
    score = int(elapsed_time / 1000)  # Convert milliseconds to seconds

    # Draw the sprites and score
    screen.fill((0, 0, 0))
    score_text = font.render("Score: {}".format(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.update()

    clock.tick(60)
