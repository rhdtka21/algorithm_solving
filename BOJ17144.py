# [파이썬 | BOJ | 17144] 미세먼지 안녕!

import sys
read = sys.stdin.readline
# 상 하 좌 우
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
cleaner = []

def myPrint(arr):
    for a in arr:
        print(a)
    print()

def copy(board, temp):
    for r in range(R):
        for c in range(C):
            board[r][c] = temp[r][c]

def diffusion():
    temp = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if board[r][c] == 0:
                continue
            if board[r][c] == -1:
                cleaner.append(r)
                continue
            temp[r][c] += board[r][c]
            for i in range(4):
                nr, nc = r + d[i][0], c + d[i][1]
                if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != -1:
                    subval = (board[r][c] // 5)
                    temp[nr][nc] += subval
                    temp[r][c] -= subval
    temp[cleaner[0]][0] = -1
    temp[cleaner[1]][0] = -1
    
    copy(board, temp)

def rotate():
    temp = board[0][0]
    for r in range(R):
        for c in range(C):
            if r == 0 and 1 <= c < C:
                board[r][c-1] = board[r][c]
            elif c == C-1 and 1 <= r <= cleaner[0]:
                board[r-1][c] = board[r][c]

            if r == R-1 and 1 <= c < C:
                board[r][c-1] = board[r][c]
            elif c == 0 and cleaner[1]+1 <= r < R:
                board[r-1][c] = board[r][c]

    for r in reversed(range(R)):
        for c in reversed(range(C)):
            if r == cleaner[0] and 0 <= c < C-1:
                board[r][c+1] = board[r][c]
            elif c == 0 and 0 <= r < cleaner[0]:
                board[r+1][c] = board[r][c]

            if r == cleaner[1] and 0 <= c < C-1:
                board[r][c+1] = board[r][c]
            elif c == C-1 and cleaner[1] <= r < R-1:
                board[r+1][c] = board[r][c]

    board[1][0] = temp
    board[cleaner[0]][1] = 0
    board[cleaner[0]][0] = 0
    board[cleaner[1]][0] = 0
    board[cleaner[1]][1] = 0
    
    #myPrint(board)
    
def dust():
    ret = 0
    for r in reversed(range(R)):
        for c in reversed(range(C)):
            ret += board[r][c]
    return ret

R, C, T = map(int, read().split())
board = []
for _ in range(R):
    board.append(list(map(int, read().split())))

for t in range(T):
    diffusion()
    rotate()
    ans = dust()

print(ans)