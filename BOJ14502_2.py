# [파이썬 | BOJ | 14502] 연구소

import sys
from collections import deque
read = sys.stdin.readline
ans = -1
dirct = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def cpyLab(a):
    b = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            b[i][j] = a[i][j]
    return b

def solve(_map):
  global ans
  lab = cpyLab(_map)
  q = deque()
  for idx in range(N*M):
    i, j = idx // M, idx % M
    if lab[i][j] == 2:
      q.append([i,j])
  while q:
    nowI, nowJ = q.popleft()
    for dI, dJ in dirct:
      nextI, nextJ = nowI + dI, nowJ + dJ
      if 0 <= nextI < N and 0 <= nextJ < M and lab[nextI][nextJ] == 0:
        lab[nextI][nextJ] = 2
        q.append([nextI, nextJ])
  
  safeArea = 0
  for idx in range(N*M):
    i, j = idx // M, idx % M
    if lab[i][j] == 0:
      safeArea += 1
  
  if ans < safeArea:
    ans = safeArea

def selWall(lab, start, cnt):
  if cnt == 3:
    solve(lab)
    return
    
  for idx in range(start, N*M):
    i, j = idx // M, idx % M

    if lab[i][j] == 0:
      lab[i][j] = 1
      selWall(lab, idx+1, cnt+1)
      lab[i][j] = 0

N, M = map(int, read().split())
orgin_lab = [list(map(int, read().split())) for _ in range(N)]
lab = cpyLab(orgin_lab)
selWall(lab, 0, 0)
print(ans)