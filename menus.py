import pygame
import time
import pickle
import os
import buttons
import game

def wait_mouse_up():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.MOUSEBUTTONUP:
				return

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
	play_ = buttons.button(40, (550, 400), "play", 3)
	quit_ = buttons.button(40, (550, 480), "quit", 3)

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
	wait_mouse_up()

def main_menu(window, win_size):
	wld = os.listdir("worlds")
	buttons_ = [buttons.button(40, (550, 120), "new game")]
	buttons_ += [buttons.button(40, (550, 200 + (count * 80)), file[0:6]) for file, count in zip(wld, range(len(wld)))]
	buttons_ += [buttons.button(40, (800, 480), "back")]

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
					wait_mouse_up()
					opening_menu(window)
				elif button == buttons_[0]:
					# new
					if wld == []:
						name = "world1"
					else:
						name = "world" + str(int(wld[-1][5]) + 1)
					game_obj = game.game_(win_size, name)
					return game_obj
				else:
					game_obj = open_(button.text[0:6])
					return game_obj

		pygame.display.update()

def pause_menu(window, game_, win_size):
	buttons_ = [buttons.button(40, (550, 220), "resume")]
	buttons_ += [buttons.button(40, (550, 300), "save")]
	buttons_ += [buttons.button(40, (550, 380), "exit")]

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
				if button == buttons_[0]:
					return
				elif button == buttons_[1]:
					game_.save()
					save_(game_)
					game_.load()
					return
				elif button == buttons_[2]:
					wait_mouse_up()
					opening_menu(window)
					game = main_menu(window, win_size)
					game.load()

		pygame.display.update()