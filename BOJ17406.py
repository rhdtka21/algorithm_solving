# [파이썬 | BOJ | 17406] 배열 돌리기 4
import sys
from copy import deepcopy
from collections import deque
read = sys.stdin.readline
minAns = sys.maxsize

def case(depth, r, ret):
    if depth == r:
        solve(ret)
        return
    for i in range(K):
        if c[i] == 0:
            c[i] = 1
            case(depth+1, r, ret + str(i))
            c[i] = 0

def solve(p):
    global minAns
    def rotate(nowR, nowC, s):
        dlst = [deque() for _ in range(s)]

        #lst to dlst
        for i in range(1, s+1):
            for c in range(nowC-i, nowC+i):
                dlst[i-1].append(lst[nowR-i][c])
            for r in range(nowR-i, nowR+i):
                dlst[i-1].append(lst[r][nowC+i])
            for c in reversed(range(nowC-i+1, nowC+i+1)):
                dlst[i-1].append(lst[nowR+i][c])
            for r in reversed(range(nowR-i+1, nowR+i+1)):
                dlst[i-1].append(lst[r][nowC-i])
        
        #rotate
        for i in range(s):
            dlst[i].appendleft(dlst[i].pop())

        #dlst to lst
        for i in range(1, s+1):
            index = 0
            for c in range(nowC-i, nowC+i):
                lst[nowR-i][c] = dlst[i-1][index]
                index += 1
            for r in range(nowR-i, nowR+i):
                lst[r][nowC+i] = dlst[i-1][index]
                index += 1
            for c in reversed(range(nowC-i+1, nowC+i+1)):
                lst[nowR+i][c] = dlst[i-1][index]
                index += 1
            for r in reversed(range(nowR-i+1, nowR+i+1)):
                lst[r][nowC-i] = dlst[i-1][index]
                index += 1

    lst = deepcopy(originLst)
    for pval in p:
        r, c, s = rotateOperation[int(pval)]
        rotate(r-1, c-1, s)
    ans = min(sum(lst[i]) for i in range(R))
    #print(ans)
    minAns = min(ans, minAns)

R, C, K = map(int, read().split())
originLst = [list(map(int, read().split())) for _ in range(R)]
rotateOperation = [list(map(int, read().split())) for _ in range(K)]

c = [0 for _ in range(K)]
case(0, K, '')

print(minAns)