# [파이썬 | BOJ | 14890] 경사로

import sys
read = sys.stdin.readline
N, L = map(int, read().split())
mapp = [list(map(int, read().split())) for _ in range(N)]
ans = 0

roads = []
for i in range(N):
  roads.append(mapp[i])
  temp = []
  for j in range(N):
    temp.append(mapp[j][i])
  roads.append(temp)


for road in roads:
  flag = True
  height = []
  for i in range(N-1):
    height.append(road[i] - road[i+1])

  check = [0 for _ in range(N)]
  for i in range(N-1):
    if abs(height[i]) > 1:
      flag = False
    elif height[i] == 1:
      for j in range(L):
        if 0 <= i+1+j < N:
          check[i+1+j] += 1
        else:
          flag = False
    elif height[i] == -1:
      for j in range(L):
        if 0 <= i-j < N:
          check[i-j] += 1
        else:
          flag = False
    else:
      pass
  for i in range(N):
    if check[i] > 1:
      flag = False
      break
  
  if flag:
    ans += 1

print(ans)