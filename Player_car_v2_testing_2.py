import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_width = 261
window_height = 377

# Create the window
screen = pygame.display.set_mode((window_width, window_height))

# Load the player car image
PLAYER_CAR = pygame.transform.scale(pygame.image.load("Assessment/Car Game/car_1.png"), (20, 40))

# Create the player car sprite
class PlayerCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = PLAYER_CAR
        self.rect = self.image.get_rect(center=(window_width/2, window_height-50))

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-10, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(10, 0)
        self.rect.clamp_ip(screen.get_rect())

# Create the player car sprite
player_car = PlayerCar()

# Create a sprite group for the player car
player_group = pygame.sprite.Group(player_car)

# this is used here for testing purposes
clock = pygame.time.Clock()
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the player car
    player_car.update(pygame.key.get_pressed())

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the player car
    player_group.draw(screen)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
