# [파이썬 | 2019 카카오 인턴쉽] 징검다리 건너기
from collections import deque
def solution(stones, k):
    temp = deque(stones[0:k])
    windowMax = max(temp)
    answer = windowMax
    for i in range(k, len(stones)):
        popped = temp.popleft()
        temp.append(stones[i])
        if popped == windowMax:
            windowMax = max(temp)
        answer = min(answer, windowMax)
    #print(answer)
    return answer

# 테스트용 input output 정의

# 3
# 2 4 5 3 2 1 4 2 5 1

K = int(input())
stones = list(map(int, input().split()))
solution(stones, K)

