# [파이썬 | BOJ | 1374] 강의실

import sys
from collections import deque
read = sys.stdin.readline
ans = -1

N = int(read())
startTime = []
endTime = []
for i in range(N):
    a, b, c = map(int, read().split())
    startTime.append([b, a])
    endTime.append([c, a])

startTime.sort(reverse = True)
endTime.sort(reverse = True)

temp = []

for time in range(endTime[0][0]+1):
    
    while startTime and time >= startTime[-1][0]:
        t, idx = startTime.pop()
        temp.append(idx)

    while endTime and time >= endTime[-1][0]:
        t, idx = endTime.pop()
        temp.remove(idx)

    if len(temp) > ans:
        ans = len(temp)
    #print(time, temp)
print(ans)
