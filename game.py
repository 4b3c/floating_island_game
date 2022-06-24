import island
import variables
import pygame
from buttons import button
import menus
import tile_classes

class game_():
	__slots__ = ("t_size", "height", "main_island", "name", "build_button", "building", "build_woodcutting", "build_mining", "building_image")

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
		self.building = 0
		self.building_image = None

	def run(self, window, mouse_pos, mouse_press):
		window.fill(variables.sky_blue)
		self.main_island.draw_island(self.t_size, window)

		mouse_pos, mouse_press = pygame.mouse.get_pos(), pygame.mouse.get_pressed()[0]
		self.build_button.draw(window, mouse_pos, mouse_press)
		if self.build_button.pressed:
			menus.wait_mouse_up()
			self.building = 1

		if self.building == 1:
			self.build_woodcutting.draw(window, mouse_pos, mouse_press)
			self.build_mining.draw(window, mouse_pos, mouse_press)

			if self.build_woodcutting.pressed:
				self.building = 2
			elif self.build_mining.pressed:
				self.building = 3

		elif self.building == 2 or self.building == 3:
			if self.building == 2:
				self.building_image = pygame.image.load('sprites/buildings/woodcutting.png')
			elif self.building == 3:
				self.building_image = pygame.image.load('sprites/buildings/mining.png')

			self.building_image.fill((255, 255, 255, 120), None, pygame.BLEND_RGBA_MULT)
			closest = variables.round_spec(mouse_pos[0]), variables.round_spec(mouse_pos[1])
			window.blit(self.building_image, (closest))
			if mouse_press:
				closest = [closest[0] / 32,(closest[1] / 32) + 1]
				coords = [c.coords for c in self.main_island.top]
				
				if closest in coords:
					if self.main_island.top[coords.index(closest)].name == "grass":
						if self.building == 2:
							self.main_island.top[coords.index(closest)] = tile_classes.woodcutting(closest)
						elif self.building == 3:
							self.main_island.top[coords.index(closest)] = tile_classes.mining(closest)



		pygame.display.update()