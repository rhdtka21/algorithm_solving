# [파이썬 | BOJ | 5014] 스타트링크

import sys
from collections import deque
read = sys.stdin.readline

def solve(start):

    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        now = q.popleft()
        if now == G:
            print(visited[G]-1)
            return

        if now + U <= F and visited[now + U] == 0:
            visited[now + U] = visited[now] + 1
            q.append(now + U)
        if now - D > 0 and visited[now - D] == 0:
            visited[now - D] = visited[now] + 1
            q.append(now - D)

    print("use the stairs")

F, S, G, U, D = map(int, read().split())
visited = [0 for _ in range(F+1)]
solve(S)
