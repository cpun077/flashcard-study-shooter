import sys
import pygame
import time
import threading
import math
from guns.pistol import Pistol
from guns.projectile import Projectile
from resources.player import Player
from resources.ammo import Ammo
from resources.rock import Rock
from resources.tree import Tree
from resources.shield import Shield
from GameState import GameState
from network.client import Client


pygame.init()
WORLD_WIDTH, WORLD_HEIGHT = (10000, 10000)

WIDTH = 1200
HEIGHT = 800

PLAYER_W = 75
PLAYER_H = 75
class Run:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("EduShoot")
        self.clock = pygame.time.Clock()
        self.player = Player(2000, 2000, PLAYER_W, PLAYER_H)
        self.bg = pygame.image.load("images/green_background.png").convert()
        self.bg = pygame.transform.smoothscale(self.bg, (WIDTH, HEIGHT))
        self.loading = pygame.image.load("images/loading.png").convert()
        self.loading = pygame.transform.smoothscale(self.loading, (WIDTH, HEIGHT))
        self.screen.blit(self.loading, (0, 0))
        pygame.display.flip()
        self.localx = 0
        self.localy = 0
        self.client = Client(sys.argv[1])
        self.client.start()
        self.opp_queue = []
        self.game_state = GameState()
        self.game_state.decode_initial_data(self.client.recv())

        self.game_info_thread = threading.Thread(target=self.get_info)
        self.game_info_thread.start()

        #self.bg = self.background

        self.b_img = pygame.image.load("images/bullet.png").convert_alpha()
        self.b_img = pygame.transform.smoothscale(
            self.b_img, (self.b_img.get_width() * 0.4, self.b_img.get_height() * 0.4)
        )
        self.projectiles = []

    def shoot_bullets(self):
        self.player.weapon.set_angle(self.player)
        self.player.set_angle()
        for event in self.events:
            if (pygame.mouse.get_pressed()[0]):

                player_x, player_y = self.player.weapon.get_pos()
                if(self.player.weapon.can_shoot()):
                    temp_proj = Projectile(player_x, player_y, self.player.weapon.get_angle(), self.player.x, self.player.y)
                    self.projectiles.append(temp_proj)

    def render_projectiles(self, delta_time):
        for proj in self.projectiles:
            proj.draw(self.screen, delta_time)

    def kill_objects(self):
        for i in range(len(self.projectiles)):
            if self.projectiles[i].projectile_dead():
                self.projectiles[i] = 0
        while 0 in self.projectiles:
            self.projectiles.remove(0)
        if(self.player.health <= 0):
            print("YOU DIED")
            return -1

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

    def draw_bar(self, pos=(WIDTH / 2 - 40, HEIGHT / 2 - 40), size = (PLAYER_W, 15), borderC=(0, 0, 0), barC=(0, 255, 0), progress=1):

        pygame.draw.rect(self.screen, borderC, (*pos, *size), 1)
        innerPos  = (pos[0]+3, pos[1]+3)
        innerSize = ((size[0]-6) * progress, size[1]-6)
        pygame.draw.rect(self.screen, barC, (*innerPos, *innerSize))

    def display_stuff(self):
        for opp_state in self.opp_queue:
            player = opp_state[0]
            projectiles = opp_state[1]
            if player:
                x, y, angle, h = player
                p_img = self.player.img
                rotImg = pygame.transform.rotozoom(p_img, -math.degrees(angle), 1)
                screenx = x - self.player.x + WIDTH / 2
                screeny = y - self.player.y + HEIGHT / 2
                newR = rotImg.get_rect(center=p_img.get_rect(center=(screenx, screeny)).center)
                self.screen.blit(rotImg, newR)
                self.draw_bar(pos=(screenx - 40, screeny - 40), progress=h/100)

            for projectile in projectiles:
                x, y, angle = projectile
                b_img = self.b_img
                rotImg = pygame.transform.rotozoom(b_img, -math.degrees(angle), 1)
                newR = rotImg.get_rect(center=b_img.get_rect(center=(x - self.player.x + WIDTH / 2, y - self.player.y + HEIGHT / 2)).center)
                b_rec = pygame.Rect(x, y, b_img.get_width(), b_img.get_height())
                if(self.player.get_rect().colliderect(b_rec)):
                    self.player.health -= 1
                self.screen.blit(rotImg, newR)
        self.opp_queue = self.opp_queue[-2:]

    def render_game_state(self):
        for ammo in self.game_state.ammo:
            if (ammo.x > self.player.x - WIDTH/1.5 and ammo.x < self.player.x + WIDTH/1.5 and ammo.y < self.player.y + HEIGHT/1.5 and ammo.y > self.player.y - HEIGHT/1.5):
                self.screen.blit(ammo.img, (ammo.x - self.player.x + WIDTH / 2 - ammo.w / 2, ammo.y - self.player.y + HEIGHT / 2 - ammo.h / 2))
        for rock in self.game_state.rocks:
            if (rock.x > self.player.x - WIDTH/1.5 and rock.x < self.player.x + WIDTH/1.5 and rock.y < self.player.y + HEIGHT/1.5 and rock.y > self.player.y - HEIGHT/1.5):
                self.screen.blit(rock.img, (rock.x - self.player.x + WIDTH / 2 - rock.w / 2, rock.y - self.player.y + HEIGHT / 2 - rock.h / 2))
        for shield in self.game_state.shields:
            if (shield.x > self.player.x - WIDTH/1.5 and shield.x < self.player.x + WIDTH/1.5 and shield.y < self.player.y + HEIGHT/1.5 and shield.y > self.player.y - HEIGHT/1.5):
                self.screen.blit(shield.img, (shield.x - self.player.x + WIDTH / 2 - shield.w / 2, shield.y - self.player.y + HEIGHT / 2 - shield.h / 2))
        for tree in self.game_state.trees:
            if (tree.x > self.player.x - WIDTH/1.5 and tree.x < self.player.x + WIDTH/1.5 and tree.y < self.player.y + HEIGHT/1.5 and tree.y > self.player.y - HEIGHT/1.5):
                self.screen.blit(tree.img, (tree.x - self.player.x + WIDTH / 2 - tree.w / 2, tree.y - self.player.y + HEIGHT / 2 - tree.h / 2))

    def ammo_shield(self):
        for i, ammo in enumerate(self.game_state.ammo):
            if (self.player.get_rect().colliderect(pygame.Rect(ammo.x, ammo.y, self.game_state.ammo_size, self.game_state.ammo_size))):
                correct = self.player.quiz(self.screen)
                if (correct):
                    self.game_state.ammo[i] = 0
                    self.player.weapon.ammo += 15
        self.game_state.ammo = list(filter(lambda a: a != 0, self.game_state.ammo))
        for i, shield in enumerate(self.game_state.shields):
            if (self.player.get_rect().colliderect(pygame.Rect(shield.x, shield.y, self.game_state.ammo_size, self.game_state.ammo_size))):
                correct = self.player.quiz(self.screen)
                if (correct):
                    self.game_state.shields[i] = 0
                    self.player.health += 100
        self.game_state.shields = list(filter(lambda a: a != 0, self.game_state.shields))

    def get_info(self):
        while True:
            try:
                data = self.client.recv()
                if not data:
                    print("bad")
                    continue
                while (data.find("]][[") != -1):
                    index = data.find("]][[")
                    self.opp_queue.append(eval(data[:(index+ 2)]))
                    data = data[(index + 2):]
                self.opp_queue.append(eval(data))
            except Exception as e:
                print("This:", e)
                print("next:", data)
                print("\n")
                continue

    def run(self):
        previous_time = time.perf_counter()
        running = True
        while running:
            self.events = pygame.event.get()
            delta_time = time.perf_counter() - previous_time
            previous_time = time.perf_counter()
            self.player.weapon.increase_time(delta_time)

            self.render_background()
            for event in self.events:
                if event.type == pygame.QUIT:
                    running = False
            self.player.weapon.set_angle(self.player)
            self.player.set_angle()

            self.shoot_bullets()
            self.render_projectiles(delta_time)
            self.player.update(delta_time)
            self.client.send(self.game_state.send_myinfo([self.player, self.projectiles]))

            self.player.draw(self.screen)
            self.ammo_shield()
            self.draw_bar(progress=self.player.health/100)
            self.player.weapon.draw(self.screen)
            self.render_game_state()
            self.display_stuff()
            a = self.kill_objects()
            if a == -1:
                running = False

            pygame.display.flip()

            self.clock.tick(60)

        pygame.display.quit()
        pygame.quit()

game = Run()
game.run()
