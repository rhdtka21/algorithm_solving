# [파이썬 | BOJ | 11404] 플로이드
import sys
read = sys.stdin.readline
INF = 10000000

N = int(read())
T = int(read())
D = [[[INF for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]
for _ in range(T):
    a, b, c = map(int, read().split())
    if D[0][a][b] > c:
        D[0][a][b] = c
for i in range(1, N+1):
    D[0][i][i] = 0
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if D[k-1][i][j] > D[k-1][i][k] + D[k-1][k][j]:
                D[k][i][j] = D[k-1][i][k] + D[k-1][k][j]
            else:
                D[k][i][j] = D[k-1][i][j]
for i in range(1, N+1):
    for x in D[N][i][1:]:
        if x == INF:
            print(0, end=' ')
        else:
            print(x, end=' ')
    print()