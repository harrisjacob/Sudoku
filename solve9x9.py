#!/usr/bin/env python3

import pygame
from sudokuCMD import (fullLine, printBoard, findBox, checkRow, checkCol, checkBox, solveBoard)
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


def runBoard():

	usrInput = createTextboxes(config.cpl)
	
	hLines = buildHLineList()
	vLines = buildVLineList()


	clock = pygame.time.Clock()
	screen = pygame.display.set_mode([config.screenSize,config.screenSize])

	running = True
	while running:
		if not config.submit:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				for textbox in usrInput:
					textbox.event_handler(event)

			screen.fill((128,128,128))
			
			
			for box in usrInput:
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
		else:
			board = createBoard(usrInput, config.cpl)
			printBoard(board)
			running = False
		

	#if not solveBoard(board, 0, 0):
		#print("No solution could be found")


if __name__ == '__main__':
	runBoard()
	pygame.quit()