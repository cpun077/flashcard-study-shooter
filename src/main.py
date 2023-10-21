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
WORLD_WIDTH, WORLD_HEIGHT = (10000, 10000)

WIDTH = 1200
HEIGHT = 800

class Run:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("EduShoot")
        self.clock = pygame.time.Clock()
        self.player = Player(9500, 9500, 50, 50)
        self.bg = pygame.image.load("images/green_background.png").convert()
        self.bg = pygame.transform.smoothscale(self.bg, (WIDTH, HEIGHT))
        self.screen.blit(self.bg, (0, 0))
        self.localx = 0
        self.localy = 0
        #self.bg = self.background


        self.projectiles = []

    def shoot_bullets(self):
        self.player.weapon.set_angle()
        self.player.set_angle()

        if (pygame.mouse.get_pressed()[0]):
            player_x, player_y = self.player.weapon.get_pos()
            if(self.player.weapon.can_shoot()):
                temp_proj = Projectile(player_x, player_y, self.player.weapon.get_angle())
                self.projectiles.append(temp_proj)

    def render_projectiles(self, delta_time):
        for proj in self.projectiles:
            proj.draw(self.screen, delta_time)

    # inspired by Steve Paget pygame functions
    def render_background(self):
        self.localx += self.player.dir_x
        self.localy += self.player.dir_y
        xOff = (0 - self.localx % WIDTH)
        yOff = (0 - self.localy % HEIGHT)

        self.screen.blit(self.bg, (xOff, yOff))
        self.screen.blit(self.bg, (xOff + WIDTH, yOff))
        self.screen.blit(self.bg, (xOff, yOff + HEIGHT))
        self.screen.blit(self.bg, (xOff + WIDTH, yOff + HEIGHT))

    def keep_inbounds(self):
        if(self.player.x < 0):
            self.player.x += self.player.speed
        if(self.player.x > WORLD_WIDTH):
            self.player.x -= self.player.speed
        if(self.player.y < 0):
            self.player.y += self.player.speed
        if(self.player.y > WORLD_HEIGHT):
            self.player.y -= self.player.speed

    def run(self):
        a = Tree(20, 20, 70, 70)
        previous_time = time.perf_counter()
        running = True
        while running:
            print(self.player.x, self.player.y)
            delta_time = time.perf_counter() - previous_time
            previous_time = time.perf_counter()
            self.player.weapon.increase_time(delta_time)
            #self.screen.blit(self.bg, (x - self.player.x_offset, y - self.player.y_offset))
            #self.screen.blit(self.bg, (x1 - self.player.x_offset, y1 - self.player.y_offset))

            self.render_background()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


            self.shoot_bullets()
            self.render_projectiles(delta_time)
            self.player.update()
            self.keep_inbounds()

            self.player.draw(self.screen)
            self.player.weapon.draw(self.screen)

            self.screen.blit(a.img, (a.rect.x - self.player.x_offset, a.rect.y - self.player.y_offset))
            pygame.display.flip()

            self.clock.tick(60)


        pygame.quit()

game = Run()
game.run()
