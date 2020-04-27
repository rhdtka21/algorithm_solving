# [파이썬 | BOJ | 3190] 뱀

import sys
from collections import deque
read = sys.stdin.readline
 
def printBoard():
    for x in board:
        print(x)
    print('-------------------------------')
 
def rotate(case, char):
    if char == 'D':
        if case < 3:
            return case + 1
        else:
            return 0
    else:
        if case > 0:
            return case - 1
        else:
            return 3
 
#방향 : 오른쪽, 아래, 왼쪽, 위쪽 ([r, c])
direction = deque([[0, 1], [1, 0], [0, -1], [-1, 0]])
    
N = int(read())
K = int(read())
sec = 0
 
apples = []
snake = deque()
snake.append([1,1,0])
 
for _ in range(K):
    apples.append(list(map(int, read().split())))
 
L = int(read())
moveSec = []
moveDir = []
for _ in range(L):
    tempSec, tempDir = read().split()
    moveSec.append(int(tempSec))
    moveDir.append(tempDir)
 
board = [[0 for _ in range(N+2)] for _ in range(N+2)]
 
#벽치기
for i in range(N+2):
    board[0][i] = -1
    board[N+1][i] = -1
    board[i][0] = -1
    board[i][N+1] = -1
 
#사과 놓기
for apple in apples:
    r, c = apple
    board[r][c] = 2
 
#뱀 초기위치
for i in range(len(snake)):
    r, c, d = snake[i]
    board[r][c] = 1
 
#printBoard()
endPoint = False
 
#print(moveSec, moveDir)
 
for sec in range(0, 11111):
    #print(sec)
    prevDir = snake[0][2]
    for i in range(len(snake)):
        for j in range(len(moveSec)):
            if (sec-i) == moveSec[j]:
                snake[i][2] = rotate(snake[i][2], moveDir[j])
 
        r, c, d = snake[i]
        dr, dc = direction[d]
        nr, nc = r+dr, c+dc
 
        if board[nr][nc] == 0:
            board[r][c] = 0
            board[nr][nc] = 1
 
            snake[i][0] = nr
            snake[i][1] = nc
 
        elif board[nr][nc] == -1:
            endPoint = True
            break
 
        elif board[nr][nc] == 1 and i == 0:
            endPoint = True
            break
        
        elif board[nr][nc] == 2:
            board[nr][nc] = 1
            d = snake[0][2]
 
            snake[0][2] = prevDir
            snake.appendleft([nr, nc, d])
            
            break
 
    #print('뱀', snake)
    #printBoard()
    if endPoint:
        break
 
print(sec+1)