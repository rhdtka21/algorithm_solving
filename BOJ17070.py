# [파이썬 | BOJ | 17070] 파이프 옮기기 1
 
import sys
read = sys.stdin.readline
cnt = 0

def direction(r1, c1, r2, c2):
    if r2 == r1 and c2-1 == c1:
        return 0
    elif r2-1 == r1 and c2 == c1:
        return 1
    elif r2-1 == r1 and c2-1 == c1:
        return 2

def go(r1, c1, r2, c2):
    global cnt

    if (r2 == N-1 and c2 == N-1):
        cnt += 1
        return
    d = direction(r1, c1, r2, c2)

    for i in range(len(nextPosition[d])):
        nr1, nc1 = r1 + nextPosition[d][i][0], c1 + nextPosition[d][i][1]
        nr2, nc2 = r2 + nextPosition[d][i][2], c2 + nextPosition[d][i][3]
    
        if 0 <= nr1 < N and 0 <= nc1 < N and 0 <= nr2 < N and 0 <= nc2 < N:
            if nr2-nr1 != nc2-nc1 and board[nr2][nc2] != 1:
                go(nr1, nc1, nr2, nc2)
            if nr2-nr1 == nc2-nc1 and board[nr1][nc1] != 1 and board[nr2][nc2] != 1 and board[nr1][nc2] != 1 and board[nr2][nc1] != 1:
                go(nr1, nc1, nr2, nc2)

#몸,머리
nextPosition = [[[0, 1, 0, 1], [0, 1, 1, 1]], 
                [[1, 0, 1, 0], [1, 0, 1, 1]], 
                [[1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]]]


N = int(read())
board = [list(map(int, read().split())) for _ in range(N)]

if N <= 12:
    go(0, 0, 0, 1)
    print(cnt)
else:
    dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
    # 0 -, 1 \, 2 |

    dp[0][0][1] = 1
    for i in range(2, N):
        if board[0][i] == 0:
            dp[0][0][i] = dp[0][0][i-1]

    for r in range(1, N):
        for c in range(1, N):
            if board[r][c] == 0 and board[r][c-1] == 0 and board[r-1][c] == 0:
                dp[1][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]

            if board[r][c] == 0:
                dp[0][r][c] = dp[0][r][c-1] + dp[1][r][c-1]
                dp[2][r][c] = dp[2][r-1][c] + dp[1][r-1][c]

    print(sum(dp[i][N-1][N-1] for i in range(3)))