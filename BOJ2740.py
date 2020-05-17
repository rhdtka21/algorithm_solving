# [파이썬 | BOJ | 2740] 행렬 곱셈

import sys
read = sys.stdin.readline

mat1 = []
mat2 = []
N, M = map(int, read().split())
for _ in range(N):
    mat1.append(list(map(int, read().split())))

M, K = map(int, read().split())
for _ in range(M):
    mat2.append(list(map(int, read().split())))

ansmat = [[0 for _ in range(K)] for _ in range(N)]
for i in range(N):
    for j in range(K):
        temp = 0
        for k in range(M):
            temp += mat1[i][k] * mat2[k][j]
        ansmat[i][j] = temp

for vec in ansmat:
    for v in vec:
        print(v, end=' ')
    print()