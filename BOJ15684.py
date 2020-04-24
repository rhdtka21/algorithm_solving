# [파이썬 | BOJ | 15684] 사다리 조작
import sys
read = sys.stdin.readline
minans = 4

def solve(added, num):
    global minans

    if added >= minans:
        return
    if check():
        minans = added
        return

    for idx in range(num+1, len(candidates)):
        i, j = candidates[idx]

        if lines[i][j-1] == 0 and lines[i][j+1] == 0:
            lines[i][j] = 1
            solve(added + 1, idx)
            lines[i][j] = 0
            
    

def check():
    for i in range(1, N+1):
        now = i
        for j in range(1, H+1):
            if lines[j][now] == 1:
                now += 1
            elif lines[j][now-1] == 1:
                now -= 1
        #print(i,'->' ,now)
        if i != now:
            return False
    return True
                

N, M, H = map(int, read().split())
lines = [[0 for _ in range(N+1)] for _ in range(H+1)]
candidates = []


for _ in range(M):
    t1, t2 = map(int, read().split())
    lines[t1][t2] = 1


for i in range(1, H+1):
    for j in range(1, N):
        if lines[i][j] == 0 and lines[i][j-1] == 0 and lines[i][j+1] == 0:
            candidates.append([i, j])

solve(0, -1)
print(minans if minans < 4 else -1)