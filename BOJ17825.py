# [파이썬 | BOJ | 17825] 주사위 윷놀이
import sys
read = sys.stdin.readline
maxAns = sys.maxsize * -1
BRANCH = [[], [], [], [], []]                                                           #20  21
BRANCH[0] = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0]        
BRANCH[1] = [10, 13, 16, 19]                                                 
BRANCH[2] = [20, 22, 24]
BRANCH[3] = [30, 28, 27, 26]
BRANCH[4] = [25, 30, 35, 40, 0]

def solve(cnt, depth):
    global maxAns
    #print(locInfo, cnt, depth)
    if depth == len(diceNum):
        if maxAns < cnt:
            maxAns = cnt
            #print(locInfo, cnt)
        return

    for horseNum, li in enumerate(locInfo):
        #현재 위치
        branch, location = li
        
        #이미 도착한 상태면 해당 말을 고를 수 없다.
        if (branch, location) == (0, 21) or (branch, location) == (4, 4): 
            continue
        
        #주사위 정보를 통한 다음위치
        nextLocation = location + diceNum[depth]

        #윷말 이동 정리 알고리즘
        #지금 0번 위치에 있는데, 말의 다음 위치가 분기점 이라면,
        if branch == 0:
            #지금 0번 위치에 있는데 말이 종점에 도착한다. (점수를 안준다.)
            if nextLocation >= 22:
                #더이상 말이 이동못할것임
                nextLocation = 21
                nextBranch = branch
            #다음 위치가 10번이라면
            elif BRANCH[branch][nextLocation] == 10:
                #1번 가지로 빠지고, 거기서 0번 위치로 이동함
                nextBranch = 1
                nextLocation = 0
            #다음 위치가 20번 이라면
            elif BRANCH[branch][nextLocation] == 20:
                #2번 가지로 빠지고, 거기서 0번 위치로 이동
                nextBranch = 2
                nextLocation = 0
            #다음 위치가 30번이라면
            elif BRANCH[branch][nextLocation] == 30:
                #3번 가지로 빠지고, 거기서 0번 위치로 이동
                nextBranch = 3
                nextLocation = 0
            #종점도, 분기점도 아니라면
            else:
                #가지는 그대로
                nextBranch = branch
        #지금 1번 위치에 있는데, 
        elif branch == 1:
            #말이 25번을 넘어간다면
            if nextLocation >= 4:
                nextBranch = 4
                nextLocation = nextLocation - 4
            #안넘어 간다면
            else:
                nextBranch = branch
            

        elif branch == 2:
            if nextLocation >= 3:
                nextBranch = 4
                nextLocation = nextLocation - 3
            else:
                nextBranch = branch
            

        elif branch == 3:
            if nextLocation >= 4:
                nextBranch = 4
                nextLocation = nextLocation - 4
            else:
                nextBranch = branch
            
        #지금 4번 위치에 있는데
        elif branch == 4:
            if nextLocation >= 4:
                #print(locInfo, cnt)
                nextBranch = branch
                nextLocation = 4
            else:
                nextBranch = branch

        
        if (nextBranch, nextLocation) == (0, 21) or (nextBranch, nextLocation) == (4, 4):
            locInfo[horseNum] = (nextBranch, nextLocation)
            solve(cnt + BRANCH[nextBranch][nextLocation], depth+1)
            locInfo[horseNum] = (branch, location)
            continue

        if (nextBranch, nextLocation) in locInfo:
            continue
        
        if (nextBranch, nextLocation) == (0, 20) and (4, 3) in locInfo:
            continue
        
        if (nextBranch, nextLocation) == (4, 3) and (0, 20) in locInfo:
            continue

        locInfo[horseNum] = (nextBranch, nextLocation)
        solve(cnt + BRANCH[nextBranch][nextLocation], depth+1)
        locInfo[horseNum] = (branch, location)
            

diceNum = list(map(int, read().split()))
locInfo = [(0,0), (0,0), (0,0), (0,0)]
solve(0, 0)
print(maxAns)