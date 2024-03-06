import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Move the Circle")

# Circle properties
circle_color = white
circle_radius = 20
circle_x = screen_width // 2
circle_y = screen_height // 2
circle_speed = 5

# Obstacle properties
obstacles = [
    pygame.Rect(200, 150, 100, 50),  # Example obstacle
    # Add more obstacles as needed
]

# Goal properties
goal_color = (0, 255, 0)  # Green
goal_position = (700, 500)  # Example position
goal_radius = 30


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key press detection
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        circle_x = max(circle_radius, circle_x - circle_speed)
    if keys[pygame.K_RIGHT]:
        circle_x = min(screen_width - circle_radius, circle_x + circle_speed)
    if keys[pygame.K_UP]:
        circle_y = max(circle_radius, circle_y - circle_speed)
    if keys[pygame.K_DOWN]:
        circle_y = min(screen_height - circle_radius, circle_y + circle_speed)
   
    # Fill the screen with black
    screen.fill(black)

    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, white, obstacle)

    # Draw the goal
    pygame.draw.circle(screen, goal_color, goal_position, goal_radius)

    # Draw the circle
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)

    # Check for collision with obstacles
    player_rect = pygame.Rect(circle_x - circle_radius, circle_y - circle_radius, circle_radius * 2, circle_radius * 2)
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            print("Collision with obstacle!")  # Handle collision

    # Check for reaching the goal
    if player_rect.collidepoint(goal_position):
        print("Goal reached!")  # Handle reaching the goal

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()