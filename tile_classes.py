import random
import pygame
from buttons import button

paths = {
	"grass": 'sprites/grass/grass_',
	"woodcutting": 'sprites/buildings/woodcutting',
	"mining": 'sprites/buildings/mining',
	"house": 'sprites/buildings/house',
	"trees": 'sprites/trees/trees_1',
	"rocks": 'sprites/rocks/rock_1',
	"ruins": 'sprites/ruins/ruins',
	"ship": 'sprites/buildings/ship',
}

resource_paths = {
	"gold": 'sprites/resources/gold.png',
	"food": 'sprites/resources/food.png',
	"wood": 'sprites/resources/wood.png',
	"stone": 'sprites/resources/stone.png'
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

tags = {
	"job": [],
	"house": [],
	"natural": []
}

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
		self.level = random.choice(["1.png", "2.png", "3.png"])
		self.name = "grass"
		self.image = None
		self.tag = "natural"

	def load(self):
		self.image = pygame.image.load(paths[self.name] + self.level).convert_alpha()

	def save(self):
		self.image = None

class trees():
	def __init__(self, coords, level = 0):
		self.coords = coords
		self.level = level
		self.name = "trees"
		self.image = None
		self.wood = 500
		self.tag = "natural"

	def load(self):
		self.image = pygame.image.load(paths[self.name] + '.png').convert_alpha()

	def save(self):
		self.image = None

class rocks():
	def __init__(self, coords, level = 0):
		self.coords = coords
		self.level = level
		self.name = "rocks"
		self.image = None
		self.rock = 500
		self.tag = "natural"

	def load(self):
		self.image = pygame.image.load(paths[self.name] + '.png').convert_alpha()

	def save(self):
		self.image = None
		

class ruins():
	def __init__(self, coords, level = 0):
		self.coords = coords
		self.level = level
		self.name = "ruins"
		self.image = None
		self.destroyed = 500
		self.tag = "job"
		self.workers = 0
		self.max_workers = 4

	def load(self):
		self.image = pygame.image.load(paths[self.name] + '.png').convert_alpha()

	def save(self):
		self.image = None
		

class ship():
	def __init__(self, coords, level = 0):
		self.coords = coords
		self.level = level
		self.name = "ship"
		self.image = None
		self.tenants = 0
		self.room = 4
		self.tag = "house"

	def load(self):
		self.image = pygame.image.load(paths[self.name] + '.png').convert_alpha()

	def save(self):
		self.image = None
		

class mining():
	def __init__(self, coords, level = 0):
		self.coords = coords
		self.level = level
		self.name = "mining"
		self.image = None
		self.jobs = 4
		self.tag = "job"
		self.workers = 0
		self.max_workers = 4

	def load(self):
		if self.level == 0:
			insert = ''
		elif self.level == 1:
			insert = '_top'
		self.image = pygame.image.load(paths[self.name] + insert + '.png').convert_alpha()

	def save(self):
		self.image = None
		

class woodcutting():
	def __init__(self, coords, level = 0):
		self.coords = coords
		self.level = level
		self.name = "woodcutting"
		self.image = None
		self.jobs = 4
		self.tag = "job"
		self.workers = 0
		self.max_workers = 4

	def load(self):
		if self.level == 0:
			insert = ''
		elif self.level == 1:
			insert = '_top'
		self.image = pygame.image.load(paths[self.name] + insert + '.png').convert_alpha()

	def save(self):
		self.image = None
		

class house():
	def __init__(self, coords, level = 0):
		self.coords = coords
		self.level = level
		self.name = "house"
		self.image = None
		self.tenants = 0
		self.room = 4
		self.tag = "house"

	def load(self):
		if self.level == 0:
			insert = ''
		elif self.level == 1:
			insert = '_top'
		self.image = pygame.image.load(paths[self.name] + insert + '.png').convert_alpha()

	def save(self):
		self.image = None


class roof():
	def __init__(self, coords, level = 0):
		self.coords = coords
		self.level = level
		self.name = "roof"
		self.image = None
		self.room = 4
		self.tag = "natural"

	def load(self):
		pass

	def save(self):
		pass