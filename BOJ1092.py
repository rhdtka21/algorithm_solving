# [파이썬 | BOJ | 1092] 배
import sys
from collections import deque
read = sys.stdin.readline

N = int(read())
crane = list(map(int, read().split()))
M = int(read())
box = list(map(int, read().split()))

crane.sort(reverse=True)
box.sort(reverse=True)
box = deque(box)
container = []
temp = []
ans = 0

while box or temp:
    if not box and len(container) != N:
        container.clear()
        ans += 1
        box.extendleft(reversed(temp))
        temp.clear()
        #print(box)

    if len(container) == N:
        container.clear()
        ans += 1
        box.extendleft(reversed(temp))
        temp.clear()
        #print(box)

    if box[0] > crane[0]:
        print(-1)
        sys.exit(0)
    
    if crane[len(container)] >= box[0]:
        container.append(box.popleft())
    
    else:
        temp.append(box.popleft())
    #print(box, container, temp)

print(ans+1)