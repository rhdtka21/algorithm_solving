# [파이썬 | BOJ | 1992] 쿼드트리

import sys
read = sys.stdin.readline

def solve(board):
    size = len(board)
    if sum(sum(board[i]) for i in range(size)) == size*size:
        return '1'
    elif sum(sum(board[i]) for i in range(size)) == 0:
        return '0'

    ans = ''
    
    lu = [[0 for _ in range(size//2)] for _ in range(size//2)]
    ru = [[0 for _ in range(size//2)] for _ in range(size//2)]
    ld = [[0 for _ in range(size//2)] for _ in range(size//2)]
    rd = [[0 for _ in range(size//2)] for _ in range(size//2)]
    
    for i in range(size):
        for j in range(size):
            if i < size // 2 and j < size // 2:
                lu[i][j] = board[i][j]
            elif i < size // 2 and j >= size // 2:
                ru[i][j-size//2] = board[i][j]
            elif i >=size // 2 and j < size // 2:
                ld[i-size//2][j] = board[i][j]
            else:
                rd[i-size//2][j-size//2] = board[i][j]
    
    ans += solve(lu) if len(solve(lu)) == 1 else '(' + solve(lu) + ')'
    ans += solve(ru) if len(solve(ru)) == 1 else '(' + solve(ru) + ')'
    ans += solve(ld) if len(solve(ld)) == 1 else '(' + solve(ld) + ')'
    ans += solve(rd) if len(solve(rd)) == 1 else '(' + solve(rd) + ')'
    return ans
    

N = int(read())
board = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    temp = list(read().replace('\n', ''))
    for j, t in enumerate(temp):
        board[i][j] = int(t)

print(solve(board) if len(solve(board)) == 1 else '(' + solve(board) + ')' )

