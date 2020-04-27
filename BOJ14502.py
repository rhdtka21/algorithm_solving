# [파이썬 | BOJ | 14502] 연구소

import sys
from queue import deque
read = sys.stdin.readline
p = [[-1,0],[1,0],[0,-1],[0,1]]
maxAns = -1
def cpyLab(a):
    '''
    b = []
    for i in a:
        b.append(i)
 
    잘은 모르겠지만 파이썬 자료구조상의 이유로 복사가 되지않고, 포인터가 복사되는듯하다. 
    즉 b와 a가 동일한 주소의 이차원 배열을 가리키게 되어서 cpy의 목적에 맞지 않게된다.  
    '''
 
    b = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            b[i][j] = a[i][j]
    return b
 
def coronaVirus(originLab):
    global maxAns
 
    tempLab = cpyLab(originLab)
    q = deque()
    for i in range(N):
        for j in range(M):
            if tempLab[i][j] == 2:
                q.append([i,j])
 
    while q:
        nowI, nowJ = map(int, q.popleft())
        for i in range(4):
            nextI, nextJ = nowI + p[i][0], nowJ + p[i][1]
            if nextI >= 0 and nextI < N and nextJ >= 0 and nextJ < M:
                if tempLab[nextI][nextJ] == 0:
                    tempLab[nextI][nextJ] = 2
                    q.append([nextI, nextJ])
    ans = 0
    for i in tempLab:
        ans += i.count(0)
    if ans > maxAns:
        maxAns = ans
    return
 
def Wall(cnt):
    if cnt == 3:
        coronaVirus(originLab)
        return
    else:
        for i in range(N):
            for j in range(M):
                if originLab[i][j] == 0:
                    originLab[i][j] = 1
                    Wall(cnt+1)
                    originLab[i][j] = 0
 
N, M = map(int, read().split())
originLab = []
 
for _ in range(N):
    originLab.append(list(map(int, read().split())))
 
Wall(0)
print(maxAns)