import random
from resources.ammo import Ammo
from resources.rock import Rock
from resources.tree import Tree
from resources.shield import Shield
import pygame
pygame.init()

WORLD_WIDTH, WORLD_HEIGHT = (10000, 10000)
class GameState:
	def __init__(self):
		self.ammo = []
		self.rocks = []
		self.shields = []
		self.trees = []
		self.ammo_size = 30
		self.rock_size = 110
		self.tree_size = 110
		self.shield_size = 50

	def initialize_random(self, num=1000):
		for i in range(num):
			rand_num = random.randint(1, 4)

			if(rand_num == 1):
				x = random.randint(1, WORLD_WIDTH)
				y = random.randint(1, WORLD_HEIGHT)
				while(self.colliding(x, y, self.ammo_size, self.ammo_size)):
					x = random.randint(1, WORLD_WIDTH)
					y = random.randint(1, WORLD_HEIGHT)
				self.ammo.append((x, y))

			elif(rand_num == 2):
				x = random.randint(1, WORLD_WIDTH)
				y = random.randint(1, WORLD_HEIGHT)
				while(self.colliding(x, y, self.tree_size, self.tree_size)):
					x = random.randint(1, WORLD_WIDTH)
					y = random.randint(1, WORLD_HEIGHT)
				self.trees.append((x, y))

			elif(rand_num == 3):
				x = random.randint(1, WORLD_WIDTH)
				y = random.randint(1, WORLD_HEIGHT)
				while(self.colliding(x, y, self.rock_size, self.rock_size)):
					x = random.randint(1, WORLD_WIDTH)
					y = random.randint(1, WORLD_HEIGHT)
				self.rocks.append((x, y))

			elif(rand_num == 4):
				x = random.randint(1, WORLD_WIDTH)
				y = random.randint(1, WORLD_HEIGHT)
				while(self.colliding(x, y, self.shield_size, self.shield_size)):
					x = random.randint(1, WORLD_WIDTH)
					y = random.randint(1, WORLD_HEIGHT)
				self.shields.append((x, y))

	def rect_collide(self, b1, b2):
		x1, y1, w1, h1 = b1
		x2, y2, w2, h2 = b2
		if (x1 < x2 + w2 and x1 + w1 > x2 and y1 < y2 + h2 and y1 + h1 > y2):
			return True

	def colliding(self, x, y, w, h):
		for x1, y1 in self.ammo:
			if(self.rect_collide((w, y, w, h), (x1, y1, self.ammo_size, self.ammo_size))):
				return True

		for x1, y1 in self.trees:
			if(self.rect_collide((w, y, w, h), (x1, y1, self.tree_size, self.tree_size))):
				return True

		for x1, y1 in self.rocks:
			if(self.rect_collide((w, y, w, h), (x1, y1, self.rock_size, self.rock_size))):
				return True

		for x1, y1 in self.shields:
			if(self.rect_collide((w, y, w, h), (x1, y1, self.shield_size, self.shield_size))):
				return True

	def encode_initial_data(self):
		t = []
		for x, y in self.trees:
			t.append(f"{x} {y}")

		r = []
		for x, y in self.rocks:
			r.append(f"{x} {y}")

		a = []
		for x, y in self.ammo:
			a.append(f"{x} {y}")

		s = []
		for x, y in self.shields:
			s.append(f"{x} {y}")

		return str([a, t, r, s])

	def send_myinfo(self, data):
		player, projectile = data
		p = [round(player.x), round(player.y), player.angle]
		proj = []
		for pr in projectile:
			proj.append([round(pr.x), round(pr.y), pr.angle])
		return str([p, proj])

	def get_xy(self, st):
		s = st.split()
		return int(s[0]), int(s[1])

	def decode_initial_data(self, data):
		data = eval(data)
		a = data[0]
		t = data[1]
		r = data[2]
		s = data[3]
		for ammo in a:
			x, y = self.get_xy(ammo)
			self.ammo.append(Ammo(x, y, self.ammo_size, self.ammo_size))
		for tree in t:
			x, y = self.get_xy(tree)
			self.trees.append(Tree(x, y, self.tree_size, self.tree_size))
		for rock in r:
			x, y = self.get_xy(rock)
			self.rocks.append(Rock(x, y, self.rock_size, self.rock_size))
		for shield in s:
			x, y = self.get_xy(shield)
			self.shields.append(Shield(x, y, self.shield_size, self.shield_size))


		
