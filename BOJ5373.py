# [파이썬 | BOJ | 5373] 큐빙
import sys
from collections import deque
read = sys.stdin.readline

def rotateAntiClock(d, code):
    d.append(d.popleft())
    d.append(d.popleft())
    d.append(d.popleft())
    temp = [[], [], []]

    if code == 'ud':
        for r in range(3):
            for c in range(3):
                temp[r].append(U[r][c])

        U[0][0] = temp[0][2]
        U[0][1] = temp[1][2]
        U[0][2] = temp[2][2]

        U[1][0] = temp[0][1]
        U[1][1] = temp[1][1]
        U[1][2] = temp[2][1]

        U[2][0] = temp[0][0]
        U[2][1] = temp[1][0]
        U[2][2] = temp[2][0]
        
    elif code == 'dd':
        for r in range(3):
            for c in range(3):
                temp[r].append(D[r][c])

        D[0][0] = temp[2][0]
        D[0][1] = temp[1][0]
        D[0][2] = temp[0][0]

        D[1][0] = temp[2][1]
        D[1][1] = temp[1][1]
        D[1][2] = temp[0][1]

        D[2][0] = temp[2][2]
        D[2][1] = temp[1][2]
        D[2][2] = temp[0][2]
        
    elif code == 'fd':
        for r in range(3):
            for c in range(3):
                temp[r].append(F[r][c])

        F[0][0] = temp[0][2]
        F[0][1] = temp[1][2]
        F[0][2] = temp[2][2]

        F[1][0] = temp[0][1]
        F[1][1] = temp[1][1]
        F[1][2] = temp[2][1]

        F[2][0] = temp[0][0]
        F[2][1] = temp[1][0]
        F[2][2] = temp[2][0]

    elif code == 'bd':
        for r in range(3):
            for c in range(3):
                temp[r].append(B[r][c])

        B[0][0] = temp[2][0]
        B[0][1] = temp[1][0]
        B[0][2] = temp[0][0]

        B[1][0] = temp[2][1]
        B[1][1] = temp[1][1]
        B[1][2] = temp[0][1]

        B[2][0] = temp[2][2]
        B[2][1] = temp[1][2]
        B[2][2] = temp[0][2]

    elif code == 'ld':
        for r in range(3):
            for c in range(3):
                temp[r].append(L[r][c])

        L[0][0] = temp[0][2]
        L[0][1] = temp[1][2]
        L[0][2] = temp[2][2]

        L[1][0] = temp[0][1]
        L[1][1] = temp[1][1]
        L[1][2] = temp[2][1]

        L[2][0] = temp[0][0]
        L[2][1] = temp[1][0]
        L[2][2] = temp[2][0]

    elif code == 'rd':
        for r in range(3):
            for c in range(3):
                temp[r].append(R[r][c])

        R[0][0] = temp[2][0]
        R[0][1] = temp[1][0]
        R[0][2] = temp[0][0]

        R[1][0] = temp[2][1]
        R[1][1] = temp[1][1]
        R[1][2] = temp[0][1]

        R[2][0] = temp[2][2]
        R[2][1] = temp[1][2]
        R[2][2] = temp[0][2]

def rotateClock(d, code):
    d.appendleft(d.pop())
    d.appendleft(d.pop())
    d.appendleft(d.pop())
    temp = [[], [], []]

    if code == 'ud':
        for r in range(3):
            for c in range(3):
                temp[r].append(U[r][c])

        U[0][0] = temp[2][0]
        U[0][1] = temp[1][0]
        U[0][2] = temp[0][0]

        U[1][0] = temp[2][1]
        U[1][1] = temp[1][1]
        U[1][2] = temp[0][1]

        U[2][0] = temp[2][2]
        U[2][1] = temp[1][2]
        U[2][2] = temp[0][2]
        

    elif code == 'dd':
        for r in range(3):
            for c in range(3):
                temp[r].append(D[r][c])

        D[0][0] = temp[0][2]
        D[0][1] = temp[1][2]
        D[0][2] = temp[2][2]

        D[1][0] = temp[0][1]
        D[1][1] = temp[1][1]
        D[1][2] = temp[2][1]

        D[2][0] = temp[0][0]
        D[2][1] = temp[1][0]
        D[2][2] = temp[2][0]

    elif code == 'fd':
        for r in range(3):
            for c in range(3):
                temp[r].append(F[r][c])

        F[0][0] = temp[2][0]
        F[0][1] = temp[1][0]
        F[0][2] = temp[0][0]

        F[1][0] = temp[2][1]
        F[1][1] = temp[1][1]
        F[1][2] = temp[0][1]

        F[2][0] = temp[2][2]
        F[2][1] = temp[1][2]
        F[2][2] = temp[0][2]

    elif code == 'bd':
        for r in range(3):
            for c in range(3):
                temp[r].append(B[r][c])

        B[0][0] = temp[0][2]
        B[0][1] = temp[1][2]
        B[0][2] = temp[2][2]

        B[1][0] = temp[0][1]
        B[1][1] = temp[1][1]
        B[1][2] = temp[2][1]

        B[2][0] = temp[0][0]
        B[2][1] = temp[1][0]
        B[2][2] = temp[2][0]

    elif code == 'ld':
        for r in range(3):
            for c in range(3):
                temp[r].append(L[r][c])

        L[0][0] = temp[2][0]
        L[0][1] = temp[1][0]
        L[0][2] = temp[0][0]

        L[1][0] = temp[2][1]
        L[1][1] = temp[1][1]
        L[1][2] = temp[0][1]

        L[2][0] = temp[2][2]
        L[2][1] = temp[1][2]
        L[2][2] = temp[0][2]

    elif code == 'rd':
        for r in range(3):
            for c in range(3):
                temp[r].append(R[r][c])

        R[0][0] = temp[0][2]
        R[0][1] = temp[1][2]
        R[0][2] = temp[2][2]

        R[1][0] = temp[0][1]
        R[1][1] = temp[1][1]
        R[1][2] = temp[2][1]

        R[2][0] = temp[0][0]
        R[2][1] = temp[1][0]
        R[2][2] = temp[2][0]

