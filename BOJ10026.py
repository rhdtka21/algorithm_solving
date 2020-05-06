# [파이썬 | BOJ | 10026] 적록색약
import sys
from collections import deque
read = sys.stdin.readline
# 상 하 좌 우
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def colorNum(char, TF):
    if TF:
        if char == 'R':
            return 0
        elif char == 'G':
            return 0
        elif char == 'B':
            return 2
    else:
        if char == 'R':
            return 0
        elif char == 'G':
            return 1
        elif char == 'B':
            return 2


def bfs(colorNum):
    check = [[0 for _ in range(N)] for _ in range(N)]

    cnt = 0
    for i in range(N*N):
        r, c = i // N , i % N
        if board[r][c] == colorNum and check[r][c] == 0:  
            cnt += 1
            q = deque()
            check[r][c] = 1
            q.append([r, c])
            while q:
                nowr, nowc = q.popleft()
                for i in range(4):
                    nextr, nextc = nowr + d[i][0], nowc + d[i][1]
                    if 0<=nextr<N and 0<=nextc<N:
                        if board[nextr][nextc] == colorNum and check[nextr][nextc] == 0:
                            check[nextr][nextc] = 1
                            q.append([nextr, nextc])
    return cnt

N = int(read())
board = []
RGboard = []

for _ in range(N):
    row = []
    RGrow = []
    for t in read().replace('\n', ''):
        row.append(colorNum(t, False))
        #색맹여부가 True
        RGrow.append(colorNum(t, True))
    board.append(row)
    RGboard.append(RGrow)

ans1 = bfs(0) + bfs(1) + bfs(2)
board = RGboard
ans2 = bfs(0) + bfs(2)

print(ans1, ans2)