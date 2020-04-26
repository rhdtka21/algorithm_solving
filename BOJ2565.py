# [파이썬 | BOJ | 2565] 전깃줄
import sys
read = sys.stdin.readline

def lis(arr):
    dp = [0 for _ in range(len(arr))]
    dp[0] = 1
    for i in range(1, N):
        maxval = 0
        for j in reversed(range(i)):
            if arr[j] < arr[i] and maxval < dp[j]:
                maxval = dp[j]
        dp[i] = maxval + 1
    #print(dp)
    return max(dp)

N = int(read())

dp = [0 for _ in range(N)]
AB = []
for _ in range(N):
    AB.append(list(map(int,read().split())))
AB.sort()
B = []
for b in AB:
    B.append(b[1])
ans = lis(B)
print(N-ans)