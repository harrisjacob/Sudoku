import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame
pygame.init()

font_size = 32											# Textbox font size
inactive_color = (255,255,255)							# Inactive textbox color
active_color = (150,150,150)							# Active (seleceted) textbox color
font_color = (0,0,0)									# Font color
font = pygame.font.Font(None, font_size)				# Font of textbox
outline_thickness = 0									# Outline of textbox thickness
output = False											# Has the solution been displayed
screenSize = 512										# Screen Size
margin = 0.05											# Ratio of margin width/height to screenSize
marginSize = int(screenSize*margin)						# Width/Height of margins
cpl = 9													# Cells per line
sectors = int(pow(cpl,0.5))								# Number of sectors
cellSize = ( screenSize - (marginSize*2) ) / cpl		# Pixel calculation of cell length/width
font_start_posX = 0.38*cellSize							# X indentation of text
font_start_posY = 0.3*cellSize 							# Y indentation of text
submit = False 											# Is the user in solution mode
light_line_weight = 3 									# Thickness of lines
heavy_line_weight = 5 									# Cell and exterior line weight
solution=[]												# Solution board