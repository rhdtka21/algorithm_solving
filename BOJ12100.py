# [파이썬 | BOJ | 12100] 2048(easy)

import sys
from copy import deepcopy
read = sys.stdin.readline

bins = [2**i for i in range(20)]

NOTATION = '0123456789ABCDEF'

def numeral_system(number, base):
    q, r = divmod(number, base)
    n = NOTATION[r]
    return numeral_system(q, base) + n if q else n

def maxval():
    ret = -1
    for r in row:
        if ret < max(r):
            ret = max(r)
    return ret

def myPrint():
    print('------row-------')
    for r in row:
        print(r)
    print('------column-------')
    for i in range(N):
        for j in range(N):
            print(column[j][i], end=' ')
        print()

def sync(op):
    #column to row
    if op == 1:
        for i in range(N):
            for j in range(N):
                row[i][j] = column[j][i]
    
    #row to column
    else:
        for i in range(N):
            for j in range(N):
                column[j][i] = row[i][j]

def check(direction):
    if direction == 0:      #상
        for i in range(N):
            for j in range(N-1):
                if column[i][j] == column[i][j+1] and column[i][j] != 0:
                    column[i][j] *= 2
                    column[i][j+1] = 0
  
    elif direction == 1:    #하
        for i in range(N):
            for j in reversed(range(1, N)):
                if column[i][j] == column[i][j-1] and column[i][j] != 0:
                    column[i][j] *= 2
                    column[i][j-1] = 0

    elif direction == 2:    #좌
        for i in range(N):
            for j in range(N-1):
                if row[i][j] == row[i][j+1] and row[i][j] != 0:
                    row[i][j] *= 2
                    row[i][j+1] = 0

    elif direction == 3:    #우
        for i in range(N):
            for j in reversed(range(1, N)):
                if row[i][j] == row[i][j-1] and row[i][j] != 0:
                    row[i][j] *= 2
                    row[i][j-1] = 0

def move(direction, doCheck):
    if direction == 0:      #상
        for i in range(N):
            for j in range(N):
                cnt = 0
                while (not column[i][j] in bins) and (cnt < N-j):
                    column[i].append(column[i].pop(j))
                    cnt += 1
        if doCheck:
            check(direction)
            move(direction, False)
        else:
            sync(1)

    elif direction == 1:    #하
        for i in range(N):
            for j in reversed(range(N)):
                cnt = 0
                while (not column[i][j] in bins) and (cnt < j):
                    column[i].insert(0, column[i].pop(j))
                    cnt += 1
        if doCheck:
            check(direction)
            move(direction, False)
        else:
            sync(1)

    elif direction == 2:    #좌
        for i in range(N):
            for j in range(N):
                cnt = 0
                while (not row[i][j] in bins) and (cnt < N-j):
                    row[i].append(row[i].pop(j))
                    cnt += 1
        if doCheck:
            check(direction)
            move(direction, False)
        else:
            sync(2)

    elif direction == 3:    #우
        for i in range(N):
            for j in reversed(range(N)):
                cnt = 0
                while (not row[i][j] in bins) and (cnt < j):
                    row[i].insert(0, row[i].pop(j))
                    cnt += 1
        if doCheck:
            check(direction)
            move(direction, False)
        else:
            sync(2)
        
N = int(read())
baseRow = []
baseColumn = []
for _ in range(N):
    baseRow.append(list(map(int, read().split())))
for i in range(N):
    temp = []
    for j in range(N):
        temp.append(baseRow[j][i])
    baseColumn.append(temp)

ans = -1
for i in range(1024):
    row = deepcopy(baseRow)
    column = deepcopy(baseColumn)

    num = (numeral_system(i, 4))
    if len(num) < 5:
        num = '0' * (5-len(num)) + num
    #print(num)

    for n in num:
        move(int(n), True)
    temp = maxval()
    #print(temp)
    if ans < temp:
        ans = temp

print(ans)