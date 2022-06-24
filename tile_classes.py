import random
import pygame

class grass():
	def __init__(self, coords):
		self.coords = coords
		path = random.choice(('grass_1.png', 'grass_2.png', 'grass_3.png'))
		self.image = pygame.image.load('sprites/grass/' + path).convert_alpha()
		self.name = "grass"

class trees():
	def __init__(self, coords):
		self.coords = coords
		self.image = pygame.image.load('sprites/trees/trees_1.png').convert_alpha()
		self.wood = 500
		self.name = "trees"

class rocks():
	def __init__(self, coords):
		self.coords = coords
		self.image = pygame.image.load('sprites/rocks/rock_1.png').convert_alpha()
		self.rock = 500
		self.name = "rocks"

class ruins():
	def __init__(self, coords):
		self.coords = coords
		self.image = pygame.image.load('sprites/ruins/ruins.png').convert_alpha()
		self.destroyed = 500
		self.name = "ruins"

class ship():
	def __init__(self, coords):
		self.coords = coords
		self.image = pygame.image.load('sprites/buildings/ship.png').convert_alpha()
		self.level = 0
		self.room = 4
		self.name = "ship"

class mining():
	def __init__(self, coords):
		self.coords = coords
		self.image = pygame.image.load('sprites/buildings/mining.png').convert_alpha()
		self.level = 0
		self.jobs = 4
		self.name = "mining"

class woodcutting():
	def __init__(self, coords):
		self.coords = coords
		self.image = pygame.image.load('sprites/buildings/woodcutting.png').convert_alpha()
		self.level = 0
		self.jobs = 4
		self.name = "woodcutting"