def myPrint():
    for r in range(3):
        for c in range(3):
            print(color[U[r][c]], end='')
        print()

def dequeToCube(code):
    if code == 'ud':
        for i in range(12):
            idx = i % 3
            if i >= 0 and i < 3:
                F[0][2-idx] = ud[i]
            elif i >= 3 and i < 6:
                L[0][2-idx] = ud[i]
            elif i >= 6 and i < 9:
                B[0][idx] = ud[i]
            elif i >= 9 and i < 12:
                R[0][idx] = ud[i]
   
    elif code == 'dd':
        for i in range(12):
            idx = i % 3
            if i >= 0 and i < 3:
                F[2][idx] = dd[i]
            elif i >= 3 and i < 6:
                R[2][2-idx] = dd[i]
            elif i >= 6 and i < 9:
                B[2][2-idx] = dd[i]
            elif i >= 9 and i < 12:
                L[2][idx] = dd[i]

    elif code == 'fd':
        for i in range(12):
            idx = i % 3
            if i >= 0 and i < 3:
                U[2][idx] = fd[i]
            elif i >= 3 and i < 6:
                R[idx][2] = fd[i]
            elif i >= 6 and i < 9:
                D[2][2-idx] = fd[i]
            elif i >= 9 and i < 12:
                L[2-idx][2] = fd[i]

    elif code == 'bd':
        for i in range(12):
            idx = i % 3
            if i >= 0 and i < 3:
                U[0][2-idx] = bd[i]
            elif i >= 3 and i < 6:
                L[idx][0] = bd[i]
            elif i >= 6 and i < 9:
                D[0][idx] = bd[i]
            elif i >= 9 and i < 12:
                R[2-idx][0] = bd[i]
    
    elif code == 'ld':
        for i in range(12):
            idx = i % 3
            if i >= 0 and i < 3:
                U[idx][0] = ld[i]
            elif i >= 3 and i < 6:
                F[idx][0] = ld[i]
            elif i >= 6 and i < 9:
                D[2-idx][0] = ld[i]
            elif i >= 9 and i < 12:
                B[2-idx][0] = ld[i]
    
    elif code == 'rd':
        for i in range(12):
            idx = i % 3
            if i >= 0 and i < 3:
                U[2-idx][2] = rd[i]
            elif i >= 3 and i < 6:
                B[idx][2] = rd[i]
            elif i >= 6 and i < 9:
                D[idx][2] = rd[i]
            elif i >= 9 and i < 12:
                F[2-idx][2] = rd[i]

