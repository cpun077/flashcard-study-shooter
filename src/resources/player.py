import pygame
from guns.pistol import Pistol
import math

class Player:
	def __init__(self, x, y, w, h):
		self.angle = 0
		self.x = x
		self.y = y
		self.ammo = 10
		self.speed = 3
		self.img = pygame.image.load("src/images/player.png")
		self.img = pygame.transform.smoothscale(self.img.convert_alpha(), (w, h))
		self.drawn_img = self.img
		self.rect = self.drawn_img.get_rect(center=(self.x, self.y))
		self.rotate_m = False
		self.rect = self.img.get_rect()
		self.rect.center = (self.x, self.y)
		self.weapon = Pistol(x, y)

	def set_angle(self):
		mouse = pygame.mouse.get_pos()
		xdiff = mouse[0] - self.x
		ydiff = mouse[1] - self.y
		self.angle = math.atan2(ydiff, xdiff)
		self.rotate_m = True

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

	def move(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP] or keys[pygame.K_w]:
			self.rect.y -= self.speed
			self.y -= self.speed
			self.nr = self.drawn_img.get_rect(center=(self.x, self.y))
			self.weapon.sety(-self.speed)
		if keys[pygame.K_DOWN] or keys[pygame.K_s]:
			self.rect.y += self.speed
			self.y += self.speed
			self.nr = self.drawn_img.get_rect(center=(self.x, self.y))
			self.weapon.sety(self.speed)
		if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
			self.rect.x += self.speed
			self.x += self.speed
			self.nr = self.drawn_img.get_rect(center=(self.x, self.y))
			self.weapon.setx(self.speed)
		if keys[pygame.K_LEFT] or keys[pygame.K_a]:
			self.rect.x -= self.speed
			self.x -= self.speed
			self.nr = self.drawn_img.get_rect(center=(self.x, self.y))
			self.weapon.setx(-self.speed)

	def update(self):
		self.move()