import island
import variables
import pygame
from buttons import button
import menus

class game_():
	__slots__ = ("t_size", "height", "main_island", "name", "build_button", "building", "build_woodcutting", "build_mining")

	def __init__(self, win_size, name):
		self.t_size = 32
		self.height = 14
		self.main_island = island.island(int(win_size[0] / self.t_size), self.height)
		self.name = name
		self.building = 0

	def load(self):
		self.main_island.to_classes()
		self.build_button = button(20, (120, 640), "build")
		self.build_woodcutting = button(20, (230, 640), "", 1.1, 1.1, 'sprites/buildings/woodcutting.png')
		self.build_mining = button(20, (270, 640), "", 1.1, 1.1, 'sprites/buildings/mining.png')

	def save(self):
		self.main_island.to_save()
		self.build_button = None
		self.build_woodcutting = None
		self.build_mining = None

	def run(self, window):
		window.fill(variables.sky_blue)
		self.main_island.draw_island(self.t_size, window)

		mouse_pos, mouse_press = pygame.mouse.get_pos(), pygame.mouse.get_pressed()[0]
		self.build_button.draw(window, mouse_pos, mouse_press)
		if self.build_button.pressed:
			menus.wait_mouse_up()
			self.building = (self.building * -1) + 1

		if self.building == 1:
			self.build_woodcutting.draw(window, mouse_pos, mouse_press)
			self.build_mining.draw(window, mouse_pos, mouse_press)

			if self.build_woodcutting.pressed:
				print("build_woodcutting")
			elif self.build_mining.pressed:
				print("build_mining")

		pygame.display.update()