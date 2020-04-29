# [파이썬 | BOJ | 1120] 문자열

import sys
read = sys.stdin.readline

def solve(A, B):
    global maxAns
    cnt = 0
    maxAns = sys.maxsize * -1
    
    while True:
        ans = 0
        length = len(A)
        for i in range(length):
            if A[i] == B[i]:
                ans += 1
        if maxAns < ans:
            maxAns = ans

        cnt += 1
        A = ' ' + A
        if length == len(B):
            return

A, B = map(str, read().split())
solve(A,B)
print(len(A)-maxAns)