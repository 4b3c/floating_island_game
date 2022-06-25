import random
import pygame
from buttons import button

paths = {
	"grass": 'sprites/grass/',
	"woodcutting": 'sprites/buildings/woodcutting',
	"mining": 'sprites/buildings/mining',
	"house": 'sprites/buildings/house',
	"trees": 'sprites/trees/trees_1',
	"rocks": 'sprites/rocks/rock_1',
	"ruins": 'sprites/ruins/ruins',
	"ship": 'sprites/buildings/ship',
}

build_buttons = [
	button(20, (120, 640), "build"),
	button(20, (230, 640), "woodcutting", 1.1, 1.1, paths["woodcutting"] + '.png'),
	button(20, (270, 640), "mining", 1.1, 1.1, paths["mining"] + '.png'),
	button(20, (310, 640), "house", 1.1, 1.1, paths["house"] + '.png')
	]

def create_class(name, pos):
	if name == "trees":
		return trees(pos)
	elif name == "rocks":
		return rocks(pos)
	elif name == "ruins":
		return ruins(pos)
	elif name == "grass":
		return grass(pos)
	elif name == "ship":
		return ship(pos)
	elif name == "woodcutting":
		return woodcutting(pos)
	elif name == "mining":
		return mining(pos)
	elif name == "house":
		return house(pos)
	elif name == "roof":
		return roof(pos)

class grass():
	def __init__(self, coords):
		self.coords = coords
		self.name = "grass"
		self.image = pygame.image.load(paths[self.name] + random.choice(('grass_1.png', 'grass_2.png', 'grass_3.png'))).convert_alpha()

class trees():
	def __init__(self, coords):
		self.coords = coords
		self.name = "trees"
		self.image = pygame.image.load(paths[self.name] + '.png').convert_alpha()
		self.wood = 500

class rocks():
	def __init__(self, coords):
		self.coords = coords
		self.name = "rocks"
		self.image = pygame.image.load(paths[self.name] + '.png').convert_alpha()
		self.rock = 500
		

class ruins():
	def __init__(self, coords):
		self.coords = coords
		self.name = "ruins"
		self.image = pygame.image.load(paths[self.name] + '.png').convert_alpha()
		self.destroyed = 500
		

class ship():
	def __init__(self, coords):
		self.coords = coords
		self.name = "ship"
		self.image = pygame.image.load(paths[self.name] + '.png').convert_alpha()
		self.level = 0
		self.room = 4
		

class mining():
	def __init__(self, coords, level = 0):
		self.coords = coords
		self.name = "mining"
		if level == 0:
			insert = ''
		elif level == 1:
			insert = '_mid'
		elif level == 2:
			insert = '_top'
		self.image = pygame.image.load(paths[self.name] + insert + '.png').convert_alpha()
		self.level = 0
		self.jobs = 4
		

class woodcutting():
	def __init__(self, coords, level = 0):
		self.coords = coords
		self.name = "woodcutting"
		if level == 0:
			insert = ''
		elif level == 1:
			insert = '_mid'
		elif level == 2:
			insert = '_top'
		self.image = pygame.image.load(paths[self.name] + insert +  '.png').convert_alpha()
		self.level = 0
		self.jobs = 4
		

class house():
	def __init__(self, coords):
		self.coords = coords
		self.name = "house"
		self.image = pygame.image.load(paths[self.name] + '.png').convert_alpha()
		self.level = 0
		self.room = 4


class roof():
	def __init__(self, coords):
		self.coords = coords
		self.name = "roof"
		self.image = None
		self.level = 0
		self.room = 4