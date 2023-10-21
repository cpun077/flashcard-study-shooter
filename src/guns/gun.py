import pygame
import math
from guns.projectile import Projectile

class Gun: 
    def __init__(self, x, y, img, ammo_cap, fire_rate):
        self.x = x
        self.y = y
        self.id = 'gun'
        self.img = img
        self.drawn_img = img
        self.ammo_cap = ammo_cap
        self.ammo = ammo_cap
        self.angle = 0
        self.prev_angle = 0
        self.fire_rate = fire_rate
        self.nr = self.drawn_img.get_rect(center=(self.x, self.y))
        self.rotate_m = False
        self.time_since_fire = 0

    def increase_time(self, dt):
        self.time_since_fire += dt

    def can_shoot(self):
        if(self.time_since_fire >= self.fire_rate):
            self.time_since_fire = 0
        else:
            return False

        if(self.ammo > 0):
            self.ammo -= 1
        else:
            return False
        return True

    def set_angle(self, player):
        mouse = pygame.mouse.get_pos()
        xdiff = mouse[0] - self.x
        ydiff = mouse[1] - self.y
        self.angle = math.atan2(ydiff, xdiff)
        self.rotate_m = True
        #self.x = self.x + player.get_width() * math.cos(self.angle)
        #self.y = self.y + player.get_height() * math.sin(self.angle)

    def rot(self):
        rotImg = pygame.transform.rotozoom(self.img, -math.degrees(self.angle), 1)
        newR = rotImg.get_rect(center=self.img.get_rect(center=(self.x, self.y)).center)
        self.rotate_m = False
        return rotImg, newR

    def draw(self, screen):
        if self.rotate_m:
            self.drawn_img, self.nr = self.rot()
            self.prev_angle = self.angle
            self.angle = 0
        screen.blit(self.drawn_img, self.nr)
    
    def setx(self, distance):
        self.x += distance
        self.nr = self.drawn_img.get_rect(center=(self.x, self.y))

    def sety(self, distance):
        self.y += distance
        self.nr = self.drawn_img.get_rect(center=(self.x, self.y))


    def get_angle(self):
        return(self.angle)

    def reload(self):
        self.ammo = self.ammo_cap

    def get_img(self):
        return self.img
    
    def get_pos(self):
        return (self.x, self.y)
    
    def get_fire_rate(self):
        return(self.fire_rate)