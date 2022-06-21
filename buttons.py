import pygame
import variables

class button():
	def __init__(self, text_size, pos, text, center_align):
		self.text = text
		self.pos = list(pos)
		self.high_pos = list(pos[:])
		self.text_size = text_size
		self.font = pygame.font.SysFont("SWRomns", self.text_size, True)
		self.size = self.font.size(text)
		self.surf_size = (self.size[0] * 1.1, self.size[1] * 1.1)
		self.high_size = (self.surf_size[0] * 1.05, self.surf_size[1])
		self.pressed = False


		# normal button surface
		self.surf = pygame.Surface(self.surf_size)
		self.surf.fill(variables.button_bg)
		pygame.draw.polygon(self.surf, (variables.high_bg), ((0, 0), (0, self.surf_size[1]), (self.surf_size)))
		text_surf = self.font.render(self.text, False, variables.word_color)
		self.surf.blit(text_surf, (text_size / 10, text_size / 10))
		pygame.draw.rect(self.surf, (variables.border), ((0, 0) + self.surf_size), int(text_size / 6))


		# highlighted button surface
		self.high_surf = pygame.Surface(self.high_size)
		self.high_surf.fill(variables.high_bg)
		pygame.draw.polygon(self.high_surf, (variables.button_bg), ((0, 0), (0, self.high_size[1]), (self.high_size)))
		text_surf = self.font.render(self.text, False, variables.word_color)
		self.high_surf.blit(text_surf, ((text_size / 10) + (self.high_size[0] * 0.025), text_size / 10))
		pygame.draw.rect(self.high_surf, (variables.border), ((0, 0) + self.high_size), int(text_size / 6))


		if center_align:
			self.pos[0] = (self.pos[0]  - (self.surf_size[0] / 2))
			self.high_pos[0] = (self.high_pos[0]  - (self.high_size[0] / 2))

	def draw(self, window, mouse_pos, mouse_press, off_y = 0):
		self.pressed = False
		if mouse_pos[0] < self.pos[0] or mouse_pos[0] > self.pos[0] + self.surf_size[0]:
			window.blit(self.surf, (self.pos[0], self.pos[1] + off_y))
		elif mouse_pos[1] < self.pos[1] or mouse_pos[1] > self.pos[1] + self.surf_size[1]:
			window.blit(self.surf, (self.pos[0], self.pos[1] + off_y))
		else:
			window.blit(self.high_surf, (self.high_pos[0], self.high_pos[1] + off_y))
			if mouse_press:
				self.pressed = True
