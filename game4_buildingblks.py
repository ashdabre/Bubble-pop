import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Bubble Pop")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

# Define bubble parameters
bubble_radius = 20
bubble_speeds = {"easy": 1, "medium": 2, "hard": 3}

# Font
font_style = pygame.font.SysFont(None, 50)

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Function to draw bubble
def draw_bubble(x, y):
    pygame.draw.circle(window, blue, (x, y), bubble_radius)

# Function to display level
def display_level(level):
    level_text = font_style.render("Level: " + level, True, black)
    window.blit(level_text, [10, 10])

# Function to display score
def display_score(score):
    score_text = font_style.render("Score: " + str(score), True, black)
    window.blit(score_text, [window_width - 200, 10])

# Function to display game over message
def game_over_message(score):
    message = font_style.render("Game Over! Score: " + str(score), True, black)
    window.blit(message, [window_width // 3, window_height // 3])

# Main game loop
def game_loop(level):
    global bubbles  # Declare bubbles as global
    score = 0
    bubble_speed = bubble_speeds[level]
    bubbles = []  # Define bubbles inside the loop

    while True:
        window.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for bubble in bubbles:
                    if ((bubble[0] - mouse_x) ** 2 + (bubble[1] - mouse_y) ** 2) ** 0.5 <= bubble_radius:
                        score += 1
                        bubbles.remove(bubble)

        # Generate new bubbles
        if len(bubbles) < 10:
            bubble_x = random.randint(bubble_radius, window_width - bubble_radius)
            bubble_y = random.randint(bubble_radius, window_height - bubble_radius)
            bubbles.append([bubble_x, bubble_y])

        # Draw bubbles and move them up
        for bubble in bubbles:
            draw_bubble(bubble[0], bubble[1])
            bubble[1] -= bubble_speed

        # Remove bubbles that go above the screen
        bubbles = [bubble for bubble in bubbles if bubble[1] > 0]

        # Display level and score
        display_level(level)
        display_score(score)

        # Check game over condition
        if score >= 10:
            game_over_message(score)
            pygame.display.update()
            pygame.time.wait(2000)
            return

        # Update display
        pygame.display.update()

        # Control frame rate
        clock.tick(60)

# Start the game
game_loop("easy")
