# [파이썬 | BOJ | 16236] 아기 상어
import sys
from collections import deque
read = sys.stdin.readline

sec = 0
#상 하 좌 우
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def myprint(arr):
    for a in arr:
        print(a)
    print()

#거리갱신
def bfs():
    q = deque()
    q.append([sharkX, sharkY])
    distance[sharkX][sharkY] = 0
    while q:
        nowX, nowY = q.popleft()
        for i in range(4):
            nextX, nextY = nowX + d[i][0], nowY + d[i][1]
            if 0 <= nextX < N and 0 <= nextY < N and board[nextX][nextY] <= sharkSize:
                if distance[nextX][nextY] == -1:
                    q.append([nextX, nextY])
                    distance[nextX][nextY] = distance[nowX][nowY] + 1

#먹이감 탐색 및 이동
def hunt(sharkSize, sharkExp):
    global sharkX, sharkY, sec

    nextX, nextY = -1, -1
    findFlag = False
    for length in range(1, N**2):
        for r in reversed(range(N)):
            for c in reversed(range(N)):
                if distance[r][c] == length and 0 < board[r][c] < sharkSize:
                    nextX, nextY = r, c
                    findFlag = True
        if findFlag:
            break

    #print(nextX, nextY)     # -1, -1이면 종료
    if nextX == -1 and nextY == -1:
        return -1, -1
    
    #상어 이동 및 경험치, 크기 증가
    sharkExp += 1
    if sharkExp == sharkSize:
        sharkSize += 1
        sharkExp = 0
    sec += length
    #print("info",sharkSize, sharkExp, sec)

    board[sharkX][sharkY] = 0
    distance[sharkX][sharkY] = -1
    board[nextX][nextY] = -1 * sharkSize

    #myprint(board)
    #상어 위치 정보 갱신
    sharkX, sharkY = nextX, nextY

    return sharkSize, sharkExp

N = int(read())
board = [list(map(int, read().split())) for _ in range(N)]

sharkX, sharkY = -1, -1
sharkSize = 2
sharkExp = 0

for r in range(N):
    for c in range(N):
        if board[r][c] == 9:
            sharkX, sharkY = r, c
            board[r][c] = -1 * sharkSize

while True:
    #bfs를 하면서 거리정보를 새로 갱신한다.
    distance = [[-1 for _ in range(N)] for _ in range(N)]
    bfs()

    #가장 최적의 먹이로 이동하고 아기상어의 정보를 갱신한다.
    sharkSize, sharkExp = hunt(sharkSize, sharkExp)

    #탈출 조건
    if sharkSize == -1 and sharkExp == -1:
        print(sec)
        break