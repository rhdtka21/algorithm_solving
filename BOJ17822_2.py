# [파이썬 | BOJ | 17822] 원판 돌리기

import sys
from collections import deque
read = sys.stdin.readline

N, M, T = map(int, read().split())
board = [deque(map(int, read().split())) for _ in range(N)]
op = [list(map(int, read().split())) for _ in range(T)]

def rotate(x, d, k):
  if d == 0:      # 시계방향
    for idx in range(x, N+1, x):
      for _ in range(k):
        board[idx-1].appendleft(board[idx-1].pop())
  else:           # 반시계 방향
    for idx in range(x, N+1, x):
      for _ in range(k):
        board[idx-1].append(board[idx-1].popleft())

def check():
  checkboard = [[0 for _ in range(M)] for _ in range(N)]
  didj = [[-1, 0], [1, 0], [0, -1], [0, 1]]
  flag = True

  # 인접하는 숫자 지우기
  for i in range(N):
    for j in range(M):
      if board[i][j] == 0:
        continue
      for di, dj in didj:
        ni, nj = i + di, j + dj
        nj %= M
        if 0 <= ni < N and 0 <= nj < M and board[i][j] == board[ni][nj]:
          checkboard[i][j], checkboard[ni][nj] = 1, 1
          flag = False

  for i in range(N):
    for j in range(M):
      if checkboard[i][j] > 0:
        board[i][j] = 0

  # 지워진게 아무것도 없으면
  if flag:
    numer, denom = getInfo()
    if denom:
      avgVal = numer / denom
      for i in range(N):
        for j in range(M):
          if board[i][j] == 0:
            continue
          if board[i][j] > avgVal:
            board[i][j] -= 1
          elif board[i][j] < avgVal:
            board[i][j] += 1

def getInfo():
  sumVal = sum( sum(board[i]) for i in range(N))
  numCnt = sum( board[i].count(0) for i in range(N))
  numCnt = N*M - numCnt
  return sumVal, numCnt


for x, d, k in op:
  rotate(x, d, k)
  check()

print(getInfo()[0])
