import pygame
import variables

def dict_to_displayers(dict_):
	displayers = []
	for key, count in zip(dict_, range(len(dict_))):
		displayers.append(displayer(22, [960, (50 * count) + 40], str(dict_[key]), 1.6, 1.4, 'sprites/resources/' + key + '.png'))

	return displayers


class displayer():
	__slots__ = ("text", "pos", "high_pos", "text_size", "font", "size", "surf_size", "high_size", "pressed", "surf", "high_surf", "highlighted")

	def __init__(self, text_size, pos, text, side_size = 1.6, top_size = 1.4, image_p = None):
		if int(text) > 999:
			text = str(round(int(text) / 1000, 1)) + "k"
		elif int(text) > 99:
			text = " " + text
		elif int(text) > 9:
			text = "  " + text
		else:
			text = "   " + text
		self.text = text
		self.pos = list(pos)
		self.high_pos = list(pos[:])
		self.text_size = text_size
		self.font = pygame.font.SysFont("SWMono", self.text_size, True)
		self.size = self.font.size(text)
		self.surf_size = (self.size[0] * side_size, self.size[1] * top_size)
		print(self.size, self.surf_size)

		if image_p != None:
			self.surf = pygame.Surface((self.surf_size[0] + 40, self.surf_size[1]))
			self.surf.fill(variables.displayer_bg)
			text_surf = self.font.render(self.text, False, variables.word_color)
			self.surf.blit(text_surf, ((self.surf_size[0] / 2 - self.size[0] / 2) + 40, text_size / 3))
			image = pygame.image.load(image_p)
			self.surf.blit(image, (4, 4))
			pygame.draw.rect(self.surf, (variables.border), (0, 0, self.surf_size[0] + 40, self.surf_size[1]), int(text_size / 6))

		if image_p == None:
			self.surf = pygame.Surface(self.surf_size)
			self.surf.fill(variables.displayer_bg)
			text_surf = self.font.render(self.text, False, variables.word_color)
			self.surf.blit(text_surf, (self.surf_size[0] / 2 - self.size[0] / 2, text_size / 3))
			pygame.draw.rect(self.surf, (variables.border), ((0, 0) + self.surf_size), int(text_size / 6))

		self.pos[0] = (self.pos[0]  - (self.surf_size[0] / 2))

	def draw(self, window):
		window.blit(self.surf, (self.pos))



# example
# displayer1 = displayer(22, [300, 100], "1109", 1.6, 1.4, 'sprites/resources/gold.png')