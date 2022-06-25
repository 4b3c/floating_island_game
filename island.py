import random
import pygame
import tile_classes
import variables

class island():
	__slots__ = ("surf", "underground", "top", "top_c")

	def __init__(self, size, surf_height):
		start = random.randint(3, int(size * 0.15))
		end = random.randint(int(size * 0.85), size - 2)
		self.surf = [[x, surf_height] for x in range(start, end)]
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

		backup = self.surf[1:]
		self.top_c = [[x, y - 1] for x, y in self.surf[1:]]
		self.top = []
		for i in range(random.randint(5, 8)):
			tile = random.choice(backup)
			self.top.append([["trees", tile]])
			backup.remove(tile)
		for i in range(random.randint(2, 3)):
			tile = random.choice(backup)
			self.top.append([["rocks", tile]])
			backup.remove(tile)
		for i in range(random.randint(1, 2)):
			tile = random.choice(backup)
			self.top.append([["ruins", tile]])
			backup.remove(tile)
		for tile in backup:
			self.top.append([["grass", tile]])
		self.top.append([["ship", [self.surf[0][0], self.surf[0][1]]]])

	def to_classes(self):
		for tower, count1 in zip(self.top, range(len(self.top))):
			for tile, count2 in zip(tower, range(len(tower))):
				self.top[count1][count2] = tile_classes.create_class(tile[0], tile[1])

	def to_save(self):
		for tower, count1 in zip(self.top, range(len(self.top))):
			for tile, count2 in zip(tower, range(len(tower))):
				self.top[count1][count2] = [tile.name, tile.coords]

	def draw_island(self, t_size, window):
		for su in self.surf:
			pygame.draw.rect(window, (variables.grass_green), (su[0] * t_size, su[1] * t_size, t_size, t_size))

		for un in self.underground:
			pygame.draw.rect(window, (variables.rock_grey), (un[0] * t_size, un[1] * t_size, t_size, t_size))

		for tower in self.top:
			for tile in tower:
				if tile.image != None:
					window.blit(tile.image, (tile.coords[0] * t_size, (tile.coords[1] - 1) * t_size))
