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

build_costs = {
	"woodcutting": [0, 0, 20, 10],
	"mining": [0, 0, 10, 20],
	"house": [0, 0, 30, 30]
}

build_buttons = [
	button(20, (120, 640), "build"),
	button(20, (230, 640), "woodcutting", 1.1, 1.1, paths["woodcutting"] + '.png'),
	button(20, (270, 640), "mining", 1.1, 1.1, paths["mining"] + '.png'),
	button(20, (310, 640), "house", 1.1, 1.1, paths["house"] + '.png')
	]

def create_class(name, pos, level = 0):
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
		return woodcutting(pos, level)
	elif name == "mining":
		return mining(pos, level)
	elif name == "house":
		return house(pos, level)
	elif name == "roof":
		return roof(pos)

class grass():
	def __init__(self, coords, level = 0):
		self.coords = coords
		self.level = level
		self.name = "grass"
		self.image = pygame.image.load(paths[self.name] + random.choice(('grass_1.png', 'grass_2.png', 'grass_3.png'))).convert_alpha()

class trees():
	def __init__(self, coords, level = 0):
		self.coords = coords
		self.level = level
		self.name = "trees"
		self.image = pygame.image.load(paths[self.name] + '.png').convert_alpha()
		self.wood = 500

class rocks():
	def __init__(self, coords, level = 0):
		self.coords = coords
		self.level = level
		self.name = "rocks"
		self.image = pygame.image.load(paths[self.name] + '.png').convert_alpha()
		self.rock = 500
		

class ruins():
	def __init__(self, coords, level = 0):
		self.coords = coords
		self.level = level
		self.name = "ruins"
		self.image = pygame.image.load(paths[self.name] + '.png').convert_alpha()
		self.destroyed = 500
		

class ship():
	def __init__(self, coords, level = 0):
		self.coords = coords
		self.level = level
		self.name = "ship"
		self.image = pygame.image.load(paths[self.name] + '.png').convert_alpha()
		self.room = 4
		

class mining():
	def __init__(self, coords, level = 0):
		self.coords = coords
		self.level = level
		self.name = "mining"
		if level == 0:
			insert = ''
		elif level == 1:
			insert = '_top'
		self.image = pygame.image.load(paths[self.name] + insert + '.png').convert_alpha()
		self.jobs = 4
		

class woodcutting():
	def __init__(self, coords, level = 0):
		self.coords = coords
		self.level = level
		self.name = "woodcutting"
		if level == 0:
			insert = ''
		elif level == 1:
			insert = '_top'
		self.image = pygame.image.load(paths[self.name] + insert +  '.png').convert_alpha()
		self.jobs = 4
		

class house():
	def __init__(self, coords, level = 0):
		self.coords = coords
		self.level = level
		self.name = "house"
		if level == 0:
			insert = ''
		elif level == 1:
			insert = '_top'
		self.image = pygame.image.load(paths[self.name] + insert + '.png').convert_alpha()
		self.room = 4


class roof():
	def __init__(self, coords, level = 0):
		self.coords = coords
		self.level = level
		self.name = "roof"
		self.image = None
		self.room = 4