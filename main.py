import pygame
pygame.init()
win_size = (1100, 700)
window = pygame.display.set_mode(win_size)

import game
import menus


menus.opening_menu(window)
game = menus.main_menu(window, win_size)
game.load()

while True:
	mouse_pos = pygame.mouse.get_pos()
	mouse_press = pygame.mouse.get_pressed()[0]
	game.run(window, mouse_pos, mouse_press)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			menus.opening_menu(window)
			game = menus.main_menu(window, win_size)
			game.load()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				if game.show_buildings == False:
					game = menus.pause_menu(window, game, win_size)
				else:
					game.show_buildings = False