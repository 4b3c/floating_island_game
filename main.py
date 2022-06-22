import pygame
import random
import island
import variables
import pickle
import buttons
import os


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


def save_(game_obj):
	file = open('worlds/' + game_obj.name + '.pickle', 'wb')
	pickle.dump(game_obj, file)
	file.close()

def open_(name):
	file = open('worlds/' + name + '.pickle', 'rb')
	game_obj = pickle.load(file)
	file.close()
	return game_obj

def opening_menu(window):
	play_ = buttons.button(40, (200, 500), "play", False)
	quit_ = buttons.button(40, (600, 500), "quit", False)

	while play_.pressed == False:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
		window.fill((0, 0, 0))
		mouse_pos = pygame.mouse.get_pos()
		mouse_press = pygame.mouse.get_pressed()[0]
		play_.draw(window, mouse_pos, mouse_press)
		quit_.draw(window, mouse_pos, mouse_press)
		pygame.display.update()

		if quit_.pressed:
			quit()

def main_menu(window, win_size):
	wld = os.listdir("worlds")
	buttons_ = [buttons.button(40, (550, 130), "new game", True)]
	buttons_ += [buttons.button(40, (550, 200 + (count * 70)), file, True) for file, count in zip(wld, range(len(wld)))]
	buttons_ += [buttons.button(40, (800, 400), "back", False)]

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
		window.fill((0, 0, 0))
		mouse_pos = pygame.mouse.get_pos()
		mouse_press = pygame.mouse.get_pressed()[0]
		for button in buttons_:
			button.draw(window, mouse_pos, mouse_press)

			if button.pressed:
				if button == buttons_[-1]:
					# back
					opening_menu(window)
				elif button == buttons_[0]:
					# new
					if wld == []:
						name = "world1"
					else:
						name = "world" + str(int(wld[-1][5]) + 1)
					game_obj = game_(win_size, name)
					return game_obj
				else:
					game_obj = open_(button.text[0:6])
					return game_obj
		pygame.display.update()




win_size = (1100, 700)
pygame.init()
window = pygame.display.set_mode(win_size)

opening_menu(window)
game = main_menu(window, win_size)
game.load()

while True:
	game.run(window)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game.save()
			save_(game)
			quit()