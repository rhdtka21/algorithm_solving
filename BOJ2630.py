# [파이썬 | BOJ | 2630] 색종이 만들기

import sys
read = sys.stdin.readline

#흰, 파
cnt = [0, 0]

def exitOption(paper):
    length = len(paper)

    if length == 1:
        return paper[0][0]

    if sum(sum(paper[i]) for i in range(length)) == 0:
        return 0
    elif sum(sum(paper[i]) for i in range(length)) == length ** 2:
        return 1
    return -1

def solve(paper):
    flag = exitOption(paper)
    if flag >= 0:
        cnt[flag] += 1
        return

    # 0 1
    # 2 3
    #print(paper)
    length = len(paper)
    nextLength = length // 2
    parts = [[[0 for _ in range(nextLength)] for _ in range(nextLength)] for _ in range(4)]

    for r in range(length):
        for c in range(length):
            if r < nextLength and c < nextLength:
                parts[0][r][c] = paper[r][c]
            elif r < nextLength and c >= nextLength:
                parts[1][r][c-nextLength] = paper[r][c]
            elif r >= nextLength and c < nextLength:
                parts[2][r-nextLength][c] = paper[r][c]
            elif r >= nextLength and c >= nextLength:
                parts[3][r-nextLength][c-nextLength] = paper[r][c]
    
    for i in range(4):
        solve(parts[i])
    



N = int(read())
paper = [list(map(int, read().split())) for _ in range(N)]
solve(paper)
for c in cnt:
    print(c)