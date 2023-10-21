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
				self.ammo.append(Ammo(random.randint(1, WORLD_WIDTH), random.randint(1, WORLD_WIDTH), 35, 35))
			if(rand_num == 2):
				self.rocks.append(Rock(random.randint(1, WORLD_WIDTH), random.randint(1, WORLD_WIDTH), 70, 70))
			if(rand_num == 3):
				self.shields.append(Tree(random.randint(1, WORLD_WIDTH), random.randint(1, WORLD_WIDTH), 70, 70))
			if(rand_num == 4):
				self.trees.append(Shield(random.randint(1, WORLD_WIDTH), random.randint(1, WORLD_WIDTH), 60, 60))

