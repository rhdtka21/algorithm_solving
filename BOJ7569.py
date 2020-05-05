# [파이썬 | BOJ | 7569] 토마토

import sys
from collections import deque
read = sys.stdin.readline

#상 하 좌 우 위 아래 (h, r, c)
d = [[0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1], [1, 0, 0], [-1, 0, 0]]

C, R, H = map(int, read().split())
tomato = [[[] for _ in range(R)] for _ in range(H)]
check = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(H)]
q = deque()
for h in range(H):
    for r in range(R):
        tomato[h][r] = list(map(int, read().split()))
        for c, t in enumerate(tomato[h][r]):
            if t == 1:
                q.append([h, r, c])
                check[h][r][c] = 1
            elif t == -1:
                check[h][r][c] = -1

while q:
    nowH, nowR, nowC = q.popleft()
    for i in range(6):
        nextH, nextR, nextC = nowH + d[i][0], nowR + d[i][1], nowC + d[i][2]
        if 0<=nextH<H and 0<=nextR<R and 0<=nextC<C:
            #next위치가 안익은 토마토이고, 방문하지 않았으면 방문 ㄱㄱ
            if check[nextH][nextR][nextC] == 0 and tomato[nextH][nextR][nextC] == 0:
                q.append([nextH, nextR, nextC])
                check[nextH][nextR][nextC] = check[nowH][nowR][nowC] + 1

maxVal = -1
temp = []
for board in check:
    for row in board:
        if row.count(0) > 0:
            print(-1)
            sys.exit(0)
        temp.append(max(row))
      
print(max(temp)-1)