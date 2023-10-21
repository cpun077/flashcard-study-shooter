import pygame
import time
from guns.pistol import Pistol
from guns.projectile import Projectile
from resources.player import Player
from resources.ammo import Ammo
from resources.rock import Rock
from resources.tree import Tree
from resources.shield import Shield

pygame.init()

WIDTH = 1200
HEIGHT = 800

class Run:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("EduShoot")
        self.clock = pygame.time.Clock()
        self.player = Player(600, 400, 50, 50)



    def run(self):
        a = Ammo(500, 500, 20, 20)
        previous_time = time.perf_counter()
        running = True
        projs = []
        while running:
            delta_time = time.perf_counter() - previous_time
            previous_time = time.perf_counter()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill((255, 255, 255))
            self.player.weapon.set_angle()

            if (pygame.mouse.get_pressed()[0]):
                player_x, player_y = self.player.weapon.get_pos()
                temp_proj = Projectile(player_x, player_y, self.player.weapon.get_angle())
                projs.append(temp_proj)

            for proj in projs:
                proj.draw(self.screen, delta_time)
                

            self.player.weapon.draw(self.screen)
            self.player.update()

            self.screen.blit(self.player.img, self.player.rect)
            self.screen.blit(a.img, a.rect)
            # Flip the display
            pygame.display.flip()

            self.clock.tick(60)


        pygame.quit()

game = Run()
game.run()
