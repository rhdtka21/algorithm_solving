# [파이썬 | BOJ | 16469] 소년 점프

import sys
from collections import deque
read = sys.stdin.readline
minAns = sys.maxsize
cnt = 0
#상 하 좌 우
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def myprint(arr):
    for a in arr:
        print(a)
    print()

def bfs(br, bc, idx):
    q = deque()
    q.append([br, bc])
    distance[idx][br][bc] = 0
    while q:
        nowR, nowC = q.popleft()
        for i in range(4):
            nextR, nextC = nowR + d[i][0], nowC + d[i][1]
            if 0 <= nextR < R and 0 <= nextC < C:
                if distance[idx][nextR][nextC] == -1 and board[nextR][nextC] == 0:
                    q.append([nextR, nextC])
                    distance[idx][nextR][nextC] = distance[idx][nowR][nowC] + 1

R, C = map(int, read().split())
board = [[0 for _ in range(C)] for _ in range(R)]
for j in range(R):
    temp = read().replace('\n', '')
    for i, t in enumerate(temp):
        board[j][i] = int(t)

billon = []
for _ in range(3):
    x, y= map(int, read().split())
    billon.append([x-1, y-1])


distance = [[[-1 for _ in range(C)] for _ in range(R)] for _ in range(3)]

for idx in range(3):
    bfs(billon[idx][0], billon[idx][1], idx)



for r in range(R):
    for c in range(C):
        if distance[0][r][c] < 0 or distance[1][r][c] < 0 or distance[2][r][c] < 0:
            continue
        ans = max(distance[0][r][c], distance[1][r][c], distance[2][r][c])
        if minAns > ans:
            minAns = ans
            cnt = 1
        elif minAns == ans:
            cnt += 1
        

if minAns == sys.maxsize:
    print(-1)
else:
    print(minAns)
    print(cnt)
