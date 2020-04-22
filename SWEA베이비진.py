# SWEA 베이비진
from collections import deque

def check():
    if len(A) < 3:
        return 0
    else:
        for i in range(len(A)):
            if A.count(A[i]) >= 3:
                return 1
            elif ((A.count(A[i]-1) > 0) and (A.count(A[i]-2) > 0)) or ((A.count(A[i]-1) > 0) and (A.count(A[i]+1) > 0)) or ((A.count(A[i]+1) > 0) and (A.count(A[i]+2) > 0)):
                return 1
            
            if B.count(B[i]) >= 3:
                return 2
            elif ((B.count(B[i]-1) > 0) and (B.count(B[i]-2) > 0)) or ((B.count(B[i]-1) > 0) and (B.count(B[i]+1) > 0)) or ((B.count(B[i]+1) > 0) and (B.count(B[i]+2) > 0)):
                return 2
        return 0

T = int(input())
for t in range(1, T+1):
    nums = deque(map(int, input().split()))
    A = []
    B = []
    for _ in range(6):
        A.append(nums.popleft())
        B.append(nums.popleft())
        print(A, B)
        ans = check()
        if ans > 0:
            break

    print('#%d %d' %(t, ans))