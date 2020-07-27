# [파이썬 | BOJ | 9506] 약수들의 합
import sys
import heapq
read = sys.stdin.readline

heap = []

N = int(read())
op = []
for _ in range(N):
    op.append(int(read()))
    
for o in op:
    if o == 0:
        if len(heap) > 0:
            temp = heapq.heappop(heap)
            print(temp[0] if temp[1] else -temp[0])
        else:
            print(0)       
    else:
        heapq.heappush(heap, [o, True] if o > 0 else [-o, False])