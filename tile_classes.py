import random
import pygame

class grass():
	def __init__(self, coords):
		self.coords = coords
		path = random.choice(('grass_1.png', 'grass_2.png', 'grass_3.png'))
		self.image = pygame.image.load('sprites/grass/' + path).convert_alpha()
		self.wood = 500

class trees():
	def __init__(self, coords):
		self.coords = coords
		self.image = pygame.image.load('sprites/trees/trees_1.png').convert_alpha()
		self.wood = 500

class rocks():
	def __init__(self, coords):
		self.coords = coords
		self.image = pygame.image.load('sprites/rocks/rock_1.png').convert_alpha()
		self.rock = 500

class ruins():
	def __init__(self, coords):
		self.coords = coords
		self.image = pygame.image.load('sprites/ruins/ruins.png').convert_alpha()
		self.destroyed = 500

class ship():
	def __init__(self, coords):
		self.coords = coords
		self.image = pygame.image.load('sprites/buildings/ship.png').convert_alpha()
		self.level = 0
		self.room = 4