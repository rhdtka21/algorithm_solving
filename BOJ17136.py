# [파이썬 | BOJ | 17136] 색종이 붙이기
import sys
read = sys.stdin.readline
CELLSIZE = 10
minAns = sys.maxsize

def myprint(arr):
    for a in arr:
        print(a)
    print()

def isok(nowr, nowc, size):
    for r in range(nowr, nowr + size):
        for c in range(nowc, nowc + size):
            if (not ((0 <= r < CELLSIZE) and (0 <= c < CELLSIZE))):
                return False
            if cell[r][c] == 0:
                return False
    return True

def attatch(nowr, nowc, size, tf):
    # tf가 0이면 붙이는것
    # tf가 1이면 떼는것
    for r in range(nowr, nowr + size):
        for c in range(nowc, nowc + size):
            cell[r][c] = tf

def isfinish():
    if sum(sum(cell[i]) for i in range(CELLSIZE)) == 0:
        return True
    else:
        return False


def solve(index, cnt):
    global minAns

    if index >= 100:
        if cnt < minAns:
            minAns = cnt
        return
    
    if cnt >= minAns:
        return
    #print(cnt, minAns)
    
    nowr = index // CELLSIZE
    nowc = index % CELLSIZE
    maxSize = 0

    for size in reversed(range(1, 6)):
        if isok(nowr, nowc, size):
            maxSize = size
            break

    if cell[nowr][nowc] == 1:
        for size in reversed(range(1, maxSize+1)):
            if papers[size] > 0:
                attatch(nowr, nowc, size, 0)
                papers[size] -=1 
                solve(index+1, cnt+1)
                papers[size] +=1
                attatch(nowr, nowc, size, 1)
    else:
        solve(index+1, cnt)

        

papers = [-1, 5, 5, 5, 5, 5]
cell = [list(map(int, read().split())) for _ in range(10)]
solve(0, 0)
print(minAns if minAns < sys.maxsize else -1)
