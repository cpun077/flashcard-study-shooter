import pygame
from guns.pistol import Pistol
import math
import flashcards.mcgen
import flashcards.samplesets
import random 

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
		self.health = 100
		self.max_health = 100

		self.flashsets = flashcards.samplesets.sampleSet()
		random.shuffle(self.flashsets)
		self.currentquiz = flashcards.mcgen.createQuiz(random.choice(self.flashsets))
		self.qcount = 0
		self.displayq = False
		self.takinganswers = False

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
			
	def quiz(self, screen):
		# temporarily a keybind
		if (self.qcount < len(self.currentquiz)-1):
			self.displayq = not self.displayq
			self.takinganswers = True
			if (self.displayq):
				font = pygame.font.Font('freesansbold.ttf', 32)
				qtext = font.render(self.currentquiz[self.qcount]["question"], True, (105, 105, 105), None)
				qRect = pygame.Rect(WIDTH/2-qtext.get_width()/2, 20, qtext.get_width(), qtext.get_height())
				screen.blit(qtext, qRect)
				a1text = font.render(self.currentquiz[self.qcount]["answeroptions"][0]["option"], True, (105, 105, 105), None)
				a1Rect = pygame.Rect(20, qRect.top+qRect.height+20, qtext.get_width(), qtext.get_height())
				screen.blit(a1text, a1Rect)
				a2text = font.render(self.currentquiz[self.qcount]["answeroptions"][1]["option"], True, (105, 105, 105), None)
				a2Rect = pygame.Rect(20, a1Rect.top+a1Rect.height+20, qtext.get_width(), qtext.get_height())
				screen.blit(a2text, a2Rect)
				a3text = font.render(self.currentquiz[self.qcount]["answeroptions"][2]["option"], True, (105, 105, 105), None)
				a3Rect = pygame.Rect(20, a2Rect.top+a2Rect.height+20, qtext.get_width(), qtext.get_height())
				screen.blit(a3text, a3Rect)
				a4text = font.render(self.currentquiz[self.qcount]["answeroptions"][3]["option"], True, (105, 105, 105), None)
				a4Rect = pygame.Rect(20, a3Rect.top+a3Rect.height+20, qtext.get_width(), qtext.get_height())
				screen.blit(a4text, a4Rect)

				if (self.takinganswers and pygame.mouse.get_pressed()[0]):
					self.takinganswers = False
					self.qcount +=1
					if(a1Rect.collidepoint(pygame.mouse.get_pos())):
						return self.currentquiz[self.qcount]["answeroptions"][0]["isCorrect"]
					if(a2Rect.collidepoint(pygame.mouse.get_pos())):
						return self.currentquiz[self.qcount]["answeroptions"][1]["isCorrect"]
					if(a3Rect.collidepoint(pygame.mouse.get_pos())):
						return self.currentquiz[self.qcount]["answeroptions"][2]["isCorrect"]
					if(a4Rect.collidepoint(pygame.mouse.get_pos())):
						return self.currentquiz[self.qcount]["answeroptions"][3]["isCorrect"]


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
	
	def get_width(self):
		return self.w
	
	def get_height(self):
		return self.h