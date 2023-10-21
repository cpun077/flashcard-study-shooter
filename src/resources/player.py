import pygame
from guns.pistol import Pistol
import math

WORLD_WIDTH, WORLD_HEIGHT = (10000, 10000)
WIDTH = 1200
HEIGHT = 800

class Player:
	def __init__(self, x, y, w, h):
		self.angle = 0
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.speed = 200
		self.img = pygame.image.load("images/player.png")
		self.img = pygame.transform.smoothscale(self.img.convert_alpha(), (w, h))
		self.drawn_img = self.img
		self.rotate_m = False
		self.rect = self.img.get_rect()
		self.weapon = Pistol(WIDTH / 2, HEIGHT / 2)
		self.x_offset = 0
		self.y_offset = 0
		self.dir_x = 0
		self.dir_y = 0

	def set_angle(self):
		mouse = pygame.mouse.get_pos()
		xdiff = mouse[0] - WIDTH / 2
		ydiff = mouse[1] - HEIGHT / 2
		self.angle = math.atan2(ydiff, xdiff)
		self.rotate_m = True

	def rot(self):
		rotImg = pygame.transform.rotozoom(self.img, -math.degrees(self.angle), 1)
		newR = rotImg.get_rect(center=self.img.get_rect(center=(WIDTH / 2, HEIGHT / 2)).center)
		self.rotate_m = False
		return rotImg, newR

	def draw(self, screen):
		if self.rotate_m:
			self.drawn_img, self.rect = self.rot()
			self.prev_angle = self.angle
			self.angle = 0
		screen.blit(self.drawn_img, self.rect)

	def move(self, dt):
		self.dir_x = 0
		self.dir_y = 0
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP] or keys[pygame.K_w]:
			if(self.y - self.speed >= 0):
				self.rect.y -= self.speed * dt
				self.y -= self.speed * dt
				self.y_offset -= self.speed * dt
				self.dir_y -= self.speed * dt

		if keys[pygame.K_DOWN] or keys[pygame.K_s]:
			if(self.y + self.speed <= WORLD_HEIGHT):	
				self.rect.y += self.speed * dt
				self.y += self.speed * dt
				self.y_offset += self.speed * dt
				self.dir_y += self.speed * dt

		if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
			if(self.x + self.speed <= WORLD_WIDTH):
				self.rect.x += self.speed * dt
				self.x += self.speed * dt
				self.x_offset += self.speed * dt
				self.dir_x += self.speed * dt

		if keys[pygame.K_LEFT] or keys[pygame.K_a]:
			if(self.x - self.speed >= 0):
				self.rect.x -= self.speed * dt
				self.x -= self.speed * dt
				self.x_offset -= self.speed * dt
				self.dir_x -= self.speed * dt

	def update(self, dt):
		self.move(dt)

	def get_rect(self):
		return pygame.Rect(self.x, self.y, self.w, self.h)