# [파이썬 | BOJ | 1874] 스택 수열

import sys
read = sys.stdin.readline

N = int(read())
lst = list(reversed(range(1, N+1)))
stack = []
nums = []
ans = ''
for _ in range(N):
    nums.append(int(read()))

for num in nums:
    if not stack:
        stack.append(lst.pop())
        ans += '+'

    while stack[-1] < num:
        stack.append(lst.pop())
        ans += '+'

    if stack[-1] == num:
        stack.pop()
        ans += '-'
    
    elif stack[-1] > num:
        print("NO")
        sys.exit(0)
    
for a in ans:
    print(a)