# [파이썬 | BOJ | 1620] 나는야 포켓몬 마스터 이다솜
import sys
read = sys.stdin.readline

l = []
d = {}
N, M = map(int, read().split())

for i in range(N):
    temp = read().replace('\n', '')
    l.append(temp)
    d[temp] = i+1

for _ in range(M):
    temp = read().replace('\n', '')
    if temp.isdigit():
        temp = int(temp)
        print(l[temp-1])
    else:
        print(d[temp])
        # print(l.index(temp)+1) 시간초과