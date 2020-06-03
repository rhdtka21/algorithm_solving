# [파이썬 | BOJ | 9205] 맥주 마시면서 걸어가기

import sys
from collections import deque
read = sys.stdin.readline

def isPossible(point1, point2):
    dist = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    if dist <= 1000:
        return True
    else:
        return False

def bfs():
    check = [0 for _ in range(N+2)]
    q = deque()
    q.append(0)
    check[0] = 1
    while q:
        nowV = q.popleft()
        for nextV in edges[nowV]:
            if check[nextV] == 0:
                q.append(nextV)
                check[nextV] = 1
    
    if check[N+1] == 1:
        print("happy")
    else:
        print("sad")

for t in range(int(read())):
    N = int(read())
    beer = [20, 0]

    points = []
    for _ in range(N+2):
        points.append(tuple(map(int, read().split())))

    edges = [[] for _ in range(N+2)]

    # 0번은 집, N+1번은 도착지
    for i in range(N+2):
        for j in range(N+2):
            if i != j:
                if isPossible(points[i], points[j]):
                    edges[i].append(j)
    
    bfs()
    