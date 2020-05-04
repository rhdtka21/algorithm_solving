# [파이썬 | BOJ | 17135] 캐슬 디펜스

import sys
from collections import deque
from itertools import combinations
from copy import deepcopy
read = sys.stdin.readline

def myprint(arr):
    for a in arr:
        print(a)
    print()


N, M, D = map(int, read().split())
originBoard = deque(list(map(int, read().split())) for _ in range(N))
ans = -1
D = min(N+M-1, D)

for case in combinations(range(M), 3):
    board = deepcopy(originBoard)
    cnt = 0
    while True:
        #종료 조건
        exitFalg = 0
        for b in board:
            exitFalg += b.count(1)
        if not exitFalg:
            if ans < cnt:
                ans = cnt
            #print("종료", cnt)
            break

        #print("초기 적 위치")
        #myprint(board)

        shootingRange = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(3)]
        for idx, cval in enumerate(case):
            for dc in range(D):
                for r in range(max(0, N-D+dc), N):
                    if cval-dc >= 0:
                        shootingRange[idx][r][cval-dc] = N-r+dc
                    if cval+dc < M:
                        shootingRange[idx][r][cval+dc] = N-r+dc

        #print("사거리")
        #myprint(shootingRange[0])
        #myprint(shootingRange[1])
        #myprint(shootingRange[2])
        
        aims = []
        for idx in range(3):
            aimDistance = D+1
            aimR, aimC = -1, -1
            for c in range(M):
                for r in reversed(range(N)):
                    #유효거리가 아니면 넘어감
                    if shootingRange[idx][r][c] == 0:
                        continue
                    #적이 있어야함.
                    if board[r][c] == 1:
                        #적이 있고, 사정거리가 지금까지중 최소일때
                        if shootingRange[idx][r][c] < aimDistance:
                            aimDistance = shootingRange[idx][r][c]
                            aimR, aimC = r, c
            #공격받을 적
            aims.append([aimR, aimC])
        
        #print("죽은 적")
        #print(aims)

        #공격받을 적을 지운다.
        for aimR, aimC in aims:
            if aimR >= 0 and aimC >= 0 and board[aimR][aimC] != 0:
                board[aimR][aimC] = 0
                cnt += 1

        #적들 진격
        board.pop()
        board.appendleft([0 for _ in range(M)])

print(ans)