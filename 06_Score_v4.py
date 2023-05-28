""" 06_Score_v4 by Sun Woo Yi
This version will have a high score that will be saved everytime the
score is higher than the high score.
27/05/2023
"""

import pygame
import csv

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

# Set the start time and high score
start_time = pygame.time.get_ticks()
high_score = 0

# Load the high score from the CSV file if it exists
try:
    with open('high_score.csv', 'r') as file:
        reader = csv.reader(file)
        high_score = int(next(reader)[0])
except FileNotFoundError:
    pass

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

    # Update the high score if necessary
    if score > high_score:
        high_score = score
        with open('high_score.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([high_score])

    # Draw the sprites and score
    screen.fill((0, 0, 0))
    score_text = font.render("Score: {}".format(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    high_score_text = font.render("High Score: {}".format(high_score), True,
                                  (255, 255, 255))
    screen.blit(high_score_text, (10, 30))
    pygame.display.update()

    clock.tick(60)

# Clean up
pygame.quit()
