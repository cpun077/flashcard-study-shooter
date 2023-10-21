from guns.gun import Gun
import pygame

class Pistol(Gun):
    img = pygame.image.load("images/pistol.png")
    fire_rate = 0.5
    ammo = 15
    def __init__(self, x, y):
        super().__init__(x, y, self.img, self.ammo, self.fire_rate)