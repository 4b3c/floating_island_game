from wacky_name_gen import random_name
import random
import variables
import pygame

class person():
	def __init__(self, pos, tags, family = None, traits = None, age = None):
		self.pos = list(pos)
		self.name = random_name(random.randint(3, 7))

		for job in tags["job"]:
			if job.workers < job.max_workers:
				job.workers += 1
				self.job = job

		for house in tags["house"]:
			if house.tenants < house.room:
				house.tenants += 1
				self.house = house

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

	def go_to(self, building):
		pos = self.pos[0]
		if building == "job":
			b_pos = (self.job.coords[0] * 32) + 12
		elif building == "house":
			b_pos = (self.house.coords[0] * 32) + 12
		else:
			b_pos = (building.coords[0] * 32) + 12
			
		if pos > b_pos:
			self.pos[0] -= 1
		elif pos < b_pos:
			self.pos[0] += 1

