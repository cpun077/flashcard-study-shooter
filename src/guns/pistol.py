from guns.gun import Gun
import pygame

class Pistol(Gun):
    img = pygame.image.load("images/pistol.png")
    def __init__(self, x, y):
        self.fire_rate = 0.5
        super().__init__(x, y, self.img, 15, self.fire_rate)