import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_width = 800
window_height = 600

# Create the window
screen = pygame.display.set_mode((window_width, window_height))

# Set the title of the window
pygame.display.set_caption("Car Game")

# Set up the car image and position
car_image = pygame.transform.scale(pygame.image.load("Assessment/Car Game/car_1.png"), (50, 50))
car_width = car_image.get_width()
car_height = car_image.get_height()
car_x = window_width/2 - car_width/2
car_y = window_height - car_height - 50

# Set up the road and obstacles
road_color = (50, 50, 50)
obstacle_color = (200, 0, 0)
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5
obstacle_x = random.randint(0, window_width - obstacle_width)
obstacle_y = -obstacle_height

# Set up the font for the score display
font = pygame.font.Font(None, 36)

# Set up the score
score = 0

# Set up the clock
clock = pygame.time.Clock()

# Start the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the car based on keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= 5
    if keys[pygame.K_RIGHT] and car_x < window_width - car_width:
        car_x += 5

    # Move the obstacles and check for collisions
    obstacle_y += obstacle_speed
    if obstacle_y > window_height:
        obstacle_x = random.randint(0, window_width - obstacle_width)
        obstacle_y = -obstacle_height
        score += 1
    if car_x < obstacle_x + obstacle_width and car_x + car_width > obstacle_x and car_y < obstacle_y + obstacle_height and car_y + car_height > obstacle_y:
        print("Collision!")
        pygame.quit()
        sys.exit()

    # Draw the road, car, and obstacles
    screen.fill(road_color)
    screen.blit(car_image, (car_x, car_y))
    pygame.draw.rect(screen, obstacle_color, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    # Draw the score
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)
