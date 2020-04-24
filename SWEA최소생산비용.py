# SWEA 최소생산비용
def bt(idx, val):
    global minans

    if val > minans:
        return

    if idx == N-1:
        if minans > val:
            minans = val
        print(minans)
        return
    
    
    for i in range(N):
        if banList[i] == 0:
            banList[i] = 1
            bt(idx+1, val+V[idx+1][i])
            banList[i] = 0

T = int(input())

for t in range(1, T+1):
    minans = 999999
    
    N = int(input())

    banList = [0]*N
    V = []
    for _ in range(N):
        V.append(list(map(int, input().split())))
    
    for i in range(N):
        banList[i] = 1
        bt(0, V[0][i])
        banList[i] = 0
    
    print("#%d %d" % (t, minans))   