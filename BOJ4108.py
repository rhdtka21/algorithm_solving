# [파이썬 | BOJ | 4108] 지뢰찾기
import sys
read = sys.stdin.readline

#좌상 좌하 우상 우하 상 하 좌 우
d = [[-1, -1], [1, -1], [-1, 1], [1, 1], [-1, 0], [1, 0], [0, -1], [0, 1]]

while True:
    R, C = map(int, read().split())
    if R == 0 and C == 0:
        break
    
    strInput = [read().rstrip() for _ in range(R)]

    _mine = [[0 for _ in range(C)] for _ in range(R)]
    _map = [[0 for _ in range(C)] for _ in range(R)]
    ans = []

    for i in range(R):
        for j in range(C):
            if strInput[i][j] == '*':
                _mine[i][j] = 1
                _map[i][j] = -1

    for i in range(R):
        for j in range(C):
            if _map[i][j] == -1:
                continue
            cnt = 0
            for k in range(8):
                ni, nj = i + d[k][0], j + d[k][1]
                if 0 <= ni < R and 0 <= nj < C:
                    cnt += _mine[ni][nj]
            _map[i][j] = cnt

    for i in range(R):
        for j in range(C):
            if  _map[i][j] == -1:
                _map[i][j] = '*'
            elif _map[i][j] >= 10:
                _map[i][j] = 'M'
            else:
                _map[i][j] = str(_map[i][j])
        ans.append(''.join(_map[i]))

    for a in ans:
        print(a)