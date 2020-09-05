# [파이썬 | BOJ | 14891] 톱니 바퀴
import sys
from collections import deque
read = sys.stdin.readline
gear = []
case = [[0, 0, 0], [0, 0, 1], [0, 1, 0],
 [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]

group = [[[0], [1], [2], [3]], 
    [[0], [1], [2, 3]],
    [[0], [1, 2], [3]],
    [[0], [1, 2, 3]],
    [[0, 1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 1, 2], [3]],
    [[0, 1, 2, 3]]
]


for _ in range(4):
  gearString = read().rstrip('\n')
  gearDeque = deque()
  for gs in gearString:
    gearDeque.append(gs)
  gear.append(gearDeque)

K = int(input())
operation = [list(map(int, read().split())) for _ in range(K)]

def contactInfo():
  # 다르면 1 (회전하면 1)
  contact = [0 for _ in range(3)]
  if gear[0][2] != gear[1][6]:
    contact[0] = 1
  if gear[1][2] != gear[2][6]:
    contact[1] = 1
  if gear[2][2] != gear[3][6]:
    contact[2] = 1  

  return contact

def rotate(gearIdx, d):
  if d > 0:
    gear[gearIdx].appendleft(gear[gearIdx].pop())
  else:
    gear[gearIdx].append(gear[gearIdx].popleft())

def solve():
  ans = 0
  for i in range(4):
    ans += int(gear[i][0]) * (2 ** (i))
  print(ans)

for op in operation:
  idx, d = op; idx -= 1
  contact = contactInfo()
  for i in range(8):
    if contact == case[i]:
      for g in group[i]:
        if idx in g:
          # 회전 주체의 index가 홀수이면
          if g.index(idx)%2:
            for p, eachGear in enumerate(g):
              rotate(eachGear, d * ((-1) ** (p+1)))
          # 회전 주체의 index가 짝수이면
          else:
            for p, eachGear in enumerate(g):
              rotate(eachGear, d * ((-1) ** (p)))
      break

solve()

  

