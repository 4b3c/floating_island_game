import pygame
import variables
import tile_classes

def align_int_texts(text):
	text = str(text)
	if int(text) > 999:
		text = str(round(int(text) / 1000, 1)) + "k"
	elif int(text) > 99:
		text = " " + text
	elif int(text) > 9:
		text = "  " + text
	else:
		text = "   " + text

	return text

def dict_to_displayers(dict_):
	displayers = []
	for key, count in zip(dict_, range(len(dict_))):
		displayers.append(displayer(22, [960, (50 * count) + 40], str(dict_[key]), 1.6, 1.4, 'sprites/resources/' + key + '.png'))

	return displayers


class displayer():
	__slots__ = ("text", "pos", "text_size", "font", "size", "surf_size", "surf", "highlighted")

	def __init__(self, text_size, pos, text, side_size = 1.6, top_size = 1.4, image_p = None, border = True, center = True,
		color = variables.word_color, align = "right"):
		if align == "right": self.text = align_int_texts(text)
		elif align == "left": self.text = str(text)
		self.pos = list(pos)
		self.text_size = text_size
		self.font = pygame.font.SysFont("SWMono", self.text_size, True)
		self.size = self.font.size(self.text)
		self.surf_size = (self.size[0] * side_size, self.size[1] * top_size)

		if image_p == None:
			self.surf = pygame.Surface(self.surf_size)
			self.surf.fill(variables.displayer_bg)
			text_surf = self.font.render(self.text, False, color)
			self.surf.blit(text_surf, (self.surf_size[0] / 2 - self.size[0] / 2, text_size / 3))
			if border:
				pygame.draw.rect(self.surf, (variables.border), ((0, 0) + self.surf_size), int(text_size / 6))

		else:
			self.surf = pygame.Surface((self.surf_size[0] + 40, self.surf_size[1]))
			self.surf.fill(variables.displayer_bg)
			text_surf = self.font.render(self.text, False, color)
			self.surf.blit(text_surf, ((self.surf_size[0] / 2 - self.size[0] / 2) + 40, text_size / 3))
			image = pygame.image.load(image_p)
			self.surf.blit(image, (4, 4))
			if border:
				pygame.draw.rect(self.surf, (variables.border), (0, 0, self.surf_size[0] + 40, self.surf_size[1]), int(text_size / 6))

		if center:
			self.pos[0] = (self.pos[0]  - (self.surf_size[0] / 2))

	def draw(self, window):
		window.blit(self.surf, (self.pos))



class cost_displayer():
	__slots__ = ("text", "font", "size", "real_surf")

	def __init__(self, text_size, building, resources):
		costs = tile_classes.build_costs[building]
		self.font = pygame.font.SysFont("SWMono", text_size, True)

		size = [0, 0]
		indiv_surfs = []
		for line, resource, count in zip(costs, resources, range(len(costs))):
			if int(line) > 0:
				if int(line) > resources[resource]:
					color = variables.red
				else:
					color = variables.word_color
				indiv_surfs.append(displayer(text_size, (0, 0), line, 1.6, 1.4, tile_classes.resource_paths[resource], False, True, color, "left"))
				size[1] += text_size * 1.75
				if self.font.size(str(line))[0] * 3 > size[0]:
					size[0] = self.font.size(str(line))[0] * 3

		self.real_surf = pygame.Surface(size)
		self.real_surf.fill(variables.displayer_bg)
		for cost, count in zip(indiv_surfs, range(len(indiv_surfs))):
			self.real_surf.blit(cost.surf, (0, count * (text_size * 1.6)))

		pygame.draw.rect(self.real_surf, (variables.border), (0, 0, size[0], size[1]), int(text_size / 6))

	def draw(self, window, pos):
		window.blit(self.real_surf, (pos))
