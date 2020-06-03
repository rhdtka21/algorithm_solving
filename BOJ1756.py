# [파이썬 | BOJ | 1756] 피자 굽기

import sys
read = sys.stdin.readline
inf = sys.maxsize

D, N = map(int, read().split())
oven = list(map(int, read().split()))
pizza = list(map(int, read().split()))

for i in range(1, D):
    oven[i] = min(oven[i], oven[i-1])

pizzaIdx = 0
depth = D-1
for i in reversed(range(D)):
    if pizzaIdx >= len(pizza):
        print(depth+1)
        sys.exit(0)

    if oven[i] >= pizza[pizzaIdx]:
        pizzaIdx += 1
        depth = i

print(0)
