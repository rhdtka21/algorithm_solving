# [파이썬 | BOJ | 15686] 치킨 배달
import sys
read = sys.stdin.readline
INF = 999999

def chickenDistance():
    dist = 0
    aliveChicken = []
    for i in range(chickenNum):
        if checkPosition[i] == 1:
            aliveChicken.append(chickenPosition[i])

    for i in range(N):
        for j in range(N):
            if maps[i][j] == 1:
                temp = INF
                for ac in aliveChicken:
                    d = (abs(ac[0]-i) + abs(ac[1]-j)) 
                    if temp > d:
                        temp = d
                #print('t', temp)
                dist += temp
   
    return dist

def solve(cnt, idx):
    global ans
    
    if cnt == M:
        cd = chickenDistance()
        if ans > cd:
            ans = cd
        return

    for i in range(chickenNum):
        if i > idx:
            checkPosition[i] = 1
            solve(cnt+1, i)
            checkPosition[i] = 0

N, M = map(int, read().split())
maps = []
chickenPosition = []
ans = INF
for _ in range(N):
    maps.append(list(map(int, read().split())))

for i in range(N):
    for j in range(N):
        if maps[i][j] == 2:
            chickenPosition.append([i,j])

chickenNum = len(chickenPosition)
checkPosition = [0 for _ in range(chickenNum)]

solve(0, -1)
print(ans)
