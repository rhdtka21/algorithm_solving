# [파이썬 | BOJ | 17825] 주사위 윷놀이
import sys
read = sys.stdin.readline
maxval = sys.maxsize * -1
BRANCH = [[], [], [], []]
BRANCH[0] = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]        
BRANCH[1] = [10, 13, 16, 19, 25, 30, 35, 40]                                                 
BRANCH[2] = [20, 22, 24, 25, 30, 35, 40]
BRANCH[3] = [30, 28, 27, 26, 25, 30, 35, 40]   

def solve(horses, cnt, depth):
    global maxval 

    if depth == 10:
        if maxval < cnt:
            maxval = cnt
        return

    go = diceNum[depth]

    # 0번말
    branch = horses[0][0]
    index = horses[0][1]

    if index == -1:
        return

    nextIndex = index + go
    if nextIndex >= len(BRANCH[0]):
        addVal = 40
        nextIndex = -1

    else:
        if branch == 0 and BRANCH[branch][nextIndex] == 10:
            branch = 1
            nextIndex = 0

        elif branch == 0 and BRANCH[branch][nextIndex] == 20:
            branch = 2
            nextIndex = 0

        elif branch == 0 and BRANCH[branch][nextIndex] == 30:
            branch = 3
            nextIndex = 0

        try:
            addVal = BRANCH[branch][nextIndex]
        except IndexError:
            addVal = 40
            nextIndex = -1
    if not (branch, nextIndex) in horses:
        if branch > 0 and nextIndex in [25, 30, 35, 40]:
            if horses[1][1] != nextIndex and horses[2][1] != nextIndex and horses[3][1] != nextIndex:
                solve([ (branch, nextIndex), horses[1], horses[2], horses[3] ], cnt + addVal, depth + 1)
        else:
            solve([ (branch, nextIndex), horses[1], horses[2], horses[3] ], cnt + addVal, depth + 1)

    # 1번말
    branch = horses[1][0]
    index = horses[1][1]

    if index == -1:
        return

    nextIndex = index + go
    if nextIndex >= len(BRANCH[0]):
        addVal = 40
        nextIndex = -1

    else:
        if branch == 0 and BRANCH[branch][nextIndex] == 10:
            branch = 1
            nextIndex = 0

        elif branch == 0 and BRANCH[branch][nextIndex] == 20:
            branch = 2
            nextIndex = 0

        elif branch == 0 and BRANCH[branch][nextIndex] == 30:
            branch = 3
            nextIndex = 0

        try:
            addVal = BRANCH[branch][nextIndex]
        except IndexError:
            addVal = 40
            nextIndex = -1
    if not (branch, nextIndex) in horses:
        if branch > 0 and nextIndex in [25, 30, 35, 40]:
            if horses[0][1] != nextIndex and horses[2][1] != nextIndex and horses[3][1] != nextIndex:
                solve([ horses[0], (branch, nextIndex), horses[2], horses[3] ], cnt + addVal, depth + 1)
        else:
            solve([ horses[0], (branch, nextIndex), horses[2], horses[3] ], cnt + addVal, depth + 1)
    # 2번말
    branch = horses[2][0]
    index = horses[2][1]

    if index == -1:
        return

    nextIndex = index + go
    if nextIndex >= len(BRANCH[0]):
        addVal = 40
        nextIndex = -1

    else:
        if branch == 0 and BRANCH[branch][nextIndex] == 10:
            branch = 1
            nextIndex = 0

        elif branch == 0 and BRANCH[branch][nextIndex] == 20:
            branch = 2
            nextIndex = 0

        elif branch == 0 and BRANCH[branch][nextIndex] == 30:
            branch = 3
            nextIndex = 0

        try:
            addVal = BRANCH[branch][nextIndex]
        except IndexError:
            addVal = 40
            nextIndex = -1
    if not (branch, nextIndex) in horses:
        if branch > 0 and nextIndex in [25, 30, 35, 40]:
            if horses[0][1] != nextIndex and horses[1][1] != nextIndex and horses[3][1] != nextIndex:
                solve([ horses[0], horses[1], (branch, nextIndex), horses[3] ], cnt + addVal, depth + 1)
        else:
            solve([ horses[0], horses[1], (branch, nextIndex), horses[3] ], cnt + addVal, depth + 1)
    # 3번말
    branch = horses[3][0]
    index = horses[3][1]

    if index == -1:
        return

    nextIndex = index + go
    if nextIndex >= len(BRANCH[0]):
        addVal = 40
        nextIndex = -1

    else:
        if branch == 0 and BRANCH[branch][nextIndex] == 10:
            branch = 1
            nextIndex = 0

        elif branch == 0 and BRANCH[branch][nextIndex] == 20:
            branch = 2
            nextIndex = 0

        elif branch == 0 and BRANCH[branch][nextIndex] == 30:
            branch = 3
            nextIndex = 0

        try:
            addVal = BRANCH[branch][nextIndex]
        except IndexError:
            addVal = 40
            nextIndex = -1
    if not (branch, nextIndex) in horses:
        if branch > 0 and nextIndex in [25, 30, 35, 40]:
            if horses[0][1] != nextIndex and horses[1][1] != nextIndex and horses[2][1] != nextIndex:
                solve([ horses[0], horses[1], horses[2], (branch, nextIndex)], cnt + addVal, depth + 1)
        else:
            solve([ horses[0], horses[1], horses[2], (branch, nextIndex)], cnt + addVal, depth + 1)

diceNum = list(map(int, read().split()))
solve([(0,0), (0,0), (0,0), (0,0)], 0, 0)

print(maxval)