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

	def initialize_random(self, num=1000):
		for i in range(num):
			rand_num = random.randint(1, 4)
			if(rand_num == 1):
				ammo = Ammo(random.randint(1, WORLD_WIDTH), random.randint(1, WORLD_WIDTH), 30, 30)
				while(self.colliding(ammo)):
					ammo = Ammo(random.randint(1, WORLD_WIDTH), random.randint(1, WORLD_WIDTH), 30, 30)
				self.ammo.append(ammo)
			elif(rand_num == 2):
				rock = Rock(random.randint(1, WORLD_WIDTH), random.randint(1, WORLD_WIDTH), 110, 110)
				while(self.colliding(rock)):
					rock = Rock(random.randint(1, WORLD_WIDTH), random.randint(1, WORLD_WIDTH), 110, 110)
				self.rocks.append(rock)
			elif(rand_num == 3):
				tree = Tree(random.randint(1, WORLD_WIDTH), random.randint(1, WORLD_WIDTH), 110, 110)
				while(self.colliding(tree)):
					tree = Tree(random.randint(1, WORLD_WIDTH), random.randint(1, WORLD_WIDTH), 110, 110)
				self.trees.append(tree)
			elif(rand_num == 4):
				shield = Shield(random.randint(1, WORLD_WIDTH), random.randint(1, WORLD_WIDTH), 50, 50)
				while(self.colliding(shield)):
					shield = Shield(random.randint(1, WORLD_WIDTH), random.randint(1, WORLD_WIDTH), 50, 50)
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


