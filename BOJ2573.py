# [파이썬 | BOJ | 2573] 빙산

import sys
from collections import deque
read = sys.stdin.readline

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

R, C = map(int, read().split())
board = [list(map(int, read().split())) for _ in range(R)]

def myprint(arr):
    for a in arr:
        print(a)
    print()

def adjacent(r, c):
    cnt = 0
    for i in range(4):
        nr, nc = r + d[i][0], c + d[i][1]
        if 0<=nr<R and 0<=nc<C and board[nr][nc] == 0:
            cnt += 1
    return cnt

def bfs():
    check = [[0 for _ in range(C)] for _ in range(R)]
    cnt = 0
    for i in range(R*C):
        r, c = i // C , i % C
        if board[r][c] > 0 and check[r][c] == 0:
            cnt += 1
            q = deque()
            q.append([r, c])
            check[r][c] = 1
            while q:
                nowR, nowC = q.popleft()
                for i in range(4):
                    nextR, nextC = nowR + d[i][0], nowC + d[i][1]
                    if 0<=nextR<R and 0<=nextC<C:
                        if board[nextR][nextC] > 0 and check[nextR][nextC] == 0:
                            q.append([nextR, nextC])
                            check[nextR][nextC] = 1
    #print(cnt)
    return cnt

year = 0
while True:
    year += 1
    temp = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if board[r][c] > 0:
                temp[r][c] = adjacent(r, c)

    for r in range(R):
        for c in range(C):
            if board[r][c] > 0:
                board[r][c] = max(0, board[r][c] - temp[r][c])

    #myprint(board)
    if bfs() > 1:
        break
    
    if sum(sum(board[i]) for i in range(R)) == 0:
        year = 0
        break
    
print(year)
