""" 05_Collisions_v3 by Sun Woo Yi
This version will show a collision being detected between two objects
When the objects collide the user will be asked if they want to carry on
or quit.
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
font = pygame.font.Font('freesansbold.ttf', 15)


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
        # Stop the game
        running = False

        # Display the message
        screen.fill((255, 255, 255))
        text = font.render("Press 'r' to restart or 'q' to quit", True, (0, 0, 0))
        text_rect = text.get_rect(center=(window_width/2, window_height/2))
        screen.blit(text, text_rect)
        pygame.display.update()

        # Wait for user input
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        # Restart the game
                        green_box.rect.y = 377 - 50
                        blue_box.rect.y = 0
                        running = True
                        waiting = False
                    elif event.key == pygame.K_q:
                        # Quit the game
                        running = False
                        waiting = False

    # Draw the boxes
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()
