# [ÆÄÀÌ½ã | BOJ | 13459, 13460] ±¸½½ Å»Ãâ 1, 2

import sys
from collections import deque
read = sys.stdin.readline
 
#»ó ÇÏ ÁÂ ¿ì
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
 
def move(rr, rc, br, bc, idx):
    rcount, bcount = 0, 0
 
    while True:
        nrr, nrc = rr + d[idx][0], rc + d[idx][1]
        if board[nrr][nrc] == '#':
            break
        rr, rc = nrr, nrc
        if board[nrr][nrc] == 'O':
            break
        rcount += 1
        
    while True:
        nbr, nbc = br + d[idx][0], bc + d[idx][1]
        if board[nbr][nbc] == '#':
            break
        br, bc = nbr, nbc
        if board[nbr][nbc] == 'O':
            break
        bcount += 1
 
    if rr == br and rc == bc:
        if rr == hole[0] and rc == hole[1]:
            return rr, rc, br, bc
        if rcount < bcount:
            br, bc = br - d[idx][0], bc - d[idx][1]
        else:
            rr, rc = rr - d[idx][0], rc - d[idx][1]
 
    return rr, rc, br, bc
 
def bfs(red, blue, depth):
    ans = 0
    q = deque()
    q.append([red, blue, depth])
    while q:
        red, blue, depth = q.popleft()
        rr, rc = red
        br, bc = blue
 
        #print(red, blue, depth)
        
        if depth > 10:
            break
        
        if br == hole[0] and bc == hole[1]:
            #print("blue hole")
            ans = -1
            continue
 
        if rr == hole[0] and rc == hole[1]:
            #print("red hole")
            if rr == br and rc == bc:
                #print("red blue hole")
                ans = -1
            ans = 1
            break
 
 
        for i in range(4):
            nrr, nrc, nbr, nbc = move(rr, rc, br, bc, i)
            #print(nrr, nrc, nbr, nbc)
            if not visited[nrr][nrc][nbr][nbc]:
                visited[nrr][nrc][nbr][nbc] = True
                q.append([[nrr, nrc], [nbr, nbc], depth+1])
    
    # ±¸½½ Å»Ãâ 1
    if ans == -1 or depth >= 11:
        print(0)
    elif ans == 1:
        print(1)
    else:
        print(0)
 
    # ±¸½½ Å»Ãâ 2
    if depth >= 11:
        print(-1)
    elif ans == 1:
        print(depth)
    else:
        print(-1)
 
R, C = map(int, read().split())
board = []
 
for _ in range(R):
    board.append(read().replace('\n', ''))
 
blue = [0, 0]
red = [0, 0]
hole = [0, 0]
 
for i in range(R):
    for j in range(C):
        if board[i][j] == 'B':
            blue[0] = i
            blue[1] = j
        if board[i][j] == 'R':
            red[0] = i
            red[1] = j
        if board[i][j] == 'O':
            hole[0] = i
            hole[1] = j    
 
visited = [[[[False] * C for _ in range(R)] for _ in range(C)] for _ in range(R)]
 
bfs(red, blue, 0)