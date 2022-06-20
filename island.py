import random
import pygame
import tile_classes
import variables

class island():
	def __init__(self, size, surf_height):
		start = random.randint(3, int(size * 0.15))
		end = random.randint(int(size * 0.85), size - 2)
		self.surface = [[x, surf_height] for x in range(start, end)]
		self.underground = []
		underground = [[x, surf_height + 1] for x in range(start, end)]
		for i in range(4):
			self.underground += [[x, y + i] for x, y in underground]
			try:
				del underground[0:random.randint(1, 4)]
				l = len(underground)
				del underground[-random.randint(1, 4):-1]
				del underground[-1]
			except:
				pass

		backup = self.surface[1:]
		self.top = []
		for i in range(random.randint(5, 8)):
			tile = random.choice(backup)
			self.top.append(tile_classes.trees(tile))
			backup.remove(tile)
		for i in range(random.randint(2, 3)):
			tile = random.choice(backup)
			self.top.append(tile_classes.rocks(tile))
			backup.remove(tile)
		for i in range(random.randint(1, 2)):
			tile = random.choice(backup)
			self.top.append(tile_classes.ruins(tile))
			backup.remove(tile)
		for tile in backup:
			self.top.append(tile_classes.grass(tile))
		self.top.append(tile_classes.ship((self.surface[0][0], self.surface[0][1])))


	def draw_island(self, t_size, window):
		for su in self.surface:
			pygame.draw.rect(window, (variables.grass_green), (su[0] * t_size, su[1] * t_size, t_size, t_size))

		for un in self.underground:
			pygame.draw.rect(window, (variables.rock_grey), (un[0] * t_size, un[1] * t_size, t_size, t_size))

		for to in self.top:
			window.blit(to.image, (to.coords[0] * t_size, (to.coords[1] - 1) * t_size))
