from guns.gun import Gun
import pygame

class Pistol(Gun):
    img = pygame.image.load("src/images/pistol.png")
    def __init__(self, x, y):
        super().__init__(x, y, self.img, 15, 500)