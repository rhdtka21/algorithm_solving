# [파이썬 | BOJ | 2644] 촌수계산
import sys
from collections import deque
read = sys.stdin.readline

N = int(read())
A, B = map(int, read().split())
M = int(read())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, read().split())
    edges[x].append(y)
    edges[y].append(x)
check = [-1 for _ in range(N+1)]

q = deque()
q.append(A)
check[A] = 0
while q:
    V = q.popleft()
    for nV in edges[V]:
        if check[nV] == -1:
            q.append(nV)
            check[nV] = check[V] + 1

print(check[B])