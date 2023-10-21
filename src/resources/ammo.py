class Ammo:
	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.img = pygame.image.load("images/ammo.png").convert_alpha()
		self.img = pygame.transform.smoothscale(self.img, (w, h))

	def draw():
		pass

	def load():
		pass