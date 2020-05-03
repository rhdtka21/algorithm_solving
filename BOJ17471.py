# [파이썬 | BOJ | 17471] 게리맨더링
import sys
from collections import deque
read = sys.stdin.readline
minAns = sys.maxsize

def case(check, depth):
    if depth == N:
        solve(check)
        return

    check[depth] = 1
    case(check, depth+1)
    check[depth] = 0
    case(check, depth+1)

def case2(depth):
    for i in range(2**depth):
        b = format(i, 'b')
        solve(list(map(int, ('0'*(depth-len(b)) + b if len(b) < depth else b))))
        
def solve(check):
    global minAns

    def bfs(startV):
        q = deque()
        q.append(startV)
        visited[startV] = 1
        thisColor = check[startV-1]
        while q:
            nowV = q.popleft()
            for nextV in edges[nowV]:
                #아직 방문한적이 없고, 같은 지역구인것만 방문.
                if visited[nextV] == 0 and check[nextV-1] == thisColor:
                    q.append(nextV)
                    visited[nextV] = 1
        return

    visited = [0 for _ in range(N+1)]

    if sum(check) == 0 or sum(check) == N: #선거구가 하나로 통일된 상황
        return
    
    cnt = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            bfs(i)
            cnt +=1
        #선거구는 총 2개뿐
        if cnt == 2:
            break
    
    #선거구 탐색을 2번했는데, 방문 안된게 있다면 불가능한 경우이다.
    for i in range(1, N+1):
        if visited[i] == 0:
            return
   
    ans = 0
    for i in range(N):
        if check[i] == 0:
            ans += population[i]
        else:
            ans -= population[i]
    #print(abs(ans))
    if abs(ans) < minAns:
        minAns = abs(ans)

N = int(read())
population = list(map(int, read().split()))

edges = [[] for _ in range(N+1)]
for i in range(1, N+1):
    temp = list(map(int, read().split()))
    edges[i] = temp[1:]

#case, case2 모두 같은 시간이 걸림
case2(N)
#case([0 for _ in range(N)], 0)
print(-1 if minAns == sys.maxsize else minAns)