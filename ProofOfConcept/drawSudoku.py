#!/usr/bin/env python3

import pygame
pygame.init()

screen_size = 500 #Screen size
margin_ratio = 0.05 #Percentage of screen reserved for margins
margin_size = int(screen_size*margin_ratio) #Screen margin
value_count = 9 #of distinct user values
light_line_weight = 3 #Thickness of lines
heavy_line_weight = 5 #Cell and exterior line weight

cell_size = (screen_size - (2*margin_size)) / (value_count)

hLineList = []
vLineList = []

#Build horizontal line list
for line in range(0,value_count-1):

	startHLine = []
	endHLine = []
	newHLine = []

	startHLine.append(margin_size+(cell_size*line)+cell_size) #Start point x
	startHLine.append(margin_size) #Start point y
	endHLine.append(margin_size+(cell_size*line)+cell_size)#End point x
	endHLine.append(screen_size-margin_size)#End point y
	
	newHLine.append(startHLine)
	newHLine.append(endHLine)
	
	hLineList.append(newHLine)

for line in range(0,value_count-1):
	startVLine = []
	endVLine = []
	newVLine = []

	startVLine.append(margin_size) #Start point x
	startVLine.append(margin_size+(cell_size*line)+cell_size) #Start point y
	endVLine.append(screen_size-margin_size)#End point x
	endVLine.append(margin_size+(cell_size*line)+cell_size)#End point y

	newVLine.append(startVLine)
	newVLine.append(endVLine)
	
	vLineList.append(newVLine)


#Build heavy line list
'''
for line in range(int(pow(value_count,0.5))-1):
	startHeavyHLine = []
	endHeavyHLine = []
	newHeavyHLine = []

	startHeavyVLine = []
	endHeavyVLine = []
	newHeavyVLine = []

	startHeavyHLine.append(margin_size+(3*line*cell_size)+3*cell_size)
	startHeavyHLine.append(margin_size)
	endHeavyHLine.append(margin_size+(3*line*cell_size)+3*cell_size)
	endHeavyHLine.append(margin_size)

	newHeavyHLine.append(startHeavyHLine)
	newHeavyHLine.append(endHeavyHLine)
	heavyLineList.append(newHeavyHLine)
'''

screen = pygame.display.set_mode([screen_size, screen_size])

running = True
while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill((255,255,255))

	
	for line in range(len(hLineList)):
		if(line%int(pow(value_count,0.5)) == 2 and line!=0):
			pygame.draw.lines(screen, (0,0,0), False, hLineList[line], heavy_line_weight)
		else:
			pygame.draw.lines(screen, (0,0,0), False, hLineList[line], light_line_weight)

	for line in range(len(vLineList)):
		if(line%int(pow(value_count,0.5)) == 2 and line!=0):
			pygame.draw.lines(screen, (0,0,0), False, vLineList[line], heavy_line_weight)
		else:
			pygame.draw.lines(screen, (0,0,0), False, vLineList[line], light_line_weight)
	pygame.draw.rect(screen, (0,0,0), (margin_size,margin_size,screen_size-(2*margin_size), screen_size-(2*margin_size)), heavy_line_weight)


	pygame.display.flip()

pygame.quit()