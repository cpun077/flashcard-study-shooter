import pygame
import math
from guns.projectile import Projectile

class Gun: 
    def __init__(self, x, y, img, ammo_cap, fire_rate):
        self.x = x
        self.y = y
        self.id = 'gun'
        self.img = img
        self.ammo_cap = ammo_cap
        self.ammo = ammo_cap
        self.angle = 0
        self.fireRate = fire_rate

    def shoot(self):
        if (pygame.mouse.get_pressed):
            delta = pygame.mouse.get_pos - pygame.Vector2(self.x, self.y)
            angle = math.atan2(delta.y, delta.x)
            self.ammo -= self.ammo
            return (angle)

    def reload(self):
        self.ammo = self.ammo_cap

    def get_img(self):
        return self.img
    
    def get_pos(self):
        return (self.x, self.y)