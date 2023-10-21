import pygame
from guns.pistol import Pistol

class Player:
	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.weapon = Pistol(x, y)
		self.ammo = 10
		self.speed = 3
		self.img = pygame.image.load("images/player.png")
		self.img = pygame.transform.smoothscale(self.img.convert_alpha(), (w, h))
		self.rect = self.img.get_rect()
		self.rect.center = (self.x, self.y)

	def move(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP] or keys[pygame.K_w]:
			self.rect.y -= self.speed
		if keys[pygame.K_DOWN] or keys[pygame.K_s]:
			self.rect.y += self.speed
		if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
			self.rect.x += self.speed
		if keys[pygame.K_LEFT] or keys[pygame.K_a]:
			self.rect.x -= self.speed

	def update(self):
		self.move()