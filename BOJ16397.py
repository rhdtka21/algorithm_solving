# [파이썬 | BOJ | 16397] 탈출(홍익대 프로그래밍 대회)

import sys
from math import log10
from collections import deque
read = sys.stdin.readline

def calA(n):
    return n+1

def calB(n):
    if n == 0:
        return 0
    n *= 2
    if n > 99999:
        return -1
    d = int(log10(n))
    return n - 10 ** d

def solve():
    global minAns

    q = deque()
    q.append([N, 0])
    check[N] =1
    while q:
        num, cnt = q.popleft()
        #print(num, cnt, G)
        if cnt > T:
            break
        if num == G:
            if minAns > cnt:
                minAns = cnt
                #print(num, cnt, G)
            continue
        nextNum = calA(num)
        if 0 <= nextNum <= 99999:
            if check[nextNum] == 0:
                q.append([nextNum, cnt+1])
                check[nextNum] = 1
        
        nextNum = calB(num)
        if 0 <= nextNum <= 99999:
            if check[nextNum] == 0:
                q.append([nextNum, cnt+1])
                check[nextNum] = 1

check = [0 for _ in range(100000)]
N, T, G = map(int, read().split())

minAns = T+1
solve()
print(minAns if minAns != T+1 else "ANG")
