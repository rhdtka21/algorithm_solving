# [파이썬 | 2019 카카오 인턴쉽] 징검다리 건너기
from collections import deque

# 효율성 검사에서 하나 시간초과 남
def solution_0(stones, k):
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

#이분탐색 알고리즘
def check(stones,k, jump):
    temp = k
    for stone in stones:
        if stone < jump:
            temp -= 1
        else:
            temp = k
        #각 돌이 예측값 jump보다 작은게 k번 연속으로 나오면
        if temp == 0:
            return False
    return True

def solution(stones, k):
    left = 0
    right = 200000000
    while left <= right:
        jump = (left + right)//2
        print(left, jump, right)
        
        canJump = check(stones,k,jump)

        if canJump:
            answer = jump
            left = jump + 1
        else:
            right = jump - 1

    #print(answer)
    return answer


# 테스트용 input output 정의

# 3
# 2 4 5 3 2 1 4 2 5 1

K = int(input())
stones = list(map(int, input().split()))
solution(stones, K)

