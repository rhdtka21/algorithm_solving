# [파이썬 | BOJ | 5557] 1학년
import sys
read = sys.stdin.readline

N = int(read())
arr = list(map(int, read().split()))
D = [[0 for _ in range(21)] for _ in range(N+1)]

D[1][arr[0]] = 1

for j in range(1, N):
    for i in range(21):
        if D[j][i] > 0:
            if 0 <= i-arr[j] <= 20:
                D[j+1][i-arr[j]] += (D[j][i])

            if 0 <= i+arr[j] <= 20:
                D[j+1][i+arr[j]] += (D[j][i])

print(D[N-1][arr[N-1]])