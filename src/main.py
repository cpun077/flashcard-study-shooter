# Simple pygame program

# Import and initialize the pygame library
import pygame
import time
from guns.pistol import Pistol
from guns.projectile import Projectile
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

clock = pygame.time.Clock()
test= Pistol(100, 100)
projs = []

# Run until the user asks to quit
running = True
previous_time = time.perf_counter()
while running:

    delta_time = time.perf_counter() - previous_time
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    test.set_angle()

    if (pygame.mouse.get_pressed()[0]):
        playerx,playery = test.get_pos()
        temp_proj = Projectile(playerx, playery, test.get_angle())
        projs.append(temp_proj)

    for proj in projs:
        proj.draw(screen, delta_time)
        

    test.draw(screen)

    # Flip the display
    pygame.display.flip()

    previous_time = time.perf_counter()
    clock.tick(60)

# Done! Time to quit.
pygame.quit()