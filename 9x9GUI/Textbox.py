#!/usr/bin/env python3

import pygame
import config

class TextBox:
	def __init__(self, xpos, ypos, w, h, row, col, text=''):
		self.box = pygame.Rect(xpos,ypos,w,h)
		self.box_color = config.inactive_color
		self.text = text
		self.render = config.font.render(text, True, self.box_color)
		self.active = False
		self.row = row
		self.col = col
		self.value = 0

	def event_handler(self, event):
		if event.type == pygame.KEYDOWN:
			if self.active:
				if event.key == pygame.K_BACKSPACE:
					self.text = self.text[:-1]
				elif event.key == pygame.K_RETURN:
					self.active = False
					config.submit = True
				else:
					if((event.unicode).isdigit()):
						if(event.unicode == '0'):
							self.text = ''
						else:
							self.text = event.unicode
						self.value = int(event.unicode)
				
				self.render = config.font.render(self.text, True, config.font_color)
		
		if event.type == pygame.MOUSEBUTTONDOWN:
			if self.box.collidepoint(event.pos):
				self.active = not self.active
			else:
				self.active = False

			if self.active:
				self.box_color = config.active_color
			else:
				self.box_color = config.inactive_color

	def update(self):
		self.render = config.font.render(self.text, True, config.font_color)

	def draw(self, screen):
		
		pygame.draw.rect(screen, self.box_color, self.box, config.outline_thickness)
		screen.blit(self.render, (self.box.x + config.font_start_posX, self.box.y + config.font_start_posY ))
'''
def main():


	global output
	clock = pygame.time.Clock()

	running = True
	while running:
		if not submit:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				for textbox in allTextboxes:
					textbox.event_handler(event)


			screen.fill((0,0,0))
			
			for box in allTextboxes:
				box.draw(screen)

			pygame.display.flip()
			clock.tick(50)
		else:
			if not output:
				for textbox in allTextboxes:
					print(textbox.value)
				output = True
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False


if __name__ == '__main__':
	main()
	pygame.quit()
'''