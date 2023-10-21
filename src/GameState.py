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
				ammo = Ammo(random.randint(1, WORLD_WIDTH), random.randint(1, WORLD_WIDTH), self.ammo_size, self.ammo_size)
				while(self.colliding(ammo)):
					ammo = Ammo(random.randint(1, WORLD_WIDTH), random.randint(1, WORLD_WIDTH), self.ammo_size, self.ammo_size)
				self.ammo.append(ammo)
			elif(rand_num == 2):
				rock = Rock(random.randint(1, WORLD_WIDTH), random.randint(1, WORLD_WIDTH), self.rock_size, self.rock_size)
				while(self.colliding(rock)):
					rock = Rock(random.randint(1, WORLD_WIDTH), random.randint(1, WORLD_WIDTH), self.rock_size, self.rock_size)
				self.rocks.append(rock)
			elif(rand_num == 3):
				tree = Tree(random.randint(1, WORLD_WIDTH), random.randint(1, WORLD_WIDTH), self.tree_size, self.tree_size)
				while(self.colliding(tree)):
					tree = Tree(random.randint(1, WORLD_WIDTH), random.randint(1, WORLD_WIDTH), self.tree_size, self.tree_size)
				self.trees.append(tree)
			elif(rand_num == 4):
				shield = Shield(random.randint(1, WORLD_WIDTH), random.randint(1, WORLD_WIDTH), self.shield_size, self.shield_size)
				while(self.colliding(shield)):
					shield = Shield(random.randint(1, WORLD_WIDTH), random.randint(1, WORLD_WIDTH), self.shield_size, self.shield_size)
				self.shields.append(shield)

	def colliding(self, resource):
		rect1 = resource.get_rect()
		for ammo in self.ammo:
			if rect1.colliderect(ammo.get_rect()):
				return True

		for rock in self.rocks:
			if rect1.colliderect(rock.get_rect()):
				return True

		for shield in self.shields:
			if rect1.colliderect(shield.get_rect()):
				return True

		for tree in self.trees:
			if rect1.colliderect(tree.get_rect()):
				return True

		return False

	def encode_initial_data(self):
		t = []
		for tree in self.trees:
			t.append(f"{tree.x} {tree.y}")

		r = []
		for rock in self.rocks:
			r.append(f"{rock.x} {rock.y}")

		a = []
		for ammo in self.ammo:
			a.append(f"{ammo.x} {ammo.y}")

		s = []
		for shield in self.shields:
			s.append(f"{shield.x} {shield.y}")

		return [a, t, r, s]

	def encode_data(self):
		a = []
		for ammo in self.ammo:
			a.append(f"{ammo.x} {ammo.y} {ammo.w} {ammo.h}")

		s = []
		for shield in self.shields:
			s.append(f"{shield.x} {shield.y} {shield.w} {shield.h}")

		return [s, s]

	def get_xy(self, st):
		s = st.split()
		return int(s[0]), int(s[1])

	def decode_initial_data(self, data):
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


		
