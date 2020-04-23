# [파이썬 | BOJ | 15683] 감시

import sys
from copy import deepcopy, copy
read = sys.stdin.readline

minans = 999999

def solve(nowR, nowC, depth, office):
    global minans

    if depth == cctvNum:
        ans = 0
        for x in office:
            ans += x.count(0)
            
        if minans > ans:
            minans = ans
        return

    initOffice = [[0 for _ in range(C)] for _ in range(R)]

    
    for r in range(R):
        for c in range(C):    
            initOffice[r][c] = office[r][c]


    for r in range(R):
        for c in range(C):
            if r < nowR or (r == nowR and c <= nowC):
                continue
            if office[r][c] >= 1 and  office[r][c] <= 5:
                cctv = office[r][c]

                #1번 cctv
                if cctv == 1:
                    #위쪽
                    for i in reversed(range(r)):
                        if office[i][c] == 0:
                            office[i][c] = 9
                        elif office[i][c] == 6:
                            break
                    solve(r,c,depth+1,office)
                    
                    for rr in range(R):
                        for cc in range(C):
                            office[rr][cc] = initOffice[rr][cc]
                    
                    #오른쪽
                    for i in range(c+1, C):
                        if office[r][i] == 0:
                            office[r][i] = 9
                        elif office[r][i] == 6:
                            break
                    solve(r,c,depth+1,office)
                    
                    for rr in range(R):
                        for cc in range(C):
                            office[rr][cc] = initOffice[rr][cc]

                    #아래쪽
                    for i in range(r+1, R):
                        if office[i][c] == 0:
                            office[i][c] = 9
                        elif office[i][c] == 6:
                            break
                    solve(r,c,depth+1,office)
                    
                    for rr in range(R):
                        for cc in range(C):
                            office[rr][cc] = initOffice[rr][cc]

                    #왼쪽
                    for i in reversed(range(c)):
                        if office[r][i] == 0:
                            office[r][i] = 9
                        elif office[r][i] == 6:
                            break
                    solve(r,c,depth+1,office)

                    for rr in range(R):
                        for cc in range(C):
                            office[rr][cc] = initOffice[rr][cc]
                
                elif cctv == 2:
                    #위쪽 아래쪽
                    for i in reversed(range(r)):
                        if office[i][c] == 0:
                            office[i][c] = 9
                        elif office[i][c] == 6:
                            break
                    for i in range(r+1, R):
                        if office[i][c] == 0:
                            office[i][c] = 9
                        elif office[i][c] == 6:
                            break

                    solve(r,c,depth+1,office)

                    for rr in range(R):
                        for cc in range(C):
                            office[rr][cc] = initOffice[rr][cc]

                    #오른쪽 왼쪽
                    for i in range(c+1, C):
                        if office[r][i] == 0:
                            office[r][i] = 9
                        elif office[r][i] == 6:
                            break
                    for i in reversed(range(c)):
                        if office[r][i] == 0:
                            office[r][i] = 9
                        elif office[r][i] == 6:
                            break

                    solve(r,c,depth+1,office)

                    for rr in range(R):
                        for cc in range(C):
                            office[rr][cc] = initOffice[rr][cc]

                elif cctv == 3:
                    #위쪽 오른쪽
                    for i in reversed(range(r)):
                        if office[i][c] == 0:
                            office[i][c] = 9
                        elif office[i][c] == 6:
                            break
                    for i in range(c+1, C):
                        if office[r][i] == 0:
                            office[r][i] = 9
                        elif office[r][i] == 6:
                            break

                    solve(r,c,depth+1,office)
                    
                    for rr in range(R):
                        for cc in range(C):
                            office[rr][cc] = initOffice[rr][cc]

                    #오른쪽 아래쪾
                    for i in range(c+1, C):
                        if office[r][i] == 0:
                            office[r][i] = 9
                        elif office[r][i] == 6:
                            break
                    for i in range(r+1, R):
                        if office[i][c] == 0:
                            office[i][c] = 9
                        elif office[i][c] == 6:
                            break

                    solve(r,c,depth+1,office)

                    for rr in range(R):
                        for cc in range(C):
                            office[rr][cc] = initOffice[rr][cc]

                    #아래쪽 왼쪽
                    for i in range(r+1, R):
                        if office[i][c] == 0:
                            office[i][c] = 9
                        elif office[i][c] == 6:
                            break
                    for i in reversed(range(c)):
                        if office[r][i] == 0:
                            office[r][i] = 9
                        elif office[r][i] == 6:
                            break

                    solve(r,c,depth+1,office)

                    for rr in range(R):
                        for cc in range(C):
                            office[rr][cc] = initOffice[rr][cc]

                    #왼쪽 위쪽
                    for i in reversed(range(c)):
                        if office[r][i] == 0:
                            office[r][i] = 9
                        elif office[r][i] == 6:
                            break
                    for i in reversed(range(r)):
                        if office[i][c] == 0:
                            office[i][c] = 9
                        elif office[i][c] == 6:
                            break

                    solve(r,c,depth+1,office)

                    for rr in range(R):
                        for cc in range(C):
                            office[rr][cc] = initOffice[rr][cc]

                elif cctv == 4:
                    #위쪽 오른쪽 왼쪽
                    for i in reversed(range(r)):
                        if office[i][c] == 0:
                            office[i][c] = 9
                        elif office[i][c] == 6:
                            break
                    for i in range(c+1, C):
                        if office[r][i] == 0:
                            office[r][i] = 9
                        elif office[r][i] == 6:
                            break
                    for i in reversed(range(c)):
                        if office[r][i] == 0:
                            office[r][i] = 9
                        elif office[r][i] == 6:
                            break

                    solve(r,c,depth+1,office)

                    for rr in range(R):
                        for cc in range(C):
                            office[rr][cc] = initOffice[rr][cc]

                    #오른쪽 아래쪽 위쪽
                    for i in range(c+1, C):
                        if office[r][i] == 0:
                            office[r][i] = 9
                        elif office[r][i] == 6:
                            break
                    for i in range(r+1, R):
                        if office[i][c] == 0:
                            office[i][c] = 9
                        elif office[i][c] == 6:
                            break
                    for i in reversed(range(r)):
                        if office[i][c] == 0:
                            office[i][c] = 9
                        elif office[i][c] == 6:
                            break

                    solve(r,c,depth+1,office)

                    for rr in range(R):
                        for cc in range(C):
                            office[rr][cc] = initOffice[rr][cc]

                    #아래쪽 왼쪽 오른쪽
                    for i in range(r+1, R):
                        if office[i][c] == 0:
                            office[i][c] = 9
                        elif office[i][c] == 6:
                            break
                    for i in reversed(range(c)):
                        if office[r][i] == 0:
                            office[r][i] = 9
                        elif office[r][i] == 6:
                            break
                    for i in range(c+1, C):
                        if office[r][i] == 0:
                            office[r][i] = 9
                        elif office[r][i] == 6:
                            break

                    solve(r,c,depth+1,office)

                    for rr in range(R):
                        for cc in range(C):
                            office[rr][cc] = initOffice[rr][cc]

                    #왼쪽 위쪽 아래쪽
                    for i in reversed(range(c)):
                        if office[r][i] == 0:
                            office[r][i] = 9
                        elif office[r][i] == 6:
                            break
                    for i in reversed(range(r)):
                        if office[i][c] == 0:
                            office[i][c] = 9
                        elif office[i][c] == 6:
                            break
                    for i in range(r+1, R):
                        if office[i][c] == 0:
                            office[i][c] = 9
                        elif office[i][c] == 6:
                            break

                    solve(r,c,depth+1,office)

                    for rr in range(R):
                        for cc in range(C):
                            office[rr][cc] = initOffice[rr][cc]

                elif cctv == 5:
                    #전방향
                    for i in reversed(range(r)):
                        if office[i][c] == 0:
                            office[i][c] = 9
                        elif office[i][c] == 6:
                            break
                    for i in range(c+1, C):
                        if office[r][i] == 0:
                            office[r][i] = 9
                        elif office[r][i] == 6:
                            break
                    for i in range(r+1, R):
                        if office[i][c] == 0:
                            office[i][c] = 9
                        elif office[i][c] == 6:
                            break
                    for i in reversed(range(c)):
                        if office[r][i] == 0:
                            office[r][i] = 9
                        elif office[r][i] == 6:
                            break
                
                    solve(r,c,depth+1,office)

                    for rr in range(R):
                        for cc in range(C):
                            office[rr][cc] = initOffice[rr][cc]
                   
R, C = map(int, read().split())
office = []
for _ in range(R):
    office.append(list(map(int, read().split())))
cctvNum = 0
for r in range(R):
    for c in range(C):
        if office[r][c] >= 1 and  office[r][c] <= 5:
            cctvNum += 1

solve(0,-1,0,office)
print(minans)