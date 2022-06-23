import island
import variables
import pygame

class game_():
	__slots__ = ("t_size", "height", "main_island", "name")

	def __init__(self, win_size, name):
		self.t_size = 32
		self.height = 12
		self.main_island = island.island(int(win_size[0] / self.t_size), self.height)
		self.name = name

	def load(self):
		self.main_island.to_classes()

	def save(self):
		self.main_island.to_save()

	def run(self, window):
		window.fill(variables.sky_blue)
		self.main_island.draw_island(self.t_size, window)
		pygame.display.update()