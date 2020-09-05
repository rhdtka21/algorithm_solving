# [파이썬 | BOJ | 9506] 약수들의 합
import sys
import math
read = sys.stdin.readline

def solve (N):
    divisor = [1, N]
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            divisor.append(i)
            divisor.append(N//i)
    divisor.sort()
    if sum(divisor) == N*2:
        ans = "{} = ".format(N)
        for d in divisor[:-1]:
            ans += str(d) + " + "
        print(ans[:-3])
        return
    else:
        print("{} is NOT perfect.".format(N))
        return

while True: 
    N = int(read())
    if N == -1:
        break
    solve(N)
