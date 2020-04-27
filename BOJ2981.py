# [파이썬 | BOJ | 2981] 검문

import sys
from math import sqrt, floor, gcd
read = sys.stdin.readline

N = int(read())
arr = []
for _ in range(N):
    arr.append(int(read()))
diff = []
ans = set()
for i in range(N):
    for j in range(i+1, N):
        diff.append((arr[i]-arr[j]) if arr[i]>arr[j] else (arr[j]-arr[i]))
diff.sort()

if len(diff) > 1:
    temp = gcd(diff[0], diff[1])
    for i in range(2, N):
        temp = gcd(temp, diff[i])
else:
    temp = diff[0]

for i in reversed(range(1, int(sqrt(temp)+1))):
    #print(i)
    if temp % i == 0:
        ans.add(i)
        ans.add(temp//i)    
ans = list(ans)
ans.sort()
for a in ans[1:]:
    print(a, end=' ')