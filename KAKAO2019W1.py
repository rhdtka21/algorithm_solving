# [파이썬 | 2019 카카오 인턴쉽] 크레인 인형뽑기 게임

cnt = 0
def checkBucket(bucket):
    global cnt
    if len(bucket) < 2:
        return
    if bucket[-1] == bucket[-2]:
        del bucket[-2:]
        cnt += 2
    return
 
def solution(board, moves):
    N = len(board)
    bucket = []
    column = [[] for _ in range(N)]
    for j in range(N):
        for i in reversed(range(N)):
            if board[i][j] > 0:
                column[j].append(board[i][j])
    
    for move in moves:
        idx = move - 1
        if len(column[idx]):
            bucket.append(column[idx].pop())
        checkBucket(bucket)
    
    answer = cnt
    print(answer)
    return answer
    
# 테스트용 input output 정의

# 5
# 0 0 0 0 0 
# 0 0 1 0 3
# 0 2 5 0 1
# 4 2 4 4 2
# 3 5 1 3 1
# 1 5 3 5 1 2 1 4

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
moves = list(map(int, input().split())) 
solution(board, moves)
