#!/usr/bin/env python3

import config

def fullLine():
	for i in range(config.cpl*3+config.cpl+1):
		print("-", end='')
	print()

def printBoard(printBoard):
	fullLine()
	for r in range(len(printBoard)):
		for c in range(len(printBoard[0])):
			if((c)%config.sectors==0):
				print(u'\u2551', end=' ')
			else:	
				print('| ', end='')
			print(printBoard[r][c], end = ' ')
		print(u'\u2551')

		if((r+1)%config.sectors == 0):
			fullLine()

def findBox(r, c):
	return int(r/config.sectors)*config.sectors+int(c/config.sectors)


def checkRow(checkBoard, r, v):
	for it in checkBoard[r]:
		if it == v:
			return False
	return True

def checkCol(checkBoard, c, v):
	for row in checkBoard:
		if row[c] == v:
			return False
	return True

def checkBox(checkBoard, b, v):
	for row in range(int(b/config.sectors)*config.sectors, int(b/config.sectors)*config.sectors+config.sectors):
		for col in range((b%config.sectors)*config.sectors,(b%config.sectors)*config.sectors + config.sectors):
			if checkBoard[row][col] == v:
				return False
	return True

def copySolution(solved):
	for row in range(config.cpl):
		newRow = []
		for col in range(config.cpl):
			newRow.append(solved[row][col])
		config.solution.append(newRow)


def solveBoard(trialBoard, r, c):
	
	v=0

	if(r < 0 or r > config.cpl):
		return False

	if(c < 0 or c > config.cpl):
		return False

	if(trialBoard[r][c]!=0):
	
		if(c<config.cpl-1):
			return solveBoard(trialBoard, r, c+1)
		elif(r<config.cpl-1):
			return solveBoard(trialBoard, r+1, 0)
		else:
			copySolution(trialBoard)
			return True
	else:
		while(v <= config.cpl):
			if(checkRow(trialBoard, r, v) and checkCol(trialBoard, c, v) and checkBox(trialBoard, findBox(r, c), v)):
				trialBoard[r][c] = v

				if(c<config.cpl-1):
					if solveBoard(trialBoard, r, c+1):
						return True
				elif(r<config.cpl-1):
					if solveBoard(trialBoard, r+1, 0):
						return True
				else:
					copySolution(trialBoard)
					return True
			v+=1
		trialBoard[r][c] = 0
		return False

