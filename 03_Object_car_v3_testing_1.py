""" 03_Object_car_v3_testing_1 by Sun Woo Yi
In this version of the component, the cars will spawn at 
random positions on the top of the screen
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

# Changing the size of the object cars
object_car1 = pygame.transform.scale(pygame.image.load("Assessment/Car Game/car_2.png"), (20, 40))
object_car2 = pygame.transform.scale(pygame.image.load("Assessment/Car Game/car_3.png"), (20, 40))
object_car3 = pygame.transform.scale(pygame.image.load("Assessment/Car Game/car_4.png"), (20, 40))
object_car4 = pygame.transform.scale(pygame.image.load("Assessment/Car Game/car_5.png"), (20, 40))
object_car5 = pygame.transform.scale(pygame.image.load("Assessment/Car Game/car_6.png"), (20, 40))

velocity = random.randint(1, 5)
y_pos = 0
y_change = velocity


# Set up the initial state of the game
cars = []  # list of active cars
spawn_timer = 0  # time until the next car should spawn
spawn_delay = 60  # time between car spawns (in frames)

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Update the game state
    spawn_timer -= 1
    if spawn_timer <= 0:
        # Spawn a new car
        car_image = random.choice([object_car1, object_car2, object_car3, object_car4, object_car5])
        car_x = random.randint(0, window_width - car_image.get_width())
        car_y = 0 - car_image.get_height()
        cars.append((car_image, car_x, car_y))
        spawn_timer = spawn_delay

    # Move the cars down the screen
    for i in range(len(cars)):
        car_image, car_x, car_y = cars[i]
        car_y += velocity
        cars[i] = (car_image, car_x, car_y)

    # Remove cars that have gone off the bottom of the screen
    cars = [car for car in cars if car[2] < window_height]

    # Draw the game objects
    screen.fill((0, 0, 0))
    for car in cars:
        car_image, car_x, car_y = car
        screen.blit(car_image, (car_x, car_y))
    pygame.display.update()
