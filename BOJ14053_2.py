# [파이썬 | BOJ | 14503] 로봇 청소기

import sys
read = sys.stdin.readline

drdc = [[0, -1], [-1, 0], [0, 1], [1, 0]]

N, M = map(int, read().split())
# r, c, d(0북 1동 2남 3서)
robot = list(map(int, read().split()))
board = [list(map(int, read().split())) for _ in range(N)]

def process_clean():
  global robot
  
  nowr, nowc, _ = robot
  board[nowr][nowc] = 2

def process_ab():
  global robot

  # print("process_ab robot info",robot)
  nowr, nowc, nowd = robot
  nextr, nextc = nowr + drdc[nowd][0], nowc + drdc[nowd][1]
  # 청소할 공간이 있다면,
  if board[nextr][nextc] == 0:
    nowd = (nowd - 1) % 4
    nowr, nowc = nextr, nextc
    robot = [nowr, nowc, nowd]
    return True
  # 청소할 공간이 없다면,
  else:
    nowd = (nowd - 1) % 4
    robot = [nowr, nowc, nowd]
    return False

def process_cd():
  global robot

  # print("process_cd robot info/",robot)
  nowr, nowc, nowd = robot
  nextr, nextc = nowr + drdc[(nowd-1)%4][0], nowc + drdc[(nowd-1)%4][1]
  # 벽이 아닌경우
  if board[nextr][nextc] == 2:
    nowr, nowc, nowd = nextr, nextc, nowd
    robot = [nowr, nowc, nowd]
    # print("process_cd robot info/False",robot)
    return False
  # 벽인 경우
  else:
    robot = [nowr, nowc, nowd]
    # print("process_cd robot info/True",robot)
    return True

def solve(board):
  print(sum( board[i].count(2) for i in range(N)))

while True:
  process_clean()
  
  cnt = 0
  while True:
    cnt += 1
    if cnt >= 5:
      break
    if process_ab():
      break

  # 4번을 돌았을 경우  
  if cnt == 5:
    if process_cd():
      break

solve(board)
