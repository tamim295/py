import pygame
import requests
from io import BytesIO
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Car Game")

# Load car image
car_url = "https://img.freepik.com/free-photo/view-3d-car_23-2150796894.jpg?ga=GA1.1.1929962036.1702011717&semt=ais_ai_generated"
car_response = requests.get(car_url)
car_image = pygame.image.load(BytesIO(car_response.content))
car_width = 60
car_height = 120

# Load background image
background_url = "https://img.freepik.com/free-photo/road-leading-mountain-range-with-blue-sky-clouds_1340-26685.jpg?ga=GA1.1.1929962036.1702011717&semt=ais_ai_generated"
background_response = requests.get(background_url)
background_image = pygame.image.load(BytesIO(background_response.content))

# Set up the clock
clock = pygame.time.Clock()

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the initial position of the car
car_x = (window_width - car_width) // 2
car_y = window_height - car_height - 20
car_speed = 5

# Set up the initial position of the enemy car
enemy_width = 60
enemy_height = 120
enemy_x = random.randint(0, window_width - enemy_width)
enemy_y = -enemy_height
enemy_speed = 3

score = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= car_speed
    if keys[pygame.K_RIGHT]:
        car_x += car_speed

    # Update the positions of the car and the enemy
    car_rect = pygame.Rect(car_x, car_y, car_width, car_height)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
    enemy_y += enemy_speed

    # Check for collision
    if car_rect.colliderect(enemy_rect):
        running = False

    # Reset the enemy car position and increase the score if it reaches the bottom of the screen
    if enemy_y > window_height:
        enemy_x = random.randint(0, window_width - enemy_width)
        enemy_y = -enemy_height
        score += 1
        enemy_speed += 0.1

    # Clear the screen
    window.fill(white)

    # Draw the background image
    window.blit(background_image, (0, 0))

    # Draw the car
    window.blit(car_image, (car_x, car_y))

    # Draw the enemy car
    pygame.draw.rect(window, black, (enemy_x, enemy_y, enemy_width, enemy_height))

    # Display the score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, black)
    window.blit(text, (10, 10))

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)

# Game over
window.fill(white)
font = pygame.font.Font(None, 72)
text = font.render("Game Over", True, black)
window.blit(text, (window_width // 2 - text.get_width() // 2, window_height // 2 - text.get_height() // 2))
pygame.display.update()

# Wait for a few seconds before quitting
pygame.time.wait(2000)

# Quit the game
pygame.quit()