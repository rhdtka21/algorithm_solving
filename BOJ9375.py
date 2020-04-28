# [파이썬 | BOJ | 9375] 패션왕 신해빈

import sys
read = sys.stdin.readline

T = int(read())

for _ in range(T):
    ans = 0
    check = [1 for _ in range(31)]
    
    N = int(read())
    temp = []
    cnt = -1
    for _ in range(N):
        a, b = map(str, read().split())
        if not b in temp:
            temp.append(b)
            cnt += 1
            check[cnt] += 1
        else:
            check[temp.index(b)] += 1
    M = len(temp)

    t = 1

    for i in range(check.index(1)):
        t *= check[i]
    print(t-1)
