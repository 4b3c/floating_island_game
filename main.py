import pygame
pygame.init()
win_size = (1100, 700)
window = pygame.display.set_mode(win_size)

import game
import menus

update_vil = 0
menus.opening_menu(window)
game = menus.main_menu(window, win_size)
game.load()

print(game.main_island.top[9][0].name)

while True:
	mouse_pos = pygame.mouse.get_pos()
	mouse_press = pygame.mouse.get_pressed()[0]
	game.run(window, mouse_pos, mouse_press)

	update_vil += 1
	if update_vil > 19:
		game.population[0].go_to(game.main_island.top[9][0])
		update_vil = 0

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