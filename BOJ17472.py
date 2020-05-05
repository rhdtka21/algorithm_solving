# [파이썬 | BOJ | 17472] 다리 만들기 2

import sys
from collections import deque
read = sys.stdin.readline
minAns = sys.maxsize
#상 하 좌 우
drdc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
BUILD = True    
UNBUILD = False

def myprint(arr):
    for a in arr:
        print(a)
    print()

def findIsland():
    countryNum = 1
    for i in range(R*C):
        r, c = i // C, i % C
        if cell[r][c] == 1 and not visited[r][c]:
            #bfs
            if not visited[r][c]:
                q = deque()
                q.append([r, c])
                visited[r][c] = countryNum
                while q:
                    nowR, nowC = q.popleft()
                    for i in range(4):
                        nextR, nextC = nowR + drdc[i][0], nowC + drdc[i][1]
                        if 0 <= nextR < R and 0 <= nextC < C and not visited[nextR][nextC]:
                            if cell[nextR][nextC] == 1:
                                q.append([nextR, nextC])
                                visited[nextR][nextC] = countryNum
            countryNum += 1
    return countryNum -1

#country에서 다른 섬들까지 섬 건설가능 여부 및 다리 길이
def buildBridge(country):
    bridgeLens = [30 for _ in range(countryNum + 1)]
    for i in range(R*C):
        nowR, nowC = i // C, i % C
        if visited[nowR][nowC] == country:
            #좌 탐색
            cnt0 = 0
            dest = 0
            for c in reversed(range(nowC)):
                if visited[nowR][c] != country:
                    if visited[nowR][c] == 0:
                        cnt0 += 1
                    else:
                        if cnt0 > 1:
                            dest = visited[nowR][c]
                            bridgeLens[dest] = min(bridgeLens[dest], cnt0)
                        break
                else:
                    cnt0 = 0
    
    
            cnt0 = 0
            dest = 0
            #우 탐색
            for c in range(nowC+1, C):
                if visited[nowR][c] != country:
                    if visited[nowR][c] == 0:
                        cnt0 += 1
                    else:
                        if cnt0 > 1:
                            dest = visited[nowR][c]
                            bridgeLens[dest] = min(bridgeLens[dest], cnt0)
                        break
                else:
                    cnt0 = 0
    
            
            #상 탐색
            cnt0 = 0
            dest = 0
            for r in reversed(range(nowR)):
                if visited[r][nowC] != country:
                    if visited[r][nowC] == 0:
                        cnt0 += 1
                    else:
                        if cnt0 > 1:
                            dest = visited[r][nowC]
                            bridgeLens[dest] = min(bridgeLens[dest], cnt0)
                        break
                else:
                    cnt0 = 0
    
            cnt0 = 0
            dest = 0
            #하 탐색
            for r in range(nowR+1, R):
                if visited[r][nowC] != country:
                    if visited[r][nowC] == 0:
                        cnt0 += 1
                    else:
                        if cnt0 > 1:
                            dest = visited[r][nowC]
                            bridgeLens[dest] = min(bridgeLens[dest], cnt0)
                        break
                else:
                    cnt0 = 0
    
    
    return bridgeLens

def exitOption(country):
    exitVisited = [0 for _ in range(countryNum+1)]
    q = deque()
    q.append(country)
    exitVisited[country] = 1
    while q:
        nowCountry = q.popleft()
        for nextCountry in edges[nowCountry]:
            if exitVisited[nextCountry] == 0:
                q.append(nextCountry)
                exitVisited[nextCountry] = 1

    #모두 연결되어 있으면
    if sum(exitVisited[1:]) == countryNum:
        return True, exitVisited
    else:
        return False, exitVisited

def solve(country, ans):
    global minAns
    if country > countryNum:
        return
    flag, exitVisited = exitOption(country)
    if flag:
        minAns = min(minAns, ans)
        #print(ans)
        #myprint(edges)
        return
    
    #현재 나라에서 연결 할 수 있는 모든 나라에 다리를 건설한다.
    bridgeLens = buildBridge(country)
    #print(country,bridgeLens)
    for i in range(1, countryNum+1):
        if exitVisited[i] == 0:
            if bridgeLens[i] < 30:
                graphUpdate(BUILD, country, i)
                solve(i, ans + bridgeLens[i])
                graphUpdate(UNBUILD, country, i)

    #그 외에도 다리를 건설 안하는 옵션
    solve(country+1, ans)


def graphUpdate(buildTF, country1, country2):
    if buildTF:
        edges[country1].append(country2)
        edges[country2].append(country1)
    else:
        edges[country1].remove(country2)
        edges[country2].remove(country1)



R, C = map(int, read().split())
cell = [list(map(int, read().split())) for _ in range(R)]
visited = [[0 for _ in range(C) ] for _ in range(R)]

countryNum = findIsland()
check = [0 for _ in range(countryNum+1)]
edges = [[] for _ in range(countryNum+1)]
#myprint(visited)

solve(1, 0)
print(minAns if minAns != sys.maxsize else -1)