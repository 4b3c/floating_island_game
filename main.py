import pygame
import random
import island
import variables


pygame.init()
window = pygame.display.set_mode((1100, 700))
window.fill(variables.sky_blue)


nm = island.island(int(1100 / variables.t_size), 12)
nm.draw_island(variables.t_size, window)


pygame.display.update()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()