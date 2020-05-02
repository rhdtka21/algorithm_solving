# [파이썬 | BOJ | 17413] 낚시왕

import sys
read = sys.stdin.readline

def myprint(arr):
    for a in arr:
        print(a)
    print()

def swap(direction):
    if direction == 1:
        return 2
    elif direction == 2:
        return 1
    elif direction == 3:
        return 4
    elif direction == 4:
        return 3

def sharkToBoard():
    board = [[[] for _ in range(C)] for _ in range(R)]
    for eachShark in sharks:
        if len(eachShark) < 6:
            continue
        idx = eachShark[0]
        sharkR, sharkC = eachShark[1], eachShark[2]
        speed = eachShark[3]
        direction = eachShark[4]
        size = eachShark[5]

        board[sharkR-1][sharkC-1].append([idx, speed, direction, size])
        board[sharkR-1][sharkC-1].sort(key = lambda x : -x[3])
        if len(board[sharkR-1][sharkC-1]) > 1:
            sharks[board[sharkR-1][sharkC-1][1][0]].clear()
        board[sharkR-1][sharkC-1] = board[sharkR-1][sharkC-1][:1]

    return board
    
#위 아래 오른쪽 왼쪽 
d = [[-1, 0], [1, 0], [0, 1], [0, -1]]

R, C, M = map(int, read().split())
#r, c, s, d, z
#(r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기이다.
#d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미한다.
sharks = [[i] + list(map(int, read().split())) for i in range(M)]
temp = [[] for _ in range(M)]

fisher = 0
ans = 0

#board init
board = sharkToBoard()
#myprint(board)

while fisher <C:
    fisher += 1
    #print("낚시꾼위치 ", fisher)
    #낚시꾼이 잡는다.
    
    deadShark = -1
    for r in range(R):
        if board[r][fisher-1]:
            deadShark = (board[r][fisher-1][0][0])
            ans += board[r][fisher-1][0][3]
            board[r][fisher-1].clear()
            break

    if deadShark > -1:
        #print(ans)
        sharks[deadShark].clear()
    #print("상어잡음.")
    #myprint(sharks)
    
    #상어 이동
    for eachShark in sharks:
        if len(eachShark) < 6:
            continue
        index = eachShark[0]
        sharkR, sharkC = eachShark[1]-1, eachShark[2]-1
        speed = eachShark[3]
        direction = eachShark[4]
        size = eachShark[5]
        
        if direction == 1:
            directionTemp = ((speed - (sharkR + 1)) // (R-1)) + 1
            if directionTemp % 2:
                direction = swap(direction)
                
            idx = (R-1) - sharkR
            idx = (idx + speed) % (2*(R-1))
            if idx >= R-1:
                idx = 2*(R-1) - idx
            idx = (R-1) - idx

            nextR = idx
            nextC = sharkC
            
        elif direction == 2:
            directionTemp = ((speed - (R - sharkR)) // (R-1)) + 1
            if directionTemp % 2:
                direction = swap(direction)
            
            idx = sharkR
            idx = (idx + speed) % (2*(R-1))
            if idx >= R-1:
                idx = 2*(R-1) - idx

            nextR = idx
            nextC = sharkC
            
        elif direction == 3:
            directionTemp = ((speed - (C - sharkC)) // (C-1)) + 1
            if directionTemp % 2:
                direction = swap(direction)
            
            
            idx = sharkC
            idx = (idx + speed) % (2*(C-1))
            if idx >= C-1:
                idx = 2*(C-1) - idx

            nextR = sharkR
            nextC = idx
            
        elif direction == 4:
            directionTemp = ((speed - (sharkC + 1)) // (C-1)) + 1
            if directionTemp % 2:
                direction = swap(direction)
            
            idx = (C-1) - sharkC
            idx = (idx + speed) % (2*(C-1))
            if idx >= C-1:
                idx = 2*(C-1) - idx
            idx = (C-1) - idx
            
            nextR = sharkR
            nextC = idx
                    
        sharks[index] = [index, nextR+1, nextC+1, speed, direction, size]

    #print("상어이동함..")
    #myprint(board)
    #myprint(sharks)
    #print("board이동..")
    #같은곳에 상어가 두마리 이상이 있으면 큰애만 살아남는다.
    
    board = sharkToBoard()
    #myprint(board)
        
#myprint(sharks)
print(ans)