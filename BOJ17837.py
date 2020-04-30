# [파이썬 | BOJ | 17873] 새로운 게임2
import sys
read = sys.stdin.readline

# →, ←, ↑, ↓
# 1, 2, 3, 4
d = [[0, 1], [0, -1], [-1, 0], [1, 0] ]

def move(hidx):
    hr, hc, hd = horses[hidx]
    nhr, nhc = hr + d[hd][0], hc + d[hd][1]

    #뒤로 돌아가야 하는 상황이면
    if not 0 <= nhr < N or not 0 <= nhc < N or color[nhr][nhc] == 2:
        #방향 전환
        nhd = hd-1 if hd%2 else hd+1
        #방향이 바뀐 정보를 갱신
        horses[hidx][2] = nhd
        #다음으로 갈 방향(뒤로가는 상황)
        nhr = hr + d[nhd][0]
        nhc = hc + d[nhd][1]
        #뒤도 막혀있으면 끝
        if not 0 <= nhr < N or not 0 <= nhc < N or color[nhr][nhc] == 2:
            return 0

    temp = []
    for i, key in enumerate(board[hr][hc]):
        if key == hidx:
            #지금 말보다 위에 있는것들을 temp에 넣어서 이동준비
            temp = (board[hr][hc][i:])
            #지금 말보다 아래있는것들만 남김
            board[hr][hc] = board[hr][hc][:i]
            break

    #다음 위치가 빨간색이면, 순서 뒤집음
    if color[nhr][nhc] == 1:
        temp = reversed(temp)

    #다음 위치에 넣고, 위치 정보를 갱신함 방향은 그대로이므로 갱신X
    for i in temp:
        board[nhr][nhc].append(i)
        horses[i][:2] = [nhr, nhc]

    #한칸에 말이 4개이상이면 종료
    if len(board[nhr][nhc]) >= 4:
        return 1
    return 0

N, K = map(int, read().split())
color = [list(map(int, read().split())) for _ in range(N)]
horses = [[] for _ in range(K)]
board = [[[] for _ in range(N)] for _ in range(N)]

for i in range(K):
    x, y, z = map(int, input().split())
    board[x-1][y-1].append(i)
    horses[i] = [x-1, y-1, z-1]

cnt = 1
while cnt <= 1000:
    for i in range(K):
        flag = move(i)
        if flag:
            print(cnt)
            sys.exit()
    cnt += 1
print(-1)

