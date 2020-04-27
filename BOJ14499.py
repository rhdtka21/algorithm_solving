# [파이썬 | BOJ | 14499] 주사위 굴리기

import sys
read = sys.stdin.readline

class Dice:
    top = 0
    bottom = 0
    north = 0
    south = 0
    east = 0
    west = 0

    def move(self, op):
        if op == 1:
            self.top, self.east, self.bottom, self.west 
 = self.west, self.top, self.east, self.bottom
        elif op == 2:
            self.top, self.east, self.bottom, self.west 
 = self.east, self.bottom, self.west, self.top
        elif op == 3:
            self.top, self.north, self.bottom, self.south 
 = self.south, self.top, self.north, self.bottom
        elif op == 4:
            self.top, self.north, self.bottom, self.south 
 = self.north, self.bottom, self.south, self.top
        print(self.top)

    def copyfrom(self, val):
        self.bottom = val

    def copyto(self):
        return self.bottom

    def show(self):
        print('t = ', self.top)
        print('b = ', self.bottom)
        print('n = ', self.north)
        print('s = ', self.south)
        print('e = ', self.east)
        print('w = ', self.west)
        print('--------------------------')

drct = [[0, 1],[0, -1],[-1, 0],[1, 0]]

N, M, x, y, K = map(int, read().split())
board = []

d = Dice()
for _ in range(N):
    board.append(list(map(int, read().split())))
oplist = list(map(int, read().split()))

for op in oplist:
    nx, ny = x + drct[op-1][0], y + drct[op-1][1]
    #범위 안이면
    if (nx >= 0 and nx < N) and (ny >= 0 and ny < M):
        x, y = nx, ny
        d.move(op)

        if board[x][y] > 0:
            d.copyfrom(board[x][y])
            board[x][y] = 0
        else:
            board[x][y] = d.copyto() 