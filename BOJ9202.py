# [파이썬 | BOJ | 9202] Boggle
import sys
read = sys.stdin.readline

#상 하 좌 우 좌상 좌하 우상 우하
d = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [1, -1], [-1, 1], [1, 1]]

def getScore(length):
    if length <= 2:
        return 0
    elif length <= 4:
        return 1
    elif length <= 5:
        return 2
    elif length <= 6:
        return 3
    elif length <= 7:
        return 5
    elif length <= 8:
        return 11

def solve(board, nowR, nowC, word, idx, wordIdx):
    global maxString
    global maxScore
    global cnt
    global check
    
    #이미 찾은적이 있다면 return
    if check[wordIdx]:
        return
    
    #마지막까지 왔고 마지막 알파벳까지 같다면, 찾은것
    if idx == len(word)-1 and board[nowR][nowC] == word[idx]:
        #찾은 개수 증가
        cnt += 1
        #점수 증가
        maxScore += getScore(len(word))
        #string길이 최대로 바꿈
        if len(word) > len(maxString):
            maxString = word
        elif len(word) == len(maxString):
            tempAlp = [maxString, word]
            tempAlp.sort()
            maxString = tempAlp[0]
        
        #찾았으니 check True로 바꿈
        check[wordIdx] = True
        return 

    #idx번째 알파벳이 다르다면 return
    if board[nowR][nowC] != word[idx]:
        return
    
    #한 word에서 같은 board 두번 방문 못함
    boardCheck[nowR][nowC] = 1
    #모든 방향 탐색
    for i in range(8):
        nextR, nextC = nowR + d[i][0], nowC + d[i][1]
        #범위 이내이고, board가 방문한적이 없어야함
        if 0<=nextR<4 and 0<=nextC<4:
            if boardCheck[nextR][nextC] == 0:
                solve(board, nextR, nextC, word, idx+1, wordIdx)
    
    #solve로 넘어가지 않았을때 다시 탐색이 올 수 있기때문에 방문안한것으로 처리해줌
    #(solve로 넘어갔을때만 현재 nowR, nowC board를 못쓰는거지, 다른 R,C에서 현재 nowR, nowC로
    # 넘어 오는 경우에는 방문을 하지 않은 상태여야 하므로)
    boardCheck[nowR][nowC] = 0

W = int(read())
words = [read().replace('\n', '') for _ in range(W)]
#빈줄 입력
_ = read()

#혹시나 같은 단어가 두번 주어지나 싶어서 해봄
words = list(set(words))
W = len(words)

B = int(read())
boards = []
for cnt in range(B):
    temp = [read().replace('\n', '') for _ in range(4)]
    boards.append(temp)
    if cnt == B-1:
        break
    _ = read()

for i in range(B):
    board = boards[i]
    maxScore = 0
    maxString = ''
    cnt = 0
    check = [False for _ in range(W)]
    for w in range(W):
        boardCheck = [[0, 0, 0, 0] for _ in range(4)]
        for n in range(16):
            r, c = n // 4, n % 4
            solve(board, r, c, words[w], 0, w)
    print(maxScore, maxString, cnt)