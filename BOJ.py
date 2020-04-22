# [파이썬 | BOJ | 10815] 숫자 카드

import sys
read = sys.stdin.readline
 
N = int(read())
card = [0 for _ in range(20000001)]
arr = list(map(int, read().split()))
for a in arr:
    card[a+10000000] = 1
M = int(read())
arr2 = list(map(int, read().split()))
ans = 0
for a in arr2:
    print(card[a+10000000], end=' ')