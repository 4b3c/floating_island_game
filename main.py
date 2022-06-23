import pygame
import game
import menus


win_size = (1100, 700)
pygame.init()
window = pygame.display.set_mode(win_size)

menus.opening_menu(window)
game = menus.main_menu(window, win_size)
game.load()

while True:
	game.run(window)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game.save()
			menus.save_(game)
			menus.opening_menu(window)
			game = menus.main_menu(window, win_size)
			game.load()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				menus.pause_menu(window, game, win_size)