import math
from random import randint
CONST_SIZE = 9 #Please make sure that the size is a perfect square number


def getColoumn(index, arr2d):
    coloumn = []
    for row in arr2d:
        coloumn.append(row[index])
    return coloumn

def getInnerMatrix(rowIndex, colIndex, arr2d):
    innerMatrix = []
    sizeOfInnerMatrix = int(math.sqrt(CONST_SIZE))
    startRowIndex = 0
    startColIndex = 0
    while((startRowIndex + sizeOfInnerMatrix) <= rowIndex):
        startRowIndex+=sizeOfInnerMatrix
    while((startColIndex + sizeOfInnerMatrix) <= colIndex):
        startColIndex+=sizeOfInnerMatrix
    endRowIndex = startRowIndex + sizeOfInnerMatrix
    endColIndex = startColIndex + sizeOfInnerMatrix
    for i in range(startRowIndex, endRowIndex):
        for j in range(startColIndex, endColIndex):
            innerMatrix.append(arr2d[i][j])
    return innerMatrix




def find_empty_location(arr,l):
	for row in range(9):
		for col in range(9):
			if(arr[row][col]==0):
				l[0]=row
				l[1]=col
				return True
	return False
    
def solveBoard(arr2d):
    l=[0,0]
    if(not find_empty_location(arr2d, l)):
        return True
    row=l[0]
    col=l[1]
    for num in range(1,CONST_SIZE+1):
        safeList = getAllPossibleNumbersInPlace(row, col, arr2d)
        if num in safeList:
            arr2d[row][col] = num
            if(solveBoard(arr2d)):
                return True
            arr2d[row][col] = 0
    return False



def getAllPossibleNumbersInPlace(rowIndex, colIndex, arr2d):
    row = arr2d[rowIndex]
    col = getColoumn(colIndex, arr2d)
    innerMatrix = getInnerMatrix(rowIndex, colIndex, arr2d)
    posibilities = [x for x in range(1, CONST_SIZE+1) if ((x not in row) and (x not in col) and (x not in innerMatrix))]
    
    return posibilities



def printBoard(arr2d):
    for row in arr2d:
        print(row)




"""
board = makeBoard()
puzzle = makePuzzleBoard(board, "moderate")
printBoard(puzzle)
#puzzle is a 2-d array, try print(puzzle)
if solveBoard(puzzle):
    print("\n\n\nSolved Solution is: ")
    printBoard(puzzle)
else:
    print("No Solution Exist")
    """
