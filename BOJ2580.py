# [파이썬 | BOJ | 2580] 스도쿠

import sys
read = sys.stdin.readline

def myPrint(arr):
    for i in arr:
        for j in i:
            print(j, end=' ')
        print()

def check(nowI, nowJ, k):
    if k in sudoku[nowI]:
        return False

    for i in range(9):
        if sudoku[i][nowJ] == k:
            return False

    tempI, tempJ = nowI//3 * 3, nowJ//3 * 3
    for i in range(3):
        for j in range(3):
            if sudoku[tempI+i][tempJ+j] == k:
                return False

    return True

def DFS(idx):
    if idx == len(blank):
        myPrint(sudoku)
        sys.exit(0)
        return
    else:
        for k in range(1, 10):
            nowI, nowJ = blank[idx][0], blank[idx][1]
            if check(nowI, nowJ, k):
                sudoku[nowI][nowJ] = k
                DFS(idx+1)
                sudoku[nowI][nowJ] = 0

sudoku = []
blank = []

for i in range(9):
    sudoku.append(list(map(int, read().split())))

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append([i,j])

DFS(0) 