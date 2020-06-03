# [파이썬 | BOJ | 2468] 안전 영역
import sys
from collections import deque
read = sys.stdin.readline

# 상 하 좌 우
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs():
    check = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0
    for i in range(N*N):
        r, c = i // N, i % N
        if under[r][c] == 0 and check[r][c] == 0:
            cnt += 1
            q = deque()
            q.append([r,c])
            check[r][c] = cnt
            while q:
                nowR, nowC = q.popleft()
                for i in range(4):
                    nextR, nextC = nowR + d[i][0], nowC + d[i][1]
                    if 0<=nextR<N and 0<=nextC<N:
                        if under[nextR][nextC] == 0 and check[nextR][nextC] == 0:
                            q.append([nextR, nextC])
                            check[nextR][nextC] = check[nowR][nowC]
    #print(check)
    return cnt

def solve(height):
    for r in range(N):
        for c in range(N):
            if board[r][c] <= height :
                under[r][c] = 1
    return bfs()

N = int(read())
board = [list(map(int, read().split())) for _ in range(N)]
under = [[0 for _ in range(N)] for _ in range(N)]
maxHeight = max( max(board[i]) for i in range(N))

ans = -1
for i in range(maxHeight+1):
    ans = max(ans, solve(i))
print(ans)