# [파이썬 | BOJ | 17142] 연구소3
import sys
from collections import deque
from itertools import combinations
read = sys.stdin.readline

minAns = 2500
def myprint(arr):
    for a in arr:
        print(a)
    print()

#상 하 좌 우
D = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def maxValue(arr):
    maxVal = -1
    for r in range(N):
        for c in range(N):
            if board[r][c] != 1:
                if maxVal < arr[r][c]:
                    maxVal = arr[r][c]
    return maxVal

def mergeInformation(mergearr, check):
    for r in range(N):
        for c in range(N):
            temp = []
            for val in check:
                temp.append(distance[val][r][c])
            mergearr[r][c] = min(temp)
    return mergearr

def bfs(idx):
    r, c = virusInfo[idx]
    q = deque()
    q.append([r,c])
    distance[idx][r][c] = 0
    #print(r, c)
    while q:
        nowR, nowC = q.popleft()
        for i in range(4):
            nextR, nextC = nowR + D[i][0], nowC + D[i][1]
            if 0 <= nextR < N and 0 <= nextC < N and board[nextR][nextC] != 1:
                if distance[idx][nextR][nextC] > distance[idx][nowR][nowC] + 1:
                    q.append([nextR, nextC])
                    distance[idx][nextR][nextC] = distance[idx][nowR][nowC] + 1
    
    for eachVirus in virusInfo:
        r, c = eachVirus
        if distance[idx][r][c] != 0:
            distance[idx][r][c] = 0

N, M = map(int, read().split())
board = [list(map(int, read().split())) for _ in range(N)]

virusCnt = 0
virusInfo = []

for r in range(N):
    for c in range(N):
        if board[r][c] == 2:
            virusCnt += 1
            virusInfo.append([r,c])
distance = [[[2500 for _ in range(N)] for _ in range(N)] for _ in range(virusCnt)]
for i in range(virusCnt):
    bfs(i)            

for case in combinations(range(virusCnt), M):
    mergeDistance = [[0 for _ in range(N)] for _ in range(N)]
    mergeDistance = mergeInformation(mergeDistance, case)
    maxVal = maxValue(mergeDistance)
    if maxVal < minAns:
        minAns = maxVal

print(-1 if minAns == 2500 else minAns)
