# [���̽� | BOJ | 14503] �κ� û�ұ�

import sys
read = sys.stdin.readline

direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def rotate(d):
    if d == 0:
        return 3
    else:
        return d-1

def unrotate(d):
    if d == 3:
        return 0
    else:
        return d+1

R, C = map(int, read().split())
r, c, d = map(int, read().split())
board = [[1 for _ in range(C+2)]]
for _ in range(R):
    board.append([1] + list(map(int, read().split())) + [1])
board.append([1 for _ in range(C+2)])
r += 1
c += 1


while True:
    cnt = 0
    board[r][c] = 2
    d = rotate(d)
    nr, nc = r + direction[d][0], c + direction[d][1]
    while board[nr][nc] != 0 and cnt < 4:
        d = rotate(d)
        nr, nc = r + direction[d][0], c + direction[d][1]
        cnt += 1

    if cnt < 4:
        r, c = nr, nc
    else:
        #�ٽ� ���� �������� ������(�ʱ⿡ ���Դ� ����)
        d = unrotate(d)
        nr, nc = r - direction[d][0], c - direction[d][1]
        #������ �ȵǴ°��
        if board[nr][nc] == 1:
            break
        #���� �ϴ°��
        else:
            r, c = nr, nc
ans = 0
for b in board:
    ans += b.count(2)
    #print(b)

print(ans) 