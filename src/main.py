# Simple pygame program

# Import and initialize the pygame library
import pygame
import time
from guns.pistol import Pistol
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

clock = pygame.time.Clock()
test= Pistol(100, 100)

# Run until the user asks to quit
running = True
previous_time = time.perf_counter()
while running:

    delta_time = time.perf_counter() - previous_time
    previous_time = time.perf_counter()
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    screen.blit(test.get_img(), test.get_pos())

    # Flip the display
    pygame.display.flip()

    clock.tick(60)

# Done! Time to quit.
pygame.quit()