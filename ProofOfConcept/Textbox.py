#!/usr/bin/env python3

import pygame

pygame.init()
screen_size = 1024
font_size = 512
box_count = 4
margin = int(screen_size*0.1)
cpl = int(pow(box_count, 0.5)) #cells per length
cell_size = (screen_size - (3*margin)) / cpl
screen = pygame.display.set_mode([screen_size,screen_size])
inactive_color = (255,255,255)
active_color = (150,150,150)
font_color = (0,0,0)
font = pygame.font.Font(None, font_size)
outline_thickness = 0
submit = False
output = False

class TextBox:
	def __init__(self, xpos, ypos, w, h, row, col, text=''):
		self.box = pygame.Rect(xpos,ypos,w,h)
		self.box_color = inactive_color
		self.text = text
		self.render = font.render(text, True, self.box_color)
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
					global submit
					submit = True
				else:
					if((event.unicode).isdigit()):
						if(event.unicode == '0'):
							self.text = ''
						else:
							self.text = event.unicode
						self.value = int(event.unicode)
				
				self.render = font.render(self.text, True, font_color)
		
		if event.type == pygame.MOUSEBUTTONDOWN:
			if self.box.collidepoint(event.pos):
				self.active = not self.active
			else:
				self.active = False

			if self.active:
				self.box_color = active_color
			else:
				self.box_color = inactive_color

	def draw(self, screen):
		pygame.draw.rect(screen, self.box_color, self.box, outline_thickness)
		screen.blit(self.render,(self.box.x+int(0.23*cell_size),self.box.y+20))

def main():

	global output
	clock = pygame.time.Clock()

	allTextboxes = []
	for box in range(box_count):
		row =  int(box/cpl)
		col = int(box%cpl)
		new_box = TextBox(margin+((cell_size+margin)*col), margin+((cell_size+margin)*row), cell_size, cell_size, row, col)
		allTextboxes.append(new_box)

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
