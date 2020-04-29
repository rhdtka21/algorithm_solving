# [파이썬 | BOJ | 17822] 원판 돌리기

import sys
from collections import deque
read = sys.stdin.readline

# 상 하 좌 우
drdc = [[-1, 0], [1, 0], [0, -1], [0, 1]]

N, M, T = map(int, read().split())
circle = [deque([0 for _ in range(M)])]
for _ in range(N):
    circle.append(deque(map(int, read().split())))
circle.append(deque([0 for _ in range(M)]))
x = []
d = []
k = []

for _ in range(T):
    # d가 0인 경우는 시계 방향, 1인 경우는 반시계 방향이다.
    X, D, K = map(int, read().split())
    x.append(X)
    d.append(D)
    k.append(K)

#print(circle)
for index in range(T):
    X, D, K = x[index], d[index], k[index]
    tx = X

    while tx <= N:
        for _ in range(K):
            if D == 0:
                circle[tx].appendleft(circle[tx].pop())
            else:
                circle[tx].append(circle[tx].popleft())
        tx += X
    flag = True
    sumVal = 0
    cntVal = 0
    for r in range(1, N+1):
        for c in range(M):
            if circle[r][c] <= 0:
                continue
            sumVal += circle[r][c]
            cntVal += 1

            for i in range(4):
                nr, nc = r + drdc[i][0], c + drdc[i][1]                
                if nc == -1:
                    nc = M-1
                elif nc == M:
                    nc = 0
                
                if circle[r][c] == abs(circle[nr][nc]):
                    circle[r][c] *= -1
                    if circle[nr][nc] > 0:
                        circle[nr][nc] *= -1
                    flag = False
    for r in range(1, N+1):
        for c in range(M):
            if circle[r][c] < 0:
                circle[r][c] = 0
    #print(circle)
    
    if flag and cntVal > 0:
        avgVal = sumVal/cntVal
        #print(avgVal)
        for r in range(1, N+1):
            for c in range(M):
                if circle[r][c] == 0:
                    continue
                if circle[r][c] > avgVal:
                    circle[r][c] -= 1
                elif circle[r][c] < avgVal:
                    circle[r][c] += 1
    #print(circle)

ans = 0
for r in range(1, N+1):
    for c in range(M): 
        ans += circle[r][c]
print(ans)