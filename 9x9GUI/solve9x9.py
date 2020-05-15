#!/usr/bin/env python3

import pygame
from sudokuCalc import findBox, checkRow, checkCol, checkBox, solveBoard
from Textbox import TextBox
from drawSudoku import buildHLineList, buildVLineList
import config

def createTextboxes(bSize):
	allBoxes = []
	for tb in range(bSize*bSize):
		
		row = int(tb/bSize)
		col = tb%bSize
		
		newTB = TextBox(config.marginSize+(col*config.cellSize),config.marginSize+(row*config.cellSize), config.cellSize, config.cellSize, row, col)
		allBoxes.append(newTB)
	
	return allBoxes


def createBoard(usrInput, bSize):
	board= []
	for row in range(bSize):
		newRow = []
		for col in range(bSize):
			if(usrInput[(bSize*row)+col].col == col and usrInput[(bSize*row)+col].row == row): #Double check corresponding elements
				newRow.append(usrInput[(bSize*row)+col].value)
			else:
				print("Error in build")
				return -1
		board.append(newRow)
	return board

def outputBoard(usrGUI):
	for row in range(config.cpl):
		for col in range(config.cpl):
			usrGUI[row*config.cpl+col].value = config.solution[row][col]
			usrGUI[row*config.cpl+col].text = str(config.solution[row][col])
			usrGUI[row*config.cpl+col].update()
	return usrGUI

def runBoard():

	usrGUI = createTextboxes(config.cpl)
	
	hLines = buildHLineList()
	vLines = buildVLineList()


	clock = pygame.time.Clock()
	screen = pygame.display.set_mode([config.screenSize,config.screenSize])

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if not config.submit:
				for textbox in usrGUI:
					textbox.event_handler(event)

		screen.fill((128,128,128))
			
		if config.submit:
			if not config.output:
				boardResult = solveBoard(createBoard(usrGUI, config.cpl), 0, 0)
				if boardResult:
					usrGUI = outputBoard(usrGUI)
				else:
					print("No solution was found")
				config.output = True

		for box in usrGUI:
			box.draw(screen)
			
		for line in range(len(hLines)):
			if(line%int(pow(config.cpl,0.5)) == 2 and line!=0):
				pygame.draw.lines(screen, (0,0,0), False, hLines[line], config.heavy_line_weight)
			else:
				pygame.draw.lines(screen, (0,0,0), False, hLines[line], config.light_line_weight)
			
			
		for line in range(len(vLines)):
			if(line%int(pow(config.cpl,0.5)) == 2 and line!=0):
				pygame.draw.lines(screen, (0,0,0), False, vLines[line], config.heavy_line_weight)
			else:
				pygame.draw.lines(screen, (0,0,0), False, vLines[line], config.light_line_weight)

		pygame.draw.rect(screen, (0,0,0), (config.marginSize,config.marginSize,config.screenSize-(2*config.marginSize), config.screenSize-(2*config.marginSize)), config.heavy_line_weight)

		pygame.display.flip()
		clock.tick(50)

			
if __name__ == '__main__':
	runBoard()
	pygame.quit()