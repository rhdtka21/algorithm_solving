# [파이썬 | BOJ | 16235] 나무 재테크
import sys
from collections import deque
read = sys.stdin.readline

def myprint(arr):
    for a in arr:
        print(a)
    print()

#상 하 좌 우 좌상 좌하 우상 우하
D = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [1, -1], [-1, 1], [1, 1]]

N, M, K = map(int, read().split())
A = [list(map(int, read().split())) for _ in range(N)]
treeInfo = [list(map(int, read().split())) for _ in range(M)]

board = [[deque() for _ in range(N)] for _ in range(N)]
nutri = [[5 for _ in range(N)] for _ in range(N)]

for eachTree in treeInfo:
    r, c, old = eachTree
    board[r-1][c-1].append(old)

#print("초기")
#myprint(board)
#myprint(nutri)

for year in range(K):
    temp = [[0 for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            treeCnt = len(board[r][c])
            if treeCnt == 0:
                nutri[r][c] += A[r][c]  #나무가 없어도 영양분은 모두 주니까
                continue

            subNutri = 0
            addNutri = 0
            sliceNum = treeCnt        #이 나무 이상으로 늙은나무는 다 죽는다.

            #정렬되어 있으므로 어린나무부터 성장
            for i in range(treeCnt):
                #양분이 부족하면
                if subNutri + board[r][c][i] > nutri[r][c]:
                    sliceNum = i
                    break
                subNutri += board[r][c][i] 
                board[r][c][i] += 1             #나무들의 나이가 증가한다.
                
            for i in range(sliceNum, treeCnt):
                addNutri += (board[r][c][i]//2)

            nutri[r][c] -= subNutri             #봄에 빠지는 양분
            nutri[r][c] += addNutri             #여름에 더해지는 양분
            nutri[r][c] += A[r][c]              #겨울에 더해지는 양분

            for _ in range(treeCnt - sliceNum):
                board[r][c].pop()    #늙은 나무 죽음
            
            treeCnt = len(board[r][c])
            #가을부분.
            for i in range(treeCnt):
                if board[r][c][i] % 5 == 0:
                    for j in range(8):
                        nextR, nextC = r + D[j][0], c + D[j][1]
                        if 0 <= nextR < N and 0 <= nextC < N:
                            #새로 추가할 1렙나무 개수
                            temp[nextR][nextC] += 1
    
    #번식한 나무를 반영한다.
    for r in range(N):
        for c in range(N):
            if temp[r][c] > 0:
                for _ in range(temp[r][c]):
                    board[r][c].appendleft(1)

    #print(year+1)
    #myprint(board)
    #myprint(nutri)

ans = 0
for r in range(N):
    for c in range(N):
        ans += len(board[r][c])
print(ans)