# [파이썬 | 2020 KAKAO BLIND RECRUITMENT | 문제 3] 자물쇠와 열쇠
def rotate_90(arr):
    N = len(arr)
    ret = [[0] * N for _ in range(N)]
    
    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = arr[r][c]
    return ret

def solution(key, lock):
    M = len(key)
    N = len(lock)
    lockCnt = 0
    for r in range(N):
        for c in range(N):
            if lock[r][c] == 0:
                lockCnt += 1

    keys = []
    for i in range(4):
        temp = key
        for _ in range(i):
            temp = rotate_90(temp)
        keys.append(temp)

    board = [[-1 for _ in range(2*M +N - 2)]for _ in range(2*M +N - 2)]
    K = len(board)

    for r in range(K):
        for c in range(K):
            if r>=M-1 and c >= M-1 and r<= M+N-2 and c <= M+N-2:
                board[r][c] = lock[r-(M-1)][c-(M-1)]
    
    answer = False
    for r in range(M+N-1):
        for c in range(M+N-1):
            for i in range(4):
                cnt = 0
                for sr in range(M):
                    for sc in range(M):
                        if board[r+sr][c+sc] == 0 and keys[i][sr][sc] == 1:
                            cnt += 1
                        elif board[r+sr][c+sc] == 1 and keys[i][sr][sc] == 1:
                            cnt = -500
                if cnt == lockCnt:
                    answer = True
            if answer == True:
                #print(answer)
                return answer
    #print(answer)
    return answer

M, N = map(int, input().split())
key = [list(map(int, input().split())) for _ in range(M)]
lock = [list(map(int, input().split())) for _ in range(N)]

solution(key, lock)