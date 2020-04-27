# [파이썬 | BOJ | 16234] 인구 이동

import sys
from collections import deque
sys.setrecursionlimit(10000)
read = sys.stdin.readline

#상 하 좌 우
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def dfs(startV, union):
    global total
    global cnt
    
    if visited[startV] != 0:
        return

    visited[startV] = union
    r, c = startV // N, startV % N
    total += A[r][c]
    cnt += 1
    for nextV in edge[startV]:
        dfs(nextV, union)

def bfs(startV, union):
    global total
    global cnt

    q = deque()
    q.append(startV)
    visited[startV] = union
    while q:
        nowV = q.popleft()
        r, c = nowV // N, nowV % N
        
        total += A[r][c]
        cnt += 1

        for nextV in edge[nowV]:
            if visited[nextV] == 0:
                q.append(nextV)
                visited[nextV] = union

def makeGraph():
    check = [0 for _ in range(num)]
    for i in range(num):
        check[i] = 1
        r, c = i // N, i % N
        for j in range(4):
            nr, nc = r + d[j][0], c + d[j][1]
            ni = nr * N + nc
            if (N > nr >= 0) and (N > nc >= 0) and check[ni] == 0:
                if R >= abs(A[nr][nc] - A[r][c]) >= L :
                    edge[i].append(ni)
                    edge[ni].append(i)

N, L, R = map(int, read().split())
num = N * N
A = []
ans = 0

for _ in range(N):
    A.append(list(map(int, read().split())))

while True:
    edge = [[] for _ in range(num)]
    visited = [0 for _ in range(num)]
    makeGraph()
    union = 1

    cal = [-1 for _ in range(1+num)]

    for i in range(num):
        total = 0
        cnt = 0
        if visited[i] == 0:   
            #bfs(i, union)      #211360KB	1648ms
            dfs(i, union)       #164320KB	1172ms
            #print(total//cnt)
            union += 1

        if cnt != 0:
            cal[union-1] = (total//cnt)
    
    #print(visited)
    #print(cal)

    idx = 0
    if visited[-1] == num:
        break

    for i in range(num):
        r, c = i//N, i%N
        A[r][c] = cal[visited[i]]
        
    #print(visited)
    #print(A)
    
    ans += 1

print(ans)