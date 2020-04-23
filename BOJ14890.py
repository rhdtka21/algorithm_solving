# [파이썬 | BOJ | 14890] 경사로
import sys
read = sys.stdin.readline

N, L = map(int, read().split())
row = []
column = []

checkRow = [[0 for _ in range(N)] for _ in range(N)]
checkColumn = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(N):
    row.append(list(map(int, read().split())))

for i in range(N):
    temp = []
    for j in range(N):
        temp.append(row[j][i])
    column.append(temp)

idx = 1
for i in range(N):
    for j in range(N-1):
        if row[i][j] - row[i][j+1] == 1:
            leftToRight = j+1
            for k in range(L):
                if leftToRight+k >= 0 and leftToRight+k < N:
                    if row[i][j] - row[i][leftToRight+k] == 1:
                        if checkRow[i][leftToRight+k] == 0:
                            checkRow[i][leftToRight+k] = idx
                        else:
                            checkRow[i][leftToRight+k] = -1
            idx += 1
        elif row[i][j] - row[i][j+1] == -1:
            rightToLeft = j
            for k in range(L):
                if rightToLeft-k >= 0 and rightToLeft-k < N:
                    if row[i][rightToLeft-k] - row[i][j+1] == -1:
                        if checkRow[i][rightToLeft-k] == 0:
                            checkRow[i][rightToLeft-k] = idx
                        else:
                            checkRow[i][rightToLeft-k] = -1
            idx += 1

        elif row[i][j] - row[i][j+1] > 1:
            checkRow[i][j+1] = -1

        elif row[i][j] - row[i][j+1] < -1:
            checkRow[i][j] = -1

idx = 1
for i in range(N):
    for j in range(N-1):
        if column[i][j] - column[i][j+1] == 1:
            leftToRight = j+1
            for k in range(L):
                if leftToRight+k >= 0 and leftToRight+k < N:
                    if column[i][j] - column[i][leftToRight+k] == 1:
                        if checkColumn[i][leftToRight+k] == 0:
                            checkColumn[i][leftToRight+k] = idx
                        else:
                            checkColumn[i][leftToRight+k] = -1
            idx += 1
        elif column[i][j] - column[i][j+1] == -1:
            rightToLeft = j
            for k in range(L):
                if rightToLeft-k >= 0 and rightToLeft-k < N:
                    if column[i][rightToLeft-k] - column[i][j+1] == -1:
                        if checkColumn[i][rightToLeft-k] == 0:
                            checkColumn[i][rightToLeft-k] = idx
                        else:
                            checkColumn[i][rightToLeft-k] = -1
            idx += 1

        elif column[i][j] - column[i][j+1] > 1:
            checkColumn[i][j+1] = -1

        elif column[i][j] - column[i][j+1] < -1:
            checkColumn[i][j] = -1

'''
for r in checkRow:
    print(r)

for i in range(N):
    for j in range(N):
        print(checkColumn[j][i], end=' ')
    print()
'''
ans = 0

for r in checkRow:
    isOk = False
    if r.count(-1) == 0:
        for i in range(N):
            if r[i] == 0:
                isOk = True
            elif r[i] > 0 and r.count(r[i]) == L:
                isOk = True
            else:
                isOk = False
                break
    if isOk:
        ans += 1
        #print(r)

for c in checkColumn:
    isOk = False
    if c.count(-1) == 0:
        for i in range(N):
            if c[i] == 0:
                isOk = True
            elif c[i] > 0 and c.count(c[i]) == L:
                isOk = True
            else:
                isOk = False
                break
    if isOk:
        ans += 1
        #print(c)

print(ans)

        
                


