# [파이썬 | BOJ | 1780] 종이의 개수

from sys import stdin
read = stdin.readline
ans = [0, 0, 0]

def solve(board):
    size = len(board)
    if sum( sum(board[i]) for i in range(size) ) == size*size:
        ans[2] += 1
        return
    elif sum( sum(board[i]) for i in range(size) ) == 0 and min( min(board[i]) for i in range(size) ) == 0:
        ans[1] += 1
        return
    elif sum( sum(board[i]) for i in range(size) ) == size*size*-1:
        ans[0] += 1
        return
    
    tempBoard = [[] for _ in range(9)]
    tempSize = size // 3
    idx = 0
    for i in range(3):
        for j in range(3):
            temp = [[0 for _ in range(tempSize)] for _ in range(tempSize)]
            for r in range(tempSize):
                for c in range(tempSize):
                    temp[r][c] = board[tempSize*i+r][tempSize*j+c]
            tempBoard[idx] = temp
            idx += 1

    for idx in range(9):
        solve(tempBoard[idx])

    
N = int(read())
board = [list(map(int, read().split())) for _ in range(N)]
solve(board)

for a in ans:
    print(a)