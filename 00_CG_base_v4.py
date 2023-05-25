""" 00_CG_base_v4 by Sun Woo Yi
I added 04_Object_car_v3_testing_3 to 00_CG_base_v3
To reduce the lagging of the game, I used .convert_alpha()
20/05/23
"""

import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_width = 261
window_height = 377

# Create the window
screen = pygame.display.set_mode((window_width, window_height))
game_icon = pygame.image.load('game_icon.png').convert_alpha()
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Car Game - by Sun Woo Yi")
font = pygame.font.Font('freesansbold.ttf', 20)

# Have two sets of backgrounds for continuously moving background
background1 = pygame.image.load("Road2.png").convert_alpha()
background2 = pygame.image.load("Road2.png").convert_alpha()

# Set the initial positions of the images
background1_y = 0
background2_y = -window_height

# Load the player car image
PLAYER_CAR = pygame.transform.scale(pygame.image.load("car_1.png"), (30, 60)).convert_alpha()

# Changing the size of the object cars
object_car1 = pygame.transform.scale(pygame.image.load("car_2.png"), (30, 60)).convert_alpha()
object_car2 = pygame.transform.scale(pygame.image.load("car_3.png"), (30, 60)).convert_alpha()
object_car3 = pygame.transform.scale(pygame.image.load("car_4.png"), (30, 60)).convert_alpha()
object_car4 = pygame.transform.scale(pygame.image.load("car_5.png"), (30, 60)).convert_alpha()
object_car5 = pygame.transform.scale(pygame.image.load("car_6.png"), (30, 60)).convert_alpha()

cars = []  # list of active cars
spawn_timer = 0  # time until the next car should spawn
spawn_delay = 60  # time between car spawns (in frames)


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


class ObjectCar:
    def __init__(self, image, rect, velocity):
        self.image = image
        self.rect = rect
        self.velocity = velocity


player_car = PlayerCar()

# Create a sprite group for the player car
player_group = pygame.sprite.Group(player_car)


def update_position():
    global background1_y, background2_y
    # Makes the background move downwards (speed can change throughout)
    background1_y += 5
    background2_y += 5
    # Check if the first image has gone off the screen
    if background1_y >= window_height:
        background1_y = -window_height
    # Check if the second image has gone off the screen
    if background2_y >= window_height:
        background2_y = -window_height


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

    # Update the game state
    spawn_timer -= 1
    if spawn_timer <= 0 and len(cars) < 4:
        # Spawn a new car with a random velocity
        car_image = random.choice([object_car1, object_car2, object_car3, object_car4, object_car5])
        car_rect = car_image.get_rect()
        car_rect.top = 0 - car_rect.height
        car_velocity = random.randint(1, 5)

        # Generate a random x position that is not within 20 pixels of any existing car's x position
        while True:
            car_rect.left = random.randint(0, window_width - car_rect.width)
            if all(existing_car.rect.right + 20 < car_rect.left or car_rect.right + 20 < existing_car.rect.left for existing_car in cars):
                break

        cars.append(ObjectCar(car_image, car_rect, car_velocity))
        spawn_timer = spawn_delay

    # Move the cars down the screen with their individual velocities
    for car in cars:
        car.rect.top += car.velocity

    # Remove cars that have gone off the bottom of the screen
    cars = [car for car in cars if car.rect.bottom < window_height + 60]

    # Draw the background on the screen
    screen.blit(background1, (0, background1_y))
    screen.blit(background2, (0, background2_y))
    player_group.draw(screen)
    # Draw tha game objects
    for car in cars:
        screen.blit(car.image, car.rect)
    pygame.display.update()
    print(len(cars))
    clock.tick(60)


pygame.quit()
quit()
