#!/usr/bin/env python3

pSize = 9
pSect = pow(pSize,0.5)

def fullLine():
	for i in range(pSize*3+pSize+1):
		print("-", end='')
	print()


def printBoard():
	fullLine()
	for r in range(len(board)):
		for c in range(len(board[0])):
			if((c)%pSect==0):
				print(u'\u2551', end=' ')
			else:	
				print('| ', end='')
			print(board[r][c], end = ' ')
		print(u'\u2551')

		if((r+1)%pSect == 0):
			fullLine()



board = [
[ 0, 1, 2, 3, 4, 5, 6, 7, 8],
[ 0, 1, 2, 3, 4, 5, 6, 7, 8],
[ 0, 1, 2, 3, 4, 5, 6, 7, 8],
[ 0, 1, 2, 3, 4, 5, 6, 7, 8],
[ 0, 1, 2, 3, 4, 5, 6, 7, 8],
[ 0, 1, 2, 3, 4, 5, 6, 7, 8],
[ 0, 1, 2, 3, 4, 5, 6, 7, 8],
[ 0, 1, 2, 3, 4, 5, 6, 7, 8],
[ 0, 1, 2, 3, 4, 5, 6, 7, 8]
]
printBoard()
