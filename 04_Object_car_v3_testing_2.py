""" 04_Object_car_v3_testing_2 by Sun Woo Yi
In this version of the component, the cars will spawn at 
random positions on the top of the screen and will start to move down at 
different speeds
23/05/23
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
object_car1 = pygame.transform.scale(pygame.image.load("car_2.png"), (20, 40)).convert_alpha()
object_car2 = pygame.transform.scale(pygame.image.load("car_3.png"), (20, 40)).convert_alpha()
object_car3 = pygame.transform.scale(pygame.image.load("car_4.png"), (20, 40)).convert_alpha()
object_car4 = pygame.transform.scale(pygame.image.load("car_5.png"), (20, 40)).convert_alpha()
object_car5 = pygame.transform.scale(pygame.image.load("car_6.png"), (20, 40)).convert_alpha()


# Set up the initial state of the game
cars = []  # list of active cars
spawn_timer = 0  # time until the next car should spawn
spawn_delay = 60  # time between car spawns (in frames)
clock = pygame.time.Clock()

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Update the game state
    spawn_timer -= 1
    if spawn_timer <= 0 and len(cars) < 4:
        # Spawn a new car with a random velocity
        car_image = random.choice([object_car1, object_car2, object_car3, object_car4, object_car5])
        car_y = 0 - car_image.get_height()
        car_velocity = random.randint(1, 5)

        # Generate a random x position that is not within 20 pixels of any existing car's x position
        while True:
            car_x = random.randint(0, window_width - car_image.get_width())
            if all(abs(car_x - existing_car[1]) > 20 for existing_car in cars):
                break

        cars.append((car_image, car_x, car_y, car_velocity))
        spawn_timer = spawn_delay


    # Move the cars down the screen with their individual velocities
    for i in range(len(cars)):
        car_image, car_x, car_y, car_velocity = cars[i]
        car_y += car_velocity
        cars[i] = (car_image, car_x, car_y, car_velocity)

    # Remove cars that have gone off the bottom of the screen
    cars = [car for car in cars if car[2] < window_height]

    # Draw the game objects
    screen.fill((255, 255, 255))
    for car in cars:
        car_image, car_x, car_y, car_velocity = car
        screen.blit(car_image, (car_x, car_y))
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)