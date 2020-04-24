# [파이썬 | BOJ | 1759] 암호 만들기
import sys
read = sys.stdin.readline
ans = set()

def solve(cnt, idx, password):
    if cnt == L:
        mo, ja = 0, 0
        for p in password:
            if p in 'aeiou':
                mo += 1
            else:
                ja += 1
        if mo >= 1 and ja >= 2:
            ans.add(''.join(sorted(password)))
        return
    
    for i in range(C):
        if check[i] == 0 and i>=idx:
            check[i] = 1
            solve(cnt+1, i, password+temp[i])
            check[i] = 0



L, C = map(int, read().split())

temp = list(map(str, read().split()))
check = [0 for _ in range(C)]


solve(0, 0, '')
ans = sorted(list(ans))
for a in ans:
    print(a)