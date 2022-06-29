from wacky_name_gen import random_name
import random
import variables
import pygame

class person():
	def __init__(self, pos, family = None, traits = None, age = None):
		self.pos = pos
		self.name = random_name(random.randint(3, 7))
		self.job = None
		self.home = None
		self.hunger = 100
		self.health = 100
		self.happiness = 100
		self.color = random.choice(variables.peoples_color)
		self.clothes_color = random.choice(variables.clothes_color)
		if age == None:
			self.age = 0
		if traits == None:
			self.traits = []
		if family == None:
			self.family = random_name(random.randint(3, 7))

	def load(self):
		self.surf = pygame.Surface((8, 16))
		self.surf.fill(self.color)
		pygame.draw.rect(self.surf, (self.clothes_color), (0, 7, 8, 9))

	def save(self):
		self.surf = None

	def draw(self, window):
		window.blit(self.surf, (self.pos))

