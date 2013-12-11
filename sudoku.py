import sys
import time

def isValid(i,j,Num, matrix):
    if matrix[i][j] != 0:
        return False
    return checkRow(i, Num, matrix) and checkCol(j,Num, matrix) \
        and checkBox(i,j,Num, matrix)

def checkRow(i, Num, matrix):
    for p in range(0,9):
        if matrix[i][p] == Num:
            return False
    return True

def checkCol(j,Num, matrix):
    for p in range(0,9):
        if matrix[p][j] == Num:
            return False
    return True

def checkBox(i,j,Num, matrix):
    i = (i // 3) * 3
    j = (j // 3) * 3
    for r in range (0,3):
        for c in range (0,3):
            if( matrix[i+r][j+c] == Num ):
                return False
    return True

def initializeMatrix():
    '''Change this puzzel to whatever you want.'''
    matrix = [[0,0,0,0,0,0,0,8,0],
              [0,8,0,0,0,0,0,0,0],
              [0,0,0,0,7,0,0,0,0],
              [0,0,0,0,0,0,0,5,0],
              [0,0,0,0,0,0,4,0,0],
              [0,6,0,0,0,0,0,0,1],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,7,0],
              [1,0,0,0,0,0,0,0,0]]
              
    return matrix
	

def printMatrix(matrix):
    j = 0
    for e in matrix:
        i = 0
        j = j + 1
        for g in e:
            print (g, end = " ")
            i = i + 1
            if i == 3:
                i = 0
                print("|", end ="")
        print()
        if j == 3:
            j = 0
            print ("_____________________")
    

def solveNext(i,j,matrix):
    if j < 8:
        return solveMatrix(i,j+1,matrix)
    else:
        return solveMatrix(i+1,0,matrix)


def deletePrevious(i,j,matrix):
    if j > 0:
        matrix[i][j-1] = 0
    else:
        matrix[i-1][8] = 0

def solveMatrix(i,j,matrix):
    if i > 8:
        print("Final Solution:")
        printMatrix(matrix)
        print("Solved!!")
        raise NameError("Solved")
        #sys.exit(0)
        return True

    elif matrix[i][j] != 0:
        solveNext(i,j,matrix)
        return True
    else:
        numbers = [9,8,7,6,5,4,3,2,1]
        
        while True:
            matrix[i][j] = 0            
            if len(numbers) == 0:
                matrix[i][j] = 0
                #print("previous")
                #deletePrevious(i,j,matrix)
                #printMatrix(matrix)
                return False
            new_num = numbers.pop()
            if isValid(i,j,new_num, matrix):
                matrix[i][j] = new_num
                #print("next")
                #printMatrix(matrix)
                solveNext(i,j,matrix)

def main():
    '''This is the main Program.'''
    print("This is the input Soduku Puzzel:")
    matrix = initializeMatrix() #To Change the input matrix, modify this 
                                #function.
    printMatrix(matrix)
    input("press enter to solve.")
    try:
        solveMatrix(0,0,matrix)
    except NameError:
        print("Done!!!")
    else:
        print("No Solution exists")
        
if __name__ == '__main__':
    main()
