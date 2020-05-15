#!/usr/bin/env python3

import config

pSize = 9
pSect = int(pow(pSize,0.5))

def fullLine():
	for i in range(pSize*3+pSize+1):
		print("-", end='')
	print()

def printBoard(printBoard):
	fullLine()
	for r in range(len(printBoard)):
		for c in range(len(printBoard[0])):
			if((c)%pSect==0):
				print(u'\u2551', end=' ')
			else:	
				print('| ', end='')
			print(printBoard[r][c], end = ' ')
		print(u'\u2551')

		if((r+1)%pSect == 0):
			fullLine()

def findBox(r, c):
	return int(r/pSect)*pSect+int(c/pSect)


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
	for row in range(int(b/pSect)*pSect, int(b/pSect)*pSect+pSect):
		for col in range((b%pSect)*pSect,(b%pSect)*pSect + pSect):
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

	if(r < 0 or r > pSize):
		return False

	if(c < 0 or c > pSize):
		return False

	if(trialBoard[r][c]!=0):
	
		if(c<pSize-1):
			return solveBoard(trialBoard, r, c+1)
		elif(r<pSize-1):
			return solveBoard(trialBoard, r+1, 0)
		else:
			copySolution(trialBoard)
			return True
	else:
		while(v <= pSize):
			if(checkRow(trialBoard, r, v) and checkCol(trialBoard, c, v) and checkBox(trialBoard, findBox(r, c), v)):
				trialBoard[r][c] = v

				if(c<pSize-1):
					if solveBoard(trialBoard, r, c+1):
						return True
				elif(r<pSize-1):
					if solveBoard(trialBoard, r+1, 0):
						return True
				else:
					copySolution(trialBoard)
					return True
			v+=1
		trialBoard[r][c] = 0
		return False

def main():

	board = [
[ 0, 0, 0, 0, 0, 6, 0, 8, 0],
[ 0, 0, 9, 1, 0, 5, 3, 7, 2],
[ 0, 8, 0, 7, 0, 0, 0, 1, 6],
[ 0, 0, 0, 0, 0, 0, 0, 3, 4],
[ 0, 0, 0, 3, 5, 1, 0, 0, 0],
[ 7, 3, 0, 0, 0, 0, 0, 0, 0],
[ 6, 1, 0, 0, 0, 8, 0, 2, 0],
[ 8, 2, 3, 9, 0, 4, 6, 0, 0],
[ 0, 7, 0, 6, 0, 0, 0, 0, 0]
]
	print("Input:")
	printBoard(board)
	print('\n')
	print('Solution:')
	if not solveBoard(board, 0, 0):
		print("No solution could be found")

if __name__ == '__main__':
	main()
