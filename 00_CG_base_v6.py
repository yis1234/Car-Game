""" 00_CG_base_v6 by Sun Woo Yi
I added 05_Collisions_v3 to the 00_CG_base_v5
27/05/23
"""

import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the window and create it
WINDOW_WIDTH = 261
WINDOW_HEIGHT = 377
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Car Game - by Sun Woo Yi")
game_icon = pygame.image.load('game_icon.png').convert_alpha()
pygame.display.set_icon(game_icon)
font = pygame.font.Font('freesansbold.ttf', 15)


# Load the images
PLAYER_CAR_IMAGE = pygame.image.load("car_1.png").convert_alpha()
OBJECT_CAR_IMAGES = [
    pygame.image.load("car_2.png").convert_alpha(),
    pygame.image.load("car_3.png").convert_alpha(),
    pygame.image.load("car_4.png").convert_alpha(),
    pygame.image.load("car_5.png").convert_alpha(),
    pygame.image.load("car_6.png").convert_alpha(),
]
BACKGROUND_IMAGE = pygame.image.load("Road2.png").convert_alpha()

# Set up the initial positions and properties of the objects
BACKGROUND_Y = 0
PLAYER_CAR_X = WINDOW_WIDTH // 2
PLAYER_CAR_Y = WINDOW_HEIGHT - 100
OBJECT_CAR_WIDTH = 30
OBJECT_CAR_HEIGHT = 60
MAX_OBJECT_CARS = 4


# Create the player car sprite
class PlayerCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale\
        (PLAYER_CAR_IMAGE, (OBJECT_CAR_WIDTH, OBJECT_CAR_HEIGHT))
        self.rect = self.image.get_rect(center=(PLAYER_CAR_X, PLAYER_CAR_Y))

    def update(self, key):
        if key[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if key[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)
        self.rect.clamp_ip(screen.get_rect())


# Create the object car sprite
class ObjectCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale\
        (random.choice(OBJECT_CAR_IMAGES), (OBJECT_CAR_WIDTH,
                                            OBJECT_CAR_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.top = 0 - self.rect.height
        self.rect.left = random.randint(0, WINDOW_WIDTH - OBJECT_CAR_WIDTH)
        while any(abs(self.rect.left - objCar.rect.left) < 30 for objCar in
                  object_car_group):
            self.rect.left = random.randint(0, WINDOW_WIDTH - OBJECT_CAR_WIDTH)
        self.velocity = random.randint(1, 5)

    def update(self):
        self.rect.top += self.velocity
        if self.rect.top >= WINDOW_HEIGHT:
            self.kill()


# Create sprite groups for the player car and object cars
player_car = PlayerCar()
player_group = pygame.sprite.Group(player_car)
object_car_group = pygame.sprite.Group()

# Keep the game running until the user closes it
clock = pygame.time.Clock()
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Handle player input
    keys = pygame.key.get_pressed()
    player_car.update(keys)

    # Check for collisions between the player car and object cars
    if pygame.sprite.groupcollide(player_group, object_car_group, False,
                                  False):
        running = False

        # Wait for user input
        waiting = True
        while waiting:
            # Display the message
            screen.fill((255, 255, 255))
            text = font.render("Press 'r' to restart or 'q' to quit", True,
                               (0, 0, 0))
            text_rect = text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
            screen.blit(text, text_rect)
            pygame.display.update()

            # Handle user input
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        # Restart the game
                        running = True
                        waiting = False

                        # Reset the object cars and the game background
                        object_car_group.empty()
                        BACKGROUND_Y = 0

                        # Create the player car sprite
                        player_car = PlayerCar()

                        # Create sprite groups for the player car and
                        # object cars
                        player_group = pygame.sprite.Group(player_car)
                        object_car_group = pygame.sprite.Group()

                        # Draw the game background and the player car
                        screen.blit(BACKGROUND_IMAGE, (0, BACKGROUND_Y))
                        player_group.draw(screen)
                        pygame.display.update()
                    elif event.key == pygame.K_q:
                        # Quit the game
                        running = False
                        waiting = False

    if len(object_car_group) < MAX_OBJECT_CARS:
        object_car_group.add(ObjectCar())
    for obj_car in object_car_group:
        obj_car.rect.top += obj_car.velocity
        if obj_car.rect.top >= WINDOW_HEIGHT:
            obj_car.kill()

    # Update the game display
    screen.blit(BACKGROUND_IMAGE, (0, BACKGROUND_Y))
    screen.blit(BACKGROUND_IMAGE, (0, BACKGROUND_Y - WINDOW_HEIGHT))
    BACKGROUND_Y += 5
    if BACKGROUND_Y >= WINDOW_HEIGHT:
        BACKGROUND_Y = 0
    player_group.draw(screen)
    object_car_group.draw(screen)
    pygame.display.update()

    # Wait for the next frame
    clock.tick(60)

# Clean up
pygame.quit()