def cubeToDeque():
    global ld, rd, ud, dd, bd, fd
    # 위 앞 아래 뒤
    ld.clear()
    for x in U[0][0], U[1][0], U[2][0], F[0][0], F[1][0], F[2][0], D[2][0], D[1][0], D[0][0], B[2][0], B[1][0], B[0][0]:
        ld.append(x)

    # 위 뒤 아래 앞
    rd.clear()
    for x in U[2][2], U[1][2], U[0][2], B[0][2], B[1][2], B[2][2], D[0][2], D[1][2], D[2][2], F[2][2], F[1][2], F[0][2]:
        rd.append(x)
    # 앞 왼 뒤 오른
    ud.clear()
    for x in F[0][2], F[0][1], F[0][0], L[0][2], L[0][1], L[0][0], B[0][0], B[0][1], B[0][2], R[0][0], R[0][1], R[0][2]:
        ud.append(x)
    # 앞 오른 뒤 왼
    dd.clear()
    for x in F[2][0], F[2][1], F[2][2], R[2][2], R[2][1], R[2][0], B[2][2], B[2][1], B[2][0], L[2][0], L[2][1], L[2][2]:
        dd.append(x)
    # 위 왼 아래 오른
    bd.clear()
    for x in U[0][2], U[0][1], U[0][0], L[0][0], L[1][0], L[2][0], D[0][0], D[0][1], D[0][2], R[2][0], R[1][0], R[0][0]:
        bd.append(x)
    # 위 오른 아래 왼
    fd.clear()
    for x in U[2][0], U[2][1], U[2][2], R[0][2], R[1][2], R[2][2], D[2][2], D[2][1], D[2][0], L[2][2], L[1][2], L[0][2]:
        fd.append(x)

def sync(code):
    '''
    print("반영 전")
    print(ld)
    print(rd)
    print(ud)
    print(dd)
    print(bd)
    print(fd)
    '''
    dequeToCube(code)
    cubeToDeque()
    '''
    print("반영 후")
    print(ld)
    print(rd)
    print(ud)
    print(dd)
    print(bd)
    print(fd)
    '''

# 윗 면은 흰색, 아랫 면은 노란색, 앞 면은 빨간색
# 뒷 면은 오렌지색, 왼쪽 면은 초록색, 오른쪽 면은 파란색이다.
color = {1 : 'w', 2 : 'y', 3 : 'r', 4 : 'o', 5 : 'g', 6 : 'b'}

T = int(read())
for t in range(T):
    
    N = int(read())
    rotateArr = list(read().split())
    
    U = [[1 for _ in range(3)] for _ in range(3)]
    D = [[2 for _ in range(3)] for _ in range(3)]
    F = [[3 for _ in range(3)] for _ in range(3)]
    B = [[4 for _ in range(3)] for _ in range(3)]
    L = [[5 for _ in range(3)] for _ in range(3)]
    R = [[6 for _ in range(3)] for _ in range(3)]

    # 위 앞 아래 뒤
    ld = deque([U[0][0], U[1][0], U[2][0], F[0][0], F[1][0], F[2][0], D[2][0], D[1][0], D[0][0], B[2][0], B[1][0], B[0][0]])
    # 위 뒤 아래 앞
    rd = deque([U[2][2], U[1][2], U[0][2], B[0][2], B[1][2], B[2][2], D[0][2], D[1][2], D[2][2], F[2][2], F[1][2], F[0][2]])
    # 앞 왼 뒤 오른
    ud = deque([F[0][2], F[0][1], F[0][0], L[0][2], L[0][1], L[0][0], B[0][0], B[0][1], B[0][2], R[0][0], R[0][1], R[0][2]])
    # 앞 오른 뒤 왼
    dd = deque([F[2][0], F[2][1], F[2][2], R[2][2], R[2][1], R[2][0], B[2][2], B[2][1], B[2][0], L[2][0], L[2][1], L[2][2]])
    # 위 왼 아래 오른
    bd = deque([U[0][2], U[0][1], U[0][0], L[0][0], L[1][0], L[2][0], D[0][0], D[0][1], D[0][2], R[2][0], R[1][0], R[0][0]])
    # 위 오른 아래 왼
    fd = deque([U[2][0], U[2][1], U[2][2], R[0][2], R[1][2], R[2][2], D[2][2], D[2][1], D[2][0], L[2][2], L[1][2], L[0][2]])
    
    for rotate in rotateArr:
        if rotate[0] == 'U':
            code = 'ud'
            if rotate[1] == '+':
                rotateClock(ud, code)
            else:
                rotateAntiClock(ud, code)

        elif rotate[0] == 'D':
            code = 'dd'
            if rotate[1] == '+':
                rotateClock(dd, code)
            else:
                rotateAntiClock(dd, code)

        elif rotate[0] == 'F':
            code = 'fd'
            if rotate[1] == '+':
                rotateClock(fd, code)
            else:
                rotateAntiClock(fd, code)

        elif rotate[0] == 'B':
            code = 'bd'
            if rotate[1] == '+':
                rotateClock(bd, code)
            else:
                rotateAntiClock(bd, code)

        elif rotate[0] == 'L':
            code = 'ld'
            if rotate[1] == '+':
                rotateClock(ld, code)
            else:
                rotateAntiClock(ld, code)

        elif rotate[0] == 'R':
            code = 'rd'
            if rotate[1] == '+':
                rotateClock(rd, code)
            else:
                rotateAntiClock(rd, code)
        sync(code)
        
    myPrint()